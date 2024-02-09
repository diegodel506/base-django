import _connectors.ConectorPython as c


def viewControl(
    total_payment,
    nit_cliente,
    nombre_cliente,
    orden_cliente,
    fecha_orden,
    propina,
    no_mesa,
    area_mesa,
    es_recibo,
):
    printers = c.ConectorV3.obtenerImpresoras()
    print(printers)

    printerName = "POS-57"
    serial = ""

    conector = c.ConectorV3(serial=serial)
    conector.Iniciar()
    conector.DeshabilitarElModoDeCaracteresChinos()
    conector.EstablecerAlineacion(c.ALINEACION_CENTRO)

    conector.Feed(1)
    conector.EscribirTexto("Parzibyte's blog\n")
    conector.EscribirTexto("Blog de un programador\n")
    conector.TextoSegunPaginaDeCodigos(2, "cp850", "Teléfono: 123456798\n")
    conector.EscribirTexto("Fecha y hora: 29/9/2022")
    conector.Feed(1)

    respuesta = conector.imprimirEn(printerName)
    if respuesta == True:
        print("Impreso correctamente")
    else:
        print("Error: " + respuesta)

    print(total_payment)
