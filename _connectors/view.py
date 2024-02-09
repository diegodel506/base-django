from rest_framework.decorators import api_view
from rest_framework.response import Response

from _connectors.connector import viewControl


@api_view(["POST"])
def PrintRequestApi(request):
    try:
        total_payment = request.data.get("total_payment", "")
        nit_cliente = request.data.get("nit_cliente", "")
        nombre_cliente = request.data.get("nombre_cliente", "")
        orden_cliente = request.data.get("orden_cliente", "")
        fecha_orden = request.data.get("fecha_orden", "")
        propina = request.data.get("propina", "")
        no_mesa = request.data.get("no_mesa", "")
        area_mesa = request.data.get("area_mesa", "")
        es_recibo = request.data.get("es_recibo", "")

        print(total_payment)

        viewControl(
            total_payment,
            nit_cliente,
            nombre_cliente,
            orden_cliente,
            fecha_orden,
            propina,
            no_mesa,
            area_mesa,
            es_recibo,
        )

        return Response({"mensaje": "Operación exitosa"})
    except Exception as e:
        print(f"Error en la vista hola_mundo_api: {e}")
        return Response({"mensaje": "Error interno del servidor"}, status=500)
