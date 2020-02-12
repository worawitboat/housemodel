from django.contrib import admin
from django.urls import path
from myapp import views
from irisapp import views as irisview
from houseapp import views as houseapp
urlpatterns = [
    path('', houseapp.index),

    path('api/species', irisview.api_species),

    path('matmul/', views.matmul),
    path('admin/', admin.site.urls),
]
