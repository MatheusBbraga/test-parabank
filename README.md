# Test Automation - ParaBank

Projeto de automação de testes **end-to-end** para a aplicação **ParaBank**, utilizando **Playwright + Pytest** em Python.

O projeto segue o padrão **Page Object Model (POM)** para melhor organização e reutilização de código.

---

## Tecnologias utilizadas

* Python
* Playwright
* Pytest
* Pytest-Playwright
* Faker
* Page Object Model (POM)

---

## Estrutura do projeto

```
test-parabank
│
├── pages
│   ├── login_page.py
│   ├── register_page.py
│   └── home_page.py
│
├── tests
│   ├── test_login.py
│   └── test_register.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Cenários automatizados

### Login

* Login com sucesso
* Validação de login sem credenciais

### Cadastro de usuário

* Cadastro de novo usuário
* Validação de criação de conta com sucesso

Os dados de cadastro são gerados dinamicamente utilizando **Faker**.

---

## Instalação do projeto

Clone o repositório:

```
git clone https://github.com/MatheusBbraga/test-parabank
```

Entre na pasta do projeto:

```
cd test-parabank
```

---

## Criar ambiente virtual

```
python -m venv venv
```

### Ativar ambiente virtual

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

---

## Instalar dependências

```
pip install -r requirements.txt
```

---

## Instalar navegadores do Playwright

```
playwright install
```

---

## Executando os testes

Executar todos os testes:

```
pytest
```

Executar apenas testes de login:

```
pytest -m login
```

Executar apenas testes de cadastro:

```
pytest -m register
```

---

## Relatório de testes

O projeto gera um relatório HTML automaticamente após a execução dos testes.

Para visualizar o relatório:

```
start report.html
```

---

## Aplicação utilizada nos testes

Aplicação de testes:
https://parabank.parasoft.com/parabank

---

## Autor

Matheus Braga
