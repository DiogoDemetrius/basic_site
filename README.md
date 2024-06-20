# Car Marketplace

## Descrição
Aplicação web para registrar e vender carros.

## Tecnologias
- Python
- FastAPI
- SQLAlchemy
- SQLite

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/projeto-carros.git
    cd projeto-carros
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```bash
    uvicorn main:app --reload
    ```

5. Acesse `http://127.0.0.1:8000` no seu navegador.