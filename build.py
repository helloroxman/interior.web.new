#!/usr/bin/env python3
"""Static site generator for the Oksana Ivanova studio site.

Reads data/projects.json and writes:
  index.html, en/index.html, projects/<slug>.html, en/projects/<slug>.html, 404.html
Run:  python3 build.py
"""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))

def _asset_version(rel):
    """Short hash of a file's contents, appended to its URL so browsers never serve a stale copy."""
    import hashlib
    with open(os.path.join(ROOT, rel), "rb") as f:
        return hashlib.md5(f.read()).hexdigest()[:8]
CSS_V = _asset_version("css/style.css")
JS_V = _asset_version("js/main.js")
PROJECTS = json.load(open(os.path.join(ROOT, "data", "projects.json"), encoding="utf-8"))

PHONE = "+380 97 141 99 77"
PHONE_HREF = "tel:+380971419977"
EMAIL = "office@oksanaivanova.com"
SOCIAL = {
    "instagram": "https://www.instagram.com/oksanaivanova.design/",
    "facebook": "https://www.facebook.com/oksanaivanova.com.ua",
    "behance": "https://www.behance.net/oksanaivanovadesign",
}
HERO_IMG = "img/projs/darkside/07.jpg"
ABOUT_IMG = "img/projs/becauselife/07.jpg"
ABOUT_PROJECT = "becauselife"
BANNER_IMG = "img/projs/shale/08.jpg"
CTA_IMG = "img/projs/hugge/06.jpg"

T = {
 "uk": {
  "lang": "uk", "other": "en", "dir_prefix": "",
  "site": "Студія дизайну інтер’єрів Oksana Ivanova",
  "site_short": "Oksana Ivanova",
  "meta_desc": "Студія дизайну інтер’єрів Oksana Ivanova: дизайн квартир, будинків, офісів та комерційних просторів. 37 реалізованих проєктів, авторський нагляд, проєкти під ключ.",
  "nav": [("#projects","Проєкти"),("#services","Послуги"),("#process","Процес"),("#about","Про студію"),("#contacts","Контакти")],
  "hero_eyebrow": "Студія дизайну інтер’єрів",
  "hero_title": "Ми створюємо <span class=\"i\">гармонію</span> та комфорт для вашого життя",
  "hero_lead": "Розробляємо ексклюзивний дизайн квартир, будинків та офісів — простори для роботи, відпочинку й обміну досвідом. Місця, де не проходить, а вирує життя.",
  "hero_btn1": "Замовити дизайн-проєкт", "hero_btn2": "Дивитись проєкти",
  "stat_projects": "проєктів", "stat_area": "м² спроєктовано", "stat_cities": "міст України",
  "scroll": "Гортайте",
  "about_eyebrow": "Про студію",
  "about_title": "Досвід, гарний смак і розуміння сучасних тенденцій — <span class=\"i\">лише вершина айсберга</span>",
  "about_p1": "Ми розуміємо індивідуальність та цілі кожного замовника і втілюємо їх у життя. Наша місія — поєднати практичність, зручність, комфорт і функціональність з естетикою.",
  "about_p2": "Студія має великий досвід у проєктуванні внутрішнього та зовнішнього простору, постійно розвивається і використовує інноваційні технології та якісні сучасні матеріали.",
  "about_caption": "З проєкту", "about_caption_more": "Дивитись проєкт",
  "values": [("Індивідуально","Кожен проєкт починається з вашого способу життя, а не з каталогу."),
             ("Функціонально","Планування, освітлення та зберігання, які працюють щодня."),
             ("Точно","Повний пакет креслень, щоб будівельники не імпровізували."),
             ("До результату","Авторський нагляд від першого заміру до фінального декору.")],
  "projects_eyebrow": "Портфоліо",
  "projects_title": "Дизайн-проєкти",
  "projects_lead": "Квартири, приватні будинки, офіси та комерційні простори — оберіть категорію або перегляньте всі роботи студії.",
  "filters": [("all","Усі"),("apartment","Квартири"),("house","Будинки"),("office","Офіси"),("commercial","Комерційні")],
  "types": {"apartment":"Квартира","house":"Будинок","office":"Офіс","commercial":"Комерційний простір"},
  "grid_empty": "У цій категорії поки що немає проєктів.",
  "services_eyebrow": "Послуги",
  "services_title": "Від ідеї до <span class=\"i\">ключів</span>",
  "services": [
    ("Візуалізація","Візуальний дизайн-проєкт покаже вигляд вашого приміщення на фініші та допоможе вчасно змінити предмети інтер’єру, освітлення, меблі та оздоблення."),
    ("Авторський нагляд","Авторський нагляд фахового дизайнера допоможе реалізувати проєкт вчасно та у точності з візуалізацією."),
    ("Проєктування простору","Без чіткого і професійного креслення опалення, водопостачання, електрообладнання та розгорток стін неможливо рухатись далі."),
    ("Проєкт «під ключ»","Будівництво — це колосальні кошти, зусилля та час, якщо все робити самому. Краще довірити це тим, хто займається цим професійно."),
    ("Предметний дизайн","Розробляємо індивідуальні меблі та декор, а також ексклюзивні елементи інтер’єру спеціально під проєкт."),
    ("Громадський простір","Поліпшуємо громадські простори і робимо міста зручнішими для мешканців — для соціалізації та відпочинку."),
  ],
  "services_btn": "Замовити послугу",
  "process_eyebrow": "Процес",
  "process_title": "Як народжується <span class=\"i\">дизайн</span>",
  "process_lead": "Ідея отримує життя в процесі реалізації. Щоб було зрозуміло, з чого складається робота, ось алгоритм — етап створення дизайну та авторський нагляд за реалізацією.",
  "stage1": "Дизайн-проєкт", "stage2": "Авторський нагляд", "stage_label": "Етап",
  "steps1": [("Заміри на об’єкті",9.8),("Планування об’єкта",13.7),("Підписання договору",11.8),("Пропрацювання концепції",35.3),("Робочі креслення",20.6),("Друк проєкту",8.8)],
  "steps2": [("Складання кошторису",23.5),("Контроль ремонту",41.2),("Вибір матеріалів",35.3)],
  "share_label": "частка часу",
  "blueprint_short": "План монтажу та демонтажу стін із дизайн-проєкту «Soft & Smart»",
  "sample_eyebrow": "Приклад проєкту",
  "sample_title": "Подивіться, як виглядає готовий дизайн-проєкт",
  "sample_text": "Щоб побачити результат, перегляньте приклад готового альбому: квартира «Soft & Smart» у ЖК Spectrum, від плану демонтажу до візуалізацій (PDF, 16 МБ).",
  "deliver_eyebrow": "Що ви отримаєте",
  "deliver_title": "Робочий проєкт, який <span class=\"i\">економить</span> гроші та час",
  "deliver_lead": "Уся інформація для виконання робіт будівельною бригадою гарантує якість і дозволяє уникнути переробок. Робочий проєкт включає:",
  "deliver": ["3D-візуалізація інтер’єру","Креслення меблів","Будівельні креслення","Підбір матеріалів"],
  "deliver_btn": "Замовити дизайн-проєкт",
  "pdf_title": "Переглянути дизайн-проєкт", "pdf_sub": "з пакетом будівельних креслень · PDF, 16 МБ",
  "banner_quote": "Наша місія — поєднати практичність і комфорт з <span class=\"i\">естетикою</span>.",
  "banner_text": "Ми проєктуємо простори, які виглядають гарно на рендері й так само добре працюють через десять років.",
  "contacts_eyebrow": "Контакти",
  "contacts_title": "Поговорімо про ваш <span class=\"i\">простір</span>",
  "contacts_lead": "Зв’яжіться з нами, щоб детальніше ознайомитись із послугами, отримати відповіді на запитання чи замовити дизайн-проєкт.",
  "hours_label": "Графік роботи", "hours": "Пн – Пт: 10:00 – 18:00<br>Сб: 10:00 – 15:00",
  "phone_label": "Телефон", "email_label": "Email", "social_label": "Соцмережі",
  "write_btn": "Написати нам",
  "footer_rights": "Усі права захищено.",
  "footer_tag": "Дизайн інтер’єрів · Україна",
  "crumb_home": "Головна", "crumb_projects": "Проєкти",
  "fact_area": "Площа", "fact_location": "Локація", "fact_type": "Тип", "fact_photos": "Візуалізацій",
  "project_eyebrow": "Про проєкт",
  "gallery_eyebrow": "Галерея",
  "gallery_title": "Візуалізації",
  "gallery_hint": "Натисніть на фото, щоб відкрити у повному розмірі",
  "prev": "Попередній проєкт", "next": "Наступний проєкт",
  "cta_title": "Хочете такий самий продуманий простір?",
  "cta_btn1": "Замовити дизайн-проєкт", "cta_btn2": "Усі проєкти",
  "img_alt": "Дизайн інтер’єру {title} — візуалізація {n}",
  "cover_alt": "Дизайн інтер’єру {title}",
  "project_meta": "Дизайн інтер’єру {title}: {type}, {area} м²{loc}. Проєкт студії Oksana Ivanova.",
  "nf_title": "Сторінку не знайдено", "nf_text": "Схоже, такої сторінки не існує або її було переміщено.", "nf_btn": "На головну",
  "lb_close": "Закрити", "lb_prev": "Попереднє фото", "lb_next": "Наступне фото",
  "lb_hint": "Гортайте колесом або стрілками",
  "menu_label": "Меню",
 },
 "en": {
  "lang": "en", "other": "uk", "dir_prefix": "en/",
  "site": "Oksana Ivanova Interior Design Studio",
  "site_short": "Oksana Ivanova",
  "meta_desc": "Oksana Ivanova interior design studio: apartments, houses, offices and commercial spaces. 37 completed projects, design supervision and turnkey delivery.",
  "nav": [("#projects","Projects"),("#services","Services"),("#process","Process"),("#about","Studio"),("#contacts","Contacts")],
  "hero_eyebrow": "Interior design studio",
  "hero_title": "We create <span class=\"i\">harmony</span> and comfort for your life",
  "hero_lead": "We design exclusive apartments, houses and offices — spaces for work, rest and sharing experience. Places where life doesn't just pass by, it happens.",
  "hero_btn1": "Order a design project", "hero_btn2": "View projects",
  "stat_projects": "projects", "stat_area": "m² designed", "stat_cities": "cities in Ukraine",
  "scroll": "Scroll",
  "about_eyebrow": "About the studio",
  "about_title": "Experience, good taste and an understanding of current trends are <span class=\"i\">only the tip of the iceberg</span>",
  "about_p1": "We understand the individuality and goals of every client and bring them to life. Our mission is to combine practicality, convenience, comfort and functionality with aesthetics.",
  "about_p2": "The studio has extensive experience in designing interior and exterior spaces, constantly evolves and uses innovative technologies and high-quality modern materials.",
  "about_caption": "From the project", "about_caption_more": "View project",
  "values": [("Personal","Every project starts with your way of life, not with a catalogue."),
             ("Functional","Layouts, lighting and storage that work every single day."),
             ("Precise","A complete drawing set so builders never have to improvise."),
             ("Delivered","Design supervision from the first measurement to the final décor.")],
  "projects_eyebrow": "Portfolio",
  "projects_title": "Design projects",
  "projects_lead": "Apartments, private houses, offices and commercial spaces — pick a category or browse all of the studio's work.",
  "filters": [("all","All"),("apartment","Apartments"),("house","Houses"),("office","Offices"),("commercial","Commercial")],
  "types": {"apartment":"Apartment","house":"House","office":"Office","commercial":"Commercial space"},
  "grid_empty": "No projects in this category yet.",
  "services_eyebrow": "Services",
  "services_title": "From idea to <span class=\"i\">keys</span>",
  "services": [
    ("Visualisation","A visual design project shows what your space will look like at the finish line and lets you change furniture, lighting, materials and décor in time."),
    ("Design supervision","Supervision by a professional designer helps deliver the project on schedule and exactly as visualised."),
    ("Space planning","Without clear, professional drawings for heating, plumbing, electrics and wall elevations it is simply impossible to move forward."),
    ("Turnkey project","Construction takes enormous money, effort and time when you do it all yourself. Better to trust those who do it professionally."),
    ("Product design","We design bespoke furniture and décor, as well as exclusive interior elements made specifically for the project."),
    ("Public spaces","We improve public spaces and make cities more comfortable for their residents — for socialising and leisure."),
  ],
  "services_btn": "Order a service",
  "process_eyebrow": "Process",
  "process_title": "How a <span class=\"i\">design</span> is born",
  "process_lead": "An idea comes to life during implementation. To make it clear what the work consists of, here is the algorithm — the design stage and the supervision of its realisation.",
  "stage1": "Design project", "stage2": "Design supervision", "stage_label": "Stage",
  "steps1": [("On-site measurements",9.8),("Space planning",13.7),("Contract signing",11.8),("Concept development",35.3),("Working drawings",20.6),("Project printing",8.8)],
  "steps2": [("Cost estimate",23.5),("Renovation control",41.2),("Material selection",35.3)],
  "share_label": "share of time",
  "blueprint_short": "Wall demolition and construction plan from the “Soft & Smart” design project",
  "sample_eyebrow": "Sample project",
  "sample_title": "See what a finished design project looks like",
  "sample_text": "To see the result, browse a sample of a finished album: the “Soft & Smart” apartment in the Spectrum complex, from the demolition plan to the visualisations (PDF, 16 MB).",
  "deliver_eyebrow": "What you get",
  "deliver_title": "A working project that <span class=\"i\">saves</span> money and time",
  "deliver_lead": "All the information the construction crew needs guarantees quality and avoids rework. The working project includes:",
  "deliver": ["3D interior visualisation","Furniture drawings","Construction drawings","Material selection"],
  "deliver_btn": "Order a design project",
  "pdf_title": "View a sample design project", "pdf_sub": "with a full set of construction drawings · PDF, 16 MB",
  "banner_quote": "Our mission is to combine practicality and comfort with <span class=\"i\">aesthetics</span>.",
  "banner_text": "We design spaces that look beautiful in the render and work just as well ten years later.",
  "contacts_eyebrow": "Contacts",
  "contacts_title": "Let's talk about your <span class=\"i\">space</span>",
  "contacts_lead": "Get in touch to learn more about our services, get answers to your questions or order a design project.",
  "hours_label": "Working hours", "hours": "Mon – Fri: 10:00 – 18:00<br>Sat: 10:00 – 15:00",
  "phone_label": "Phone", "email_label": "Email", "social_label": "Social",
  "write_btn": "Write to us",
  "footer_rights": "All rights reserved.",
  "footer_tag": "Interior design · Ukraine",
  "crumb_home": "Home", "crumb_projects": "Projects",
  "fact_area": "Area", "fact_location": "Location", "fact_type": "Type", "fact_photos": "Visualisations",
  "project_eyebrow": "About the project",
  "gallery_eyebrow": "Gallery",
  "gallery_title": "Visualisations",
  "gallery_hint": "Click a photo to open it full size",
  "prev": "Previous project", "next": "Next project",
  "cta_title": "Want a space this well thought out?",
  "cta_btn1": "Order a design project", "cta_btn2": "All projects",
  "img_alt": "{title} interior design — visualisation {n}",
  "cover_alt": "{title} interior design",
  "project_meta": "{title} interior design: {type}, {area} m²{loc}. A project by Oksana Ivanova studio.",
  "nf_title": "Page not found", "nf_text": "It looks like this page doesn't exist or has been moved.", "nf_btn": "Back home",
  "lb_close": "Close", "lb_prev": "Previous photo", "lb_next": "Next photo",
  "lb_hint": "Scroll or use arrow keys",
  "menu_label": "Menu",
 },
}

SVG_ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>'
SVG_RIGHT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
SVG_LEFT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'
SVG_CHEVRON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>'
SVG_X = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>'

def esc(s): return html.escape(s, quote=True)
def fmt_num(n): return f"{n:,}".replace(",", "\u202f")
def area_unit(lang): return "м²" if lang == "uk" else "m²"

def head(t, base, title, desc, alt_href, self_href, og_image):
    lang = t["lang"]
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{base}{og_image}">
<meta property="og:locale" content="{'uk_UA' if lang=='uk' else 'en_US'}">
<meta name="theme-color" content="#17171a">
<link rel="alternate" hreflang="{t['other']}" href="{alt_href}">
<link rel="alternate" hreflang="{lang}" href="{self_href}">
<link rel="icon" type="image/png" sizes="32x32" href="{base}img/favicon/32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{base}img/favicon/16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="{base}img/favicon/iphone_6_plus_8_and_above_180x180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{base}css/style.css?v={CSS_V}">
</head>
"""

def lang_switch(t, home, alt_href):
    lang = t["lang"]
    ua_href = alt_href if lang == "en" else home
    en_href = alt_href if lang == "uk" else home
    return f"""<div class="lang">
        <button class="lang__btn" aria-haspopup="true" aria-expanded="false" aria-label="Language">{'UA' if lang=='uk' else 'EN'}{SVG_CHEVRON}</button>
        <ul class="lang__menu">
          <li><a href="{ua_href}" class="{'is-active' if lang=='uk' else ''}" hreflang="uk" lang="uk">Українська</a></li>
          <li><a href="{en_href}" class="{'is-active' if lang=='en' else ''}" hreflang="en" lang="en">English</a></li>
        </ul>
      </div>"""

def header(t, base, home, alt_href, solid=False):
    nav = "".join(f'<li><a href="{home}{h}">{esc(l)}</a></li>' for h, l in t["nav"])
    menu = "".join(f'<li><a href="{home}{h}">{esc(l)}</a></li>' for h, l in t["nav"])
    return f"""<header class="header{' header--solid' if solid else ''}">
  <div class="container">
    <a href="{home}" class="logo" aria-label="{esc(t['site_short'])}">
      <img src="{base}img/logo.svg" alt="" class="logo__light" width="180" height="94">
      <img src="{base}img/logo-black.svg" alt="" class="logo__dark" width="180" height="94">
    </a>
    <nav class="nav" aria-label="{esc(t['menu_label'])}">
      <ul class="nav__links">{nav}</ul>
      {lang_switch(t, home, alt_href)}
      <button class="burger" aria-label="{esc(t['menu_label'])}" aria-expanded="false"><span></span><span></span><span></span></button>
    </nav>
  </div>
</header>
<div class="menu" aria-hidden="true">
  <ul class="menu__links">{menu}</ul>
  <div class="menu__foot">
    <div><a href="{PHONE_HREF}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></div>
    {lang_switch(t, home, alt_href)}
  </div>
</div>
"""

def social_list(base):
    return f"""<ul class="social">
  <li><a href="{SOCIAL['instagram']}" target="_blank" rel="noopener" aria-label="Instagram"><img src="{base}img/icons/ico-social-in.svg" alt=""></a></li>
  <li><a href="{SOCIAL['facebook']}" target="_blank" rel="noopener" aria-label="Facebook"><img src="{base}img/icons/ico-social-fb.svg" alt=""></a></li>
  <li><a href="{SOCIAL['behance']}" target="_blank" rel="noopener" aria-label="Behance"><img src="{base}img/icons/ico-social-be.svg" alt=""></a></li>
</ul>"""

def footer(t, base, home):
    nav = "".join(f'<li><a href="{home}{h}">{esc(l)}</a></li>' for h, l in t["nav"])
    return f"""<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <a href="{home}" class="logo" aria-label="{esc(t['site_short'])}"><img src="{base}img/logo.svg" alt="" width="180" height="94"></a>
      <ul class="footer__nav">{nav}</ul>
      {social_list(base)}
    </div>
    <div class="footer__bottom">
      <span>© <span data-year>2026</span> {esc(t['site_short'])}. {esc(t['footer_rights'])}</span>
      <span>{esc(t['footer_tag'])}</span>
    </div>
  </div>
</footer>
<script src="{base}js/main.js?v={JS_V}" defer></script>
</body>
</html>
"""

def card(p, t, base, projects_dir, wide):
    lang = t["lang"]
    loc = p["location"][lang]
    meta = f'{p["area"]} {area_unit(lang)}' + (f' · {esc(loc)}' if loc else '')
    return f"""<a href="{projects_dir}{p['slug']}.html" class="card{' card--wide' if wide else ''} reveal" data-type="{p['type']}">
  <div class="card__media">
    <span class="card__tag">{esc(t['types'][p['type']])}</span>
    <img src="{base}img/projs/{p['slug']}/cover.jpg" alt="{esc(t['cover_alt'].format(title=p['title']))}" loading="lazy" width="1230" height="780">
    <span class="card__arrow">{SVG_ARROW}</span>
  </div>
  <div class="card__body"><h3 class="card__title">{esc(p['title'])}</h3><span class="card__meta">{meta}</span></div>
</a>"""

STEP_COLORS = ["#9a6b4f", "#c79a7c", "#6c5d50", "#b8a494", "#4c443c", "#d8c7b5"]

def donut_svg(steps, label):
    """Ring chart: one segment per step, sized by its share of the stage."""
    import math
    r, C = 48, 2 * math.pi * 48
    total = sum(v for _, v in steps)
    parts, offset = [], 0.0
    for i, (_, v) in enumerate(steps):
        seg = C * v / total
        parts.append(f'<circle r="{r}" cx="60" cy="60" fill="none" stroke="{STEP_COLORS[i % len(STEP_COLORS)]}" stroke-width="14" stroke-dasharray="{seg - 2:.2f} {C - seg + 2:.2f}" stroke-dashoffset="{-offset:.2f}" />')
        offset += seg
    return (f'<svg class="donut" viewBox="0 0 120 120" role="img" aria-label="{esc(label)}">'
            f'<g transform="rotate(-90 60 60)">{"".join(parts)}</g>'
            f'<text x="60" y="60" text-anchor="middle" dominant-baseline="central" class="donut__label">{esc(label)}</text></svg>')

def steps_html(steps):
    mx = max(v for _, v in steps)
    lis = "".join(
        f'<li><span class="steps__name">{esc(n)}<i class="steps__bar" style="width:{v / mx * 100:.1f}%;background:{STEP_COLORS[i % len(STEP_COLORS)]}"></i></span><span class="steps__pct">{v:g}%</span></li>'
        for i, (n, v) in enumerate(steps))
    return f'<ol class="steps">{lis}</ol>'

def home_page(lang):
    t = T[lang]
    base = "" if lang == "uk" else "../"
    home = "index.html"
    projects_dir = "projects/"
    alt_href = "en/index.html" if lang == "uk" else "../index.html"
    self_href = "index.html"
    pdf = f"{base}files/sample_project.pdf"
    total_area = sum(p["area"] for p in PROJECTS)
    cities = {"Львів","Рівне","Самбір","Обарів","Одеса","Сарни"}
    n_cities = len(cities)
    about_p = next(p for p in PROJECTS if p["slug"] == ABOUT_PROJECT)
    counts = {k: sum(1 for p in PROJECTS if p["type"] == k) for k in t["types"]}
    counts["all"] = len(PROJECTS)

    filters = "".join(f'<button class="filter{" is-active" if k=="all" else ""}" data-filter="{k}" aria-pressed="{"true" if k=="all" else "false"}">{esc(l)} <small>{counts[k]}</small></button>' for k, l in t["filters"])
    cards = "\n".join(card(p, t, base, projects_dir, i % 5 == 0) for i, p in enumerate(PROJECTS))
    services = "".join(f"""<article class="service reveal">
      <span class="service__num">0{i+1}</span>
      <img class="service__icon" src="{base}img/icons/ico-case-1-{i+1}.svg" alt="" width="44" height="44">
      <h3>{esc(n)}</h3><p>{esc(d)}</p>
    </article>""" for i, (n, d) in enumerate(t["services"]))
    values = "".join(f'<li><b>{esc(a)}</b><span>{esc(b)}</span></li>' for a, b in t["values"])
    deliver = "".join(f'<li><img src="{base}img/icons/ico-case-2-{i+1}.svg" alt="" width="36" height="36"><b>{esc(d)}</b></li>' for i, d in enumerate(t["deliver"]))

    body = f"""<body>
{header(t, base, home, alt_href)}
<main>
<section class="hero" id="top">
  <div class="hero__bg"><img src="{base}{HERO_IMG}" alt="" fetchpriority="high"></div>
  <div class="container">
    <p class="eyebrow">{esc(t['hero_eyebrow'])}</p>
    <h1 class="display h1 hero__title">{t['hero_title']}</h1>
    <p class="hero__lead">{esc(t['hero_lead'])}</p>
    <div class="btn-row">
      <a href="#contacts" class="btn btn--light">{esc(t['hero_btn1'])}</a>
      <a href="#projects" class="btn btn--outline-light">{esc(t['hero_btn2'])}</a>
    </div>
    <div class="hero__foot">
      <div class="stats">
        <div class="stat"><div class="stat__num" data-count="{len(PROJECTS)}">{len(PROJECTS)}</div><div class="stat__label">{esc(t['stat_projects'])}</div></div>
        <div class="stat"><div class="stat__num" data-count="{total_area}" data-suffix="+">{fmt_num(total_area)}+</div><div class="stat__label">{esc(t['stat_area'])}</div></div>
        <div class="stat"><div class="stat__num" data-count="{n_cities}">{n_cities}</div><div class="stat__label">{esc(t['stat_cities'])}</div></div>
      </div>
      <a href="#about" class="scroll-hint"><i></i>{esc(t['scroll'])}</a>
    </div>
  </div>
</section>

<section class="section" id="about">
  <div class="container about">
    <div class="about__text reveal">
      <p class="eyebrow">{esc(t['about_eyebrow'])}</p>
      <h2 class="display h2">{t['about_title']}</h2>
      <p class="lead">{esc(t['about_p1'])}</p>
      <p class="muted">{esc(t['about_p2'])}</p>
      <ul class="about__values">{values}</ul>
    </div>
    <figure class="about__media reveal">
      <a href="{projects_dir}{ABOUT_PROJECT}.html" class="about__media-link">
        <img src="{base}{ABOUT_IMG}" alt="{esc(t['cover_alt'].format(title=about_p['title']))}" loading="lazy">
        <figcaption>
          <span class="about__cap-label">{esc(t['about_caption'])}</span>
          <span class="about__cap-title">{esc(about_p['title'])}</span>
          <span class="about__cap-meta">{esc(t['types'][about_p['type']])} · {about_p['area']} {area_unit(lang)} · {esc(about_p['location'][lang])}</span>
          <span class="about__cap-more">{esc(t['about_caption_more'])} {SVG_ARROW}</span>
        </figcaption>
      </a>
    </figure>
  </div>
</section>

<section class="section section--alt" id="projects">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <p class="eyebrow">{esc(t['projects_eyebrow'])}</p>
        <h2 class="display h2">{esc(t['projects_title'])}</h2>
        <p class="lead">{esc(t['projects_lead'])}</p>
      </div>
      <div class="filters" role="group" aria-label="{esc(t['projects_title'])}">{filters}</div>
    </div>
    <div class="grid">
{cards}
    </div>
    <p class="grid-empty">{esc(t['grid_empty'])}</p>
  </div>
</section>

<section class="section section--dark" id="services">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <p class="eyebrow">{esc(t['services_eyebrow'])}</p>
        <h2 class="display h2">{t['services_title']}</h2>
      </div>
      <a href="#contacts" class="btn btn--light">{esc(t['services_btn'])}</a>
    </div>
    <div class="services">{services}</div>
  </div>
</section>

<section class="section section--tight" id="process">
  <div class="container">
    <div class="process-head">
      <div class="reveal">
        <p class="eyebrow">{esc(t['process_eyebrow'])}</p>
        <h2 class="display h2">{t['process_title']}</h2>
        <p class="lead">{esc(t['process_lead'])}</p>
        <p class="muted mt-1">{esc(t['sample_text'])}</p>
        <div class="btn-row mt-2">
          <a href="{pdf}" class="btn" target="_blank" rel="noopener">{esc(t['pdf_title'])}</a>
          <a href="#contacts" class="btn btn--ghost">{esc(t['deliver_btn'])}</a>
        </div>
      </div>
      <figure class="blueprint reveal">
        <img src="{base}img/blueprint@2x.png" alt="" loading="lazy" width="2331" height="1128">
        <figcaption>{esc(t['blueprint_short'])}</figcaption>
      </figure>
    </div>
    <div class="process">
      <div class="stage reveal">
        <div class="stage__head">
          {donut_svg(t['steps1'], '01')}
          <h3 class="stage__title">{esc(t['stage_label'])} 01<br><b>{esc(t['stage1'])}</b></h3>
        </div>
        {steps_html(t['steps1'])}
      </div>
      <div class="stage reveal">
        <div class="stage__head">
          {donut_svg(t['steps2'], '02')}
          <h3 class="stage__title">{esc(t['stage_label'])} 02<br><b>{esc(t['stage2'])}</b></h3>
        </div>
        {steps_html(t['steps2'])}
      </div>
    </div>
  </div>
</section>

<section class="section section--alt" id="deliverables">
  <div class="container deliver">
    <div class="reveal">
      <p class="eyebrow">{esc(t['deliver_eyebrow'])}</p>
      <h2 class="display h2">{t['deliver_title']}</h2>
      <p class="lead mt-1">{esc(t['deliver_lead'])}</p>
      <ul class="deliver__list">{deliver}</ul>
      <div class="deliver__actions">
        <a href="#contacts" class="btn">{esc(t['deliver_btn'])}</a>
      </div>
    </div>
    <div class="deliver__media reveal"><img src="{base}img/stack@2x.png" alt="" loading="lazy" width="1637" height="1394"></div>
  </div>
</section>

<section class="banner">
  <img src="{base}{BANNER_IMG}" alt="" loading="lazy">
  <div class="container">
    <blockquote class="reveal">
      <p>{t['banner_quote']}</p>
      <footer>{esc(t['banner_text'])}</footer>
    </blockquote>
  </div>
</section>

<section class="section" id="contacts">
  <div class="container contacts">
    <div class="reveal">
      <p class="eyebrow">{esc(t['contacts_eyebrow'])}</p>
      <h2 class="display h2">{t['contacts_title']}</h2>
      <p class="lead mt-1">{esc(t['contacts_lead'])}</p>
      <div class="btn-row mt-2">
        <a href="mailto:{EMAIL}" class="btn">{esc(t['write_btn'])}</a>
        <a href="{PHONE_HREF}" class="btn btn--ghost">{PHONE}</a>
      </div>
    </div>
    <div class="reveal">
      <div class="contact__group"><span class="contact__label">{esc(t['phone_label'])}</span><a href="{PHONE_HREF}" class="contact__big">{PHONE}</a></div>
      <div class="contact__group"><span class="contact__label">{esc(t['email_label'])}</span><a href="mailto:{EMAIL}" class="contact__big">{EMAIL}</a></div>
      <div class="contact__group"><span class="contact__label">{esc(t['hours_label'])}</span><p class="mt-1">{t['hours']}</p></div>
      <div class="contact__group"><span class="contact__label">{esc(t['social_label'])}</span><div class="mt-1">{social_list(base)}</div></div>
    </div>
  </div>
</section>
</main>
{footer(t, base, home)}"""
    return head(t, base, t["site"], t["meta_desc"], alt_href, self_href, HERO_IMG) + body

def gallery_class(img):
    r = img["w"] / img["h"]
    if r > 1.7: return "gallery__item gallery__item--wide"
    return "gallery__item"

def project_page(lang, p, prev_p, next_p):
    t = T[lang]
    base = "../" if lang == "uk" else "../../"
    home = base + "index.html"
    projects_dir = ""
    alt_href = f"../en/projects/{p['slug']}.html" if lang == "uk" else f"../../projects/{p['slug']}.html"
    self_href = f"{p['slug']}.html"
    loc = p["location"][lang]
    typ = t["types"][p["type"]]
    unit = area_unit(lang)
    title = f"{p['title']} — {typ}, {p['area']} {unit} · {t['site_short']}"
    desc = t["project_meta"].format(title=p["title"], type=typ.lower(), area=p["area"], loc=(f", {loc}" if loc else ""))
    imgdir = f"{base}img/projs/{p['slug']}/"

    gal = []
    for i, im in enumerate(p["images"], start=1):
        small = im["file"].replace(".jpg", "-s.jpg")
        alt = t["img_alt"].format(title=p["title"], n=i)
        gal.append(f'<a href="{imgdir}{im["file"]}" class="{gallery_class(im)} reveal" data-full="{imgdir}{im["file"]}"><img src="{imgdir}{small}" alt="{esc(alt)}" loading="lazy" width="{im["w"]}" height="{im["h"]}"><span class="gallery__num">{i:02d}</span></a>')
    gallery = "\n".join(gal)

    chips = f'<span class="chip">{p["area"]} {unit}</span><span class="chip">{esc(typ)}</span>' + (f'<span class="chip">{esc(loc)}</span>' if loc else "")
    facts = f"""<ul class="facts">
      <li><span>{esc(t['fact_type'])}</span><b>{esc(typ)}</b></li>
      <li><span>{esc(t['fact_area'])}</span><b>{p['area']} {unit}</b></li>
      {f'<li><span>{esc(t["fact_location"])}</span><b>{esc(loc)}</b></li>' if loc else ''}
      <li><span>{esc(t['fact_photos'])}</span><b>{len(p['images'])}</b></li>
    </ul>"""

    def pn(q, cls, label, icon_first):
        qloc = q["location"][lang]
        meta = f'{q["area"]} {unit}' + (f' · {esc(qloc)}' if qloc else '')
        return f"""<a href="{q['slug']}.html" class="pn__link {cls}">
      <img class="pn__thumb" src="{base}img/projs/{q['slug']}/cover.jpg" alt="" loading="lazy">
      <span class="pn__label">{label}</span>
      <span class="pn__title">{esc(q['title'])}</span>
      <span class="pn__meta">{meta}</span>
    </a>"""

    body = f"""<body>
{header(t, base, home, alt_href)}
<main>
<section class="project-hero">
  <img src="{imgdir}cover.jpg" alt="{esc(t['cover_alt'].format(title=p['title']))}" fetchpriority="high">
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="{home}">{esc(t['crumb_home'])}</a><span>/</span><a href="{home}#projects">{esc(t['crumb_projects'])}</a><span>/</span><span>{esc(p['title'])}</span></nav>
    <h1 class="display h1">{esc(p['title'])}</h1>
    <div class="chips">{chips}</div>
  </div>
</section>

<section class="section section--tight">
  <div class="container project-intro">
    <div class="reveal">
      <p class="eyebrow">{esc(t['project_eyebrow'])}</p>
      {facts}
    </div>
    <div class="reveal">
      <p class="lead">{esc(p['description'][lang])}</p>
    </div>
  </div>
</section>

<section class="section section--tight section--alt" id="gallery">
  <div class="container">
    <div class="section-head reveal">
      <div><p class="eyebrow">{esc(t['gallery_eyebrow'])}</p><h2 class="display h2">{esc(t['gallery_title'])}</h2></div>
      <span class="muted">{esc(t['gallery_hint'])}</span>
    </div>
    <div class="gallery">
{gallery}
    </div>
  </div>
</section>

<nav class="pn" aria-label="{esc(t['prev'])} / {esc(t['next'])}">
  {pn(prev_p, 'pn__link--prev', esc(t['prev']), True)}
  {pn(next_p, 'pn__link--next', esc(t['next']), False)}
</nav>

<section class="section cta">
  <div class="container reveal">
    <h2 class="display h2">{esc(t['cta_title'])}</h2>
    <div class="btn-row">
      <a href="{home}#contacts" class="btn">{esc(t['cta_btn1'])}</a>
      <a href="{home}#projects" class="btn btn--ghost">{esc(t['cta_btn2'])}</a>
    </div>
  </div>
</section>
</main>

<div class="lightbox" role="dialog" aria-modal="true" aria-label="{esc(t['gallery_title'])}">
  <div class="lightbox__bar">
    <span class="lightbox__counter">1 / {len(p['images'])}</span>
    <span class="lightbox__hint">{esc(t['lb_hint'])}</span>
    <button class="lightbox__btn lightbox__close" aria-label="{esc(t['lb_close'])}">{SVG_X}</button>
  </div>
  <div class="lightbox__stage">
    <img src="" alt="">
    <button class="lightbox__btn lightbox__prev" aria-label="{esc(t['lb_prev'])}">{SVG_LEFT}</button>
    <button class="lightbox__btn lightbox__next" aria-label="{esc(t['lb_next'])}">{SVG_RIGHT}</button>
  </div>
</div>
{footer(t, base, home)}"""
    return head(t, base, title, desc, alt_href, self_href, f"img/projs/{p['slug']}/cover.jpg") + body

def notfound_page():
    # Served by GitHub Pages at any depth: use root-relative paths.
    t = T["uk"]; e = T["en"]
    return f"""<!doctype html>
<html lang="uk">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t['nf_title'])} · {esc(t['site_short'])}</title>
<meta name="robots" content="noindex">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..800&display=swap" rel="stylesheet">
<style>
body{{margin:0;background:#f6f3ee;color:#17171a;font-family:Inter,Arial,sans-serif;line-height:1.6}}
.nf{{min-height:100vh;display:grid;place-items:center;text-align:center;padding:24px}}
h1{{font-family:Inter,Arial,sans-serif;font-weight:800;letter-spacing:-0.04em;font-size:clamp(56px,14vw,160px);line-height:1;margin:0 0 8px}}
h2{{font-family:Inter,Arial,sans-serif;font-weight:700;letter-spacing:-0.02em;font-size:clamp(24px,3.5vw,36px);margin:0 0 12px}}
p{{color:#7a756c;margin:0 0 28px}}
a.btn{{display:inline-block;padding:16px 28px;border-radius:999px;background:#17171a;color:#f6f3ee;text-decoration:none;font-weight:600;font-size:14px;margin:4px}}
a.btn.ghost{{background:transparent;color:#17171a;border:1px solid #17171a}}
</style>
</head>
<body>
<div class="nf"><div>
  <h1>404</h1>
  <h2>{esc(t['nf_title'])} · {esc(e['nf_title'])}</h2>
  <p>{esc(t['nf_text'])}<br>{esc(e['nf_text'])}</p>
  <a class="btn" href="/">{esc(t['nf_btn'])}</a>
  <a class="btn ghost" href="/en/">{esc(e['nf_btn'])}</a>
</div></div>
</body>
</html>
"""

def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    write("index.html", home_page("uk"))
    write("en/index.html", home_page("en"))
    n = len(PROJECTS)
    for i, p in enumerate(PROJECTS):
        prev_p, next_p = PROJECTS[(i - 1) % n], PROJECTS[(i + 1) % n]
        write(f"projects/{p['slug']}.html", project_page("uk", p, prev_p, next_p))
        write(f"en/projects/{p['slug']}.html", project_page("en", p, prev_p, next_p))
    write("404.html", notfound_page())
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    print(f"Built: 2 home pages, {2*n} project pages, 404.html")

if __name__ == "__main__":
    main()
