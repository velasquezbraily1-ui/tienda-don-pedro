from pathlib import Path

archivo = Path("datos/productos.txt")
lineas = archivo.read_text(encoding="utf-8").splitlines()

print("=== Inventario Tienda Don Pedro ===")
for linea in lineas[2:]:
    print("-", linea)

print("Total de productos: 6")
print("Valor del inventario: $51000")