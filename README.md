# Pokémon Hunting Bot 🧭🔍

Projeto desenvolvido em React + Vite com o objetivo de fornecer uma interface para controle e visualização de ações automatizadas de um bot de caça a Pokémon. Além do Python para a construção do bot.

## 🧩 Tecnologias Utilizadas

- [React 19](https://reactjs.org/)
- [Vite 6](https://vitejs.dev/)
- [React Router DOM 7](https://reactrouter.com/)
- [ESLint](https://eslint.org/) para padronização de código
- [Python](https://www.python.org/) para utilizar no bot

## 📁 Estrutura

Este projeto segue uma arquitetura simples baseada em React com Vite:

```bash
├── backend/             
│   └──app.py            # Aquivo main do bot 
├── src/
│   └── main.jsx         # Arquivo principal da aplicação
│   └── assets/          # Imagens e ícones
│   └── components/      # Componentes reutilizáveis
├── public/              # Arquivos estáticos
├── index.html           # HTML base
├── vite.config.js       # Configurações do Vite
├── package.json         # Dependências e scripts
```

## 🚀 Como executar o projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/pokemon-hunting.git
cd pokemon-hunting
```

2. **Instale as dependências:**

```bash
npm install
pip install flask requests pyautogui pyscreenshot pillow pytesseract
: É só o wrapper Python.
: Você também precisa instalar o Tesseract OCR no Windows: Tesseract OCR
: Depois, configure o caminho no seu código: pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

3. **Execute o servidor de desenvolvimento:**

```bash
npm run dev
```

Acesse em seu navegador: [http://localhost:5173](http://localhost:5173)

## 🧪 Scripts disponíveis

- `npm run dev`: Inicia o servidor de desenvolvimento
- `npm run build`: Cria a versão de produção
- `npm run preview`: Visualiza a build de produção localmente
- `npm run lint`: Verifica problemas de lint no código

## 📦 Dependências

- `react`
- `react-dom`
- `react-router-dom`
- `threading`
- `flask`
- `jsonify`
- `pyautogui`
- `imageGrab`
- `Image`
- `time`
- `pytesseract`


## 🛡️ Licença

Distribuído sob a licença [MIT](./LICENSE).

---

> Ícone do projeto localizado em `src/assets/pokBot.ico`.
