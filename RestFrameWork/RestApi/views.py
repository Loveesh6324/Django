from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializer import StudentSerializer

import boto3
s3 = boto3.resource(
    service_name='s3',
    region_name='ap-south-1',
    aws_access_key_id='AKIAULICBHAMZPW5FXKN',
    aws_secret_access_key='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'
)

# GenericsApiView---------------------------------------------------------------------------------------------------


class classget(generics.ListAPIView):
    queryset = Student.objects.get_queryset()
    serializer_class = StudentSerializer


class classgetpost(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.get_queryset()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


class classputdel(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    lookup_field = 'pk'
    queryset = Student.objects.get_queryset()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]


# Class based API---------------------------------------------------------------------------------------------------


class StudentGetPostList(APIView):

    def get(self, request):
        if request.method == 'GET':
            get_obj = Student.objects.all()
            serializer = StudentSerializer(get_obj, many=True)
            return Response(serializer.data, status=200)

    def post(self, request):
        if request.method == 'POST':
            _data = request.data.values()
            user_data = list(_data)
            if type(user_data[0]) == type("") and type(user_data[1]) == type("") and type(user_data[2]) == type(1):
                if len(user_data[0]) == 0 or len(user_data[1]) == 0 or len(str(user_data[2])) == 0:
                    return Response("One or more entries missed", status=204)
                else:
                    if Student.objects.filter(email=user_data[1]):
                        # checks only in email feild.
                        return Response("Dublicate data is not allowed", status=226)
                    else:
                        serializer = StudentSerializer(data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=201)
                        return Response(serializer.errors)
            else:
                return Response("Type error", status=500)


class StudentPutDelList(APIView):
    def put(self, request, pk):
        if request.method == 'PUT':
            _data = request.data.values()
            user_data = list(_data)
            tut = Student.objects.get(pk=pk)
            if type(user_data[0]) == type("") and type(user_data[1]) == type("") and type(user_data[2]) == type(1):
                if len(user_data[0]) == 0 or len(user_data[1]) == 0 or len(str(user_data[2])) == 0:
                    return Response("One or more entries missed", status=204)
                else:
                    if(list(_data) == [tut.name, tut.email, tut.age]):
                        # checks only in email feild.
                        return Response("Dublicate data is not allowed", status=226)
                    else:
                        serializer = StudentSerializer(tut, data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            return Response(serializer.data, status=200)
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response('Type error', status=500)

    def delete(self, request, pk):
        if request.method == 'DELETE':
            tut = Student.objects.get(pk=pk)
            tut.delete()
            return Response({'message': 'deleted successfully!'}, status=200)


# Function based API------------------------------------------------------------------------------------------------
@api_view(['GET'])
def getapi(request):
    if request.method == 'GET':
        get_obj = Student.objects.all()
        serializer = StudentSerializer(get_obj, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def postapi(request):
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['PUT'])
def putapi(request, pk):
    if request.method == 'PUT':
        tut = Student.objects.get(pk=pk)

        serializer = StudentSerializer(tut, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['DELETE'])
def deleteapi(request, pk):
    if request.method == 'DELETE':
        tut = Student.objects.get(pk=pk)
        tut.delete()
        return Response({'message': 'deleted successfully!'})


@api_view(['GET'])
def s3get(request):
    if request.method == 'GET':
        get_obj = s3.Bucket('loveesh3601')
        for obj in get_obj.objects.all():
            body = obj.get()['Body'].read()
        return Response(body)