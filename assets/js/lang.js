// Idioma de la página: el elegido antes, el del navegador o español. Los textos están en bloques [data-l].
(function(){
  var LANGS = ['es', 'en', 'fr', 'pt'];
  var root = document.documentElement;
  function pick(){
    try { var s = localStorage.getItem('rrf-lang'); if (LANGS.indexOf(s) >= 0) return s; } catch (e) {}
    var q = (location.search.match(/[?&]lang=(\w\w)/) || [])[1]; if (LANGS.indexOf(q) >= 0) return q;
    var nav = navigator.languages || [navigator.language || 'es'];
    for (var i = 0; i < nav.length; i++){ var b = String(nav[i]).slice(0, 2).toLowerCase(); if (LANGS.indexOf(b) >= 0) return b; }
    return 'en';
  }
  function set(l){
    root.setAttribute('data-lang', l); root.lang = l === 'pt' ? 'pt-BR' : l;
    var buttons = document.querySelectorAll('.langs button');
    for (var i = 0; i < buttons.length; i++) buttons[i].setAttribute('aria-pressed', buttons[i].getAttribute('data-set') === l);
    var t = document.querySelector('meta[name="title-' + l + '"]'); if (t) document.title = t.content;
  }
  set(pick());
  document.addEventListener('DOMContentLoaded', function(){
    set(root.getAttribute('data-lang'));
    document.querySelectorAll('.langs button').forEach(function(b){
      b.addEventListener('click', function(){ var l = b.getAttribute('data-set'); try { localStorage.setItem('rrf-lang', l); } catch (e) {} set(l); });
    });
  });
})();
