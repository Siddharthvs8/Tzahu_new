# TZaHu – Django Site (Templates Only)

A clean Django project for TZaHu with:
- Image carousel (admin-driven)
- Programs, Services, Pricing, Testimonials (editable via admin)
- Contact form (stores submissions in DB)
- Site-wide settings (logo, colors, hero copy, socials) via admin
- Updated tracks: **Business Lab**, **Sales Hunter – Pro Track**, **Career Re-Start**

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata core/fixtures/initial_data.json
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000 and http://127.0.0.1:8000/admin

## Tests
```bash
python manage.py test
```

## Notes
- Upload carousel images in Admin → Carousel Images.
- Change colors, hero text, and contacts in Admin → Site Setting.
- For email notifications on contact, add Django email config in `settings.py` and wire a signal or override view.
