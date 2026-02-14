import os
import sys
from modelos.producto import Producto
from servicios.inventario import Inventario

# Instancia única del servicio
servicio = Inventario()

def _limpiar():
    """Limpia la pantalla de forma compatible."""
    os.system('cls' if os.name == 'nt' else 'clear')

def _pausa():
    input("\nPresione ENTER para continuar...")

# --- Funciones de Interfaz ---
def ui_aniadir():
    _limpiar()
    print("--- AÑADIR NUEVO PRODUCTO ---")
    id_in = input("Ingrese ID único: ").strip()
    if not id_in: return
    
    nom_in = input("Ingrese Nombre: ").strip()
    try:
        cant_in = int(input("Ingrese Cantidad: "))
        prec_in = float(input("Ingrese Precio: "))
        
        nuevo = Producto(id_in, nom_in, cant_in, prec_in)
        if servicio.agregar_producto(nuevo):
            print(">> Éxito: Producto registrado.")
        else:
            print(f">> Error: El ID '{id_in}' ya existe.")
    except ValueError:
        print(">> Error: Cantidad y Precio deben ser números.")
    _pausa()

def ui_eliminar():
    _limpiar()
    print("--- ELIMINAR PRODUCTO ---")
    id_in = input("ID del producto a eliminar: ")
    if servicio.eliminar_producto(id_in):
        print(">> Producto eliminado.")
    else:
        print(">> Error: ID no encontrado.")
    _pausa()

def ui_actualizar():
    _limpiar()
    print("--- ACTUALIZAR PRODUCTO ---")
    id_in = input("ID del producto: ")
    
    print("(Presione ENTER para no cambiar el valor)")
    s_cant = input("Nueva Cantidad: ")
    s_prec = input("Nuevo Precio: ")

    try:
        n_cant = int(s_cant) if s_cant else None
        n_prec = float(s_prec) if s_prec else None
        
        if servicio.actualizar_producto(id_in, n_cant, n_prec):
            print(">> Actualización exitosa.")
        else:
            print(">> Error: Producto no encontrado.")
    except ValueError:
        print(">> Error: Datos numéricos inválidos.")
    _pausa()

def ui_buscar():
    _limpiar()
    print("--- BUSCAR POR NOMBRE ---")
    term = input("Nombre a buscar: ")
    res = servicio.buscar_producto_por_nombre(term)
    
    if res:
        print(f"\nSe encontraron {len(res)} productos:")
        print("-" * 60)
        for p in res:
            print(p)
    else:
        print("\n>> No se encontraron coincidencias.")
    _pausa()

def ui_listar():
    _limpiar()
    print("--- INVENTARIO COMPLETO ---")
    lista = servicio.obtener_todos()
    if not lista:
        print(">> El inventario está vacío.")
    else:
        print(f"{'ID':<10} | {'NOMBRE':<20} | {'CANT':>5} | {'PRECIO':>8}")
        print("-" * 60)
        for p in lista:
            print(p)
    _pausa()

def ui_salir():
    print("\nSaliendo del sistema...")
    sys.exit()

# --- Ejecución Principal ---
def iniciar_programa():
    # Mapeo de opciones a funciones de interfaz
    menu_opciones = {
        "1": ui_aniadir,
        "2": ui_eliminar,
        "3": ui_actualizar,
        "4": ui_buscar,
        "5": ui_listar,
        "6": ui_salir
    }

    while True:
        _limpiar()
        print("==============================")
        print("   GESTIÓN DE INVENTARIOS")
        print("==============================")
        print(" 1. Añadir producto")
        print(" 2. Eliminar producto")
        print(" 3. Actualizar producto")
        print(" 4. Buscar por nombre")
        print(" 5. Listar todo")
        print(" 6. Salir")
        print("==============================")
        
        seleccion = input("Opción: ")
        
        accion = menu_opciones.get(seleccion)
        if accion:
            accion()
        else:
            print("Opción inválida.")
            _pausa()

if __name__ == "__main__":
    iniciar_programa()
