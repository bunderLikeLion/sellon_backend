from django.db import models
from config.models import BaseModel
from django.core.validators import MaxValueValidator, MinValueValidator

from dealing.models import Dealing
from user.models import User


class UserEvaluation(BaseModel):

    class Meta:
        db_table = 'user_evaluations'
        verbose_name = 'UserEvaluation'
        verbose_name_plural = 'UserEvaluations'

        constraints = [
            models.UniqueConstraint(
                fields=['evaluated_user', 'dealing'],
                name='unique_evaluated_user_dealing',
            )
        ]

    evaluator = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='평가 하는 유저',
        related_name='evaluator',
    )
    evaluated_user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='평가 받는 유저',
        related_name='evaluated_user',
    )
    dealing = models.ForeignKey(
        Dealing,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='거래 내역'
    )
    rate = models.IntegerField(
        verbose_name='점수',
        null=False,
        validators=[
            MaxValueValidator(5, message='점수는 5까지 설정할 수 있습니다.'),
            MinValueValidator(1, message='점수는 0보다 커야 합니다.')
        ],
    )
