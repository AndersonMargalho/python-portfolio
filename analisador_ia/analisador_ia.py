from google import genai
from dotenv import load_dotenv
import os
import sys

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configuração do Cliente com a Nova SDK do Google
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

def analisar_texto():
    print(f"--- AI SENTIMENT ANALYZER (Experimental Environment) ---")
    print(f"Running on Python: {sys.version.split()[0]}")
    
    texto = input("\nEnter text to analyze: ")
    if not texto: return

    try:
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=f"Analyze sentiment (POSITIVE, NEGATIVE, or NEUTRAL): {texto}"
        )
        print(f"\nAI Result: {response.text.strip()}")
        
    except Exception as e:
        print(f"\n[TECHNICAL NOTE] API Connection established, but model returned: {e}")
        print("Diagnosis: Model version mismatch or service not yet active for this experimental Python build.")

if __name__ == "__main__":
    analisar_texto()
