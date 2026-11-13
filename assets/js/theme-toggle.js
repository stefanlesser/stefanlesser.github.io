/*
Theme toggle.

Default theme follows the OS setting (handled by pure CSS via
prefers-color-scheme, so no flash of wrong theme and the site works
with JavaScript disabled). When the visitor toggles, the choice is
stored in sessionStorage for the rest of the browsing session and wins
over the OS setting; a new visit starts from the system setting again.
If the OS setting changes while the page is open and the visitor has
not toggled, the page follows it live.
*/
(function () {
  'use strict';

  var root = document.documentElement;
  var toggle = document.getElementById('theme-toggle');
  var meta = document.querySelector('meta[name="theme-color"]');
  var mql = window.matchMedia('(prefers-color-scheme: dark)');

  var THEME_KEY = 'theme';
  var THEME_COLORS = { light: '#ffffff', dark: '#1a1a1a' };

  function readStored() {
    try {
      var t = sessionStorage.getItem(THEME_KEY);
      return t === 'light' || t === 'dark' ? t : null;
    } catch (e) {
      return null;
    }
  }

  function currentTheme() {
    var stored = readStored();
    if (stored) {
      return stored;
    }
    return mql.matches ? 'dark' : 'light';
  }

  function apply(theme) {
    root.setAttribute('data-theme', theme);
    if (meta) {
      meta.setAttribute('content', THEME_COLORS[theme]);
    }
    if (toggle) {
      toggle.setAttribute(
        'aria-label',
        theme === 'dark' ? 'Switch to light theme' : 'Switch to dark theme'
      );
    }
  }

  toggle.addEventListener('click', function () {
    var next = currentTheme() === 'dark' ? 'light' : 'dark';
    try {
      sessionStorage.setItem(THEME_KEY, next);
    } catch (e) {
      /* private browsing: toggle still works for this page */
    }
    apply(next);
  });

  function onSystemChange() {
    if (!readStored()) {
      apply(currentTheme());
    }
  }

  if (typeof mql.addEventListener === 'function') {
    mql.addEventListener('change', onSystemChange);
  } else if (typeof mql.addListener === 'function') {
    mql.addListener(onSystemChange); // older Safari
  }

  apply(currentTheme());
})();
