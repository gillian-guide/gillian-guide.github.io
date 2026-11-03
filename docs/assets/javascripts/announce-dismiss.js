/**
 * Dismiss the announcement banner for good.
 *
 * The theme persists the dismissal in `localStorage` under a key scoped to the
 * current directory (`/<page path>.__announce`), so pressing the X on one page
 * only hides the banner on that page - every other page, and every other
 * language, shows it again.
 *
 * This keeps the Material for MkDocs behaviour instead: one fingerprint of the
 * banner text, stored once, hiding the banner everywhere until the notice
 * itself changes.
 */
(function () {
  var KEY = "announce-dismissed";

  /* Cheap and stable fingerprint of the banner text */
  function fingerprint(text) {
    var hash = 0;
    var value = text.replace(/\s+/g, " ").trim();
    for (var i = 0; i < value.length; i++) {
      hash = (hash * 31 + value.charCodeAt(i)) | 0;
    }
    return String(hash);
  }

  function setup(banner) {
    var content = banner.querySelector(".md-typeset") || banner;
    var mark = fingerprint(content.textContent);

    var stored = null;
    try {
      stored = window.localStorage.getItem(KEY);
    } catch (error) {
      /* storage disabled: leave the banner alone */
    }

    if (stored === mark) {
      banner.hidden = true;
      return;
    }

    var button = banner.querySelector(".md-banner__button");
    if (!button || button.dataset.announceBound) return;
    button.dataset.announceBound = "1";
    button.addEventListener("click", function () {
      try {
        window.localStorage.setItem(KEY, mark);
      } catch (error) {
        /* storage disabled: the theme still hides it for this page */
      }
      banner.hidden = true;
    });
  }

  function run() {
    document.querySelectorAll('[data-md-component="announce"]').forEach(setup);
  }

  if (window.document$) {
    window.document$.subscribe(run);
  } else {
    document.addEventListener("DOMContentLoaded", run);
  }
})();
