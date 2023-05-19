from django.db import models
from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    creator = models.ForeignKey("accounts.User", on_delete = models.CASCADE, verbose_name=_('creator'), related_name=_('creator_post'))
    title = models.CharField(verbose_name = _('title'),max_length = 100)
    body = models.TextField(verbose_name=_('body'))
    created_at = models.DateTimeField(verbose_name = _('created'),auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name=_('updated'),auto_now = True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'posts_post'

    def __str__(self):
        return self.title