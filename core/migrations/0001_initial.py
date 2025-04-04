# Generated by Django 4.2.7 on 2025-04-02 20:49

import ckeditor_uploader.fields
import core.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('saved', models.DecimalField(decimal_places=2, default='0.00', max_digits=12)),
                ('shipping_method', models.CharField(blank=True, max_length=100, null=True)),
                ('tracking_id', models.CharField(blank=True, max_length=100, null=True)),
                ('tracking_website_address', models.CharField(blank=True, max_length=100, null=True)),
                ('paid_status', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid'), ('failed', 'Failed'), ('refunded', 'Refunded')], default='pending', max_length=30)),
                ('order_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('product_status', models.CharField(choices=[('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='processing', max_length=30)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', blank=True, length=5, max_length=20, null=True, prefix='SKU')),
                ('oid', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', blank=True, length=5, max_length=20, null=True, prefix='')),
                ('stripe_payment_intent', models.CharField(blank=True, max_length=1000, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=100, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cart Order',
                'ordering': ['-order_date'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='cat', unique=True)),
                ('title', models.CharField(default='Food', max_length=100)),
                ('image', models.ImageField(default='category.jpg', upload_to='category')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField(default=True)),
                ('valid_from', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_to', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='pro', unique=True)),
                ('title', models.CharField(default='Fresh product', max_length=100)),
                ('image', models.ImageField(default='product.jpg', upload_to=core.models.user_directory_path)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='This is a product', null=True)),
                ('price', models.DecimalField(decimal_places=2, default='9.99', max_digits=12)),
                ('old_price', models.DecimalField(decimal_places=2, default='19.99', max_digits=12)),
                ('specification', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('type', models.CharField(blank=True, default='Organic', max_length=100, null=True)),
                ('stock_count', models.CharField(blank=True, default='10', max_length=100, null=True)),
                ('life', models.CharField(blank=True, default='100 Days', max_length=100, null=True)),
                ('mfd', models.DateTimeField(blank=True, null=True)),
                ('product_status', models.CharField(choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('rejected', 'Rejected'), ('in_review', 'In Review'), ('published', 'Published')], default='in_review', max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('digital', models.BooleanField(default=False)),
                ('sku', shortuuid.django_fields.ShortUUIDField(alphabet='1234567890', length=4, max_length=10, prefix='sku', unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='core.category')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Wishlists',
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='ven', unique=True)),
                ('title', models.CharField(default='New vendor', max_length=100)),
                ('image', models.ImageField(default='vendor.jpg', upload_to=core.models.user_directory_path)),
                ('cover_image', models.ImageField(default='vendor.jpg', upload_to=core.models.user_directory_path)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='I am a vendor', null=True)),
                ('address', models.CharField(default='Egypt, Cairo', max_length=100)),
                ('contact', models.CharField(default='+20123456789', max_length=100)),
                ('chat_resp_time', models.CharField(default='100', max_length=100)),
                ('shipping_on_time', models.CharField(default='100', max_length=100)),
                ('authentic_rating', models.CharField(default='100', max_length=100)),
                ('days_return', models.CharField(default='100', max_length=100)),
                ('warranty_period', models.CharField(default='100', max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'vendors',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '★☆☆☆☆'), (2, '★★☆☆☆'), (3, '★★★☆☆'), (4, '★★★★☆'), (5, '★★★★★')], default=None)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='core.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Product Reviews',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='product.jpg', upload_to='product-images')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p_images', to='core.product')),
            ],
            options={
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product', to='core.vendor'),
        ),
        migrations.CreateModel(
            name='CartOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=200)),
                ('product_status', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('qty', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('price', models.DecimalField(decimal_places=2, default='9.99', max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, default='9.99', max_digits=12)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='core.cartorder')),
            ],
            options={
                'verbose_name_plural': 'Cart Order Items',
            },
        ),
        migrations.AddField(
            model_name='cartorder',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.coupon'),
        ),
        migrations.AddField(
            model_name='cartorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefgh12345', length=10, max_length=20, prefix='add', unique=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('is_default', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Address',
                'ordering': ['-is_default', '-created_at'],
            },
        ),
    ]
