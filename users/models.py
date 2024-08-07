from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='email address'
    )

    phone = models.CharField(
        max_length=35,
        verbose_name='Номер телефона',
        blank=True, null=True,
        help_text='Введите номер телефона в формате +7 (XXX)')
    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        blank=True, null=True,
        help_text='Выберите страну'
    )
    avatar = models.ImageField(
        upload_to='users/avatars/',
        verbose_name='Аватар',
        blank=True, null=True,
        help_text='Загрузите аватар'
    )

    token = models.CharField(
        max_length=100,
        verbose_name='Токен',
        blank=True, null=True,
        help_text='Токен для входа в систему'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']

    def __str__(self):
        return self.email
