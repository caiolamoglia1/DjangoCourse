# DjangoCourse

Projeto Django para estudo e prática.

## Requisitos
- Python 3.11+
- Git
- (Recomendado) VS Code

## Passos para rodar o projeto

1. **Clone o repositório:**
   ```
   git clone https://github.com/caiolamoglia1/DjangoCourse.git
   cd DjangoCourse
   ```

2. **Crie e ative o ambiente virtual:**
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure pre-commit (opcional, recomendado):**
   ```
   pre-commit install
   pre-commit run --all-files
   ```

5. **Rode as migrações do banco:**
   ```
   python manage.py migrate
   ```

6. **Crie o superusuário (opcional):**
   ```
   python manage.py createsuperuser
   ```

7. **Inicie o servidor de desenvolvimento:**
   ```
   python manage.py runserver
   ```
   Acesse: http://127.0.0.1:8000/

8. **Rode os testes:**
   ```
   pytest -q
   ```

## Qualidade de código
- Lint: [ruff](https://docs.astral.sh/ruff/)
- Formatador: [black](https://black.readthedocs.io/)
- Type checking: [mypy](https://mypy.readthedocs.io/)
- Testes: [pytest-django](https://pytest-django.readthedocs.io/)
- Hooks: [pre-commit](https://pre-commit.com/)

## Estrutura do projeto
```
DjangoCourse/
├── config/         # Projeto Django
├── core/           # App principal
├── templates/      # Templates HTML
├── requirements.txt
├── pyproject.toml
├── pytest.ini
├── .pre-commit-config.yaml
├── .gitignore
├── README.md
└── venv/           # Ambiente virtual (não versionado)
```

## Observações
- Sempre ative o venv antes de rodar comandos Python/Django.
- O ambiente virtual e arquivos temporários estão ignorados no .gitignore.
- Para dúvidas, consulte a documentação oficial do Django: https://docs.djangoproject.com/
