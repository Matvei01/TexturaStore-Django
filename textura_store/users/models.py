from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True, null=True, verbose_name='Аватар')
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    is_subscribed = models.BooleanField(default=False, verbose_name="Подписка на рассылку")

    class Meta:
        db_table = 'user'
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
