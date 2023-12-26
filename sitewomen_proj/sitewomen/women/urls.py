from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    # path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    # path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    # # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
    # path('archive/<year4:year>/', views.archive, name='archive'),
	path('addpage/', views.addpage, name='add_page'),
	path('contact/', views.contact, name='contact'),
	path('login', views.login, name='login'),
	path('post/<int:post_id>/', views.show_post, name='post'),
]
