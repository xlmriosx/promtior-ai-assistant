import os
import requests

def ensure_ollama_model(model_name):
    ollama_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    pull_url = f"{ollama_url}/api/pull"
    try:
        print(f"Verificando existencia del modelo '{model_name}' en Ollama...")
        tags_url = f"{ollama_url}/api/tags"
        resp = requests.get(tags_url, timeout=10)
        if resp.status_code == 200 and model_name in resp.text:
            print(f"Modelo '{model_name}' ya está disponible en Ollama.")
            return
        
        print(f"Descargando modelo '{model_name}' en Ollama...")
        r = requests.post(
            pull_url,
            json={"name": model_name},
            timeout=60
        )
        if r.status_code == 200:
            print(f"Modelo '{model_name}' descargado correctamente.")
        else:
            print(f"Error al descargar el modelo: {r.text}")
    except Exception as e:
        print(f"Error verificando/descargando modelo en Ollama: {e}")
