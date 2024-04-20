from .serializers import (
    DoctorSerializer,
    DoctorExperienceSerializer,
    GetAllDoctorSerializer,
)
from .models import Doctor, DoctorExperience
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from v1.renderers import ErrorRenderer
from datetime import datetime
from v1.api.account.models import User
from v1.api.rating.models import Rating
from v1.api.rating.serializers import RatingSerializer
# ADD DOCTOR VIEW
class PostDoctorView(APIView):
    renderer_classes = [ErrorRenderer]
    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = User.objects.get(pk=serializer.data["primary_id"])
            user.role='doctor'
            user.save()
            return Response(
                {
                    "message": "Doctor details is saved Successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )


# ADD DOCTOR EXPERIENCE VIEW
class PostDoctorExperienceView(APIView):
    renderer_classes = [ErrorRenderer]

    def post(self, request, format=None):
        serializer = DoctorExperienceSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "message": "Doctor experience details is saved Successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )


# EDIT DOCTOR VIEW
class EditDoctorView(APIView):
    renderer_classes = [ErrorRenderer]

    def get(self, request,pk=None, format=None, ):
        if pk is None:
            try:
                doctors = Doctor.objects.all()
                serializer = GetAllDoctorSerializer(doctors, many=True)
                return Response(
                    {"msg": "all doctors is found", "Data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            except:
                return Response(
                    {"msg": "no data is found", "data": {}},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            try:
                doctor = Doctor.objects.get(primary_id=pk)
                serializer = DoctorSerializer(doctor)
                # Calculate age from date of birth
                experience = DoctorExperience.objects.filter(primary_id=pk)
                experience_serializer=DoctorExperienceSerializer(experience,many=True)
                total_years = 0
                total_months = 0
                for exp in experience_serializer.data:
                    exp_str = exp["calculated_experience"].split()
                    years = int(exp_str[0]) if len(exp_str) > 1 else 0
                    months = int(exp_str[2]) if len(exp_str) > 3 else 0
                    total_years += years
                    total_months += months
                # Adjust total months if it exceeds 12
                total_years += total_months // 12
                total_months = total_months % 12
                total_experience = f"{total_years} years, {total_months} months"
                dob = doctor.dob
                current_date = datetime.now().date()
                age = (
                    current_date.year
                    - dob.year
                    - ((current_date.month, current_date.day) < (dob.month, dob.day))
                )
                rating = Rating.objects.filter(ratee_id=pk)
                review=rating.count()
                rating_serializer=RatingSerializer(rating,many=True)
                total_stars = 0
                for star in rating_serializer.data:
                    total_stars+=star['star']
                serialized_data = serializer.data 
                serialized_data["age"] = age 
                serialized_data['experience']=total_experience
                serialized_data["review"] = review
                serialized_data['total_star']=total_stars/review

                return Response(
                    {"msg": "data of single user is get", "data": serialized_data},
                    status=status.HTTP_200_OK,
                )
            except Doctor.DoesNotExist:
                return Response(
                    {"msg": "no data is found", "data": {}},
                    status=status.HTTP_404_NOT_FOUND,
                )

    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            return None

    def patch(self, request, pk, format=None):
        doctor = self.get_object(pk)
        if not doctor:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if "email" in request.data:
            doctor.primary_id.email = request.data["email"]
            doctor.primary_id.save()
        if "user_name" in request.data:
            doctor.primary_id.user_name = request.data["user_name"]
            doctor.primary_id.save()
        serializer = DoctorSerializer(
            doctor, data=request.data, partial=True, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response = serializer.data
            response["email"] = doctor.primary_id.email
            response["user_name"] = doctor.primary_id.user_name
            return Response(
                {
                    "msg": "doctor is updated successfully",
                    "Data": response,
                },
                status=status.HTTP_200_OK,
            )
