from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse("<h1>Hello {} de {} anos de idade</h1>".format(nome, idade))#Rertorna na tela Hello World
    #<h1> formatação html, retorna o texto como se fosse um título. Isso é possível por conta do HttpResponse que está sendo importado
    #Parâmetro nome foi acrescentado para que seja possível exibir em tela o nome desejado.