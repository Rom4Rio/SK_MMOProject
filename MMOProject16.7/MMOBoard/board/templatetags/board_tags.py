from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):

    context_copy = context['request'].GET.copy()
    for key, value in kwargs.items():
        context_copy[key] = value
    return context_copy.urlencode()
