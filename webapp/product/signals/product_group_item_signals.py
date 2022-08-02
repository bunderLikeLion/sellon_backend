from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.forms import ValidationError

from product.models import ProductGroupItem, Product
from product.models.product_group import ProductGroup


@receiver(m2m_changed, sender=ProductGroupItem)
def product_group_item_changed(sender, instance, **kwargs):
    product_group = instance

    if product_group is not None and not isinstance(product_group, ProductGroup):
        raise ValidationError({'product_group': '정상적인 접근이 아닙니다'})

    if not product_group.auction:
        raise ValidationError({'auction': '경매장 정보가 없습니다'})

    auction = product_group.auction

    if auction.is_ended:
        raise ValidationError({'auction': '이미 종료된 경매장입니다'})

    action = kwargs.pop('action', None)
    product_ids = list(kwargs.pop('pk_set', {}))

    if action == 'pre_remove':
        # NOTE: 이후 개발을 위해 남겨둠.
        pass
    elif action == 'post_remove':
        # NOTE: 그룹에서 제거된 product의  상태를 HIDDEN으로 변경함.
        products = Product.objects.filter(pk__in=product_ids)
        products.update(status=Product.HIDDEN_STATUS)
    elif action == 'pre_add':
        products = Product.objects.filter(pk__in=product_ids)

        product_statuses = list(set(products.values_list('status', flat=True)))
        product_user_ids = list(set(products.values_list('user', flat=True)))

        if len(product_user_ids) > 1 or product_user_ids[0] != product_group.user.id:
            raise ValidationError({'product_ids': '다른 유저의 상품은 등록할 수 없습니다'})

        if len(product_statuses) > 1 or product_statuses[0] != Product.HIDDEN_STATUS:
            raise ValidationError({'product_ids': '이미 사용중인 상품을 선택했습니다'})
    elif action == 'post_add':
        # NOTE: 그룹에 추가된 product의  상태를 IN_AUCTION으로 변경함.
        products = Product.objects.filter(pk__in=product_ids)
        products.update(status=Product.IN_AUCTION_STATUS)
