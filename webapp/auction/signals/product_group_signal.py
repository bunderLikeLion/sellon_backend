from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver

from product.models import ProductGroup


@receiver(pre_save, sender=ProductGroup)
def product_group_pre_save(sender, instance: ProductGroup, **kwargs):
    if instance.id is None:
        auction = instance.auction
        auction.product_groups_count += 1
        auction.save()


@receiver(post_delete, sender=ProductGroup)
def product_group_post_delete(sender, instance: ProductGroup, **kwargs):
    auction = instance.auction
    auction.product_groups_count -= 1
    auction.save()
