from rest_framework import serializers
from .models import Details
from django.db.models import fields

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Details
        fields = ('name', 'email', 'mobile', 'address')
