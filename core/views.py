from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse("<h1>Hello {} de {} anos de idade</h1>".format(nome, idade))#Rertorna na tela Hello World
    #<h1> formatação html, retorna o texto como se fosse um título. Isso é possível por conta do HttpResponse que está sendo importado
    #Parâmetro nome foi acrescentado para que seja possível exibir em tela o nome desejado.

#Criando função para realizar a soma de dois números inteiros passados como argumentos via barra de endereço
def somar(request, num1, num2):
    return HttpResponse("<h1> A soma dos números {} + {} é: {}</h1>".format(num1, num2, (num1 + num2)))

#Criando função para realizar a subtração de dois números inteiros passados como argumentos via barra de endereço
def subtrair(request, num1, num2):
    return HttpResponse("<h1> A subtração dos números {} - {} é: {}</h1>".format(num1, num2, (num1 - num2)))

#Criando função para realizar a multiplicação entre dois números inteiros passados como argumentos via barra de endereço
def multiplicar(request, num1, num2):
    return HttpResponse("<h1> A multiplicação dos números {} * {} é: {}</h1>".format(num1, num2, (num1 * num2)))

#Criando função para realizar a divisão entre dois números interiso passados como argumentos via barra de endereço
def dividir(request, num1, num2):
    try:
        num1 / num2
    except:
        return HttpResponse("<h1> Não é possível fazer divisão por zero!</h1>")
    else:
        return HttpResponse("<h1> A divisão dos números {} / {} é: {}</h1>".format(num1, num2, (num1 / num2)))
