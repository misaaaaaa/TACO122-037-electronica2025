from PIL import Image
import os

# Carpeta donde están las imágenes JPG
# Recuerda tener estas carpetas ya creadas en la carpeta donde tengas este script
# Deberías poder ejecutar: 
# python convertir_a_bmp.py
# Tienes que tener instalado antes "PIL"
input_folder = "imagenes_jpg"
output_folder = "imagenes_bmp"

# Crea la carpeta de salida si no existe
os.makedirs(output_folder, exist_ok=True)

# Recorre todos los archivos de la carpeta
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpg") or filename.lower().endswith(".jpeg"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # 🔸 Convierte a blanco y negro (escala de grises)
        img = img.convert("L")

        # Nombre del nuevo archivo con extensión .bmp
        base_name = os.path.splitext(filename)[0]
        bmp_path = os.path.join(output_folder, base_name + ".bmp")

        # Guarda en formato BMP
        img.save(bmp_path, format="BMP")
        print(f"Convertido (B/N): {filename} → {base_name}.bmp")

print("✅ Conversión completa en blanco y negro.")
