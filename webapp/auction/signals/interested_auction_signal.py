from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from auction.models import InterestedAuction


@receiver(post_save, sender=InterestedAuction)
def interested_auction_pre_save(sender, instance: InterestedAuction, created, **kwargs):
    if created:
        auction = instance.auction

        auction.interested_auctions_count += 1
        auction.save()


@receiver(post_delete, sender=InterestedAuction)
def interested_auction_post_delete(sender, instance: InterestedAuction, **kwargs):
    auction = instance.auction

    if auction is None:
        return

    auction.interested_auctions_count -= 1
    auction.save()
