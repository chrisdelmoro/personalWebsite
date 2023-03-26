from django import template

register = template.Library()

@register.filter(name='image_url')
def image_url(dict, key):
	return dict[key].image.url