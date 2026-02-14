from typing import List, Optional
from modelos.producto import Producto

class Inventario:
    def __init__(self):
        self._lista_productos: List[Producto] = []

    def agregar_producto(self, nuevo_prod: Producto) -> bool:
        """Añade producto verificando unicidad del ID con una expresión generadora."""
        # Verificación eficiente en una línea
        if any(p.get_id() == nuevo_prod.get_id() for p in self._lista_productos):
            return False
        
        self._lista_productos.append(nuevo_prod)
        return True

    def eliminar_producto(self, id_prod: str) -> bool:
        """Elimina usando búsqueda directa."""
        prod = self._buscar_interno(id_prod)
        if prod:
            self._lista_productos.remove(prod)
            return True
        return False

    def actualizar_producto(self, id_prod: str, n_cant: Optional[int] = None, n_prec: Optional[float] = None) -> bool:
        """Actualiza cantidad o precio si se proporcionan valores."""
        target = self._buscar_interno(id_prod)
        if not target:
            return False
        
        if n_cant is not None:
            target.set_cantidad(n_cant)
        if n_prec is not None:
            target.set_precio(n_prec)
        return True

    def buscar_producto_por_nombre(self, termino: str) -> List[Producto]:
        """Búsqueda insensible a mayúsculas usando list comprehension."""
        termino = termino.lower()
        return [p for p in self._lista_productos if termino in p.get_nombre().lower()]

    def obtener_todos(self) -> List[Producto]:
        return self._lista_productos

    def _buscar_interno(self, id_prod: str) -> Optional[Producto]:
        """Helper privado optimizado."""
        return next((p for p in self._lista_productos if p.get_id() == id_prod), None)
