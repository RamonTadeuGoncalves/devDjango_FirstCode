"""helloDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<int:idade>', views.hello), #deve apontar para alguma método que retornará alguma coisa na tela. Aponta pra o views do core.
    #podemos colocar parâmetros dentro do path, como no nosso exemplo temos o parâmetro <nome>.
    #Para isso, precisa ir na função def hello(request) e acrescentar o parâmetro nome.
    #<int:idade> parâmetro idade adicionado à URL, e deve ser do tipo int, qualquer outro formato dará erro.
]
