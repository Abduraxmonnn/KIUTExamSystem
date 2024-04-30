from rest_framework import serializers

from apps.main.auth_tokens.models import CustomToken


class CustomTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomToken
        fields = ('key',)
