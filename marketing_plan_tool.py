"""Interactive content marketing plan generator for banks.

This module exposes a small command line interface that helps marketers
craft a six month social media marketing plan tailored for banks.  It
behaves a little bit like a low-fi version of lovable by listing fields
that can be "clicked" (selected via numbers) and refined in place.  The
interface is intentionally lightweight so it can be driven entirely
through chat input in environments without a graphical browser.
"""

from __future__ import annotations

import dataclasses
import textwrap
from typing import Dict, List


MONTH_NAMES = [
    "Monat 1",
    "Monat 2",
    "Monat 3",
    "Monat 4",
    "Monat 5",
    "Monat 6",
]


@dataclasses.dataclass
class Settings:
    """Holds global plan configuration provided by the user."""

    bank_name: str
    target_persona: str
    brand_versprechen: str
    tone_of_voice: str
    hauptkanale: str
    call_to_action: str
    plan_version: str


@dataclasses.dataclass
class MonthPlan:
    """Stores the content marketing plan for a single month."""

    themenfokus: str
    ziel: str
    helden_content: str
    wochenstruktur: str
    messgroesse: str
    community_impuls: str


def request_input(prompt: str, default: str) -> str:
    """Read user input while supporting defaults."""

    raw = input(f"{prompt} [{default}]\n> ").strip()
    return raw or default


def request_plan_version(default: str = "1") -> str:
    """Ask the user which blueprint version should be used."""

    prompt = (
        "Welche Plan-Version möchtest du verwenden?\n"
        "1. Version 1 – Strategischer 6-Monats-Fokus\n"
        "2. Version 2 – Kampagnen- und Event-orientiert\n"
        f"Auswahl [{default}]"
    )
    while True:
        choice = input(f"{prompt}\n> ").strip() or default
        if choice in {"1", "2"}:
            return choice
        print("Bitte 1 oder 2 eingeben.\n")


def collect_settings() -> Settings:
    """Ask the user for the basic plan configuration."""

    print("Willkommen beim Bank Marketing Planer!\n")
    bank_name = request_input("Wie heißt die Bank oder Marke?", "FutureBank")
    target_persona = request_input(
        "Beschreibe die Zielperson (z.B. junge Berufstätige, Familien, Unternehmer)",
        "Digital affine Berufseinsteiger*innen",
    )
    brand_versprechen = request_input(
        "Was ist das zentrale Leistungsversprechen?",
        "Finanzielle Sicherheit und smarte Vermögensplanung",
    )
    tone_of_voice = request_input(
        "Welcher Tonfall soll verwendet werden?",
        "vertrauensvoll, beratend, empathisch",
    )
    hauptkanale = request_input(
        "Welche Social-Media-Kanäle stehen im Fokus?",
        "LinkedIn, Instagram, YouTube Shorts",
    )
    call_to_action = request_input(
        "Was ist der wichtigste Call-to-Action?",
        "Termin zur Finanzberatung buchen",
    )
    plan_version = request_plan_version()

    return Settings(
        bank_name=bank_name,
        target_persona=target_persona,
        brand_versprechen=brand_versprechen,
        tone_of_voice=tone_of_voice,
        hauptkanale=hauptkanale,
        call_to_action=call_to_action,
        plan_version=plan_version,
    )


def blueprint_version_one(settings: Settings) -> List[MonthPlan]:
    """Return the original six month blueprint using sensible defaults."""

    persona = settings.target_persona
    cta = settings.call_to_action
    brand = settings.brand_versprechen

    return [
        MonthPlan(
            themenfokus="Purpose & Vertrauen aufbauen",
            ziel="Markenvertrauen steigern, Kernwerte der Bank verankern",
            helden_content=(
                "Manifest-Video über die Rolle der Bank beim Aufbau"
                f" finanzieller Sicherheit für {persona}"
            ),
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Purpose-Storytelling Post + Mitarbeiter*innen-Spotlight
                Woche 2: Karussell mit Werten & Services, Umfrage in Stories
                Woche 3: Kundenreferenz (Video) + Behind-the-Scenes
                Woche 4: Live Q&A zur Finanzplanung + CTA zu {cta}
                """
            ).strip(),
            messgroesse="Reichweite, Sentiment, Anzahl Q&A-Teilnahmen",
            community_impuls="Frage an Community: Was bedeutet finanzielle Sicherheit?",
        ),
        MonthPlan(
            themenfokus="Finanzbildung & Mehrwert",
            ziel="Finanzwissen vermitteln und Beratungsangebot positionieren",
            helden_content=(
                "Mini-Masterclass Reihe zu Finanzbasics für"
                f" {persona} mit Download-Checkliste"
            ),
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Tutorial-Post (Karussell) + Stories-Quiz
                Woche 2: Erklärvideo + Community-Fragerunde im Kommentarbereich
                Woche 3: Blog-Teaser mit CTA zu {cta}
                Woche 4: Live-Webinar mit Berater*in, Follow-Up E-Mail
                """
            ).strip(),
            messgroesse="Anmeldungen Webinar, Checklisten-Downloads, Watchtime",
            community_impuls="Quizfrage der Woche rund ums Sparen",
        ),
        MonthPlan(
            themenfokus="Produkte & Use-Cases",
            ziel="Relevante Finanzprodukte kontextualisieren",
            helden_content=(
                f"Case Study Serie: Wie {brand}"
                " Kund*innen durch Lebensmomente begleitet"
            ),
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Kund*innen Story (Text + Visual)
                Woche 2: Produkt-Demo Video + FAQ Karussell
                Woche 3: Vergleiche/Infografiken + CTA zu Beratungsgespräch
                Woche 4: Testimonial Reel + Retargeting-Ad Hinweis
                """
            ).strip(),
            messgroesse="Klicks auf Produktseiten, Beratungsanfragen, CTR",
            community_impuls="Frag die Bank: Kommentiere deine aktuelle Finanzfrage",
        ),
        MonthPlan(
            themenfokus="Community & Nachhaltigkeit",
            ziel="Engagement fördern und nachhaltige Initiativen zeigen",
            helden_content="Behind-the-scenes Serie zu nachhaltigen Projekten der Bank",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Nachhaltigkeitsbericht als Snackable Content
                Woche 2: Mitarbeitende erzählen über Impact-Projekte
                Woche 3: Community-Voting für Sponsoring-Projekt
                Woche 4: Livestream von CSR-Event + CTA zu {cta}
                """
            ).strip(),
            messgroesse="Engagement Rate, Teilnahme am Voting, CSR-News Abos",
            community_impuls="Challenge: Teile deine nachhaltige Finanzidee",
        ),
        MonthPlan(
            themenfokus="Innovation & Zukunft",
            ziel="Digital-Kompetenz und Innovation der Bank unterstreichen",
            helden_content="Tech-Demo zur Banking-App mit Use-Cases",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Produktneuheit (Video) + Beta-Anmeldung CTA
                Woche 2: Experteninterview zu FinTech Trends
                Woche 3: Kundenfeedback-Post + Feature-Sneak Peek
                Woche 4: Recap-Thread + Reminder {cta}
                """
            ).strip(),
            messgroesse="App-Downloads, Beta-Anmeldungen, Shares",
            community_impuls="Frage: Welches Feature wünschst du dir?",
        ),
        MonthPlan(
            themenfokus="Vertriebs-Offensive & Abschluss",
            ziel="Beratungsabschlüsse und Leads maximieren",
            helden_content="Success-Story Kampagne + limitierte Beratungsslots",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Recap der Reise + Social Proof Sammelpost
                Woche 2: Angebot der Woche + FAQs im Live-Chat
                Woche 3: Reminder Posts + Lead Magnet Re-Launch
                Woche 4: Abschluss-Event (Live) + Danke-Post
                """
            ).strip(),
            messgroesse="Leads, gebuchte Beratungstermine, Abschlussrate",
            community_impuls="Countdown zur Beratung: Was brauchst du als nächstes?",
        ),
    ]


def blueprint_version_two(settings: Settings) -> List[MonthPlan]:
    """Provide an alternative blueprint with campaign-focused themes."""

    persona = settings.target_persona
    cta = settings.call_to_action

    return [
        MonthPlan(
            themenfokus="Kick-off Kampagne",
            ziel="Neue Zielgruppen aktivieren und Markenbekanntheit steigern",
            helden_content="Launch-Video mit Storytelling rund um Kund*innen-Erfolge",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Launch-Video + Behind-the-Scenes Stories
                Woche 2: Gewinnspiel mit Lead-Formular und CTA zu {cta}
                Woche 3: Interview mit Bankexpert*in zu Trends
                Woche 4: Recap Post + Retargeting Reminder
                """
            ).strip(),
            messgroesse="Leads, Video-Views, Gewinnspielteilnahmen",
            community_impuls="Welche Finanzziele möchtest du dieses Jahr erreichen?",
        ),
        MonthPlan(
            themenfokus="Community Engagement",
            ziel="Community aufbauen und Dialoge fördern",
            helden_content=f"Live Q&A Serie für {persona} mit Moderator*in",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Teaser-Reel + Fragen sammeln
                Woche 2: Live Q&A + Stories mit Highlight-Antworten
                Woche 3: Community-Spotlights + User Generated Content
                Woche 4: Tipps-Karussell + CTA zu {cta}
                """
            ).strip(),
            messgroesse="Kommentare, Live-Teilnahmen, Shares",
            community_impuls="Stelle deine dringlichste Finanzfrage!",
        ),
        MonthPlan(
            themenfokus="Produkt Stories",
            ziel="Beratungsangebote konvertieren",
            helden_content="Fallstudien-Reihe mit klaren Outcomes",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Kundenstory (Video) + CTA zu Beratung
                Woche 2: Vergleichsgrafik + Expertenzitat
                Woche 3: Testimonials + FAQ-Thread
                Woche 4: Lead Magnet Download + Follow-Up E-Mail
                """
            ).strip(),
            messgroesse="Downloads, Beratungsanfragen, CTR",
            community_impuls="Teile dein Feedback zu unseren Services",
        ),
        MonthPlan(
            themenfokus="Events & Vor-Ort",
            ziel="Physische Events mit digitalem Storytelling verzahnen",
            helden_content="Hybrid-Event mit Live-Streaming",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Event-Ankündigung + Early Bird Anmeldung
                Woche 2: Speaker-Vorstellung + Themenumfrage
                Woche 3: Live-Berichterstattung + Insta-Takeover
                Woche 4: Event-Recap + CTA zu {cta}
                """
            ).strip(),
            messgroesse="Anmeldungen, Livestream-Views, Event-Feedback",
            community_impuls="Welche Speaker-Themen interessieren dich?",
        ),
        MonthPlan(
            themenfokus="Partnerschaften",
            ziel="Kooperationen nutzen, um Reichweite zu erhöhen",
            helden_content="Kooperation mit lokalen Unternehmen",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Partner-Announcement + Cross-Posting
                Woche 2: Gemeinsame Challenge + Gewinnspiel CTA
                Woche 3: Expertenbeitrag des Partners
                Woche 4: Erfolgsgeschichte + Reminder {cta}
                """
            ).strip(),
            messgroesse="Partnerreichweite, Challenge-Teilnahmen, Leads",
            community_impuls="Welche Kooperation wünschst du dir?",
        ),
        MonthPlan(
            themenfokus="Jahresabschluss",
            ziel="Lernings sichern und nächste Schritte vorbereiten",
            helden_content="Best-of Recap Video + Ausblick auf kommende Kampagnen",
            wochenstruktur=textwrap.dedent(
                f"""
                Woche 1: Highlights Compilation + Dankesbotschaft
                Woche 2: Insights Karussell + Feedback Umfrage
                Woche 3: Vorausschau auf neue Formate
                Woche 4: Abschluss-Live + CTA zu {cta}
                """
            ).strip(),
            messgroesse="Feedback-Einsendungen, Abschluss-Leads, Viewtime",
            community_impuls="Welche Themen sollen wir 2025 vertiefen?",
        ),
    ]


def base_plan_blueprint(settings: Settings) -> List[MonthPlan]:
    """Return a six month blueprint for the selected plan version."""

    if settings.plan_version == "1":
        return blueprint_version_one(settings)
    return blueprint_version_two(settings)


def render_month(number: int, month: MonthPlan) -> str:
    """Pretty print a single month plan."""

    lines = [
        f"[{number}] {MONTH_NAMES[number - 1]} – {month.themenfokus}",
        f"    Ziel: {month.ziel}",
        f"    Helden-Content: {month.helden_content}",
        "    Wochenstruktur:",
    ]
    for line in month.wochenstruktur.splitlines():
        lines.append(f"        {line}")
    lines.append(f"    Messgrößen: {month.messgroesse}")
    lines.append(f"    Community-Impuls: {month.community_impuls}")
    return "\n".join(lines)


def display_plan(settings: Settings, plan: List[MonthPlan]) -> None:
    """Print the full plan in a structured format."""

    header = textwrap.dedent(
        f"""
        ============================================
        6-Monats Content Marketing Plan – {settings.bank_name}
        ============================================
        Zielperson: {settings.target_persona}
        Markenversprechen: {settings.brand_versprechen}
        Tonalität: {settings.tone_of_voice}
        Hauptkanäle: {settings.hauptkanale}
        Primärer CTA: {settings.call_to_action}
        Plan-Version: {settings.plan_version}
        """
    ).strip()
    print(header)
    print()
    for index, month in enumerate(plan, start=1):
        print(render_month(index, month))
        print()


def edit_month(plan: List[MonthPlan], index: int) -> None:
    """Allow editing of a single month entry."""

    month = plan[index]
    fields = {
        "1": ("Themenfokus", "themenfokus"),
        "2": ("Ziel", "ziel"),
        "3": ("Helden-Content", "helden_content"),
        "4": ("Wochenstruktur", "wochenstruktur"),
        "5": ("Messgrößen", "messgroesse"),
        "6": ("Community-Impuls", "community_impuls"),
    }

    while True:
        print("Welches Feld möchtest du bearbeiten?")
        for key, (label, _) in fields.items():
            print(f"{key}. {label}")
        print("7. Zurück")
        choice = input("> ").strip()
        if choice == "7":
            break
        if choice not in fields:
            print("Bitte eine gültige Option wählen.\n")
            continue
        label, attr = fields[choice]
        current = getattr(month, attr)
        print(f"Aktueller Wert ({label}):\n{current}\n")
        new_value = input("Neuen Wert eingeben (leer lassen für keine Änderung):\n> ").strip()
        if new_value:
            setattr(month, attr, new_value)
            print(f"{label} aktualisiert!\n")


def interactive_loop(settings: Settings, plan: List[MonthPlan]) -> None:
    """Main command loop for interacting with the plan."""

    while True:
        display_plan(settings, plan)
        print("Aktionen:")
        print("1. Monat bearbeiten")
        print("2. Einstellungen anpassen & Plan neu erstellen")
        print("3. Plan als Markdown speichern")
        print("4. Beenden")
        choice = input("> ").strip()

        if choice == "1":
            month_choice = input("Welchen Monat möchtest du bearbeiten? (1-6)\n> ").strip()
            if month_choice not in {"1", "2", "3", "4", "5", "6"}:
                print("Ungültige Auswahl.\n")
                continue
            index = int(month_choice) - 1
            edit_month(plan, index)
        elif choice == "2":
            new_settings = collect_settings()
            plan[:] = base_plan_blueprint(new_settings)
            settings.bank_name = new_settings.bank_name
            settings.target_persona = new_settings.target_persona
            settings.brand_versprechen = new_settings.brand_versprechen
            settings.tone_of_voice = new_settings.tone_of_voice
            settings.hauptkanale = new_settings.hauptkanale
            settings.call_to_action = new_settings.call_to_action
            settings.plan_version = new_settings.plan_version
        elif choice == "3":
            export_plan(settings, plan)
        elif choice == "4":
            print("Viel Erfolg mit deinem Marketingplan!")
            break
        else:
            print("Bitte eine gültige Option wählen.\n")


def export_plan(settings: Settings, plan: List[MonthPlan]) -> None:
    """Export the current plan to a markdown file."""

    filename = input(
        "Dateiname für Export (z.B. marketing-plan.md) [marketing-plan.md]\n> "
    ).strip() or "marketing-plan.md"
    lines: List[str] = [
        f"# 6-Monats Content Marketing Plan – {settings.bank_name}",
        "",
        f"- **Zielperson:** {settings.target_persona}",
        f"- **Markenversprechen:** {settings.brand_versprechen}",
        f"- **Tonalität:** {settings.tone_of_voice}",
        f"- **Hauptkanäle:** {settings.hauptkanale}",
        f"- **Primärer CTA:** {settings.call_to_action}",
        f"- **Plan-Version:** {settings.plan_version}",
        "",
    ]
    for idx, month in enumerate(plan, start=1):
        lines.extend(
            [
                f"## {MONTH_NAMES[idx - 1]} – {month.themenfokus}",
                "",
                f"- **Ziel:** {month.ziel}",
                f"- **Helden-Content:** {month.helden_content}",
                "- **Wochenstruktur:**",
            ]
        )
        for line in month.wochenstruktur.splitlines():
            lines.append(f"  - {line}")
        lines.extend(
            [
                f"- **Messgrößen:** {month.messgroesse}",
                f"- **Community-Impuls:** {month.community_impuls}",
                "",
            ]
        )

    with open(filename, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
    print(f"Plan als '{filename}' gespeichert!\n")


def main() -> None:
    settings = collect_settings()
    plan = base_plan_blueprint(settings)
    interactive_loop(settings, plan)


if __name__ == "__main__":
    main()
