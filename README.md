# RRF-APPS — web de desarrollador

Web estática servida con GitHub Pages en <https://rirofer82.github.io/>.

| Página | URL | Para qué |
|---|---|---|
| Portada | `/` | Presentación y lista de apps |
| Política de privacidad | `/privacy/` | **Una sola para todas las apps**: es la URL que se pone en Play Console de cada app |
| Deepdoku | `/deepdoku/` | Página del juego con las imágenes de la ficha |
| app-ads.txt | `/app-ads.txt` | Vendedores autorizados de AdMob (la web de desarrollador de la ficha de Google Play debe ser `https://rirofer82.github.io`) |

Todos los textos están en español, inglés, francés y portugués; se ve el del navegador y se puede cambiar arriba a la derecha.

## Cambiar algo

Los textos están en `tools/build.py`. Después de editar:

```bash
python3 tools/build.py   # regenera las páginas
git commit -am "…" && git push
```

- **App nueva:** añádela a `APPS` (aparece en la política), crea su página copiando el bloque de Deepdoku y su tarjeta en la portada.
- **Deepdoku ya publicado:** pon `PLAY_LIVE = True` para que el botón enlace a Google Play.
- **Cambios en la política:** actualiza `UPDATED` con la fecha.
