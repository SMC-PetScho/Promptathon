const form = document.getElementById("plan-form");
const planContainer = document.getElementById("plan");
const planTemplate = document.getElementById("plan-template");
const rowTemplate = document.getElementById("row-template");

const monthLabels = [
  "Monat 1",
  "Monat 2",
  "Monat 3",
  "Monat 4",
  "Monat 5",
  "Monat 6",
];

const baseThemes = [
  "Finanzielle Bildung & Grundlagen",
  "Digitale Services & Mobile Banking",
  "Vertrauen & Sicherheit",
  "Community & regionale Engagements",
  "Produkte & Mehrwerte",
  "Kundenerfolg & Testimonials",
];

const channelMix = [
  "LinkedIn, Instagram Reels, Blog",
  "Instagram Stories, YouTube Shorts, Website",
  "LinkedIn, Facebook, Newsletter",
  "Instagram, TikTok, Event-Livestream",
  "LinkedIn, Blog, Webinar",
  "LinkedIn, YouTube, Podcast",
];

const ideaLibrary = [
  [
    "5-Punkte-Carousel zur Schuldenprävention",
    "Infografik über Spar- und Investmentoptionen",
    "Live Q&A mit Finanzcoach"
  ],
  [
    "App-Feature Walkthrough mit Screenshots",
    "Behind-the-Scenes Reel zur Produktentwicklung",
    "Community-Umfrage zur Lieblingsfunktion"
  ],
  [
    "Video-Statement der Sicherheitsabteilung",
    "Checkliste zur Passwortsicherheit",
    "Blog-Artikel über DSGVO-konforme Prozesse"
  ],
  [
    "Story-Reihe zu regionalen Förderprojekten",
    "Fotostrecke vom lokalen Event",
    "Kooperation mit lokalen Influencer:innen"
  ],
  [
    "Webinar zur Immobilienfinanzierung",
    "Vergleichsgrafik Girokonto vs. Premiumkonto",
    "Lead-Magnet: Whitepaper zu Anlage-Trends"
  ],
  [
    "Interview mit langjährigem Kunden",
    "Case-Study als Carousel",
    "User-generated Content Challenge"
  ],
];

const kpiLibrary = [
  "Reichweite, gespeicherte Beiträge, Webinar-Anmeldungen",
  "App-Downloads, Klickrate, Story-Replies",
  "Vertrauensindex (Umfrage), Newsletter-Anmeldungen",
  "Event-Anmeldungen, Social Shares, Community-Wachstum",
  "Lead-Anfragen, Landing-Page-Conversions, CTR",
  "Testimonial-Views, Empfehlungsrate, Kundenbindungs-Score",
];

function personaliseText(templateText, context) {
  return templateText
    .replace(/{{audience}}/g, context.audience)
    .replace(/{{positioning}}/g, context.positioning)
    .replace(/{{primaryGoal}}/g, context.primaryGoal)
    .replace(/{{secondaryGoal}}/g, context.secondaryGoal)
    .replace(/{{tone}}/g, context.toneLabel);
}

const toneTranslations = {
  vertrauensvoll: "vertrauensvolle",
  innovativ: "innovative",
  beratung: "beratende",
  locker: "lockere",
};

function buildNarrative(context) {
  return [
    `Starte mit edukativen Inhalten, die ${context.audience} in ihrer Finanzreise abholen.`,
    `Zeige anschließend, wie eure digitalen Services den Alltag erleichtern und ${context.primaryGoal.toLowerCase()} unterstützen.`,
    `Verstärke das Vertrauen durch Einblicke in Sicherheitsprozesse und persönliche Beratung.`,
    `Positioniere die Bank als aktiven Teil der Gemeinschaft und stärke die emotionale Bindung.`,
    `Präsentiere konkrete Produkte und Services mit klaren Mehrwerten und starken Calls-to-Action.`,
    `Schließe mit Erfolgsstories und sozialem Proof ab, um langfristige Beziehungen zu vertiefen.`,
  ];
}

function createPlanRows(context) {
  return monthLabels.map((month, index) => {
    const row = rowTemplate.content.firstElementChild.cloneNode(true);
    const ideas = ideaLibrary[index];
    const narrative = buildNarrative(context)[index];

    row.querySelector(".month").textContent = month;
    row.querySelector(".theme").textContent = personaliseText(baseThemes[index], context);
    row.querySelector(".ideas").innerHTML = `
      <strong>Storyline:</strong> ${narrative}<br /><br />
      <ul>
        ${ideas.map((idea) => `<li>${personaliseText(idea, context)}</li>`).join("")}
      </ul>
    `;
    row.querySelector(".channels").textContent = channelMix[index];
    row.querySelector(".kpis").textContent = kpiLibrary[index];

    row.addEventListener("click", () => {
      row.classList.toggle("flagged");
    });

    return row;
  });
}

function renderPlan(context) {
  const planFragment = planTemplate.content.cloneNode(true);
  const tbody = planFragment.querySelector("tbody");
  const rows = createPlanRows(context);

  rows.forEach((row) => tbody.appendChild(row));

  planContainer.innerHTML = "";
  planContainer.appendChild(planFragment);

  const legend = document.createElement("p");
  legend.className = "flag-legend";
  legend.innerHTML = "<span></span> Markiert für Feedback";
  planContainer.appendChild(legend);
}

form.addEventListener("submit", (event) => {
  event.preventDefault();
  const formData = new FormData(form);

  const toneKey = formData.get("tone");
  const context = {
    audience: formData.get("audience"),
    positioning: formData.get("positioning"),
    primaryGoal: formData.get("primaryGoal"),
    secondaryGoal: formData.get("secondaryGoal") || "",
    tone: toneKey,
    toneLabel: toneTranslations[toneKey],
  };

  renderPlan(context);
});

// Initial rendering with defaults
renderPlan({
  audience: form.elements["audience"].value,
  positioning: form.elements["positioning"].value,
  primaryGoal: form.elements["primaryGoal"].value,
  secondaryGoal: form.elements["secondaryGoal"].value,
  tone: form.elements["tone"].value,
  toneLabel: toneTranslations[form.elements["tone"].value],
});
