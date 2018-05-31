from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# views are code that's run when user visits api endpoint

class HelloApiView(APIView):
    """Test API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'is mapped manually to URLS'
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
