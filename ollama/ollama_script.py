from flask import Flask, request, jsonify
import ollama
import subprocess
import time
import json

app = Flask(__name__)

MODEL = "tinyllama"  # Define um modelo padrão para evitar erro "model is required"

# Função para iniciar o servidor Ollama
def start_ollama():
    try:
        print("Iniciando o servidor Ollama...")
        subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(5)  # Espera 5 segundos para garantir que o servidor suba
    except Exception as e:
        print(f"Erro ao iniciar Ollama: {e}")

@app.route('/')
def home():
    return "Ollama API está rodando! Use /run para interagir. Exemplo de GET: /run?query=teste"

@app.route('/run', methods=['GET', 'POST'])
def run_ollama():
    try:
        if request.method == 'POST':
            data = request.json
            query = data.get('query', 'Olá, Ollama!')
        else:  # Método GET
            query = request.args.get('query', 'Olá, Ollama!')

        # Chama Ollama com um modelo válido
        response = ollama.chat(model=MODEL, messages=[{"role": "user", "content": query}])

        # print(response)  # Para verificar o formato da resposta


        # return jsonify({"response": response["message"]})
        return jsonify({"response": response.get("message", {}).get("content", "")})

    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    start_ollama()  # Garante que o Ollama está rodando antes de iniciar a API Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
