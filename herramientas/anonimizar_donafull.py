"""Prepara las capturas de DonaFull para el portfolio.

- Reemplaza el nombre de la cajera por "Caja 1".
- Pixela los montos de facturación (se dejan las cantidades).
- Recorta la barra de título de Windows y la marca de agua "Activar Windows".

Uso: python herramientas/anonimizar_donafull.py
Lee material/donafull-originales y escribe en img/donafull.
Las coordenadas son de capturas de 1600x900.
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ / "material" / "donafull-originales"
DESTINO = RAIZ / "img" / "donafull"

FONDO_BARRA = (19, 35, 48)
FUENTE = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 14)

# Recorte común: sin barra de título (arriba) ni marca de agua (abajo).
RECORTE = (0, 23, 1600, 805)

# archivo original -> (nombre de salida, zonas a pixelar, zonas a desenfocar)
CAPTURAS = {
    "01-punto-de-venta.png": ("punto-de-venta", [], []),
    # Inventario: se recorta desde el buscador para no mostrar las tarjetas de arriba
    # (el stock "gigante" es intencional, pero afuera se lee como error).
    "02-inventario.webp": ("inventario", [], [], (0, 355, 1600, 805)),
    "04-reportes.webp": (
        "reportes",
        [
            (535, 255, 895, 318),   # total vendido
            (930, 255, 1170, 318),  # ticket promedio
            (1440, 465, 1540, 765), # columna Total del top 10
            (282, 450, 328, 745),   # eje con montos del gráfico
        ],
        [(330, 440, 1135, 800)],    # rótulos chiquitos sobre las barras
    ),
    "05-analisis-excel.png": (
        "analisis-excel",
        [
            (285, 368, 640, 428),   # total vendido
            (980, 368, 1250, 428),  # ticket promedio
        ],
        [],
    ),
}


def pixelar(im: Image.Image, caja: tuple[int, int, int, int], bloque: int = 14) -> None:
    zona = im.crop(caja)
    chica = zona.resize((max(1, zona.width // bloque), max(1, zona.height // bloque)), Image.BILINEAR)
    im.paste(chica.resize(zona.size, Image.NEAREST), caja[:2])


def desenfocar(im: Image.Image, caja: tuple[int, int, int, int]) -> None:
    im.paste(im.crop(caja).filter(ImageFilter.GaussianBlur(2.2)), caja[:2])


def anonimizar(nombre_origen: str, nombre_destino: str, pixeles, desenfoques, recorte=RECORTE) -> Path:
    im = Image.open(ORIGEN / nombre_origen).convert("RGB")
    for caja in desenfoques:
        desenfocar(im, caja)
    for caja in pixeles:
        pixelar(im, caja)
    dibujo = ImageDraw.Draw(im)
    # Nombre de la cajera en la barra superior (al lado del ícono de usuario).
    dibujo.rectangle((1333, 42, 1410, 70), fill=FONDO_BARRA)
    dibujo.text((1336, 46), "Caja 1", font=FUENTE, fill=(235, 240, 245))
    im = im.crop(recorte)
    DESTINO.mkdir(parents=True, exist_ok=True)
    salida = DESTINO / f"{nombre_destino}.webp"
    im.save(salida, "WEBP", quality=86)
    return salida


if __name__ == "__main__":
    for origen, (destino, *resto) in CAPTURAS.items():
        print(anonimizar(origen, destino, *resto))
