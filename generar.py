from faker import Faker
import random
import json

# Crear una instancia de Faker con configuración para español
fake = Faker('es_ES')
data = []

# Generar 1000 registros
for _ in range(1000):
    num_telefonos = random.randint(1, 5)  # Número aleatorio de teléfonos entre 1 y 5
    telefonos = [fake.phone_number() for _ in range(num_telefonos)]
    data.append({
        'nombre': fake.name(),
        'telefonos': telefonos,
        'email': fake.email(),
        'direccion': fake.address(),
        'ciudad': fake.city(),
        'pais': fake.country()
    })

# Guardar los datos generados en un archivo JSON con codificación UTF-8
output_path = 'C:/Users/juanc/Documents/ifp/2023-2024/bdd/clientes.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"Datos guardados en {output_path}")
