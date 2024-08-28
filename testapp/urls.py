from django.urls import path
from .views import home,welcome,login,signup
urlpatterns = [
    path('', home,name="home"),
    path('signup/', signup,name="signup"),
    path('login/', login,name="login"),
    path('welcome/',welcome,name='welcome')
]