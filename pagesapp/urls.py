from django.urls import path
from .views import HomePageView, AboutPageView, BasePageView, ContactPageView, NewsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('base/', BasePageView.as_view(), name="base"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('news/', NewsPageView.as_view(), name="news"),
]
