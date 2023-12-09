from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .managers import PerevalManager
from .models import Pereval
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.mixins import UpdateModelMixin
from .serializers import PerevalSerializer

class SubmitDataView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        result = PerevalManager.submit_data(data)
        return Response(result, status=result['status'])

class GetSingleSubmissionView(RetrieveAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    @swagger_auto_schema(
        responses={
            200: "Успешно обновлено",
            404: "Запись не найдена",
        })
    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Pereval.DoesNotExist:
            return Response({'status': 404, 'message': 'Запись не найдена'}, status=status.HTTP_404_NOT_FOUND)

class PatchSubmissionView(UpdateModelMixin, APIView):
    @swagger_auto_schema(
        responses={
            200: "Успешно обновлено",
            400: "Ошибка валидации данных",
            404: "Запись не найдена",
        }
    )
    def patch(self, request, *args, **kwargs):
        try:
            instance = Pereval.objects.get(id=self.kwargs.get('pk'), status='new')
        except Pereval.DoesNotExist:
            return Response({'state': 0, 'message': 'Запись не найдена или нельзя редактировать в текущем статусе'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PerevalSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'state': 1, 'message': 'Успешно обновлено'})
        else:
            return Response({'state': 0, 'message': 'Ошибка валидации данных'}, status=status.HTTP_400_BAD_REQUEST)

class GetUserSubmissionsView(ListAPIView):
    serializer_class = PerevalSerializer

    @swagger_auto_schema(
        responses={
            200: "Успешно",
            500: "Внутренняя ошибка сервера",
        }
    )
    def get_queryset(self):
        email = self.request.query_params.get('user__email', '')
        return Pereval.objects.filter(user_email=email)

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception:
            return Response({'status': 500, 'message': 'Внутренняя ошибка сервера'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)