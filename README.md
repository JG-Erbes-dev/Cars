
# Cars
Projeto das aulas do curso Django Master, ministrado pelo Felipe Azambuja.

A aplicação web foi desenvolvida em Python, utilizando o Django e integrando a API de IA do Google Gemini.

A aplicação é simples e possui uma home page com visualização de carros, tem opção de ver detalhes dos carros, login, registro de usuário e de carros, e possui IA Gemini integrada para criação de descrição dos carros.

## Etiquetas
![Static Badge](https://img.shields.io/badge/License-MIT-yellow?style=flat)
![Static Badge](https://img.shields.io/badge/Framework-Django-green?style=flat)
![Static Badge](https://img.shields.io/badge/Language-Python-blue?style=flat)
![Static Badge](https://img.shields.io/badge/IA-Gemini-purple?style=flat)

<h4 align="center"> 
    :construction:  Projeto em construção  :construction:
</h4>

## Stack utilizada

O projeto foi desenvolvido utilizando as seguintes Stacks:

**Front-end:** HTML, CSS, JavaScript

**Back-end:** Python v2024.14.1, Django v5.1.1

**IA:** Google Gemini API v0.6.9

## Instalação via download ZIP

1- Descompacte os arquivos 
2- Abra seu editor
3- Vá em arquivo
4- Abrir pasta
5- Escolha a pasta do projeto (Cars)
6- Crie seu ambiente virtual utilizando o comando:
    python -m venv "nome do ambiente de sua escolha"
7- Acesse seu ambiente virtual criado através do comando:
    .\"nome do ambiente de sua escolha"\Scripts\activate
Você verá que o seu terminal ficara com o nome do seu ambiente entre parênteses e na cor verde, à esquerda do endereço do seu terminal.
8- Instale as dependencias através do comando:
    pip install -r requirements.txt
9- Após o final da instalação, para rodar a aplicação será necessário executar o comando:
    python manage.py runserver

## Instalação via clonagem

Para rodar esse projeto, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com)

Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

1- Abra o Git Bash
2- Altere o diretório de trabalho atual para o local do diretório desejado
3- Digite git clone https://github.com/JG-Erbes-dev/Cars.git
4- Aperte ENTER e aguarde o final da clonagem
5- Siga os passos 2 até 9 da instalação via download ZIP


## Ajustando integração da IA:

Será necessário gerar uma `API_KEY` do Google Gemini AI, e inserir no arquivo client.py, localizado na pasta gemini_api para gerar as avaliações.

O código também poderá ser utilizado com integração da API Openai.

