from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('',include('testapp.urls'))
    #path('', include('question.urls'))
]
