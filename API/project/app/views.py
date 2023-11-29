from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .managers import PerevalManager

class SubmitDataView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        result = PerevalManager.submit_data(data)
        return Response(result, status=result['status'])

