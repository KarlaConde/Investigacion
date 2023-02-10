# Generated by Django 4.1.5 on 2023-01-06 22:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("username", models.CharField(max_length=100, unique=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=150,
                        null=True,
                        unique=True,
                        verbose_name="Correo",
                    ),
                ),
                (
                    "tipo_documento",
                    models.CharField(
                        choices=[("cedula", "Cedula"), ("pasaporte", "Pasaporte")],
                        max_length=20,
                        verbose_name="Tipo de documento",
                    ),
                ),
                (
                    "cedula",
                    models.CharField(
                        blank=True, max_length=13, null=True, verbose_name="Cedula"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Nombres"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Apellidos"
                    ),
                ),
                (
                    "estudios_p",
                    models.TextField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Estudios Primarios",
                    ),
                ),
                (
                    "estudios_s",
                    models.TextField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Estudios Secundarios",
                    ),
                ),
                (
                    "universidad",
                    models.TextField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Universidad",
                    ),
                ),
                (
                    "cursos",
                    models.TextField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Cursos o Certificaciones",
                    ),
                ),
                (
                    "experiencia",
                    models.TextField(
                        blank=True,
                        max_length=700,
                        null=True,
                        verbose_name="Experiencia Laboral",
                    ),
                ),
                (
                    "celular",
                    models.CharField(
                        blank=True, max_length=13, null=True, verbose_name="N.Celular"
                    ),
                ),
                (
                    "direccion",
                    models.CharField(
                        blank=True, max_length=20, null=True, verbose_name="Direccion"
                    ),
                ),
                (
                    "foto",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Fotos_usuarios/",
                        verbose_name="Subir una foto",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Categoria_Inv",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "categoria_investigacion",
                    models.CharField(max_length=150, verbose_name="Categoria"),
                ),
                ("descripcion", models.TextField()),
                (
                    "foto",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="fotos_categorías/",
                        verbose_name="Foto categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Investigacion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_investigacion",
                    models.CharField(max_length=150, verbose_name="Emprendimiento"),
                ),
                ("titulo", models.CharField(max_length=150, verbose_name="direccion")),
                ("Resumen", models.TextField()),
                (
                    "ImagenD",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="Imagen Destacada",
                        verbose_name="Subir una foto",
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(blank=True, null=True, verbose_name="Linkedin"),
                ),
                ("uploadedFile", models.FileField(upload_to="Uploaded Files/")),
                ("dateTimeOfUpload", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Administrador",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("fecha_inicio", models.DateTimeField()),
                ("fecha_actualizacion", models.DateTimeField()),
                ("estado", models.BooleanField()),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("administracion.persona",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "investigaciones",
                    models.ManyToManyField(
                        blank=True, to="administracion.investigacion"
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("administracion.persona",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
