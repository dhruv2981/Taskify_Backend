from rest_framework import serializers
from Taskify_App.models import *
from .project import ProjectSerializer


class UserSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True,read_only=True)

    class Meta:

        model = User
        fields = '__all__'
        # use exclude when to leave one or two
        # if u want to have field whose value cant be edited (add read_only)
        # if u want to keep any check or validation (for single field ,multiple field,)

    def validate_enrollment_no(self, value):
        if (value < 9999999 or value > 99999999):
            raise serializers.ValidationError('Not valid enrollment number')
            # in terminal ,
        return value
