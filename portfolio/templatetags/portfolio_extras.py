from django import template

register = template.Library()

@register.filter
def is_gestor(user):
    return user.is_authenticated and user.groups.filter(name='gestor-portfolio').exists()