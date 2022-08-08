from django.db import models
from django.db import transaction
from django.core.exceptions import ValidationError


from config.models import BaseModel
from user.models import User
from dealing.models import Dealing


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

    @property
    def dealing_obj(self):
        return Dealing.objects.find(pk=self.dealing) if isinstance(self.dealing, int) else self.dealing

    def clean(self):
        self.validate_in_progress_dealing()

    def validate_in_progress_dealing(self):
        dealing = self.dealing_obj

        if dealing.is_completed:
            raise ValidationError({'dealing': '거래 종료 후에는 메세지를 보낼 수 없습니다.'})

    @transaction.atomic
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        super().save(force_insert, force_update, using, update_fields)
