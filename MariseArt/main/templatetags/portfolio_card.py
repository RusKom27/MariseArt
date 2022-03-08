from django import template

register = template.Library()


@register.inclusion_tag('main/components/portfolio_card.html')
def portfolio_card(picture_info):
    return {'picture_info': picture_info}

