from django.http.response import HttpResponse
from django.shortcuts import render
from product.forms import CreateBurgerForm
from product.models import Burger, Category
from django.views.generic.edit import CreateView

# Create your views here.
# Create your views here.
def import_data(request):
    import csv         
    import os

    settings_dir = os.path.dirname(__file__)
    # print(settings_dir)
    # path = settings_dir + "\maxway.csv"
    info = ''
    categories = {}
    with open(settings_dir + "\maxway_category.csv") as f:
            reader = csv.reader(f)                        
            for row in reader:                
                categories[row[0]]=Category.objects.create(
                    pk = int(row[0]),
                    name = row[1]
                    )
                info = f"{info}\n{row[0]}. {row[1]}"

    info = info + "\n\n\n"
    with open(settings_dir + "\maxway.csv") as f:
            reader = csv.reader(f)                        
            for row in reader:
                price = int(row[3].rstrip('сум').replace(" ", "")) if row[3] else 0
                Burger.objects.create(
                    name=row[1],
                    content=row[2],
                    price=price,
                    rasmi = row[0],
                    category = categories[row[4]]
                    )
                info = f"{info}\n {row[1]}\n"
    return HttpResponse("Success")



def get_product(request):
    categories = Category.objects.all()
    products = Burger.objects.all()
    products_by_categories = {}
    for c in categories:
        lst = []
        for p in products:
            if c == p.category:
                lst.append(p)
        if len(lst) != 0:
            products_by_categories[c.name] = lst

    context = {
        "categories": categories, 
        "products_by_categories": products_by_categories}
    return render(request, 'products/maxway.html', context)

def get_by_category_id(request, category_id):
    categories = Category.objects.all()
    products = Burger.objects.filter(category=category_id)
    products_by_categories = {}
    for c in categories:
        lst = []
        for p in products:
            if c == p.category:
                lst.append(p)
        if len(lst) != 0:
            products_by_categories[c.name] = lst

    context = {
        "categories": categories, 
        "products_by_categories": products_by_categories}
    return render(request, 'products/maxway.html', context)

class CreateBurgerView(CreateView):
    template_name = 'products/create.html'
    form_class = CreateBurgerForm
    success_url = '/'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context