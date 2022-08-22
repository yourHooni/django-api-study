"""
    Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

# User model 참조 방법
# 1. from django.contrib.auth.models import User
#    -> 유지보수 어려움
# 2. from django.contrib.auth import get_user_model
#    -> 객체 인스턴스 리턴
#       django 앱이 로드되는 순간 실행, 유효하지 않은 사용자 모델 객체가 리턴될수 있음
#       INSTALLED_APPS 변경 등 앱 다시 로드시 문제 생길 확률 높아짐
# 3. (추천) from django.conf import settings: settings.AUTH_USER_MODEL
#    -> 외래키 모델 전달시 문자열 리턴
#       외래키가 임포트될 때 모델 클래스 탐색 실패시, 모든 앱이 로드될때까지 탐색 중단
#       항상 올바른 사용자 모델을 받을수 있음

# 인증 관련
# django.contrib.auth: 장고에서 제공하는 인증시스템
# rest_framework.authtoken: TokenAuthentication(토큰 기반 인증)


class UserManager(BaseUserManager):
    """Manager for users(include superuser)."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""

        if not email:
            raise ValueError('User must have an email address')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        # set encrypted password
        # set_password <- AbstractBaseUser
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and saves a new super user."""
        # user = self.create(email=self.normalize_email(email), password=password)
        user = self.create(email=self.normalize_email(email), **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
