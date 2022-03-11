from django import template

register = template.Library()


@register.inclusion_tag('main/components/cards.html')
def cards(pictures, commercial):
    return {'pictures': pictures,
            'commercial': commercial}

