from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from product.models import ProductGroup


@receiver(post_save, sender=ProductGroup)
def product_group_post_save(sender, **kwargs):
    auction = kwargs['instance'].auction
    auction.product_groups_count += 1
    auction.save()


@receiver(post_delete, sender=ProductGroup)
def product_group_post_delete(sender, **kwargs):
    auction = kwargs['instance'].auction
    auction.product_groups_count -= 1
    auction.save()
