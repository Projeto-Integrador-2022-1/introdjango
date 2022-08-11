# Introdução ao Django
Demonstrações de sala de aula com Django

## Como preparar o seu ambiente de desenvolvimento

Algumas ferramentas precisam ser instaladas previamente para facilitar sua
atuação no desenvolvimento de um projeto. Utilize os modos recomendados de instalação
para o seu sistema operacional. Antes de tudo são:

- Python, versão 3.9 ou mais recente, que você pode baixar [aqui](https://python.org).
- Git você baixa [aqui](https://git-scm.com/)
- GitHub Desktop (por enquando não tem pra GNU/Linux) [aqui](https://desktop.github.com/)

> Ao instalar o Python, lembre de selecionar a opção para configurar o PATH (no Windows).

Com isso você terá um ambiente minimamente funcional para desenvolver pequenos projetos em Python
e manter seus códigos sincronizados via GitHub.

Mas estamos falando de projetos maiores, onde precisamos gerir dependências, garantir qualidade
de código, e seguir boas práticas de programação. Como em alguns sistemas pode ser meio complicado
instalar algumas delas, segue uma sequência que torna mais suave a instalação (nesse caso, 
siga a ordem indicada):

1. Instale o pipx seguindo as orientações (aqui)[https://pypa.github.io/pipx/installation/]
2. Instale o Poetry via pipx com `pipx install poetry`

> O pipx é um instalador de "executáveis" Python que simplifica a instalação de várias ferramentas.

> O Poetry é um gerenciador de projetos e suas dependências.

3. Configure o Poetry para criar um virtualenv no diretório atual com `poetry config virtualenvs.in-project true`
4. Abra o terminal no diretório do projeto (este, por exemplo)
5. Crie o virtualenv do projeto com `poetry shell`
6. Instale as dependências de desenvolvimento com `poetry install`
7. Crie o banco de dados de desenvolvimento com `python manage.py migrate`
8. Crie o superusuário do seu sistema de desenvolvimento com `python manage.py createsuperuser`
9. Execute o projeto Django com `python manage.py runserver`

O VS Code tem algumas extensões que ajudam a manter a qualidade do seu código, que podem usar
dependências que adicionei no pyproject.toml deste projeto.
- Black é um formatador de código leve e inteligente
- Pylint verifica que seu código está seguindo boas práticas de desenvolvimento

Pressionando ctrl + P, você pode selecionar o Pylint na opção: Python>Selecionar linter.

Você pode configurar o Black como formatador pressionando ctrl + , e procurando a opção "Python: Formatting: Provider" e alterando para Black. Para que ele formate seus arquivos sempre que você
salvá-los, procure a opção "Editor: Format on save".

Siga boas práticas, aproveite os alertas do Pylint para melhorar sua qualidade como desenvolvedor.
Esse tipo de ferramente não é exclusiva do Python e você pode progredir muito por fazer bom uso
delas.
