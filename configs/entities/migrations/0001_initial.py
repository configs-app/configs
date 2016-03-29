from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID'
                    )
                ),
                (
                    'name', models.CharField(
                        max_length=255,
                        unique=True
                    )
                ),
                (
                    'notes', models.TextField(
                        blank=True,
                        null=True
                    )
                ),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
