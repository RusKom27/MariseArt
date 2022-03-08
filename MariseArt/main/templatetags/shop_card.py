from django import template

register = template.Library()


@register.inclusion_tag('main/components/shop_card.html')
def shop_card(picture_info):
    return {'picture_info': picture_info}

