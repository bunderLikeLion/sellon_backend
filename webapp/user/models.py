""" User App Models"""

from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


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

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_superuser
