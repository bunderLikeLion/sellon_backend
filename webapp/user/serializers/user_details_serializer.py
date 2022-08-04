from dj_rest_auth.serializers import UserModel
from django.conf import settings
from drf_writable_nested.serializers import WritableNestedModelSerializer

from file_manager.serializers.abstract_image_serializer import AbstractImageSerializer


class UserDetailsSerializer(WritableNestedModelSerializer):
    """
    User model w/o password
    """
    avatar = AbstractImageSerializer(
        required=False,
    )

    @staticmethod
    def validate_username(username):
        if 'allauth.account' not in settings.INSTALLED_APPS:
            return username

        from allauth.account.adapter import get_adapter
        username = get_adapter().clean_username(username)
        return username

    class Meta:
        extra_fields = ['avatar']
        if hasattr(UserModel, 'USERNAME_FIELD'):
            extra_fields.append(UserModel.USERNAME_FIELD)
        if hasattr(UserModel, 'EMAIL_FIELD'):
            extra_fields.append(UserModel.EMAIL_FIELD)
        model = UserModel
        fields = ('pk', *extra_fields)
        read_only_fields = ('email', 'username')
