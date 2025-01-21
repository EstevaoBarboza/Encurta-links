# Encurtador de URLs

Este é um aplicativo simples desenvolvido em Python usando o framework Flask. Ele permite encurtar URLs longas para facilitar o compartilhamento. O projeto utiliza o TinyURL para realizar o encurtamento de links.

## Funcionalidades

- Validação de URLs para garantir que o link fornecido seja válido.
- Geração de URLs curtas utilizando a biblioteca `pyshorteners`.
- Interface simples e amigável para o usuário.
- Persistência de dados (opcional) usando `Flask-SQLAlchemy` (banco de dados SQLite).

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Flask**: Framework web para construir o servidor e rotas.
- **SQLite**: Banco de dados local para possíveis expansões.
- **Pyshorteners**: Biblioteca para encurtar URLs.
- **HTML**: Para criar a interface do usuário.

---

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.7 ou superior instalado.
- Gerenciador de pacotes `pip`.

### Passos para Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/encurtador-urls.git
   cd encurtador-urls
2. Crie e ative um ambiente virtual:
   ```bash
    python -m venv venv
    source venv/bin/activate 
    
3. Inicie o servidor local:
   ```bash
    python app.py
---
## Teste a aplicação
https://encurta-links-im3enqfow-estevaos-projects-5ea65504.vercel.app/
