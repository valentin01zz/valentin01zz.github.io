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
                  ("Tecnología", "Python · SQLite"), ("Año", "2026")],
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
            "App de celular para el dueño.",
        ],
        "galeria": [
            ("donafull/reportes.webp", 1600, 782, "Reportes del mes con ventas por día y top 10 de productos", True),
            ("donafull/inventario.webp", 1600, 450, "Inventario con buscador y productos con stock bajo resaltados", False),
            ("donafull/analisis-excel.webp", 1600, 782, "Análisis de ventas que genera un Excel con gráficos", False),
        ],
        "telefonos": [],
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
<html lang="es-AR" data-type="service">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · Valentín Gil</title>
<meta name="description" content="{bajada}">
<meta name="page-type" content="service">
<meta name="site-kind" content="other">
<meta name="theme-color" content="#efede8">
<meta property="og:type" content="article">
<meta property="og:title" content="{titulo} · Valentín Gil">
<meta property="og:description" content="{bajada}">
<meta property="og:image" content="https://valentin01zz.github.io/img/compartir.jpg">
<link rel="canonical" href="https://valentin01zz.github.io/proyectos/{slug}.html">
<meta property="og:url" content="https://valentin01zz.github.io/proyectos/{slug}.html">
<link rel="icon" href="../img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..100,500..800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../css/sitio.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>

<header class="nav">
  <div class="wrap nav-barra">
    <a class="skip-link label" href="#contenido">Saltar al contenido</a>
    <a class="logo label" href="../index.html" aria-label="Valentín Gil, inicio"><span class="logo-marca" aria-hidden="true">VG</span><span>Valentín Gil</span></a>
    <button class="menu-boton label" type="button" data-abrir-menu aria-expanded="false" aria-controls="menu">Menú <span class="puntos" aria-hidden="true"><i></i><i></i><i></i></span></button>
  </div>
</header>

<div class="menu" id="menu" data-abierto="false" role="dialog" aria-modal="true" aria-label="Menú">
  <div class="menu-cabeza">
    <span class="label">Valentín Gil</span>
    <button class="menu-cerrar label" type="button" data-cerrar-menu>Cerrar ✕</button>
  </div>
  <ul class="menu-links">
    <li><a class="display" href="../index.html#proyectos"><span class="label">01</span>Proyectos</a></li>
    <li><a class="display" href="../index.html#trabajo"><span class="label">02</span>Cómo trabajo</a></li>
    <li><a class="display" href="../index.html#bitacora"><span class="label">03</span>Bitácora</a></li>
    <li><a class="display" href="../index.html#contacto"><span class="label">04</span>Contacto</a></li>
  </ul>
  <div class="menu-pie label">
    <span>San Juan, Argentina</span>
    <a href="{wa}" target="_blank" rel="noopener">WhatsApp ↗</a>
    <a href="mailto:{mail}">{mail}</a>
    <a href="{github}" target="_blank" rel="noopener">GitHub ↗</a>
  </div>
</div>

<main id="contenido">

  <section class="caso-portada" data-entrada aria-labelledby="titulo">
    <div class="wrap">
      <div class="hero-text">
        <a class="volver label" href="../index.html#proyectos">← Todos los proyectos</a>
        <p class="label acento aparece">{num} / Caso real</p>
        <h1 class="display" id="titulo"><span class="linea"><span>{titulo}</span></span></h1>
        <p class="caso-bajada aparece">{bajada}</p>
        <div class="botones label aparece" style="margin-top:28px">{cta}</div>
      </div>
      <dl class="ficha label aparece">
{ficha}
      </dl>
    </div>
  </section>

  <section class="seccion caso-pantalla{fondo}" aria-labelledby="t-vista">
    <div class="wrap">
      <h2 class="display titulo-seccion" id="t-vista">Pantallas de {titulo}</h2>
{portada}
{datos}
    </div>
  </section>

  <section class="seccion" aria-labelledby="t-problema">
    <div class="wrap bloque-grilla">
      <div class="bloque-texto-col">
        <h2 class="display titulo-seccion" id="t-problema">Qué necesitaba</h2>
        <div class="bloque-texto">
{problema}
        </div>
        <h3 class="subtitulo">Qué construí</h3>
        <ul class="lista-hecho">
{hecho}
        </ul>
      </div>
      <div class="bloque-imagen">{lado}</div>
    </div>
  </section>

{galeria}
</main>

<footer class="closing oscuro">
  <div class="wrap">
    <div class="cierre-caso">
      <div>
{links}
        <h2 class="display titulo-cierre">¿Querés algo así para tu negocio?</h2>
        <div class="botones label" style="margin-top:24px"><a class="btn btn-principal" href="{wa_caso}" target="_blank" rel="noopener">Escribime por WhatsApp <span class="flecha" aria-hidden="true">→</span></a></div>
      </div>
      <a class="siguiente" href="{sig_slug}.html">
        <span class="marco siguiente-foto">{sig_img}</span>
        <span class="label apagado" style="display:block;margin-top:16px">Siguiente proyecto →</span>
        <span class="display" style="display:block;margin-top:8px">{sig_titulo}</span>
      </a>
    </div>
    <p class="pie label">© 2026 Valentín Gil · <a href="{wa}" target="_blank" rel="noopener">¿Tenés una idea? Escribime ↗</a> · <a href="#titulo">Volver arriba ↑</a></p>
  </div>
</footer>

<nav class="actionbar" aria-label="Contacto rápido">
  <a class="btn btn-principal label" href="{wa}" target="_blank" rel="noopener">Escribime por WhatsApp <img src="../img/iconos/whatsapp.svg" alt="" width="20" height="20"></a>
</nav>

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
        portada = f'      <div class="caso-vista"><div class="marco">{img(src, w, h, alt)}</div></div>'
        fondo = " oscuro"
    else:
        tel = "".join(f'<span class="telefono">{img(s, 390, 844, a)}</span>' for s, a in c["telefonos"][:4])
        portada = f'      <div class="galeria-telefonos">{tel}</div>'
        fondo = " superficie"

    datos = ""
    if c["datos"]:
        items = "".join(
            f'<p class="dato"><strong data-contar="{n}">{numero(n)}</strong><span class="label apagado">{escape(t)}</span></p>'
            for n, t in c["datos"])
        datos = f'      <div class="datos" style="margin-top:20px">{items}</div>'

    problema = "\n".join(f"          <p>{p}</p>" for p in c["problema"])
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
        lado += f'<div class="marco" style="margin-top:24px">{img(s1, w1, h1, a1)}</div>'
        resto = []

    galeria = ""
    if resto:
        items = "".join(
            f'<div class="marco{" ancha" if ancha else ""}">{img(s, w, h, a)}</div>'
            for s, w, h, a, ancha in resto)
        galeria = (
            '  <section class="seccion superficie" aria-labelledby="t-pantallas">\n'
            '    <div class="wrap">\n'
            '      <h2 class="display titulo-seccion" id="t-pantallas">Más pantallas</h2>\n'
            f'      <div class="galeria">{items}</div>\n'
            '    </div>\n'
            '  </section>\n')

    links = ""
    if c["links"]:
        items = "".join(
            f'<a class="btn{" btn-principal" if i == 0 else ""}" href="{u}" target="_blank" rel="noopener">{escape(t)} <span class="flecha" aria-hidden="true">↗</span></a>'
            for i, (t, u) in enumerate(c["links"]))
        links = (
            '        <div class="comprobalo">\n'
            '          <p class="label apagado">Comprobalo vos</p>\n'
            f'          <div class="botones label">{items}</div>\n'
            '        </div>')

    texto_wa = quote(f"Hola Valentín, vi el caso de {c['titulo']} en tu portfolio y quiero algo parecido para mi negocio.")
    wa_caso = f"{WA}?text={texto_wa}"
    if c["links"]:
        t0, u0 = c["links"][0]
        cta = f'<a class="btn btn-principal" href="{u0}" target="_blank" rel="noopener">{escape(t0)} <span class="flecha" aria-hidden="true">↗</span></a>'
    else:
        cta = f'<a class="btn btn-principal" href="{wa_caso}" target="_blank" rel="noopener">Quiero algo así <span class="flecha" aria-hidden="true">→</span></a>'

    return PLANTILLA.format(
        slug=c["slug"], titulo=escape(c["titulo"]), num=c["num"], bajada=escape(c["bajada"]), ficha=ficha,
        portada=portada, fondo=fondo, datos=datos, problema=problema, hecho=hecho, galeria=galeria, links=links,
        sig_slug=c["siguiente"][0], sig_titulo=escape(c["siguiente"][1]),
        sig_img=img(*FOTO_SIGUIENTE[c["siguiente"][0]]), lado=lado, cta=cta, wa_caso=wa_caso, wa=WA, mail=MAIL, github=GITHUB)


if __name__ == "__main__":
    SALIDA.mkdir(exist_ok=True)
    for caso in CASOS:
        destino = SALIDA / f"{caso['slug']}.html"
        destino.write_text(generar(caso), encoding="utf-8")
        print(destino)
