from rest_framework import serializers
from accounts import models


class GroupSerializerREST(serializers.ModelSerializer):
    class Meta:
        model = models.Group
        fields = ('pk', 'name')


class RegisterSerializer(serializers.ModelSerializer):
    def validate(self, data):
        try:
            user = models.User.objects.filter(username=data.get('username'))
            if len(user) > 0:
                raise serializers.ValidationError(_("Username already exists"))
        except models.User.DoesNotExist:
            pass
        return data

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'password', 'is_active')
        extra_kwargs = {'confirm_password': {'read_only': True}}
