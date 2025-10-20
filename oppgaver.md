# Oppgaver – Mini-blogg med Flask – **kun lister**

Sett opp virtual enviroment i prosjektmappen din:

python3 -m venv .venv 

Start virtual enviromentet

source .venv/bin/activate`

## Oppgave 1 – Hello Flask

1. Kjør `starter/app.py` og sjekk at «It works!» vises.
2. Se i `templates/` og `static/` (filer finnes med TODO).
3. Bytt rot-ruten til å bruke `render_template('index.html')` når du kommer til Oppgave 2.

**Sjekkpunkt:** Serveren restarter når du lagrer, og du når http://127.0.0.1:5000/

---

## Oppgave 2 – Templates og layout

1. Lag `base.html` med `<header>`, `<main>` og `<footer>`.
2. Lag `index.html` som **arver** fra `base.html` og viser «Innlegg».
3. Koble `static/style.css` via `url_for('static', filename='style.css')`.

**Sjekkpunkt:** `index.html` renderes med `render_template(...)` i `app.py`.

---

## Oppgave 3 – Hardkodede innlegg (lister) på forsiden

1. I `app.py`: Lag en liste `posts` med 3–4 **lister**. Hver post er
   
   ```python
   [id, title, content_html]
   # eksempel: [1, "Første innlegg", "<p>Hei!</p>"]
   ```

2. Send `posts` til `index.html` og **loop** i Jinja:
   
   - Vis tittel med `post[1]`.
   - Lag lenke til detaljside: `url_for('post_detail', post_id=post[0])`.

**Sjekkpunkt:** Forsiden viser en liste over innleggstitler som lenker til detaljsider (ennå ikke laget).

---

## Oppgave 4 – Detaljside (via id) og 404

1. Lag rute `@app.route('/post/<int:post_id>')` i `app.py`.
2. Finn riktig post ved å slå opp på `post_id` (sammenlign med `post[0]`). Hvis ikke funnet: `abort(404)`.
3. Lag `post.html` som viser tittel `post[1]` og `post[2]` (bruk `|safe` for HTML-innhold).
4. Lag en `404.html` og error handler i `app.py` som returnerer den.

**Sjekkpunkt:** Klikk tittel på forsiden → detaljside. Ukjent id → 404-side.

---

## Oppgave 5 – Finish & pynt

- Litt CSS (margins, font, maks bredde).
- Sorter `posts` synkende på `id` (valgfritt).
- Egen «Om»-side som ny rute og template (valgfritt).
- Legg inn «Tilbake»-lenke fra detaljsiden.

---
