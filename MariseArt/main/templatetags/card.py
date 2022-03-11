from django import template

register = template.Library()


@register.inclusion_tag('main/components/card.html')
def card(picture, commercial):
    return {'picture': picture,
            'commercial': commercial}

