from rest_framework import serializers
from .models import Employee, DeletedEmployee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'


class DeletedEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeletedEmployee
        fields = '__all__'