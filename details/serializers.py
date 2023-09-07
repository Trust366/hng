# from rest_framework import serializers
from .models import Details

# class DetailSerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Details 
        # exclude = ['status_code']
        
        
from rest_framework import serializers


class DetailSerializer(serializers.Serializer):
    slack_name = serializers.CharField()
    track = serializers.CharField()
    current_day = serializers.CharField()
    utc_time = serializers.DateTimeField()
    github_file_url = serializers.URLField()
    github_repo_url = serializers.URLField()
    status_code = serializers.IntegerField()
        