from django.conf.urls import url, include
from . import views
from opt_online.clviews import GoodListView, GoodView
# Create your views here.


# urlpatterns = [
# 	url(r'^$',  views.index, name='index'),
# 	url(r"^good/(?P<code>\d+)/$", views.good, name='good'),
# ]

urlpatterns = [
	url(r'^(?:(?P<cat_id>\d+)/)?$',  GoodListView.as_view(), name='index'),
	url(r"^good/(?P<code>\d+)/$", GoodView.as_view(), name='good'),
]