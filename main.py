"""Script de demostración del sistema Lavanderia-ExpressClean."""

from model.cliente import Cliente
from model.ropa_normal import RopaNormal
from model.alfombra import Alfombra
from model.edredon_cobertor import EdredonCobertor
from model.orden import Orden
from model.cotizacion_dolar import CotizacionDolar
from model.producto_quimico import ProductoQuimico
from model.cajero import Cajero
from model.operario import Operario
from model.maquina import Maquina
from model.excepciones import (
    OrdenNoPagadaError,
    EstadoInicialNoRegistradoError,
)


def main():
    print("=== LAVANDERIA EXPRESSCLEAN ===\n")

    # 1. Cliente y validación de RUT
    print("--- 1. Cliente ---")
    cliente = Cliente("12.345.678-5")
    print(f"RUT cliente: {cliente.rut}")
    print(f"RUT válido: {cliente.validar_rut()}\n")

    # 2. Crear los tres subtipos de Prenda
    ropa_normal = RopaNormal(
        estado_inicial="Buen estado",
        lavado_seco=False
    )

    alfombra = Alfombra(
        estado_inicial="Mancha en un borde",
        lavado_seco=False
    )

    edredon = EdredonCobertor(
        estado_inicial="Buen estado general",
        lavado_seco=False
    )

    # 3. Polimorfismo
    print("--- 2. Polimorfismo de prendas ---")

    prendas = [
        ropa_normal,
        alfombra,
        edredon
    ]

    for prenda in prendas:
        print(
            f"{prenda.__class__.__name__}: "
            f"Costo ${prenda.calcular_costo()} | "
            f"Tiempo {prenda.calcular_tiempo_lavado()} minutos"
        )

    print()

    # 4. Agregación Cliente - Orden
    print("--- 3. Orden asociada al cliente ---")

    orden = Orden(
        num_orden=101,
        num_boleta="BOL-001",
        cliente=cliente,
        pagada=False
    )

    print(f"Número de orden: {orden.num_orden}")
    print(f"Cliente asociado: {orden.cliente.rut}")
    print(f"Identificación válida: {orden.validar_identificacion()}\n")

    # 5. Composición Orden - DetalleOrden
    print("--- 4. Detalles de la orden ---")

    for prenda in prendas:
        orden.agregar_detalle(prenda)

    print(f"Cantidad de detalles: {len(orden.detalles)}")
    print(f"Total de la orden: ${orden.calcular_total()}\n")

    # 6. Regla de negocio: no entregar si no está pagada
    print("--- 5. Orden no pagada ---")

    try:
        orden.entregar_orden()

    except OrdenNoPagadaError as error:
        print(f"Excepción controlada: {error}")

    print("El programa continúa después de la excepción.\n")

    # 7. Pagar y entregar correctamente
    print("--- 6. Pago y entrega ---")

    orden.pagada = True
    entrega = orden.entregar_orden()

    print(f"Orden pagada: {orden.verificar_pago()}")
    print(f"Orden entregada: {entrega}\n")

    # 8. Regla de negocio: lavado en seco sin estado inicial
    print("--- 7. Lavado en seco sin estado inicial ---")

    prenda_lavado_seco = RopaNormal(
        estado_inicial="",
        lavado_seco=True
    )

    try:
        prenda_lavado_seco.validar_estado()

    except EstadoInicialNoRegistradoError as error:
        print(f"Excepción controlada: {error}")

    print("El programa continúa después de la excepción.\n")

    # 9. Cotización del dólar y producto químico
    print("--- 8. Producto químico importado ---")

    cotizacion = CotizacionDolar(
        fecha="2026-10-06",
        valor_dolar=950.0
    )

    producto = ProductoQuimico(
        nombre="Producto químico lavado en seco",
        precio_dolar=25.0
    )

    precio_pesos = producto.calcular_precio_pesos(
        cotizacion.obtener_valor_dolar()
    )

    print(f"Producto: {producto.nombre}")
    print(f"Precio en dólares: USD {producto.precio_dolar}")
    print(f"Valor dólar: ${cotizacion.obtener_valor_dolar()}")
    print(f"Precio convertido a pesos: ${precio_pesos}\n")

    # 10. Cajero, Operario y Máquina
    print("--- 9. Empleados y máquina ---")

    cajero = Cajero("CAJ-001")
    operario = Operario("OPE-001")
    maquina = Maquina("MAQ-001")

    cajero.recibir_prendas()
    cajero.registrar_orden()
    cajero.cobrar_orden()

    operario.procesar_prenda(ropa_normal)
    operario.operar_maquina(maquina)

    print(f"Cajero: {cajero.id_empleado}")
    print(f"Operario: {operario.id_empleado}")
    print(f"Máquina: {maquina.id_maquina}")
    print(f"Entrega por cajero: {cajero.entregar_prendas()}\n")

    print("=== Demostracion finalizada correctamente ===")


if __name__ == "__main__":
    main()
