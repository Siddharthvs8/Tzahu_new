from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='TZaHu', max_length=120)),
                ('tagline', models.CharField(blank=True, default='The Sales Hunter', max_length=200)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('primary_color', models.CharField(default='#000000', max_length=7)),
                ('accent_color', models.CharField(default='#f5c518', max_length=7)),
                ('text_color', models.CharField(default='#eaeaea', max_length=7)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('location', models.CharField(blank=True, default='Kochi • Kerala • India', max_length=120)),
                ('instagram_url', models.URLField(blank=True)),
                ('linkedin_url', models.URLField(blank=True)),
                ('youtube_url', models.URLField(blank=True)),
                ('hero_badge', models.CharField(blank=True, default='Proven playbooks • 100% placement support', max_length=160)),
                ('hero_headline', models.CharField(default='Build a hunter-class sales engine.', max_length=160)),
                ('hero_subheadline', models.TextField(blank=True, default='We train teams, place talent, and design revenue systems for entrepreneurs, freshers, and growing companies. Scripts, cadences, and strategy—delivered.')),
                ('cta_primary_text', models.CharField(default='Get Free Audit →', max_length=60)),
                ('cta_secondary_text', models.CharField(default='Explore Programs', max_length=60)),
                ('footer_text', models.CharField(blank=True, default='All rights reserved.', max_length=200)),
            ],
            options={
                'verbose_name': 'Site Setting (create exactly one)',
                'verbose_name_plural': 'Site Setting',
            },
        ),
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel/')),
                ('alt_text', models.CharField(blank=True, max_length=200)),
                ('caption', models.CharField(blank=True, max_length=200)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=80)),
                ('title', models.CharField(max_length=160)),
                ('points_text', models.TextField(help_text='One bullet per line')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('text', models.CharField(max_length=240)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('price_label', models.CharField(help_text='e.g., ₹50,000 / month or Custom', max_length=120)),
                ('highlight', models.BooleanField(default=False)),
                ('perks_text', models.TextField(help_text='One bullet per line')),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('role', models.CharField(blank=True, max_length=160)),
                ('quote', models.TextField()),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['order', 'id']},
        ),
        migrations.CreateModel(
            name='ContactSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
