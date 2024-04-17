from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MedicineModel
from .serializers import MedicineSerializer


class MedicineListCreateAPIView(APIView):
    def get(self, request):
        medicines = MedicineModel.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicineRetrieveUpdateDestroyAPIView(APIView):

    def get(self, request, pk):
        medicine = MedicineModel.objects.get(pk=pk)
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)

    def put(self, request, pk):
        medicine = self.get_object(pk)
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        medicine = self.get_object(pk)
        medicine.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
