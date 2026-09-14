"""
Ejemplo vanilla: Gemini API con requests
Para probar la capa gratuita antes de decidir si se usa en clase.

A diferencia de PokeAPI, esta API si pide autenticacion. Para conseguir
una API key gratuita (sin tarjeta):

1. Entrar a https://aistudio.google.com
2. Iniciar sesion con una cuenta de Google normal
3. Click en "Get API key" y copiar la key que genera

Documentacion oficial: https://ai.google.dev/gemini-api/docs
"""
from api_key import API_KEY 
import requests

# Pega aqui tu API key (la que copiaste de Google AI Studio).
#Constantes
VERBOSE = True
MODEL = "gemini-3.6-flash"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

print (f"\n========================")
print (f"Gemini  Model:{MODEL}  ")
print (f"API_KEY: {API_KEY}")
print (f"\n========================")



# Construir API KEY
headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": API_KEY,
}

while True:
    print(f"\n========== Gemini ===========")
    user_prompt = input("En que piensas?: (ingresa tu prompt o 'salir' para terminar la sesion): ")

    #Revisar si el usuario quiere salir
    if user_prompt.lower().strip() == "salir":
        print("\n Hasta luego!!")
        break

        #Construir body de request
    body = {
            "contents": [
                {
                    "parts": [
                        {"text": user_prompt }
                    ]
                }
            ]
        }

     #Realizar Request post
    respuesta = requests.post(URL, headers=headers, json=body)

    print("Status code:", respuesta.status_code)

    if respuesta.status_code != 200:
        print("Algo salio mal:")
        print(respuesta.text)
    else:
        datos = respuesta.json()

        # La respuesta de Gemini viene anidada varios niveles:
         # datos -> candidates -> [0] -> content -> parts -> [0] -> text
        respuesta_gemini = datos["candidates"][0]["content"]["parts"][0]["text"]
        print("\nRespuesta de Gemini:\n")
        print(respuesta_gemini)
