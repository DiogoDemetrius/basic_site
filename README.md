# Car Marketplace

## Descrição
Aplicação web para registrar e usuários.

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

5. Acesse `http://127.0.0.1:8000` no seu navegador.]

## Funcionalidades

1. Registro de Usuário: Os usuários podem se registrar fornecendo um nome de usuário e senha. Essas informações são armazenadas no banco de dados.

2. Login de Usuário: Os usuários podem fazer login com seu nome de usuário e senha. Se as credenciais forem válidas, eles são redirecionados para a página inicial, onde podem ver os carros disponíveis. Caso contrário, uma mensagem de erro é exibida.

3. Visualização de Carros Disponíveis: Os carros disponíveis são exibidos na página inicial após o login do usuário. Cada carro exibido inclui a marca, modelo, ano e preço.

4. Registro de Novo Carro: Os usuários podem registrar um novo carro fornecendo detalhes como marca, modelo, ano e preço. Após o registro, o novo carro é adicionado à lista de carros disponíveis e exibido na página inicial.

5. Detalhes do Carro: Os usuários podem clicar em um carro na página inicial para ver os detalhes completos desse carro, incluindo sua marca, modelo, ano e preço.

6. Mensagens de Feedback: Mensagens informativas são exibidas ao usuário, como "Bem-vindo!" ao fazer login com sucesso ou "Credenciais inválidas!" se as credenciais de login forem incorretas.