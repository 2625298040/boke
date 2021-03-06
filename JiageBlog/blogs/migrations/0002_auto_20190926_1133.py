# Generated by Django 2.0.6 on 2019-09-26 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloginfo',
            options={'verbose_name': '博客信息', 'verbose_name_plural': '博客信息'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '博客类别', 'verbose_name_plural': '博客类别'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '博客评论', 'verbose_name_plural': '博客评论'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '博客标签', 'verbose_name_plural': '博客标签'},
        ),
        migrations.AlterField(
            model_name='bloginfo',
            name='add_time',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comments', to='blogs.BlogInfo', verbose_name='博客'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub',
            field=models.DateTimeField(auto_now=True, verbose_name='发布时间'),
        ),
    ]
