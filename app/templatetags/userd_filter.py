from django import template

register=template.Library()
@register.filter()
def swap(value):
    return value.swapcase()

@register.filter()
def title(value):
    return value.title()

@register.filter()
def count(value,arg):
    c=0
    for i in range(len(value)):
        if arg==value[i:i+len(arg)]:
            c+=1
    return c

#register.filter('count',count)
#register.filter('title', title)
#register.filter('swap',swap)