(() => {
  const input = document.querySelector("#search");
  const results = document.querySelector("#search-results");
  if (!input || !results || !window.GUIDEBOOK_SEARCH) return;

  const pages = window.GUIDEBOOK_SEARCH;
  const normalize = (value) => value.toLocaleLowerCase("zh-CN");

  function run() {
    const query = normalize(input.value.trim());
    if (!query) {
      results.hidden = true;
      results.replaceChildren();
      return;
    }
    const terms = query.split(/\s+/).filter(Boolean);
    const ranked = pages
      .map((page) => {
        const title = normalize(page.title);
        const text = normalize(page.text);
        let score = 0;
        for (const term of terms) {
          if (!title.includes(term) && !text.includes(term)) return null;
          score += title.includes(term) ? 20 : 0;
          score += Math.min((text.match(new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "g")) || []).length, 10);
        }
        return { page, score };
      })
      .filter(Boolean)
      .sort((a, b) => b.score - a.score)
      .slice(0, 12);

    results.hidden = false;
    results.replaceChildren(...ranked.map(({ page }) => {
      const link = document.createElement("a");
      link.href = window.SEARCH_ROOT + page.url;
      const title = document.createElement("strong");
      title.textContent = page.title;
      const summary = document.createElement("small");
      summary.textContent = page.summary;
      link.append(title, summary);
      return link;
    }));
  }

  input.addEventListener("input", run);
  input.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      input.value = "";
      run();
      input.blur();
    }
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "/" && document.activeElement !== input) {
      event.preventDefault();
      input.focus();
    }
  });
})();
