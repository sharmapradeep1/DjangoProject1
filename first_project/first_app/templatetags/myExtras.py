from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values of arg from String
    """
    return value.replace(arg,'')

#register.filter('cut',cut) replaced by decorator above


##### Pattern 11 Step 70, home 3 - Add function cut to filters library and use in template for home 3
