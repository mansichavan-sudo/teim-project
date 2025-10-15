# Generated manually to fix existing NULLs and set defaults

from django.db import migrations, models

def set_default_for_recommendation(apps, schema_editor):
    Recommendation = apps.get_model('lead_automation', 'Recommendation')
    # Update NULL values to empty string
    Recommendation.objects.filter(upsell_item__isnull=True).update(upsell_item='')
    Recommendation.objects.filter(cross_sell_item__isnull=True).update(cross_sell_item='')

class Migration(migrations.Migration):

    dependencies = [
        ('lead_automation', '0001_initial'),  # Change this if your initial migration has a different name
    ]

    operations = [
        migrations.RunPython(set_default_for_recommendation),
        migrations.AlterField(
            model_name='recommendation',
            name='upsell_item',
            field=models.CharField(max_length=100, blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='recommendation',
            name='cross_sell_item',
            field=models.CharField(max_length=100, blank=True, default=''),
        ),
    ]
