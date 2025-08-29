from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Colonnes affichées dans la liste des utilisateurs
    list_display = ('id', 'email', 'first_name', 'last_name', 'filiere', 'is_staff', 'is_active', 'created_at')
    list_filter = ('filiere', 'is_staff', 'is_active', 'is_superuser', 'created_at')
    search_fields = ('email', 'first_name', 'last_name', 'filiere')
    ordering = ('-created_at',)

    # Organisation des champs dans la page de détail
    fieldsets = (
        ("Identifiants", {'fields': ('email', 'password')}),
        ("Informations personnelles", {'fields': ('first_name', 'last_name', 'filiere')}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ("Dates importantes", {'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')}),
    )

    # Champs affichés lors de la création d’un nouvel utilisateur
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'last_name', 'filiere', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
