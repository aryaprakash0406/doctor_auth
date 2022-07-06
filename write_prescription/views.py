from multiprocessing.spawn import import_main_path
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from write_prescription.renderers import UserRenderer
from write_prescription.serializers import prescribe_medicineSrializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class prescribeMedicineView(APIView):
    renderer_classes = [UserRenderer]
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializers=prescribe_medicineSrializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response({'msg':'Data submitted'}, status=status.HTTP_201_CREATED)
