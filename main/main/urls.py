"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
import main.views
import newsletter.views
import diet.views
import workout.views

app_name = "main"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.index, name='index'),
    path('news/', main.views.newspage, name='newspage'),
    path('diet/', main.views.dietpage, name='dietpage'),
    path('workout/', main.views.workoutpage, name='workoutpage'),
    path('user/', include('user.urls')),
    path('workout/routine1',main.views.routine1, name='routine1'),
    path('workout/routine2',main.views.routine2, name='routine2'),
    path('workout/routine3',main.views.routine3, name='routine3'),
    path('workout/routine4',main.views.routine4, name='routine4'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
