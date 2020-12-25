from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('runWebCrawlTask/', views.runWebCrawlTask, name="runWebCrawlTask"),
]