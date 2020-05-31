from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_doctor_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
