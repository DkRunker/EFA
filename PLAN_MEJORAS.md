# Plan de mejoras — Plataforma EFA (ronda tras periodo de pruebas)

Fecha: 19/08/2026. Cuatro frentes: (A) que se vea bien en el móvil, (B) modo
claro/oscuro, (C) quitar el reclamo de "oficial", (D) reforzar el bloque de
macroeconomía del Módulo 1 con un libro de licencia libre.

Las tareas A, B y C las hago yo directamente sobre el frontend. La tarea D
(contenido) se hace con **un único subagente cada vez**, secuencial, para no
gastar la ventana de contexto.

---

## A. Que se vea bien en el móvil (responsive)

**Diagnóstico:** `App.css` está vacío y no hay *media queries*; el layout usa
anchos y rejillas pensados para pantalla grande, y muchos estilos van "en línea"
dentro de `App.tsx`. En el móvil el contenido se sale de la pantalla y la teoría
(barra lateral + contenido) no se apila.

**Mi opinión sobre la letra:** el problema principal **no es solo el tamaño de
letra**, es que el diseño no se adapta al ancho. Agrandar la fuente sin arreglar
el layout no soluciona que el contenido se salga. Por eso propongo:
1. **Layout adaptable** (lo que más se nota): en pantallas estrechas, todo a
   **una sola columna**; la barra lateral de secciones pasa a un desplegable
   arriba; las rejillas del panel se apilan.
2. **Tablas y fórmulas** que se desborden con **scroll horizontal propio** (dentro
   de su caja) en vez de romper la página.
3. **Tipografía de lectura más cómoda en móvil**: sí, subir un punto el tamaño
   del cuerpo de la teoría (para lectura larga) y el interlineado (~1.7), con
   márgenes/padding adecuados. No un "todo más grande", sino más legible donde se
   lee mucho texto.

**Cómo:** añadir *media queries* (p. ej. `@media (max-width: 768px)`) en
`index.css`, un contenedor de teoría que se apile, y sacar a clases CSS los
estilos en línea que estorben en móvil. Verificación con el navegador en tamaño
móvil.

## B. Modo claro / oscuro

**Diagnóstico:** la app es **solo oscura** (`color-scheme: dark`, colores fijos y
muchos `#fff`/`rgba(0,0,0,…)` en línea). Para un modo claro usable hay que
convertir esos colores a **variables de tema**.

**Cómo:**
1. Definir la paleta **clara** y **oscura** con variables CSS (`:root` = claro por
   defecto; `[data-theme="dark"]` = oscuro), respetando `prefers-color-scheme`
   para el primer arranque.
2. Sustituir los colores fijos que se romperían en claro (inputs con `color:#fff`
   sobre fondo oscuro, etc.) por variables.
3. **Botón para alternar** tema en la cabecera, con **persistencia** en
   `localStorage` (recuerda la elección del usuario).
4. Verificación en el navegador en claro y oscuro.

## C. Quitar el reclamo de "oficial"

**Diagnóstico:** en la pantalla de acceso (`App.tsx:697`) pone *"Accede a tu
simulador inteligente oficial"*. Eso puede dar a entender un respaldo oficial de
EFPA que no tenemos.

**Cómo:**
1. Cambiar ese texto por uno neutro (p. ej. *"Tu simulador inteligente para
   preparar la certificación"*).
2. Actualizar el test que lo comprueba (`App.test.tsx:10`).
3. **Revisar** los otros usos de "oficial" (insignia "Oficial", "convocatorias
   oficiales", "examen oficial de acceso"): describen que las preguntas provienen
   de convocatorias reales de EFPA, lo cual es cierto, pero conviene suavizar el
   tono para no sugerir vínculo con EFPA. Se propondrá redacción neutra y se
   decide contigo antes de aplicarla.

## D. Reforzar la macroeconomía del Módulo 1 (con un único subagente)

**Fuente:** *Principles of Macroeconomics 2e* — **OpenStax (Rice University)**,
licencia **Creative Commons Attribution 4.0 (CC BY 4.0)**. Verificado en el propio
libro. Es **contenido libre y adaptable con atribución**; el "All rights reserved"
del EPUB es de la reempaquetadora (XanEdu) y solo cubre logos/marcas, no el texto.
> Para evitar cualquier problema: se escribe **texto original en el estilo propio
> de la app** (los conceptos macro no son propiedad de nadie), usando el libro
> como referencia de exactitud y cobertura, **sin copiar/parafrasear de cerca**.
> Se añadirá una **nota de atribución** a OpenStax (CC BY 4.0) en el módulo.

**Alcance — "apartado primero del Módulo 1" = bloque macro**, sus tres secciones:
- `[0]` Fundamentos Macroeconómicos (~40k) → libro cap. 6-9, 11
- `[1]` Ciclos Económicos e Indicadores de Coyuntura (~39k) → cap. 11-13, 6-9
- `[2]` Política Monetaria y Política Fiscal (~35k, la más corta) → cap. 14-15, 17-18

**Método (uno cada vez, secuencial):**
Para cada sección, un subagente:
1. Cruza el temario actual con las **preguntas de test y los exámenes** para
   detectar los puntos flojos (dónde fallan/qué se pregunta y no está bien
   explicado).
2. **Refuerza y completa** esos puntos con el material del libro (extraído en
   `scratchpad/LIBRO_MACRO.md`), en el estilo de la app: definiciones con
   `[[término::definición]]`, callouts `:::ejemplo/:::error`, KaTeX con **una sola
   barra**, y simuladores donde aporten.
3. **Escribe el JSON de la sección a disco cuanto antes** y luego valida.
4. Yo **fusiono** (`fusionar_apartados.py`) y **valido** (`validar_json_seccion.py`)
   cada sección antes de pasar a la siguiente.

Empezamos por `[0]`, que es sin ambigüedad el "apartado primero". Tras verlo,
confirmamos alcance para `[1]` y `[2]`.

---

## Orden de ejecución

1. **C** (rápido): quitar "oficial" de la pantalla de acceso + test.
2. **A**: responsive/móvil.
3. **B**: modo claro/oscuro.
4. **D**: subagente para `[0]` → fusionar/validar → `[1]` → `[2]`.
   (D puede ir en paralelo a A/B: el subagente trabaja mientras yo toco el
   frontend, porque escribe a disco y no consume mi contexto.)

## Notas
- El contenido con licencia del libro y el `LIBRO_MACRO.md` extraído **no** se
  suben al repo público (igual que los exámenes).
- Añadir la nota de atribución CC BY a OpenStax cuando se integre el contenido.
