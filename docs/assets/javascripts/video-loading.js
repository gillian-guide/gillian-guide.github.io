/**
 * Behaviour for the lite YouTube embeds used in video rows.
 *
 * - Video rows become a snapping carousel on narrow screens, opening on the
 *   card the page recommends rather than on the first one.
 * - On a phone, tapping a poster opens YouTube itself instead of loading a
 *   player into the card.
 * - On wider screens the player loads in place, and a spinner covers the gap
 *   between the click and the iframe arriving.
 */
(function () {
  var SPINNER = "lyt-spinner";
  var LOADING = "lyt-loading";
  var TIMEOUT = 10000;
  var FRAME_TIMEOUT = 3500;
  var NARROW = "(max-width: 50rem)";
  var WATCH = "https://www.youtube.com/watch?v=";

  function narrow() {
    return window.matchMedia(NARROW).matches;
  }

  function spinnerFor(embed) {
    if (!embed.querySelector("." + SPINNER)) {
      var spinner = document.createElement("span");
      spinner.className = SPINNER;
      spinner.setAttribute("aria-hidden", "true");
      embed.append(spinner);
    }
  }

  /* The recommended card keeps its ring while the player runs, so it needs a
     layer of its own instead of a shadow the player would cover */
  function ringFor(embed) {
    if (!embed.classList.contains("video-featured")) return;
    if (embed.querySelector(".lyt-ring")) return;
    var ring = document.createElement("span");
    ring.className = "lyt-ring";
    ring.setAttribute("aria-hidden", "true");
    embed.append(ring);
  }

  function activate(embed) {
    // Already playing: there is nothing to wait for
    if (embed.querySelector("iframe")) return;

    var settled = false;

    function stop() {
      if (settled) return;
      settled = true;
      embed.classList.remove(LOADING);
    }

    function bind() {
      var frame = embed.querySelector("iframe");
      if (!frame) return false;
      if (frame.dataset.spinnerBound) return true;
      frame.dataset.spinnerBound = "1";
      frame.addEventListener("load", stop, { once: true });
      // A cached player can finish before this listener exists - never let the
      // spinner outlive the player for more than a moment
      window.setTimeout(stop, FRAME_TIMEOUT);
      return true;
    }

    embed.classList.add(LOADING);

    // Watch for the player from before the embed creates it, so the load
    // listener is attached before the iframe can finish loading
    var observer = new MutationObserver(function () {
      if (bind()) observer.disconnect();
    });
    observer.observe(embed, { childList: true, subtree: true });

    // A player that never reports a load event must not leave the spinner up
    window.setTimeout(stop, TIMEOUT);
  }

  /* Open the recommended card of every carousel instead of its first card */
  function centre(row) {
    var featured = row.querySelector("lite-youtube.video-featured");
    if (!featured) return;
    if (row.scrollWidth <= row.clientWidth + 1) return; // a row, not a carousel
    var left = featured.getBoundingClientRect().left - row.getBoundingClientRect().left;
    row.scrollLeft = left + row.scrollLeft - (row.clientWidth - featured.offsetWidth) / 2;
    if (row.updateDots) row.updateDots();
  }

  /* Dots under a carousel, so it reads as something you can swipe */
  function setupRow(row) {
    if (row.dataset.dotsReady) return;
    var cards = Array.prototype.slice.call(row.querySelectorAll("lite-youtube"));
    if (cards.length < 2) return;
    row.dataset.dotsReady = "1";

    var dots = document.createElement("div");
    dots.className = "video-dots";

    var buttons = cards.map(function (card, index) {
      var button = document.createElement("button");
      button.type = "button";
      button.className = "video-dot";
      var author = card.querySelector(".lyt-author");
      button.setAttribute(
        "aria-label",
        author && author.textContent.trim() ? author.textContent.trim() : "Video " + (index + 1)
      );
      button.addEventListener("click", function () {
        card.scrollIntoView({ inline: "center", block: "nearest", behavior: "smooth" });
      });
      dots.appendChild(button);
      return button;
    });

    row.parentNode.insertBefore(dots, row.nextSibling);

    function update() {
      var middle = row.scrollLeft + row.clientWidth / 2;
      var best = 0;
      var bestDistance = Infinity;
      cards.forEach(function (card, index) {
        var distance = Math.abs(card.offsetLeft + card.offsetWidth / 2 - middle);
        if (distance < bestDistance) {
          bestDistance = distance;
          best = index;
        }
      });
      buttons.forEach(function (button, index) {
        button.classList.toggle("active", index === best);
      });
    }

    row.addEventListener(
      "scroll",
      function () {
        window.requestAnimationFrame(update);
      },
      { passive: true }
    );
    window.addEventListener("resize", update);
    row.updateDots = update;
    update();
  }

  function run() {
    document.querySelectorAll("lite-youtube").forEach(spinnerFor);
    document.querySelectorAll("lite-youtube").forEach(ringFor);
    document.querySelectorAll(".video-row").forEach(setupRow);
    document.querySelectorAll(".video-row").forEach(centre);
  }

  // Runs before the embed's own click handler (capture phase), so the spinner
  // observes the player being created, and a phone tap never reaches the embed.
  document.addEventListener(
    "click",
    function (event) {
      var embed = event.target.closest("lite-youtube");
      if (!embed) return;

      if (!narrow()) {
        activate(embed);
        return;
      }

      event.preventDefault();
      event.stopPropagation();
      var id = embed.getAttribute("videoid");
      if (id) window.location.href = WATCH + id;
    },
    true
  );

  window.addEventListener("resize", function () {
    document.querySelectorAll(".video-row").forEach(centre);
  });

  if (window.document$) {
    window.document$.subscribe(run);
  } else {
    document.addEventListener("DOMContentLoaded", run);
  }
})();
