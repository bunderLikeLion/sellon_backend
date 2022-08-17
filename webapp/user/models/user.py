""" User App Models"""
import random
from django.db import models
from django.core.files import File
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.html import format_html
from sorl.thumbnail import get_thumbnail

RANDOM_PROFILE = [
    'avatars/1.jpg',
    'avatars/2.jpg',
    'avatars/3.jpg',
    'avatars/4.jpg',
    'avatars/5.jpg',
    'avatars/6.jpg',
    'avatars/7.jpg',
    'avatars/8.jpg'
]


def get_random_profile_filename():
    return random.choice(RANDOM_PROFILE)


def user_directory_path(instance, filename):
    return 'avatars/user_{}/{}'.format(instance.username, filename)


class UserManager(BaseUserManager):
    """ModelManager definition for User Model"""

    def _create_user(self, username, password, **kwargs):
        user = self.model(
            username=username,
            **kwargs,
        )
        user.set_password(password)
        user.save()

    def create_user(self, username, password, **kwargs):
        """일반 유저 생성 메소드"""
        self._create_user(username, password, **kwargs)

    def create_superuser(self, username, password, **kwargs):
        """슈퍼 유저(superuser) 생성 메소드"""
        kwargs.setdefault('is_superuser', True)
        self._create_user(username, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""

    class Meta:
        db_table = 'users'
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    USERNAME_FIELD = 'username'

    username = models.CharField(
        unique=True,
        max_length=20,
    )  # 사용자명
    email = models.EmailField(
        unique=True,
    )  # 이메일

    created_at = models.DateTimeField(
        auto_now_add=True
    )  # 유저 레코드가 생성된 일자
    updated_at = models.DateTimeField(
        auto_now=True
    )  # 유저 레코드가 수정된 일자
    avatar = models.ImageField(
        null=True,
        blank=True,
        verbose_name='프로필 이미지',
        upload_to=user_directory_path,
    )   # 유저 프로필 이미지
    completed_dealings_count = models.PositiveIntegerField(
        default=0,
        verbose_name='거래횟수',
    )

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser

    @property
    def avatar_preview(self):
        if self.avatar:
            _thumbnail = get_thumbnail(
                self.avatar,
                '300x300',
                upscale=False,
                crop=False,
                quality=100
            )
            return format_html(
                '<img src="{}" width="{}" height="{}">'.format(
                    _thumbnail.url, _thumbnail.width, _thumbnail.height
                )
            )
        return ''

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self._state.adding:
            filename = get_random_profile_filename()
            f = open('static/' + filename, 'rb')
            self.avatar = File(f)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self) -> str:
        return f'[{self.id}] {self.username} ({self.email})'
