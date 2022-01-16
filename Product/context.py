




from Product.models import Category


def header(request):
        sub_cat=[]
        parent_cat=Category.objects.all().filter(sub_cat=None).order_by('cat_title')
        for cat in parent_cat:
            sub_cat.append(cat.cattocat.all())

        context = { 
        'parent_cats':parent_cat, 
        'sub_cats':sub_cat, 
        
        }
        return context

            