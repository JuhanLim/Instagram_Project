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

from django.urls import path

from .views import UploadFeed,Profile,UploadReply,ToggleLike,ToggleBookmark
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('content/upload',UploadFeed.as_view()), # 앱이름이 디폴트로 안붙기 때문에 content/ 까지 붙여줘야 정상 작동한다. 
    path('profile', Profile.as_view()),
    path('reply', UploadReply.as_view()),
    path('like', ToggleLike.as_view()),
    path('bookmark', ToggleBookmark.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 