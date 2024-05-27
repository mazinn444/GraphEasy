# GraphEasy

GraphEasy é uma aplicação web interativa desenvolvida com Flask que permite aos usuários calcular e visualizar gráficos de funções quadráticas.

## Funcionalidades

- **Cálculo de Gráficos:** Insira os coeficientes da função quadrática (a, b, c) e visualize o gráfico gerado.
- **Raízes da Função:** Calcule e exiba as raízes da função quadrática, quando existirem.
- **Páginas de Erro Personalizadas:** Melhora a experiência do usuário fornecendo páginas de erro customizadas.

## Tecnologias Utilizadas

- **Flask:** Framework web em Python utilizado para desenvolvimento do servidor.
- **NumPy:** Biblioteca utilizada para cálculos numéricos.
- **Matplotlib:** Biblioteca usada para a geração dos gráficos.
- **HTML/CSS:** Utilizados para a estrutura e estilo das páginas web.

## Como Utilizar Este Projeto

1. Clone este repositório para o seu ambiente local:
    ```bash
    git clone https://github.com/mazinn444/GraphEasy.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd GraphEasy
    ```
3. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate # Para Windows use `venv\Scripts\activate`
    ```
4. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```
    **Nota:** Se o arquivo `requirements.txt` não estiver disponível, instale as bibliotecas individualmente:
    ```bash
    pip install flask numpy matplotlib
    ```
5. Inicie o servidor Flask:
    ```bash
    flask run
    ```
6. Abra seu navegador e acesse:
    ```
    http://127.0.0.1:5000
    ```

## Estrutura do Projeto

- **app.py:** Arquivo principal contendo o código do servidor Flask.
- **templates/:** Diretório contendo os arquivos HTML.
- **static/:** Diretório contendo os arquivos CSS e outros recursos estáticos.
