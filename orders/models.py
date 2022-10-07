# from django.db import models
# from django.utils.translation import gettext_lazy as _
#
# from carts.models import Purchase
# from main.models import Item
# from users.models import User
#
#
# class OrderStory(models.Model):
#     customer_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'))
#     product_id = models.ForeignKey(Item, on_delete=models.NOT_PROVIDED, verbose_name=_('Product name'))
#     order_id = models.ForeignKey(Purchase, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=0, verbose_name=_('Quantity'))
#     product_name = models.CharField(null=True, max_length=50, verbose_name=_('Product name'))
#     unit_price = models.IntegerField(null=True, verbose_name=_('Price'))
