from rest_framework import serializers
from api import models

class InstituteSerializer(serializers.ModelSerializer):
    class Meta :
        model=models.Institute
        fields="_all_"

class StudentSerializer(serializers.ModelSerializer):
    institute=InstituteSerializer(read_only=True)

    class Meta :
        model=models.Student
        fields="_all_"