from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserAbstractSerializer
from .models import User


class DestroyUserAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(username=self.request.user.username)
            return instance
        except User.DoesNotExist:
            content = {'No User Exist': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)


class RetrieveUserAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserAbstractSerializer
