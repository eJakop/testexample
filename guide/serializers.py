from rest_framework import serializers
from .models import Guide


class GuideSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'
        