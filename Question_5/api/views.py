from openpyxl import Workbook
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from api.serializers import UserSerializer
from quesapp.models import User

# Create your views here.

wb = Workbook()


class UserCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        ws = wb.active
        ws.append([instance.name, instance.dob, instance.country])
        wb.save("sample.xlsx")
        return Response(data={"status": "successful"}, status=status.HTTP_200_OK)


class ReadOnlyUserModelViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
