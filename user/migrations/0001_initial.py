# Generated by Django 4.2.4 on 2023-08-31 12:44

from django.db import migrations, models
import user.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50, verbose_name='first-name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last-name')),
                ('nickname', models.CharField(max_length=50, unique=True, verbose_name='nickname')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('password', models.CharField(max_length=250, verbose_name='password')),
                ('avatar', models.ImageField(upload_to='upload/images/users/avatar/', verbose_name='avatar')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is_superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_moderator', models.BooleanField(default=False, verbose_name='is_moderator')),
                ('groups', models.ManyToManyField(related_name='custom_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='custom_users_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            managers=[
                ('objects', user.models.user.CustomUserManager()),
            ],
        ),
    ]