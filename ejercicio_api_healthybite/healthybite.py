"""
Consulta los valores nutricionales de una lista de alimentos usando la API de Open Food Facts.
"""
import requests

# Constantes
URL_BASE = "https://world.openfoodfacts.org/api/v3/product/"
HEADERS = {"User-Agent": "HealthyBite/1.0"}

# Guarda los productos ya consultados para no repetir la misma peticion a la API
CACHE = {}

# Alimentos disponibles: numero -> (nombre, codigo de barras real en Open Food Facts)
PRODUCTOS = {
    "1": ("Nutella", "3017620422003"),
    "2": ("Coca-Cola", "5449000000996"),
    "3": ("Oreo Enrobed", "7622300489434"),
    "4": ("Cruesly mezcla de nueces", "3168930010265"),
    "5": ("Biscuits Nutella", "8000500310427"),
    "6": ("Nesquik Cacao", "3033710065967"),
    "7": ("Twix helado", "5000159484695"),
    "8": ("Gazpacho Alvalle", "5410188031072"),
    "9": ("Coca-Cola Light", "5000112548167"),
    "10": ("Ritter Sport Marzipan", "4000417025005"),
}


def obtener_producto(codigo):
    """Consulta la API de Open Food Facts y devuelve el diccionario del producto (o None)."""
    if codigo in CACHE:
        return CACHE[codigo]

    try:
        respuesta = requests.get(URL_BASE + codigo, headers=HEADERS, timeout=10)
    except requests.RequestException:
        print("Error de conexion con la API.")
        return None

    if respuesta.status_code != 200:
        print("Error HTTP:", respuesta.status_code)
        return None

    data = respuesta.json()

    if data.get("status") != "success":
        print("Producto no encontrado.")
        return None

    producto = data["product"]
    CACHE[codigo] = producto
    return producto


def mostrar_productos():
    """Muestra los alimentos disponibles usando la lista local, sin llamar a la API."""
    print("\n========== Alimentos disponibles ==========")
    for numero, (nombre, _codigo) in PRODUCTOS.items():
        print(f"{numero}. {nombre}")


def mostrar_informacion_producto(producto):
    """Muestra nombre, marca y datos nutricionales de un alimento."""
    nutrientes = producto.get("nutriments", {})

    nombre = producto.get("product_name", "No disponible")
    marca = producto.get("brands", "No disponible")
    calorias = nutrientes.get("energy-kcal_100g", "No disponible")
    proteina = nutrientes.get("proteins_100g", "No disponible")
    carbohidratos = nutrientes.get("carbohydrates_100g", "No disponible")
    grasas = nutrientes.get("fat_100g", "No disponible")
    nutriscore = producto.get("nutriscore_grade", "No disponible")

    print("\n========== Informacion nutricional ==========")
    print("Nombre:", nombre)
    print("Marca:", marca)
    print("Calorias:", calorias)
    print("Proteina:", proteina)
    print("Carbohidratos:", carbohidratos)
    print("Grasas:", grasas)
    print("Nutri-Score:", nutriscore)


def mostrar_menu():
    print("\n========== Healthy Bite ==========")
    print("1. Ver alimentos disponibles")
    print("2. Ver informacion nutricional")
    print("3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opcion: ")

        if opcion == "1":
            mostrar_productos()

        elif opcion == "2":
            mostrar_productos()
            numero = input("Elige el numero del alimento (1-10): ")
            item = PRODUCTOS.get(numero)
            if item is None:
                print("Opcion invalida.")
                continue
            _nombre, codigo = item
            producto = obtener_producto(codigo)
            if producto:
                mostrar_informacion_producto(producto)

        elif opcion == "3":
            print("\nAdios guapo!")
            break

        else:
            print("Opcion invalida.")


if __name__ == "__main__":
    main()
