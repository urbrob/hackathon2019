from rest_framework import serializers
from accounts import models
from django.utils.translation import gettext_lazy as _


class RegisterSerializer(serializers.ModelSerializer):

    def validate(self, data):
        try:
            user = models.User.objects.filter(username=data.get('username'))
            if len(user) > 0:
                raise serializers.ValidationError(_("Username already exists"))
        except models.User.DoesNotExist:
            pass
        return data

    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'password', 'is_active')
        extra_kwargs = {'confirm_password': {'read_only': True}}
