"""
URL configuration for myinstagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import Main
from content.views import Sub,UploadFeed
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', Main.as_view()),
    path('main/',Sub.as_view()),
    # path('content/upload',UploadFeed.as_view())
    path('',include('content.urls')),
    path('',include('user.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 에 이미지 파일을 올렸을때 해당 이미지를 조회할수 있게끔