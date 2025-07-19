import os

def crear_unidad_virtual(letra_unidad, ruta_carpeta):
    # Verifica si la carpeta existe
    if not os.path.exists(ruta_carpeta):
        print(f"La carpeta '{ruta_carpeta}' no existe. Creándola...")
        os.makedirs(ruta_carpeta)

    # Comando para crear la unidad virtual
    comando = f'subst {letra_unidad}: "{ruta_carpeta}"'
    resultado = os.system(comando)

    if resultado == 0:
        print(f"✅ Unidad virtual {letra_unidad}: creada con éxito apuntando a '{ruta_carpeta}'")
    else:
        print("❌ Error al crear la unidad virtual")

def eliminar_unidad_virtual(letra_unidad):
    comando = f'subst {letra_unidad}: /d'
    resultado = os.system(comando)

    if resultado == 0:
        print(f"🗑️ Unidad virtual {letra_unidad}: eliminada con éxito")
    else:
        print("❌ Error al eliminar la unidad virtual")

# Ejemplo de uso
if __name__ == "__main__":
    letra = "Z"  # Puedes cambiarla por cualquier letra libre
    carpeta = "C:\\SimuladorPendrive"

    crear_unidad_virtual(letra, carpeta)

    # Para eliminarla después, puedes llamar a:
    # eliminar_unidad_virtual(letra)
