from django.views.generic.base import TemplateView
from django.views.generic.list  import ListView, BaseListView
from django.core.paginator import Paginator, InvalidPage
from .models import Category, Goods
from django.http import HttpResponse, Http404


class GoodListView(ListView):
	template_name = 'opt_online/index.html'
	paginate_by = 1
	category = None

	def get(self, request, *args, **kwargs):
		"""
		Присваивает gеременной контекста данных
		в которой должен храниться список
		записей, этот самый список.
		(То есть инициализирует сам context)
		"""

		if self.kwargs['cat_id']:
			self.category = Category.objects.get(pk=kwargs['cat_id'])
		return super(GoodListView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		"""
		Создает контекст данных
		"""
		context = super(GoodListView, self).get_context_data(**kwargs) # Формирует сам контекст данных и заполнит его начальными данными, в частности значениями полученными контроллером параметров.
		context['cats'] = Category.objects.order_by('name')
		context['category'] = self.category
		return context

	def get_queryset(self): 
		"""
		Этот метод вызврощает спичсок 
		записей которые будут выводиться 
		на экран
		""" 

		if self.category:
			return Goods.objects.filter(category=self.category).order_by('code')
		else:
			return Goods.objects.all().order_by('code')



class GoodView(TemplateView):
	template_name = 'opt_online/good.html'
	def get(self, request, *args, **kwargs):
		return super(GoodView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(GoodView, self).get_context_data(**kwargs)
		try:
			context['pn'] = self.request.GET['page']
		except KeyError:
			context['pn'] = 1
		context['good'] = Goods.objects.get(code=context['code'])
		return context


	def get_queryset(self):
		return Goods.objects.get(code=context['code'])



# class GoodView(TemplateView):
# 	template_name = 'opt_online/good.html'
# 	def get_context_data(self, **kwargs):
# 		context = super(GoodView, self).get_context_data(**kwargs)
# 		try:
# 			context['pn'] = self.request.GET['page']
# 		except KeyError:
# 			context['pn'] = 1
# 		good = Goods.objects.get(code=context['code'])
# 		context['good'] = good
# 		return context