from django.db import models

from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    tag_title = models.CharField(
        max_length=50,
        verbose_name=_("Tag's title")
    )

    tag_description = models.CharField(
        max_length=400,
        verbose_name=_("Tag's description")
    )

    discount = models.IntegerField(
        default=0,
        verbose_name=_('Discount')
    )

    def __str__(self):
        return str(self.tag_title)
