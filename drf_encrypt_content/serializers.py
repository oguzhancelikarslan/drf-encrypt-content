from rest_framework import serializers

from .mixins import RestEncryptContentMixin


class EncryptedModelSerializer(RestEncryptContentMixin, serializers.ModelSerializer):
    pass
