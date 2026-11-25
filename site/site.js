// Copy buttons and the Loop phase filter. The site works without this script.
(() => {
  document.documentElement.classList.add("js");

  document.addEventListener("click", async (event) => {
    const button = event.target.closest("button[data-copy]");
    if (!button) return;
    const show = (label) => {
      button.textContent = label;
      setTimeout(() => { button.textContent = "Copy"; }, 1600);
    };
    try {
      await navigator.clipboard.writeText(button.dataset.copy);
      show("Copied");
    } catch {
      const code = button.parentElement.querySelector("code");
      if (code) {
        const range = document.createRange();
        range.selectNodeContents(code);
        const selection = getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
      }
      show("Selected");
    }
  });

  const bar = document.querySelector(".filter");
  if (!bar) return;
  const cards = [...document.querySelectorAll(".card[data-phases]")];
  const groups = [...document.querySelectorAll(".plugin")];
  bar.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-phase]");
    if (!button) return;
    const phase = button.dataset.phase;
    bar.querySelectorAll("button").forEach((b) => b.setAttribute("aria-pressed", String(b === button)));
    cards.forEach((card) => {
      card.hidden = phase !== "all" && !card.dataset.phases.split(" ").includes(phase);
    });
    groups.forEach((group) => { group.hidden = !group.querySelector(".card:not([hidden])"); });
  });
})();
