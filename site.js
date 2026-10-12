// The taskbar clock, and the filter box on the asset list. The pages work without it.
(function () {
  var clock = document.getElementById("clock");
  function tick() {
    if (!clock) return;
    clock.textContent = new Date().toLocaleTimeString([], { hour: "numeric", minute: "2-digit" });
  }
  tick();
  setInterval(tick, 15000);

  var filter = document.getElementById("filter");
  if (!filter) return;
  var rows = Array.prototype.slice.call(document.querySelectorAll("#catalog tbody tr"));
  var note = document.getElementById("filter-count");
  filter.addEventListener("input", function () {
    var q = filter.value.trim().toLowerCase();
    var shown = 0;
    rows.forEach(function (row) {
      var hit = !q || row.textContent.toLowerCase().indexOf(q) !== -1;
      row.hidden = !hit;
      if (hit) shown++;
    });
    if (note) note.textContent = q ? shown + " matching rows" : "";
  });
})();
