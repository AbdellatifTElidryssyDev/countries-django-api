from django.conf.urls import url
from countries import views

urlpatterns = [
    url(r'^countries$', views.countries_list),
    url(r'^countries/(?P<pk>[0-9]+)$', views.countries_detail)

]
