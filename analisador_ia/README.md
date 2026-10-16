# 🤖 AI Sentiment Analyzer

Real-world integration with Google Gemini API for Natural Language Processing.

## 🇺🇸 English

### Features
- Sentiment analysis (Positive, Negative, Neutral)
- Integration with Google Gemini API
- Real-world AI application
- Error handling and technical diagnostics
- Experimental Python 3.14 environment

### Requirements
- Google Gemini API key
- `google-genai` SDK
- Python 3.14 (experimental)

### Installation
```bash
pip install google-genai
```

### How to Use
1. Get your API key at [Google AI Studio](https://aistudio.google.com/)
2. Replace `SUA_CHAVE_AQUI` with your actual API key
3. Run the script:
```bash
python analisador_ia.py
```

### Example
```
--- AI SENTIMENT ANALYZER (Experimental Environment) ---
Running on Python: 3.14.0

Enter text to analyze: I love this new project!

AI Result: POSITIVE
```

### ⚠️ Technical Note
The script uses the `gemini-1.5-flash` model. If you receive a 404 error, the model version may not be active yet for your Python build. Check the [Gemini documentation](https://ai.google.dev/) for the latest model names.

### ⚠️ Security
Never commit your API key to GitHub. Use environment variables or a `.env` file.

---

## 🇧🇷 Versão em Português

### Funcionalidades
- Análise de sentimento (Positivo, Negativo, Neutro)
- Integração com API do Google Gemini
- Aplicação real de IA
- Tratamento de erros e diagnóstico técnico
- Ambiente experimental Python 3.14

### Requisitos
- Chave de API do Google Gemini
- SDK `google-genai`
- Python 3.14 (experimental)

### Instalação
```bash
pip install google-genai
```

### Como Usar
1. Obtenha sua chave de API em [Google AI Studio](https://aistudio.google.com/)
2. Substitua `SUA_CHAVE_AQUI` pela sua chave real
3. Execute o script:
```bash
python analisador_ia.py
```

### Exemplo
```
--- AI SENTIMENT ANALYZER (Experimental Environment) ---
Running on Python: 3.14.0

Enter text to analyze: I love this new project!

AI Result: POSITIVE
```

### ⚠️ Nota Técnica
O script usa o modelo `gemini-1.5-flash`. Se você receber um erro 404, a versão do modelo pode não estar ativa ainda para o seu build do Python. Verifique a [documentação do Gemini](https://ai.google.dev/) para os nomes de modelos mais recentes.

### ⚠️ Segurança
Nunca faça commit da sua chave de API no GitHub. Use variáveis de ambiente ou um arquivo `.env`.

---

**Author:** Anderson Margalho
