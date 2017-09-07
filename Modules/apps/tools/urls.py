from django.conf.urls import url
from Modules.apps.tools import views

urlpatterns = {
    url(r'^$', views.index),
    url(r'^menu1$',views.menu1),
    url(r'^menu2$',views.menu2),
}
