"""Prepara capturas de DonaFull Monitor (app del dueño) para el portfolio.

Pixela montos de plata y nombres de cajeros. Las cantidades (ventas, productos) quedan.
Uso: python herramientas/anonimizar_monitor.py
Lee ../donafull-monitor/.impeccable/review y escribe en img/donafull-monitor.
Coordenadas de capturas de 1080x2400.
"""
from pathlib import Path

from PIL import Image

RAIZ = Path(__file__).resolve().parent.parent
ORIGEN = RAIZ.parent / "donafull-monitor" / ".impeccable" / "review"
DESTINO = RAIZ / "img" / "donafull-monitor"

CAPTURAS = {
    "real_01_hoy.png": ("hoy", [
        (80, 400, 700, 520),     # total del día
        (80, 570, 1000, 700),    # quién atiende + promedio
        (30, 760, 1060, 900),    # leyenda de cajeros con montos
        (820, 1240, 1065, 2170), # montos por franja
        (320, 1240, 600, 2170),  # nombres en cada franja
        (150, 1760, 300, 1835),  # nombre en el cambio de turno
    ]),
    "real_03_stock.png": ("stock", []),
    "real_07_reportes.png": ("reportes", [
        (40, 570, 620, 700),     # total del período
        (240, 700, 640, 790),    # promedio por día
        (15, 970, 140, 1440),    # eje con montos
        (760, 1630, 1065, 2110), # montos por día
    ]),
}


def pixelar(im, caja, bloque=18):
    zona = im.crop(caja)
    chica = zona.resize((max(1, zona.width // bloque), max(1, zona.height // bloque)), Image.BILINEAR)
    im.paste(chica.resize(zona.size, Image.NEAREST), caja[:2])


if __name__ == "__main__":
    DESTINO.mkdir(parents=True, exist_ok=True)
    for origen, (nombre, cajas) in CAPTURAS.items():
        im = Image.open(ORIGEN / origen).convert("RGB")
        for caja in cajas:
            pixelar(im, caja)
        im = im.crop((0, 90, 1080, 2400))  # sin la barra de estado del celular
        im.thumbnail((540, 1200))
        salida = DESTINO / f"{nombre}.webp"
        im.save(salida, "WEBP", quality=86)
        print(salida, im.size)
