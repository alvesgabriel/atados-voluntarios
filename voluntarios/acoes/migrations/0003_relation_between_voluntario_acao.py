# Generated by Django 3.1.2 on 2020-10-12 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acoes', '0002_voluntario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acao',
            old_name='instituica',
            new_name='instituicao',
        ),
        migrations.CreateModel(
            name='Inscrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('acao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acoes.acao')),
                ('voluntario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acoes.voluntario')),
            ],
        ),
        migrations.AddField(
            model_name='acao',
            name='voluntarios',
            field=models.ManyToManyField(related_name='voluntarios', through='acoes.Inscrito', to='acoes.Voluntario'),
        ),
        migrations.AddField(
            model_name='voluntario',
            name='acoes',
            field=models.ManyToManyField(related_name='_voluntario_acoes_+', through='acoes.Inscrito', to='acoes.Voluntario'),
        ),
    ]
