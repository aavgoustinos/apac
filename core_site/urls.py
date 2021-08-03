from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('about', views.about, name="about"),
    path('news', views.news, name="news"),
    path('<slug:slug>/', views.page, name='page'),
    path('news/<slug:slug>/', views.new, name='new'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)