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
