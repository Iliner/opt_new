from django.shortcuts import render
from .models import Goods, Category
from django.core.paginator import Paginator, InvalidPage
	


def index(request):
	try:
		page_num = request.GET['page']
	except KeyError:
		page_num = 1
	pag = Paginator(Goods.objects.all(), 2)
	try:
		goods = pag.page(page_num)
	except InvalidPage:
		goods = pag.page(1)
	return render(request, 'opt_online/index.html', {'goods': goods, 'page': page_num})

def good(request, code):
	try:
		page_num = request.GET['page']
	except KeyError:
		page_num = 1
	good = Goods.objects.get(code=code)
	#good = code
	return render(request, 'opt_online/good.html', {'good': good, 'pn': page_num})


# def categories(request):
# 	categories = Category.objects.all()
# 	list_categories = "<h1>Cписок категорий:</h1>"
# 	for category in categories:
# 		list_categories  += "<h2>№{} {}".format(category.pk, category.name)
# 	return HttpResponse(list_categories)	