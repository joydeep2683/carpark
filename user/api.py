from django.http import Http404

from rest_framework.views import APIView

from user.serializer import UserSerializer

from user.models import Users, UserDetails, UserPreferance

class UserDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return Users.objects.get(pk=pk)
        except Users.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        pass

    def post(self, request):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass