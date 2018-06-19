from django.views.generic.base import TemplateView
from django.views.generic.list  import ListView, BaseListView
from django.core.paginator import Paginator, InvalidPage
from .models import Category, Goods
from django.http import HttpResponse, Http404


class GoodListView(ListView):
	template_name = 'opt_online/index.html'
	#queryset = Goods.objects.all().order_by('code')
	#context_object_name = 'ivan_list'
	paginate_by = 2
	category = None

	def get(self, request, *args, **kwargs):
		if self.kwargs['cat_id']:
			self.category = Category.objects.get(pk=kwargs['cat_id'])
		return super(GoodListView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(GoodListView, self).get_context_data(**kwargs)
		context['cats'] = Category.objects.order_by('name')
		context['category'] = self.category
		return context

	def get_queryset(self):
		if self.category:
			return Goods.objects.filter(category=self.category).order_by('code')
		else:
			return Goods.objects.all().order_by('code')

	# def get_context_data(self, **kwargs):
	# 	context = super(GoodListView, self).get_context_data(**kwargs)
	# 	try:
	# 		page_num = self.request.GET['page']   
	# 	except KeyError:
	# 		page_num = 1
	# 	context['cats'] = Category.objects.order_by('name')	
	# 	if kwargs['cat_id']:
	# 		context['category'] = Category.objects.get(pk = kwargs['cat_id'])
	# 		paginator = Paginator(Goods.objects.filter(category = context['category']).order_by('code'), 1)
	# 	else:
	# 		paginator = Paginator(Goods.objects.all().order_by('code'), 2)
	# 	try:
	# 		context['goods'] = paginator.page(page_num)
	# 	except InvalidPage:
	# 		context['goods'] = paginator.page(1)
	# 	return context





class GoodView(TemplateView):
	template_name = 'opt_online/good.html'
	def get_context_data(self, **kwargs):
		context = super(GoodView, self).get_context_data(**kwargs)
		try:
			context['pn'] = self.request.GET['page']
		except KeyError:
			context['pn'] = 1
		good = Goods.objects.get(code=context['code'])
		context['good'] = good
		return context