from django.conf import settings
from django.db import models


class Tag(models.Model):
    """Tag to be used for a recipe."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient to be used for a recipe."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe object"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    # DecimalField: 10진수 표현
    #  - max_digits: 최대 자리수
    #  - decimal_places: 저장되는 소수 자리
    #  - coerce_to_string: True(return 문자열), False(return Decimal)
    #        기본값 = COERCE_DECIMAL_TO_STRING(설정), 기본 True
    #  - max_value
    #  - min_value
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    tags = models.ManyToManyField('Tag')
    # auto 일자
    # auto_now=True -> 수정일자, save 될때마다 현재날짜로 갱신
    # auto_now_add=True -> 생성일자, insert(최초 저장)시에만 현재날짜로 저장

    created_at = models.DateTimeField(auto_now=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
