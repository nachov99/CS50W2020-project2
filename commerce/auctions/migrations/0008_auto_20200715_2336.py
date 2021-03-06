# Generated by Django 3.0.7 on 2020-07-15 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20200715_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='min_price',
            new_name='price',
        ),
        migrations.AlterField(
            model_name='bid',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='item_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Listing'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.Category'),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='product',
            field=models.ManyToManyField(to='auctions.Listing'),
        ),
    ]
