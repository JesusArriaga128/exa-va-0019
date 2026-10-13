# Jesus Arriaga
#  NC= 0019
import cv2
from pathlib import Path

# 1. Definir las rutas de trabajo
carpeta_proyecto = Path(__file__).resolve().parent.parent

carpeta_img_orig = carpeta_proyecto / "img-original-0019"
if not carpeta_img_orig.exists():
    carpeta_img_orig = carpeta_proyecto / "img-original-0777"

# Buscar automáticamente cualquier archivo que empiece por 'img-BMW-0019'
archivos_encontrados = list(carpeta_img_orig.glob("img-BMW-0019*"))

if not archivos_encontrados:
    raise FileNotFoundError(
        f"No se encontró ningún archivo que empiece por 'img-BMW-0019' en '{carpeta_img_orig}'."
    )

# Usar el primer archivo encontrado con ese nombre
ruta_original = archivos_encontrados[0]
print(f"Cargando imagen desde: {ruta_original}")

carpeta_resultados = carpeta_proyecto / "resultados-img-0019"
carpeta_resultados.mkdir(parents=True, exist_ok=True)

# 2. Leer la imagen original con imread
img0019 = cv2.imread(str(ruta_original))

if img0019 is None:
    raise ValueError(
        f"OpenCV no pudo decodificar el archivo '{ruta_original.name}'.\n"
        f"Asegúrate de que la imagen sea un formato válido (JPG, PNG, WEBP) y no esté dañada."
    )

# 3. Rotar la imagen 90 grados en sentido horario
img90_0019 = cv2.rotate(img0019, cv2.ROTATE_90_CLOCKWISE)

# 4. Rotar la imagen 45 grados
alto, ancho = img0019.shape[:2]
centro = (ancho // 2, alto // 2)
matriz_rotacion = cv2.getRotationMatrix2D(centro, 45, 1.0)
img45_0019 = cv2.warpAffine(img0019, matriz_rotacion, (ancho, alto))

# 5. Redimensionar a 600 x 500 píxeles
img600x500_0019 = cv2.resize(img0019, (600, 500))

# 6. Dibujar un rectángulo rojo
img_rojo_0019 = img0019.copy()
x1, y1 = 50, 50
x2, y2 = x1 + 100, y1 + 200
cv2.rectangle(img_rojo_0019, (x1, y1), (x2, y2), (0, 0, 255), 3)

# 7. Mostrar las cinco imágenes
cv2.imshow("BMW original 0019", img0019)
cv2.imshow("BMW 90 0019", img90_0019)
cv2.imshow("BMW 45 0019", img45_0019)
cv2.imshow("BMW 600x500 0019", img600x500_0019)
cv2.imshow("BMW rojo 0019", img_rojo_0019)

# 8. Guardar las imágenes procesadas (usando la misma extensión original)
ext = ruta_original.suffix
cv2.imwrite(str(carpeta_resultados / f"img-BMW1-0019{ext}"), img90_0019)
cv2.imwrite(str(carpeta_resultados / f"img-BMW2-0019{ext}"), img45_0019)
cv2.imwrite(str(carpeta_resultados / f"img-BMW3-0019{ext}"), img600x500_0019)
cv2.imwrite(str(carpeta_resultados / f"img-BMW4-0019{ext}"), img_rojo_0019)

print("Imágenes procesadas y guardadas exitosamente.")
print("Presiona cualquier tecla en una de las ventanas para cerrar.")
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Programa realizado por Jesus Arriaga 0019")
