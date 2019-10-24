from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    telegram_chat_id = models.CharField(max_length=255, null=True, default=None)
    telegram_username = models.CharField(max_length=255, null=True, blank=True, unique=True)

    name = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'core_users'
        ordering = ('name',)

    def __str__(self):
        return "%s" % self.telegram_username


class Item(models.Model):
    creator = models.ForeignKey(User, verbose_name="Creator", db_column='creator_id', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    amount = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        db_table = "core_itens"
        ordering = ('name',)

    def __str__(self):
        return "%s" % self.name
