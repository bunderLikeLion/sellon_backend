from django.db import models
from config.models import BaseModel
from user.models import User


class Message(BaseModel):

    class Meta:
        db_table = 'messages'
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='받는 사람',
        related_name='receiver',
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        verbose_name='보내는 사람',
        related_name='sender',
    )
    content = models.TextField(
        max_length=300,
        null=False,
        verbose_name='쪽지 내용'
    )
    dealing = models.ForeignKey(
        'dealing.Dealing',
        on_delete=models.SET_NULL,
        verbose_name='거래',
        related_name='messages',
        null=True,
    )
