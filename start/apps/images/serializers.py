from rest_framework import serializers

from .models import Image
from .fields import ChoiceField
from .constants import Gender

class ImageSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    gender = ChoiceField(Gender)

    class Meta:
        model = Image
        fields = ("id", "name", "url", "gender")
