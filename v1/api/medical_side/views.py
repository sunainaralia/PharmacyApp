# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import MedicineModel, AddressModel, OrderItem
# from .serializers import MedicineSerializer, AddressSerializer, OrderItemSerializer


# class MedicineListCreateAPIView(APIView):
#     def get(self, request):
#         medicines = MedicineModel.objects.all()
#         serializer = MedicineSerializer(medicines, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MedicineSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MedicineRetrieveUpdateDestroyAPIView(APIView):

#     def get(self, request, pk):
#         medicine = MedicineModel.objects.get(pk=pk)
#         serializer = MedicineSerializer(medicine)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         medicine = self.get_object(pk)
#         serializer = MedicineSerializer(medicine, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         medicine = self.get_object(pk)
#         medicine.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class AddressListCreateAPIView(APIView):
#     def get(self, request):
#         addresses = AddressModel.objects.all()
#         serializer = AddressSerializer(addresses, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = AddressSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AddressRetrieveUpdateDestroyAPIView(APIView):
#     def get(self, request, pk):
#         address = AddressModel.objects.get(pk=pk)
#         serializer = AddressSerializer(address)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         address = self.get_object(pk)
#         serializer = AddressSerializer(address, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         address = self.get_object(pk)
#         address.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class OrderItemListCreateAPIView(APIView):
#     def get(self, request):
#         order_items = OrderItem.objects.all()
#         serializer = OrderItemSerializer(order_items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = OrderItemSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class OrderItemRetrieveUpdateDestroyAPIView(APIView):

#     def get(self, request, pk):
#         order_item = OrderItem.objects.get(pk=pk)
#         serializer = OrderItemSerializer(order_item)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         order_item = self.get_object(pk)
#         serializer = OrderItemSerializer(order_item, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         order_item = self.get_object(pk)
#         order_item.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
