# Generated by Django 3.0.4 on 2020-03-11 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_question_publish'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionStat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_choice', models.CharField(editable=False, help_text="La réponse choisie par l'internaute", max_length=50)),
                ('created', models.DateTimeField(auto_now=True, help_text='La date & heure de la réponse')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='api.Question')),
            ],
        ),
    ]
