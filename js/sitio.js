// Portfolio Valentín Gil — menú, entrada de la portada y contadores.
(function () {
  "use strict";

  const raiz = document.documentElement;
  raiz.classList.add("js");
  const quieto = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // ---------- Menú a pantalla completa ----------
  const menu = document.getElementById("menu");
  const abrir = document.querySelector("[data-abrir-menu]");
  const cerrar = menu && menu.querySelector("[data-cerrar-menu]");
  let ultimoFoco = null;

  function abrirMenu() {
    ultimoFoco = document.activeElement;
    menu.dataset.abierto = "true";
    menu.removeAttribute("inert");
    abrir.setAttribute("aria-expanded", "true");
    document.body.classList.add("menu-abierto");
    const primero = menu.querySelector(".menu-links a");
    if (primero) setTimeout(() => primero.focus(), 50);
  }

  function cerrarMenu() {
    menu.dataset.abierto = "false";
    menu.setAttribute("inert", "");
    abrir.setAttribute("aria-expanded", "false");
    document.body.classList.remove("menu-abierto");
    if (ultimoFoco) ultimoFoco.focus();
  }

  if (menu && abrir) {
    menu.setAttribute("inert", "");
    abrir.addEventListener("click", abrirMenu);
    cerrar.addEventListener("click", cerrarMenu);
    menu.querySelectorAll("a").forEach((a) => a.addEventListener("click", () => {
      ultimoFoco = null;
      cerrarMenu();
    }));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && menu.dataset.abierto === "true") cerrarMenu();
    });
  }

  // ---------- Entrada de la portada ----------
  document.querySelectorAll("[data-entrada]").forEach((el) => {
    if (quieto) { el.classList.add("entro"); return; }
    requestAnimationFrame(() => requestAnimationFrame(() => el.classList.add("entro")));
  });

  // ---------- Contadores ----------
  // El HTML ya trae el número final (se ve igual sin JS). Al aparecer, cuenta desde 0.
  const formato = new Intl.NumberFormat("es-AR");
  const contadores = document.querySelectorAll("[data-contar]");

  function contar(el) {
    const final = Number(el.dataset.contar);
    const duracion = 1400;
    const inicio = performance.now();
    function paso(ahora) {
      const t = Math.min(1, (ahora - inicio) / duracion);
      const suave = 1 - Math.pow(1 - t, 3);
      el.textContent = formato.format(Math.round(final * suave));
      if (t < 1) requestAnimationFrame(paso);
    }
    el.textContent = "0";
    requestAnimationFrame(paso);
  }

  if (!quieto && "IntersectionObserver" in window && contadores.length) {
    const obs = new IntersectionObserver((entradas) => {
      entradas.forEach((e) => {
        if (e.isIntersecting) { contar(e.target); obs.unobserve(e.target); }
      });
    }, { threshold: 0.6 });
    contadores.forEach((el) => obs.observe(el));
  }
})();
