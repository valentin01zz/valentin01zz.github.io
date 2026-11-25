// Portfolio Valentín Gil — portada con scroll, palabras que rotan, menú, carrusel, terminal y contadores.
(function () {
  "use strict";

  const raiz = document.documentElement;
  raiz.classList.add("js");
  const quieto = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- Entrada al cargar ----------
  document.querySelectorAll("[data-entrada]").forEach((el) => {
    if (quieto) { el.classList.add("entro"); return; }
    requestAnimationFrame(() => requestAnimationFrame(() => el.classList.add("entro")));
  });

  // ---------- Portada: progreso del scroll en --p ----------
  const escenas = document.querySelectorAll("[data-escena]");
  function progreso() {
    escenas.forEach((s) => {
      const r = s.getBoundingClientRect();
      const recorrido = r.height - innerHeight;
      const p = recorrido > 0 ? Math.min(1, Math.max(0, -r.top / recorrido)) : 0;
      s.style.setProperty("--p", p.toFixed(4));
    });
  }
  if (escenas.length) {
    addEventListener("scroll", progreso, { passive: true });
    addEventListener("resize", progreso);
    progreso();
  }

  // ---------- Palabras que rotan ----------
  const rotas = document.querySelectorAll(".rota");
  if (rotas.length && !quieto) {
    setInterval(() => {
      rotas.forEach((r) => {
        const ems = [...r.children];
        const i = ems.findIndex((e) => e.classList.contains("on"));
        ems.forEach((e) => e.classList.remove("out"));
        ems[i].classList.replace("on", "out");
        ems[(i + 1) % ems.length].classList.add("on");
      });
    }, 2300);
  }

  // ---------- Menú desplegable de la píldora ----------
  const boton = document.querySelector("[data-abrir-menu]");
  const menu = document.getElementById("menu");
  if (boton && menu) {
    const cerrar = () => { menu.dataset.abierto = "false"; boton.setAttribute("aria-expanded", "false"); };
    boton.addEventListener("click", (e) => {
      e.stopPropagation();
      const abierto = menu.dataset.abierto === "true";
      menu.dataset.abierto = String(!abierto);
      boton.setAttribute("aria-expanded", String(!abierto));
      if (!abierto) { const a = menu.querySelector("a"); if (a) a.focus(); }
    });
    menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", cerrar));
    document.addEventListener("click", (e) => { if (!menu.contains(e.target)) cerrar(); });
    document.addEventListener("keydown", (e) => { if (e.key === "Escape" && menu.dataset.abierto === "true") { cerrar(); boton.focus(); } });
  }

  // ---------- Carrusel de trabajos ----------
  document.querySelectorAll("[data-carrusel]").forEach((bloque) => {
    const pista = bloque.querySelector(".carrusel");
    const paso = () => (pista.querySelector(".tarjeta")?.offsetWidth || 400) + 20;
    bloque.querySelector("[data-anterior]")?.addEventListener("click", () => pista.scrollBy({ left: -paso(), behavior: quieto ? "auto" : "smooth" }));
    bloque.querySelector("[data-siguiente]")?.addEventListener("click", () => pista.scrollBy({ left: paso(), behavior: quieto ? "auto" : "smooth" }));
  });

  // ---------- Terminal que se escribe sola (una vez, al aparecer) ----------
  const terminal = document.querySelector("[data-terminal]");
  if (terminal && !quieto && "IntersectionObserver" in window) {
    const final = terminal.innerHTML;
    const texto = terminal.textContent;
    const obs = new IntersectionObserver((entradas) => {
      if (!entradas[0].isIntersecting) return;
      obs.disconnect();
      let i = 0;
      terminal.textContent = "";
      const t = setInterval(() => {
        i += 2;
        terminal.textContent = texto.slice(0, i);
        if (i >= texto.length) { clearInterval(t); terminal.innerHTML = final; }
      }, 18);
    }, { threshold: 0.5 });
    obs.observe(terminal);
  }

  // ---------- Contadores (el HTML ya trae el número final) ----------
  const formato = new Intl.NumberFormat("es-AR");
  const contadores = document.querySelectorAll("[data-contar]");
  if (!quieto && "IntersectionObserver" in window && contadores.length) {
    const obs = new IntersectionObserver((entradas) => {
      entradas.forEach((e) => {
        if (!e.isIntersecting) return;
        obs.unobserve(e.target);
        const el = e.target, final = Number(el.dataset.contar), inicio = performance.now();
        const paso = (ahora) => {
          const t = Math.min(1, (ahora - inicio) / 1400);
          el.textContent = formato.format(Math.round(final * (1 - Math.pow(1 - t, 3))));
          if (t < 1) requestAnimationFrame(paso);
        };
        requestAnimationFrame(paso);
      });
    }, { threshold: 0.6 });
    contadores.forEach((el) => obs.observe(el));
  }
})();
