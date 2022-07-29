from rest_framework import generics, status
from rest_framework.response import Response
from .models import User


class DeleteUser(generics.DestroyAPIView):
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(username=self.request.user.username)
            return instance
        except User.DoesNotExist:
            content = {'No User Exist': 'nothing to see here'}
            return Response(content, status=status.HTTP_404_NOT_FOUND)
