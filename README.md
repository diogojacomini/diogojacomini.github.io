# Portfólio Diogo Jacomini

Um portfólio profissional desenvolvido com Flask, destacando experiência em Engenharia de Dados e Engenharia de Software.

## 🌐 Deploy

O portfólio está disponível em: **https://diogojacomini.github.io/**

### GitHub Pages

Este projeto utiliza GitHub Actions para converter automaticamente a aplicação Flask em um site estático e publicar no GitHub Pages.

**Como funciona:**
1. O código Flask é executado em um ambiente de build
2. O script `generate_static.py` gera os arquivos HTML estáticos
3. Os arquivos são publicados automaticamente no GitHub Pages

### Deploy Local

Para executar localmente:

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar aplicação Flask
python app.py

# Ou gerar arquivos estáticos
python generate_static.py
```

## 🛠️ Tecnologias

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: CSS Grid, Flexbox, Font Awesome
- **Deploy**: GitHub Pages, GitHub Actions
- **Responsivo**: Design mobile-first

## 📂 Estrutura

```
├── app.py                 # Aplicação Flask principal
├── generate_static.py     # Script para gerar site estático
├── requirements.txt       # Dependências Python
├── templates/
│   └── index.html        # Template principal
├── static/
│   ├── css/
│   │   └── styles.css    # Estilos CSS
│   ├── js/
│   │   └── script.js     # JavaScript
│   └── images/           # Imagens e assets
└── .github/
    └── workflows/
        └── deploy.yml    # GitHub Actions workflow
```

## ✨ Funcionalidades

- ✅ Design responsivo e moderno
- ✅ Seções: Sobre, Habilidades, Formação, Experiência, Certificações, Projetos
- ✅ Links para projetos reais no GitHub
- ✅ Certificação Databricks integrada
- ✅ Informações confidenciais protegidas visualmente
- ✅ Deploy automático via GitHub Actions

## 🔧 Configuração do GitHub Pages

Para configurar o deploy:

1. **Habilitar GitHub Actions**: Vá em Settings → Pages → Source: "GitHub Actions"
2. **Fazer commit**: As mudanças acionam o workflow automaticamente
3. **Aguardar deploy**: O site estará disponível em alguns minutos

## 🚀 Próximos Passos

- [ ] Adicionar mais certificações
- [ ] Integrar analytics
- [ ] Implementar tema escuro
- [ ] Adicionar blog/artigos
