# Publicar la plataforma en internet

Guía para poner la aplicación en línea como **instalación privada**: accesible
desde cualquier sitio, pero solo para las cuentas que tú autorices.

---

## 1. Antes de empezar: qué NO debe publicarse

La aplicación incluye 1.450 preguntas importadas de un libro comercial del que
tienes **licencia personal**. Esa licencia te permite estudiar, pero **no
redistribuir** el contenido a otras personas. Por eso el despliegue se configura
como privado con lista de acceso: mientras solo entres tú, no hay redistribución.

Si algún día quieres abrirlo al público, antes habría que retirar ese contenido
o conseguir permiso por escrito del autor. Ten en cuenta además que «EFA» y
«EFPA» son marcas registradas.

---

## 2. Preparar la configuración

1. Copia `.env.ejemplo` a `backend/.env` y rellénalo.
2. Genera la clave de firma de sesiones:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Pon el resultado en `EFA_SECRET_KEY`. **Si cambias esta clave, todas las
sesiones abiertas dejan de valer** (que es justo lo que quieres si sospechas
que se ha filtrado).

3. Rellena `EFA_USUARIOS_PERMITIDOS` con tu correo y/o tu usuario, separados por
   comas. **Este es el candado de la instalación privada**: sin él, cualquiera
   con una cuenta de Google podría entrar.

```
EFA_USUARIOS_PERMITIDOS=tucorreo@gmail.com,pablo
```

4. Ajusta las direcciones a tu dominio:

```
EFA_ORIGENES_CORS=https://tudominio.com
EFA_URL_FRONTEND=https://tudominio.com
```

---

## 3. Dar de alta los proveedores de acceso

Esto **debes hacerlo tú**: hay que crear las aplicaciones en cada proveedor y
obtener credenciales. Yo no manejo secretos; los pegas en `backend/.env`.

En los tres casos, la URL de retorno que debes autorizar es:

```
https://TU-DOMINIO/api/auth/oauth/<proveedor>/callback
```

| Proveedor | Dónde se da de alta | Notas |
|---|---|---|
| **Google** | [Google Cloud Console → Credenciales](https://console.cloud.google.com/apis/credentials) | Crea un «ID de cliente de OAuth 2.0» de tipo *Aplicación web*. Es el más sencillo. |
| **Microsoft** | [Microsoft Entra → Registros de aplicaciones](https://entra.microsoft.com) | Elige cuentas «personales y de organización» si quieres admitir ambas. |
| **Facebook** | [Meta for Developers](https://developers.facebook.com/apps) | Exige HTTPS (salvo en localhost). Para pedir el correo a usuarios que no sean administradores de la app, Meta obliga a pasar una revisión. |

El proveedor que no configures simplemente **no aparece** en la pantalla de
acceso, así que puedes empezar solo con Google y añadir el resto después.

---

## 4. Desplegar

La aplicación es un único proceso: FastAPI sirve la API **y** el frontend ya
compilado, así que no necesitas dos servicios ni configurar CORS entre dominios.

```bash
# 1. Compilar el frontend
cd frontend && npm ci && npm run build && cd ..

# 2. Instalar dependencias del servidor
python -m pip install -r requirements-portable.txt

# 3. Arrancar (el proxy inverso se encarga del HTTPS)
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000
```

**HTTPS es obligatorio.** Los tokens de sesión viajan en las cabeceras: sin TLS
cualquiera en la misma red podría capturarlos. Lo normal es poner delante un
proxy (Caddy, Nginx) o usar una plataforma que ya dé HTTPS (Railway, Render,
Fly.io, Azure App Service…).

Ejemplo mínimo con Caddy, que gestiona el certificado solo:

```
tudominio.com {
    reverse_proxy localhost:8000
}
```

### Persistencia

Los usuarios registrados se guardan en `EFA_DATA_DIR` (por defecto `data/`).
En plataformas con sistema de ficheros efímero, monta ahí un volumen
persistente o se perderán en cada despliegue.

---

## 5. Comprobaciones antes de dar por bueno el despliegue

```bash
python -m pytest backend/ -q          # toda la batería en verde
```

Y en el navegador, ya con el dominio real:

- [ ] Entrar con usuario y contraseña.
- [ ] Entrar con Google (y con los demás proveedores que hayas configurado).
- [ ] Comprobar que una cuenta **no** incluida en `EFA_USUARIOS_PERMITIDOS`
      recibe «Esta instalación es privada y tu cuenta no está autorizada».
- [ ] Recargar la página: la sesión debe mantenerse.
- [ ] Cerrar sesión y confirmar que el temario deja de ser accesible.

Para verificar que la API está realmente protegida:

```bash
curl -i https://tudominio.com/api/study/secciones/M1
```

Debe responder **401**, no el contenido.

---

## 6. Qué queda fuera de esta guía

Cosas que no hacen falta para un uso privado, pero que serían obligatorias si
algún día lo abres a más gente:

- Política de privacidad y base legal del tratamiento (RGPD), al haber datos
  personales de terceros.
- Recuperación de contraseña y verificación por correo.
- Limitación de intentos de acceso (fuerza bruta) y registro de auditoría.
- Copias de seguridad de los datos de usuario.
