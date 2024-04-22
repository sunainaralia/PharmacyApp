from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from v1.renderers import ErrorRenderer
from v1.api.account.models import User


# post patient view
class PatientView(APIView):
    renderer_classes = [ErrorRenderer]

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.get(pk=serializer.data["primary_id"])
            user.role = "patient"
            user.save()
            return Response(
                {"msg": "patient is saved successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )

    def patch(self, request, pk, format=None):
        patient = Patient.objects.get(primary_id=pk)
        if not patient:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            if "email" in request.data:
                patient.primary_id.email = request.data["email"]
                patient.primary_id.save()
            if "user_name" in request.data:
                patient.primary_id.user_name = request.data["user_name"]
                patient.primary_id.save()
            serializer = PatientSerializer(patient, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                serialized_data = serializer.data
                serialized_data["email"] = patient.primary_id.email
                serialized_data["user_name"] = patient.primary_id.user_name
                return Response(
                    {"msg": "patient is updated successfully", "data": serialized_data},
                    status=status.HTTP_200_OK,
                )
