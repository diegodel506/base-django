from io import BytesIO

import requests
import win32print
from PIL import Image, ImageOps

import _connectors.ConectorPython as ConectorPython

encoder = "cp437"


def initialize_printer(hPrinter):
    win32print.WritePrinter(hPrinter, b"\x1B@")
    win32print.WritePrinter(hPrinter, b"\x1C\x2E")


def feed(hPrinter, lRange):
    for i in range(lRange):
        win32print.WritePrinter(hPrinter, b"\x0A")


def text_align_center(hPrinter, ancho_impresora, texto):
    posicion_inicial_horizontal = int(
        (ancho_impresora - len(texto.encode(encoder))) / 2
    )
    posicion_inicial_horizontal = max(0, min(posicion_inicial_horizontal, 255))
    nL = posicion_inicial_horizontal % 256
    nH = posicion_inicial_horizontal // 256
    comando_posicion_horizontal = b"\x1B$" + bytes([nL, nH])
    comando_centro_horizontal = b"\x1Ba\x01"

    comandos = (
        comando_posicion_horizontal + comando_centro_horizontal + texto.encode(encoder)
    )
    win32print.WritePrinter(hPrinter, comandos)


def text_align_left(hPrinter):
    win32print.WritePrinter(hPrinter, b"\x0D")


def set_text(hPrinter, text):
    win32print.WritePrinter(hPrinter, text.encode(encoder))


def print_barcode(hPrinter, ancho, alto, valor):
    # Comando ESC/POS para establecer el ancho del código de barras (2 a 5)
    comando_width = b"\x1Dw" + bytes([ancho])
    # Comando ESC/POS para establecer la altura del código de barras (0 a 255)
    comando_height = b"\x1Dh" + bytes([alto])

    comando_imprimir = b"\x1Dk\x06" + valor.encode(encoder) + b"\x00"
    comandos = comando_width + comando_height + comando_imprimir
    win32print.WritePrinter(hPrinter, comandos)


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
    printer_name = "P-58"
    desactivar_kanji = b"\x1C\x2E"
    printer_exists = False
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL, None, 1)
    for printer in printers:
        if printer[2] == printer_name:
            printer_exists = True

    # print(propina)
    propinaMount = float(total_payment) * 0.10
    numero_formateado = "{:.2f}".format(propinaMount)

    if printer_exists:
        try:
            hPrinter = win32print.OpenPrinter(printer_name)
            hJob = win32print.StartDocPrinter(
                hPrinter, 1, ("ESC/POS Receipt", None, "RAW")
            )
            win32print.StartPagePrinter(hPrinter)

            initialize_printer(hPrinter)
            win32print.WritePrinter(hPrinter, desactivar_kanji)

            printerWidth = 53

            if not es_recibo:
                # Bloque SAT
                sat_text = (
                    "DOCUMENTO DE FACTURACION \nDE LA SAT XD\nABCD-EFGH-IJKL-MNOP"
                )
                text_align_center(hPrinter, printerWidth, sat_text)
                feed(hPrinter, 1)
            else:
                text_align_center(hPrinter, printerWidth, "PRE-CUENTA")

            # Bloque Titulo
            header_text = "RESTAURANTE\nLA CATRINA\n"
            line = "=========================="
            total_line = "-------------------------------"
            text_align_center(hPrinter, printerWidth, header_text)
            text_align_center(hPrinter, printerWidth, line)
            feed(hPrinter, 1)

            if not es_recibo:
                text_align_center(
                    hPrinter, printerWidth, "Nombre: " + nombre_cliente + "\n"
                )
                text_align_center(hPrinter, printerWidth, "Nit: " + nit_cliente + "\n")
            text_align_center(hPrinter, printerWidth, "Fecha: " + fecha_orden + "\n")
            text_align_center(hPrinter, printerWidth, "Mesa: " + str(no_mesa) + "\n")
            text_align_center(hPrinter, printerWidth, "Area: " + area_mesa + "\n")

            # Bloque de Factura
            text_align_center(hPrinter, printerWidth, total_line)
            set_text(hPrinter, "Descripción\t\tPrecio\n")
            text_align_center(hPrinter, printerWidth, total_line)

            ##LOGICA DE DESGLOSAR PEDIDOS##
            for orden in orden_cliente:
                title = orden.get("title", "")
                price = orden.get("price", "")
                set_text(hPrinter, title + "\t\tQ. " + price + "\n")
                ###############################

            if propina:
                feed(hPrinter, 1)
                set_text(
                    hPrinter,
                    "Propina Sugerida" + "\t\tQ. " + str(numero_formateado) + "\n",
                )
                tempTotalMount = float(total_payment) + float(numero_formateado)
                formatTempTotal = "{:.2f}".format(tempTotalMount)
                total_payment = str(formatTempTotal)

            text_align_center(hPrinter, printerWidth, total_line)

            total_text = "Total:  Q " + total_payment + "\n"
            set_text(hPrinter, total_text)
            text_align_center(hPrinter, printerWidth, total_line)

            if not es_recibo:
                set_text(hPrinter, "¡GRACIAS POR SU VISITA\nVUELVA PRONTO!")

                feed(hPrinter, 1)

                # Bloque final
                text_align_center(hPrinter, printerWidth, line)
                feed(hPrinter, 1)
                print_barcode(hPrinter, 4, 55, "54321")

            text_align_center(hPrinter, printerWidth, line)

            if es_recibo:
                text_align_center(
                    hPrinter,
                    printerWidth,
                    "\nNit:_______________\nNombre:________________",
                )

                text_align_center(
                    hPrinter,
                    printerWidth,
                    "\n**Este no es un documento**\ntributario\n",
                )
            feed(hPrinter, 6)
            win32print.EndPagePrinter(hPrinter)
            win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)
