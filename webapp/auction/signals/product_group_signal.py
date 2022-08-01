from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import ProductGroup


@receiver(post_save, sender=ProductGroup)
def product_group_post_save(sender, **kwargs):
    product_group = kwargs['instance']
    auction = product_group.auction
    if product_group.deleted_at is None:
        auction.product_groups_count += 1
    else:
        auction.product_groups_count -= 1

    auction.save()
