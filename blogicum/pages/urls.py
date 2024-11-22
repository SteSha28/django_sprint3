from django.urls import path
from . import views


app_name = 'pages'

urlpatterns = [
    path('about/', view=views.about, name='about'),
    path('rules/', view=views.rules, name='rules'),
]
