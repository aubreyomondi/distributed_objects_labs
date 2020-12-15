from rest_framework import serializers 
from rest_app.models import Student
 
 
class StudentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Student
        fields = ('id',
                  'admission',
                  'full_name',
                  'email',
                  'course')
    