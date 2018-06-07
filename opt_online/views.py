from django.shortcuts import render
from .models import Goods, Category
	

def hello(request):
	return render(request, 'opt_online/hello.html', {})



def index(request):
	goods = Goods.objects.all()
	#paginator = Paginator(Good.objects.filter(category=cat).order_by('name'), 1)
	return render(request, 'opt_online/index.html', {'goods': goods})

def good(request, code):
	good = Goods.objects.get(code=code)
	#good = code
	return render(request, 'opt_online/good.html', {'good': good, 'req': request})


# def categories(request):
# 	categories = Category.objects.all()
# 	list_categories = "<h1>Cписок категорий:</h1>"
# 	for category in categories:
# 		list_categories  += "<h2>№{} {}".format(category.pk, category.name)
# 	return HttpResponse(list_categories)	