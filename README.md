# RRF-APPS — web de desarrollador

Web estática servida con GitHub Pages en <https://rirofer82.github.io/>.

| Página | URL | Para qué |
|---|---|---|
| Portada | `/` | Presentación y lista de apps |
| Política de privacidad | `/privacy/` | **Una sola para todas las apps**: es la URL que se pone en Play Console de cada app |
| Deepdoku | `/deepdoku/` | Página del juego con las imágenes de la ficha |
| Culture Quizzes | `/culture-quizzes/` | Página del juego (Preguntas Cultura) con las imágenes de su ficha de Google Play |
| Box Rally | `/box-rally/` | Página del juego (próximamente) con las imágenes de su ficha de Google Play |
| app-ads.txt | `/app-ads.txt` | Vendedores autorizados de AdMob (la web de desarrollador de la ficha de Google Play debe ser `https://rirofer82.github.io`) |

Todos los textos están en español, inglés, francés y portugués; se ve el del navegador y se puede cambiar arriba a la derecha.

## Cambiar algo

Los textos están en `tools/build.py`. Después de editar:

```bash
python3 tools/build.py   # regenera las páginas
git commit -am "…" && git push
```

- **App nueva:** añádela a `APPS` (aparece en la política), crea su página copiando el bloque de Deepdoku y su tarjeta en la portada.
- **Botones de Google Play:** `PLAY_LIVE` (Deepdoku) y `CQ_PLAY_LIVE` (Culture Quizzes) están en `True` porque las dos apps ya están publicadas; `BR_PLAY_LIVE` (Box Rally) está en `False` y el botón muestra «Muy pronto en Google Play». Cuando se publique, ponlo en `True` y cambia su etiqueta de la portada (`br_tag`) a «Disponible».
- **Imágenes de Box Rally:** salen de `fastlane/metadata/android/<idioma>/images` del repo express-delivery-game (`npm run store` allí), pasadas a WebP en `box-rally/img/` (capturas a 960 × 540).
- **Imágenes de Culture Quizzes:** salen de `fastlane/metadata/android/<idioma>/images` del repo culture-quizzes-javascript (`npm run store` allí), pasadas a WebP en `culture-quizzes/img/`.
- **Cambios en la política:** actualiza `UPDATED` con la fecha.
