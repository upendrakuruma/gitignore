from rest_framework import serializers 
from .models import *

class Studentserializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model=Student