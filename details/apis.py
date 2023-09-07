# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated

# from .models import Details

# class DetailView(APIView):
        # def get(self, request):
            # detail_objects = Detail.objects.all()   
            # detail_objects = Detail.objects.all()
        
            # Serialize the queryset using your serializer
            # serializer = DetailSerializer(detail_objects, many=True)
        
            # Return the serialized data in a JSON response
            # return Response(serializer.data)


from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DetailSerializer


class DetailView(APIView):
    @staticmethod
    def get(request):
        # Retrieve query parameter
        slack_name = request.query_params.get('slack_name')
        track = request.query_params.get('track')

        # Current day and time
        current_day = datetime.now().strftime("%A")
        utc_time = datetime.utcnow()

        # GitHub URLs
        github_file_url = "https://github.com/Sanctus-Peter/HNG-x/blob/main/HNG-X-1/django/core/api.py"
        github_repo_url = "https://github.com/Sanctus-Peter/HNG-x/tree/main/HNG-X-1/"

        response_data = {
            "slack_name": slack_name,
            "current_day": current_day,
            "utc_time": utc_time,
            "track": track,
            "github_file_url": github_file_url,
            "github_repo_url": github_repo_url,
            "status_code": 200,
        }

        serializer = DetailSerializer(data=response_data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)