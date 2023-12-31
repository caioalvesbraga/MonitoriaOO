# MonitoriaOO
Este repositório contém um projeto Django para servir de inspiração para os alunos da disciplina de Orientação a Objetos quando construírem os seus projetos.
<br><br>
A aplicação é uma plataforma de cadastro de alunos da monitoria de OO, mas que possui um template que pode ser convertido em qualquer outra ideia que implemente as operações CRUD (Create, Read, Update, Delete).

## Arquitetura da aplicação
A Arquitetura do projeto segue o padrão MTV, que é muito semelhante ao MVC(Model, View, Controller), mas que se divide da seguinte maneira:
1. MODELS = Mapeamento do banco de dados para o projeto.
2. TEMPLATES = Páginas para a visualização dos dados.
3. VIEWS = Lógica de Negócio

## Como rodar a aplicação?

1. Primeiramente, clone o repositório para a sua máquina:
  ```bash
      git clone https://github.com/caioalvesbraga/MonitoriaOO.git
  ```
   -> E, no terminal, vá até o diretório MonitoriaOO/project
  <br><br>
  
2. Feito isso, com o Docker e o Docker Compose previamente instalados na sua máquina, basta rodar o comando:

```bash
sudo docker-compose up --build
```
Esse comando instalará todas as dependências necessárias e subirá o ambiente da aplicação.
Após isso, basta acessar o link gerado e utlizar o programa :)

