import secrets
from hashids import Hashids
from django.db import IntegrityError, transaction, models


class StringIdModel(models.Model):
    """Its abstract model we want inherite by when model will be exposed to the API."""

    STRATEGY_VAR = "var"
    STRATEGY_CONST_32 = "const32"
    _create_retries = 10
    _min_id = 1000000
    _max_id = 10000000000
    id = models.CharField(max_length=32, primary_key=True, editable=False)

    class Meta:
        abstract = True

    def get_hash_strategy(self):
        return StringIdModel.STRATEGY_VAR

    def save(self, *args, **kwargs):
        """Override default save method in order to change id to string type.

        We are using atomic to make it safe-fail.
        """
        if not self.pk:
            try:
                with transaction.atomic():
                    if self.get_hash_strategy() == StringIdModel.STRATEGY_VAR:
                        hashids = Hashids()
                        self.id = hashids.encode(
                            self._min_id + secrets.randbelow(self._max_id)
                        )
                    elif self.get_hash_strategy() == StringIdModel.STRATEGY_CONST_32:
                        self.id = secrets.token_urlsafe(32)[0:32]
                    else:
                        raise InvalidStrategyException()
                    super().save(*args, **kwargs)
            except IntegrityError as err:
                self.id = None
                self._create_retries -= 1
                if self._create_retries == 0:
                    raise IntegrityError(err)
                else:
                    self.save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)
