from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    """
    Расширенная модель пользователя с дополнительным полем типа пользователя
    """
    USER_TYPE_CHOICES = (
        ('admin', 'professor'),
        ('professor', 'professor'),
        ('student', 'student'),
    )
    
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='student',
        verbose_name=_('Тип пользователя'),
    )
    
    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        
    def __str__(self):
        return self.username