## Removedor de Fundo com Interface Gráfica (Tkinter)

Este é um aplicativo desktop simples desenvolvido em Python que permite **remover o fundo de imagens** com apenas alguns cliques, usando a biblioteca `rembg`. A interface foi feita com `tkinter`, facilitando o uso para qualquer usuário final.

## Funcionalidades

- Interface gráfica amigável (Tkinter)
- Suporte a imagens `.png`, `.jpg`, `.jpeg`, `.bmp`
- Remove o fundo automaticamente com o `rembg`
- Permite escolher e salvar a imagem final com fundo transparente (`.png`)
- Processamento em **thread separada**, evitando travamentos da interface

## Requisitos

- Python 3.8 ou superior

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/removedor-fundo-gui.git
cd removedor-fundo-gui
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv
# Ative o ambiente:
# No Windows:
venv\Scripts\activate
# No Linux/macOS:
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### Arquivo `requirements.txt`

Crie um arquivo chamado `requirements.txt` com o seguinte conteúdo:

```
rembg
pillow
pyinstaller
```

> Obs: Não inclua `tkinter` — ele já vem com o Python e **não deve** ser instalado via `pip`.

## Como Executar

```bash
python removedor_fundo.py
```

A interface será aberta permitindo que você selecione uma imagem e remova o fundo com facilidade.

## Como Gerar um Executável (.exe)

Para transformar o programa em um executável no Windows:

```bash
pyinstaller --onefile --windowed removedor_fundo.py
```

- `--onefile`: empacota tudo em um único `.exe`
- `--windowed`: evita abrir o terminal junto (recomendado para apps com GUI)

O executável será gerado dentro da pasta `dist/`.

### Adicionar Ícone (opcional)

Se quiser adicionar um ícone ao programa:

```bash
pyinstaller --onefile --windowed --icon=icone.ico removedor_fundo.py
```

## Estrutura do Projeto

```
removedor-fundo-gui/
├── removedor_fundo.py       # Código principal
├── requirements.txt         # Dependências
└── README.md                # Este arquivo
```

## ✅ Testado em

- Windows 10/11 com Python 3.10

## Tecnologias Utilizadas

- [rembg](https://github.com/danielgatis/rembg) – Remoção automática de fundo via IA
- [Pillow (PIL)](https://python-pillow.org) – Manipulação de imagens
- [Tkinter](https://docs.python.org/3/library/tk.html) – Interface gráfica nativa do Python
- [PyInstaller](https://pyinstaller.org) – Empacotamento em executável

## Autor
Ivys Emanoel Coredeiro de Souza Lima

