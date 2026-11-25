"""Genera las páginas de caso (proyectos/*.html) desde los datos de abajo.

Uso: python herramientas/generar_casos.py
Para cambiar un texto de un caso, editalo acá y volvé a correr el script.
"""
from html import escape
from urllib.parse import quote
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / "proyectos"

WA = "https://wa.me/5492646319973"
MAIL = "gilvalentin402@gmail.com"
GITHUB = "https://github.com/valentin01zz"

# Foto que se muestra en "Siguiente proyecto"
FOTO_SIGUIENTE = {
    "donafull": ("donafull/punto-de-venta.webp", 1600, 782, "Punto de venta de DonaFull"),
    "turnofacil": ("turnofacil/inicio.webp", 1440, 830, "Inicio de TurnoFacil"),
    "mytrainapp": ("mytrainapp/collage.webp", 1330, 924, "Tres pantallas de MyTrainApp en el celular"),
}

CASOS = [
    {
        "slug": "donafull",
        "titulo": "DonaFull",
        "num": "01",
        "bajada": "Sistema de caja, inventario y reportes para un drugstore de barrio, con una app de celular para que el dueño siga el negocio desde donde esté.",
        "ficha": [("Cliente", "Drugstore de barrio"), ("Tipo", "Programa de PC + app de celular"),
                  ("Tecnología", "Python · SQLite · Flutter · Firebase"), ("Año", "2026")],
        "portada_img": ("donafull/punto-de-venta.webp", 1600, 782, "Pantalla de punto de venta de DonaFull"),
        "datos": [(2862, "ventas en un mes"), (790, "productos cargados"), (7, "secciones con atajo de teclado")],
        "problema": [
            "Un drugstore vende cientos de productos chicos por día, con más de un cajero y varias formas de pago.",
            "Hacía falta <strong>cobrar rápido</strong>, saber qué queda en stock y <strong>cerrar cada turno sin que falte plata</strong>. Y que el dueño pudiera ver todo sin estar en el local.",
        ],
        "hecho": [
            "Punto de venta con lector de códigos y atajos de teclado (F1 a F7).",
            "Cobro en efectivo, tarjeta, transferencia o mixto, con el vuelto calculado.",
            "Inventario con buscador, categorías y aviso de stock bajo.",
            "Cierre de caja por turno: compara lo que debería haber con lo que se contó.",
            "Reportes del mes: ventas por día y los productos más vendidos.",
            "Exporta un Excel con gráficos por día, medio de pago, vendedor y categoría.",
            "DonaFull Monitor: la app del dueño, con el día dibujado como una línea de subte, el stock y los reportes en tiempo real.",
        ],
        "galeria": [
            ("donafull/reportes.webp", 1600, 782, "Reportes del mes con ventas por día y top 10 de productos", True),
            ("donafull/inventario.webp", 1600, 450, "Inventario con buscador y productos con stock bajo resaltados", False),
            ("donafull/analisis-excel.webp", 1600, 782, "Análisis de ventas que genera un Excel con gráficos", False),
        ],
        "telefonos": [],
        "monitor": [
            ("donafull-monitor/hoy.webp", "Pantalla Hoy: el día como una línea de subte, con cada franja horaria como estación"),
            ("donafull-monitor/stock.webp", "Pantalla Stock con filtros de reponer y sin stock"),
            ("donafull-monitor/reportes.webp", "Pantalla Reportes con el gráfico de ventas de los últimos 14 días"),
        ],
        "links": [],
        "siguiente": ("turnofacil", "TurnoFacil"),
    },
    {
        "slug": "turnofacil",
        "titulo": "TurnoFacil",
        "num": "02",
        "bajada": "Turnos online para peluquerías, barberías y estéticas. Es mi propio producto: lo pensé, lo diseñé, lo programé y lo publiqué.",
        "ficha": [("Tipo", "Producto propio"), ("Para", "Negocios de servicios"),
                  ("Tecnología", "Django · PostgreSQL · MercadoPago"), ("Año", "2026")],
        "portada_img": ("turnofacil/inicio.webp", 1440, 830, "Página de inicio de TurnoFacil"),
        "datos": [(47, "archivos de pruebas automáticas"), (6, "módulos del sistema")],
        "problema": [
            "Muchos negocios de servicios siguen dando turnos por WhatsApp y anotándolos en un cuaderno.",
            "Se pisan horarios, la gente se olvida y el dueño pasa el día con el teléfono en la mano. <strong>TurnoFacil le da al negocio un link</strong> para que sus clientes reserven solos.",
        ],
        "hecho": [
            "Registro del negocio con verificación por email.",
            "Servicios con su duración y profesionales con sus horarios.",
            "Reserva online desde el celular, sin que el cliente cree una cuenta.",
            "Recordatorio por email un día antes del turno.",
            "El cliente reprograma o cancela solo, hasta 2 horas antes.",
            "Planes con prueba gratis y cobro por MercadoPago.",
            "Límite de intentos de ingreso, 47 archivos de pruebas y CI en GitHub.",
        ],
        "galeria": [
            ("turnofacil/pasos.webp", 1240, 530, "Los tres pasos de TurnoFacil: cargás tu negocio, compartís tu link, mirás tu agenda", True),
            ("turnofacil/funciones.webp", 1240, 400, "Funciones: recordatorio por email, cambios sin llamadas, agenda por profesional, hecho para el celular", True),
        ],
        "telefonos": [],
        "links": [("Probalo en turnofacil.online", "https://turnofacil.online/"),
                  ("Mirá el código en GitHub", "https://github.com/valentin01zz/TurnoFacil")],
        "siguiente": ("mytrainapp", "MyTrainApp"),
    },
    {
        "slug": "mytrainapp",
        "titulo": "MyTrainApp",
        "num": "03",
        "bajada": "Una app para que una entrenadora personal arme rutinas, anote pagos y sesiones, y sus alumnos vean su progreso desde el celular.",
        "ficha": [("Cliente", "Entrenadora personal"), ("Tipo", "App web para celular y compu"),
                  ("Tecnología", "Django · PostgreSQL · Render"), ("Año", "2026")],
        "portada_img": None,
        "datos": [],
        "problema": [
            "Una entrenadora con alumnos presenciales y a distancia necesitaba <strong>un solo lugar</strong> para las rutinas, los pagos y las sesiones.",
            "Y que cada alumno pudiera ver su rutina y su progreso <strong>sin instalar nada</strong> ni recordar una contraseña.",
        ],
        "hecho": [
            "Panel privado con la lista de alumnos y aviso de pagos vencidos.",
            "Rutinas por día con series, repeticiones y video de cada ejercicio.",
            "Registro de cada sesión con las cargas de cada serie.",
            "Pagos con fecha de vencimiento.",
            "Un enlace personal para cada alumno, sin usuario ni contraseña.",
            "Progreso del alumno: cuántos kilos sumó desde que empezó.",
            "Dominio propio, modo día y noche, páginas legales y guía de uso en PDF.",
        ],
        "galeria": [],
        "telefonos": [
            ("mytrainapp/alumnos.webp", "Lista de alumnos con avisos de pago"),
            ("mytrainapp/ficha.webp", "Ficha de un alumno con pagos y sesiones"),
            ("mytrainapp/planilla.webp", "Planilla para anotar las cargas de una sesión"),
            ("mytrainapp/progreso.webp", "Progreso del alumno por ejercicio"),
        ],
        # Sin link: la página pública muestra el nombre de la entrenadora.
        "links": [],
        "siguiente": ("donafull", "DonaFull"),
    },
]

PLANTILLA = """<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · Valentín Gil</title>
<meta name="description" content="{bajada}">
<meta name="theme-color" content="#faf8f5">
<meta property="og:type" content="article">
<meta property="og:title" content="{titulo} · Valentín Gil">
<meta property="og:description" content="{bajada}">
<meta property="og:image" content="https://portafolio-gilvalentin.com.ar/img/compartir.jpg">
<link rel="canonical" href="https://portafolio-gilvalentin.com.ar/proyectos/{slug}.html">
<meta property="og:url" content="https://portafolio-gilvalentin.com.ar/proyectos/{slug}.html">
<link rel="icon" href="../img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@300;400;500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/sitio.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
<a class="skip-link" href="#contenido">Saltar al contenido</a>

<header class="nav">
  <nav class="pill" aria-label="Principal">
    <a class="logo" href="../index.html" aria-label="Valentín Gil, inicio">valentín<span class="punto">.</span></a>
    <button class="menu-boton" type="button" data-abrir-menu aria-expanded="false" aria-controls="menu">Menú <svg class="chev" width="12" height="12" viewBox="0 0 12 12" aria-hidden="true"><path d="M3 4.5l3 3 3-3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg></button>
    <a class="contacto" href="../index.html#contacto">Contacto +</a>
  </nav>
  <div class="menu" id="menu" data-abierto="false">
    <a href="../index.html#trabajos">Trabajos <span>01</span></a>
    <a href="../index.html#sobre">Sobre mí <span>02</span></a>
    <a href="../index.html#servicios">Servicios <span>03</span></a>
    <a href="../index.html#proceso">Proceso <span>04</span></a>
    <a href="../index.html#contacto">Contacto <span>05</span></a>
    <a href="{wa}" target="_blank" rel="noopener">WhatsApp <span>↗</span></a>
  </div>
</header>

<main id="contenido">

  <section class="caso-portada" data-entrada aria-labelledby="titulo">
    <div class="wrap">
      <a class="volver entra" href="../index.html#trabajos">← Todos los trabajos</a>
      <p class="kicker entra">{num} · Caso real</p>
      <h1 id="titulo">{titulo}<span class="punto">.</span></h1>
      <p class="caso-bajada">{bajada}</p>
      <div class="caso-acciones">{cta}</div>
      <dl class="ficha">
{ficha}
      </dl>
    </div>
  </section>

  <section aria-labelledby="t-vista">
    <div class="wrap">
      <h2 class="kicker" id="t-vista" style="margin-bottom:24px">Pantallas de {titulo}</h2>
{portada}
{datos}
    </div>
  </section>

  <section class="seccion" aria-labelledby="t-problema">
    <div class="wrap caso-grilla">
      <div class="caso-texto">
        <p class="kicker">El problema</p>
        <h2 class="titulo" id="t-problema">Qué <em>necesitaba</em><span class="punto">.</span></h2>
{problema}
        <h3 class="subtitulo">Qué construí</h3>
        <ul class="lista-hecho">
{hecho}
        </ul>
      </div>
      <div class="caso-lado">{lado}</div>
    </div>
  </section>

{monitor}
{galeria}
  <section class="seccion" aria-labelledby="t-cierre">
    <div class="wrap cierre-caso">
      <div>
{links}
        <h2 class="titulo" id="t-cierre">¿Querés algo así para <em>tu negocio</em>?</h2>
        <div><a class="btn btn-rojo" href="{wa_caso}" target="_blank" rel="noopener">Escribime por WhatsApp <span class="flecha" aria-hidden="true">→</span></a></div>
      </div>
      <a class="siguiente" href="{sig_slug}.html">
        <span class="siguiente-foto">{sig_img}</span>
        <span class="kicker">Siguiente proyecto</span>
        <strong>{sig_titulo} →</strong>
      </a>
    </div>
  </section>

</main>

<footer class="pie">
  <div class="wrap">
    <div class="pie-arriba">
      <a href="#titulo">Volver arriba ↑</a>
      <div class="pie-links">
        <a href="{wa}" target="_blank" rel="noopener">WhatsApp ↗</a>
        <a href="{github}" target="_blank" rel="noopener">GitHub ↗</a>
        <a href="mailto:{mail}">Correo ↗</a>
      </div>
    </div>
    <p class="pie-marca" aria-hidden="true">valentín<span class="punto">.</span></p>
  </div>
  <div class="pie-legal wrap"><span>© 2026 Valentín Gil · San Juan, Argentina</span></div>
</footer>

<script src="../js/sitio.js" defer></script>
</body>
</html>
"""


def img(src, w, h, alt, extra=""):
    return f'<img src="../img/{src}" width="{w}" height="{h}" alt="{escape(alt)}" loading="lazy"{extra}>'


def numero(n):
    return f"{n:,}".replace(",", ".")


def generar(c):
    ficha = "\n".join(f"        <div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>" for k, v in c["ficha"])

    if c["portada_img"]:
        src, w, h, alt = c["portada_img"]
        portada = f'      <div class="caso-vista">{img(src, w, h, alt)}</div>'
    else:
        tel = "".join(f'<span class="telefono">{img(s, 390, 844, a)}</span>' for s, a in c["telefonos"][:4])
        portada = f'      <div class="caso-telefonos">{tel}</div>'

    datos = ""
    if c["datos"]:
        items = "".join(
            f'<p class="dato"><strong data-contar="{n}">{numero(n)}</strong><span>{escape(t)}</span></p>'
            for n, t in c["datos"])
        datos = f'      <div class="datos">{items}</div>'

    problema = "\n".join(f"        <p>{p}</p>" for p in c["problema"])
    hecho = "\n".join(
        f'          <li><span class="vineta" aria-hidden="true"></span><span>{escape(t)}</span></li>'
        for t in c["hecho"])

    if c["galeria"]:
        s0, w0, h0, a0, _ = c["galeria"][0]
        lado = f'<div class="marco">{img(s0, w0, h0, a0)}</div>'
        resto = c["galeria"][1:]
    else:
        lado = f'<span class="telefono">{img("mytrainapp/alumno-rutina.webp", 390, 844, "Rutina del alumno vista desde su celular")}</span>'
        resto = []
    if len(resto) == 1:
        s1, w1, h1, a1, _ = resto[0]
        lado += f'<div class="marco">{img(s1, w1, h1, a1)}</div>'
        resto = []

    galeria = ""
    if resto:
        items = "".join(
            f'<div class="marco{" ancha" if ancha else ""}">{img(s, w, h, a)}</div>'
            for s, w, h, a, ancha in resto)
        galeria = (
            '  <section aria-labelledby="t-pantallas">\n'
            '    <div class="wrap">\n'
            '      <h2 class="kicker" id="t-pantallas" style="margin-bottom:24px">Más pantallas</h2>\n'
            f'      <div class="galeria">{items}</div>\n'
            '    </div>\n'
            '  </section>\n')

    links = ""
    if c["links"]:
        items = "".join(
            f'<a class="chip" href="{u}" target="_blank" rel="noopener">{escape(t)} ↗</a>'
            for t, u in c["links"])
        links = f'        <div class="sobre-links">{items}</div>'

    texto_wa = quote(f"Hola Valentín, vi el caso de {c['titulo']} en tu portfolio y quiero algo parecido para mi negocio.")
    wa_caso = f"{WA}?text={texto_wa}"
    if c["links"]:
        t0, u0 = c["links"][0]
        cta = (f'<a class="btn btn-rojo" href="{u0}" target="_blank" rel="noopener">{escape(t0)} <span class="flecha" aria-hidden="true">↗</span></a>'
               f'<a class="btn" href="{wa_caso}" target="_blank" rel="noopener">Quiero algo así</a>')
    else:
        cta = f'<a class="btn btn-rojo" href="{wa_caso}" target="_blank" rel="noopener">Quiero algo así <span class="flecha" aria-hidden="true">→</span></a>'

    monitor = ""
    if c.get("monitor"):
        tels = "".join(f'<span class="telefono">{img(s, 540, 1155, a)}</span>' for s, a in c["monitor"])
        monitor = (
            '  <section class="seccion monitor" id="monitor" aria-labelledby="t-monitor">\n'
            '    <div class="wrap monitor-grilla">\n'
            '      <div class="monitor-texto">\n'
            '        <p class="kicker">App del dueño</p>\n'
            '        <h2 class="titulo" id="t-monitor">DonaFull <em>Monitor</em><span class="punto">.</span></h2>\n'
            '        <p>El dueño no tiene que estar en el local para saber cómo va. Abre el celular y ve el día dibujado como una línea de subte: cada franja horaria es una estación, cada cajero una línea de color y el cambio de turno, un transbordo.</p>\n'
            '        <p>Stock con alertas de reposición, movimientos, ventas y reportes diarios, semanales y mensuales. Todo en tiempo real, sincronizado con la caja de la PC.</p>\n'
            '        <div class="etiquetas"><span class="etiqueta">Flutter</span><span class="etiqueta">Firebase</span><span class="etiqueta">Tiempo real</span><span class="etiqueta">Android</span></div>\n'
            '      </div>\n'
            f'      <div class="monitor-telefonos">{tels}</div>\n'
            '    </div>\n'
            '  </section>\n')

    return PLANTILLA.format(
        slug=c["slug"], titulo=escape(c["titulo"]), num=c["num"], bajada=escape(c["bajada"]), ficha=ficha,
        portada=portada, datos=datos, problema=problema, hecho=hecho, galeria=galeria, links=links,
        sig_slug=c["siguiente"][0], sig_titulo=escape(c["siguiente"][1]),
        sig_img=img(*FOTO_SIGUIENTE[c["siguiente"][0]]), monitor=monitor, lado=lado, cta=cta, wa_caso=wa_caso,
        wa=WA, mail=MAIL, github=GITHUB)


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for caso in CASOS:
        destino = SALIDA / f"{caso['slug']}.html"
        destino.write_text(generar(caso), encoding="utf-8")
        print(destino)
