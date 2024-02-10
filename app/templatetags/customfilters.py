from django import template
register = template.Library()




def low(value):


    return value.lower()

@register.filter()
def swap(value):


    return value.swapcase()





register.filter('low',low)
# register.filter('swa',swap)




