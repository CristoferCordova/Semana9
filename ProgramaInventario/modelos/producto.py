class Producto:
    def __init__(self, id_prod: str, nombre: str, cantidad: int, precio: float):
        """
        Clase Producto con los atributos solicitados.
        :param id_prod: Identificador único (ID).
        :param nombre: Nombre del producto.
        :param cantidad: Cantidad disponible.
        :param precio: Precio unitario.
        """
        # Atributos protegidos
        self._id = id_prod
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # --- Getters ---
    def get_id(self) -> str:
        return self._id

    def get_nombre(self) -> str:
        return self._nombre

    def get_cantidad(self) -> int:
        return self._cantidad

    def get_precio(self) -> float:
        return self._precio

    # --- Setters ---
    def set_id(self, nuevo_id: str):
        self._id = nuevo_id

    def set_nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre

    def set_cantidad(self, nueva_cantidad: int):
        self._cantidad = nueva_cantidad

    def set_precio(self, nuevo_precio: float):
        self._precio = nuevo_precio

    def __str__(self):
        # Formato limpio para consola
        return f"[ID: {self._id}] {self._nombre:<20} | Cant: {self._cantidad:>4} | Precio: ${self._precio:.2f}"
