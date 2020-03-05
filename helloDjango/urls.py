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
    #podemos colocar parâmetros dentro do path, como no nosso exemplo temos o parâmetro <nome>.
    #Para isso, precisa ir na função def hello(request) e acrescentar o parâmetro nome.
    #<int:idade> parâmetro idade adicionado à URL, e deve ser do tipo int, qualquer outro formato dará erro.
    path('hello/<nome>/<int:idade>', views.hello), #deve apontar para alguma método que retornará alguma coisa na tela. Aponta pra o views do core.

    #Criando rota para cálculo da soma de dois números inteiros
    path('somar/<int:num1>/<int:num2>', views.somar),#Aponta para a função somar que retornará o resultado em tela.

    #Criando rota para cálculo da subtração de dois números inteiros
    path('subtrair/<int:num1>/<int:num2>', views.subtrair),#Aponta pra a função subtrair que retornará o resultado em tela.

    #Criando rota para cálculo da multiplicação de dois números inteiros
    path('multiplicar/<int:num1>/<int:num2>', views.multiplicar),#Aponta pra a função multiplicar que retornará o resultado em tela.

    #Criando rota para cálculo da divisão de dois números inteiros
    path('dividir/<int:num1>/<int:num2>', views.dividir),#Aponta para a função dividir que retornará o resultado em tela.

]
