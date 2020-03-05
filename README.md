# dev_django
Primeira aplicação web utilizando o framework Django.
O projeto inicial se chama hellodjango, e dentro dele foi criado a aplicação core.

Nesse primeiro contato com o Django foi utilziado comandos simples para exibir no navegador web um Hello, seguido de um nome e de uma idade.
Por exemplo, rodando o arquivo manage.py, será exibido em tela (navegador web) a seguinte mensagem: Hello NOME de IDADE anos de idade.

Para rodar o arquivo manage.py:
1)  Abra o terminal e navegue até o diretório onde se encontra o arquivo manage.py
2)  Em seguida, digite o comando python manage.py runserver
    Algumas informações aparecerão no terminal. Procure por: Starting development server at http://127.0.0.1:8000/
3)  Clique no link http exibido no seu terminal. Você será direcionado para o navegador web.
4)  Ao abrir o navegado, você precisará completar o endereço da seguinte forma para que a mensagem seja exibida:
    127.0.0.1:8000/hello/Ramon/32
5)  Ao pressionar ENTER, a mensagem é exibida: Hello Ramon de 32 anos de idade
6)  Para rodar a função somar, informe, por exemplo: http://127.0.0.1:8000/somar/10/2
    Resultado: A soma dos números 10 + 2 é: 12
7)  Para rodar a função subtrair, informe, por exemplo: http://127.0.0.1:8000/subtrair/10/2
    Resultado: A subtração dos números 10 - 2 é: 8
8)  Para rodar a função multiplicar, informe, por exmplo: http://127.0.0.1:8000/multiplicar/10/2
    Resultado: A multiplicação dos números 10 * 2 é: 20
9)  Para rodar a função dividir, informe, por exemplo: http://127.0.0.1:8000/dividir/10/2
    Resultado:  A divisão dos números 10 / 2 é: 5.0
