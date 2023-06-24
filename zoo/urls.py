from django.urls import path
from zoo.views import ZooView, Zoo2View, CategoryListView, uslygi_view
app_name = 'zoo'
urlpatterns=[
    path('', ZooView.as_view(), name='zoo'),
    path('tovar/', Zoo2View.as_view(), name='tovar'),
    path('catalog/', CategoryListView.as_view(), name='catalog'),
    path('uslygi/', uslygi_view, name='uslygi'),
 

    ]