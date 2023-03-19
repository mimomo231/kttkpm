from django import template
from ..models import Category
register = template.Library() 

@register.inclusion_tag("category_list.html")
def category_list(request_path): 
    allcategories = Category.objects.all()
    # l = [i.slug for i in allcategories]
    # print(l)
    return { 
        'allcategories': allcategories,
        'request_path': request_path 
    }