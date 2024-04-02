from rest_framework import serializers

from backend.models import Employee,User


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields ='__all__'
        # fields =['last_name']

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields ='__all__'