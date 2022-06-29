
from django.urls import path
from . import views


app_name = 'bio'
urlpatterns = [
    path('', views.HomeViews, name='homeviews'),
    path('bip', views.BioViews, name='bioviews' ),
    path('redes/', views.Redes, name='redes'),
    path('proyectos/', views.Proyectos, name='proyectos'),
    path('historias/', views.Historias, name='historias'),
    path("citas/",views.Citas  , name="citas")
]
