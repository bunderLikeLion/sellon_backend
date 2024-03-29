from dj_rest_auth.serializers import JWTSerializer
from .user_abstract_serializer import UserAbstractSerializer


class UserLoginSerializer(JWTSerializer):
    user = UserAbstractSerializer(read_only=True)
