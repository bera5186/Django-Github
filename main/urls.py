from django.urls import path, include
import main.views as Views

urlpatterns = [
    path('', Views.index, name='index'),
    path('test/', Views.test, name='test'),
    path('profile/', Views.profile, name='profile'),
]
