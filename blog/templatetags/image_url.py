# Used to find dictionary key of post body images since dict keys are not accessible from django's templates
from django import template

register = template.Library()

@register.filter(name='image_url')
def image_url(dict, key):
	return dict[key].image.url