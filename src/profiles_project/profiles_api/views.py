from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

from . import serializers
from . import models
from . import permissions

# views are code that's run when user visits api endpoint

class HelloApiView(APIView):
    """Test API View."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'is mapped manually to URLS'
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""

        #passes in request data. Request object contains details of request made to api call
        serializer = serializers.HelloSerializer(data=request.data)

        #checks to make sure restrictions from serializer are satisfied
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #updates whole object
    def put(self, request, pk=None):
        """Handles updating an object"""

        return Response({'method': 'put'})


    #updates part of object
    def patch(self, request, pk=None):
        """Patch request, only updates fields provided in the request"""

        return Response({'method': 'patch'})


    def delete(self, request, pk=None):
        """Delete an object"""

        return Response({'method': 'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test api viewset"""

    serializer_class = serializers.HelloSerializer

    #these don't use http functions
    #they use different functions you would perform on an object
    #
    #Viewsets can also use Routers!

    def list(self, request):
        """return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update, delete)',
            'Automatically maps to URLs using Routers',
            'provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})


    def create(self, request):
        """create a new hello message."""
        serializer = serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """handles getting an object by its ID."""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """handles updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """handles updating part of the object."""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles removing an object"""

        return Response({'http_method': 'DELETE'})

#Model viewset takes care of logic for your model items
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading, and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,) #uses a comma so PYthon knows to create as a tuple
    permission_classes = (permissions.UpdateOwnProfile,) #include commas so you can add additional permissions/authentications
