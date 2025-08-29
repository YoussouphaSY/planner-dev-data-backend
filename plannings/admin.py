from django.contrib import admin
from .models import PlanningPeriod, Planning, Task

# Inline pour afficher les plannings directement dans une période
class PlanningInline(admin.TabularInline):
    model = Planning
    extra = 1  # nombre de formulaires vides supplémentaires
    show_change_link = True  # permet de cliquer pour éditer le planning

# Inline pour afficher les tâches directement dans un planning
class TaskInline(admin.TabularInline):
    model = Task
    extra = 1
    show_change_link = True

# Admin pour PlanningPeriod
@admin.register(PlanningPeriod)
class PlanningPeriodAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_debut', 'date_fin', 'est_expire')
    list_filter = ('user', 'date_debut', 'date_fin')
    search_fields = ('user__username',)
    inlines = [PlanningInline]

# Admin pour Planning
@admin.register(Planning)
class PlanningAdmin(admin.ModelAdmin):
    list_display = ('jour', 'period', 'period_user')
    list_filter = ('jour',)
    search_fields = ('period__user__username',)

    def period_user(self, obj):
        return obj.period.user
    period_user.short_description = 'Utilisateur'

# Admin pour Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('titre', 'planning', 'jour', 'duree_estimee', 'statut')
    list_filter = ('statut', 'planning__jour')
    search_fields = ('titre', 'planning__period__user__username')

    def jour(self, obj):
        return obj.planning.jour
    jour.short_description = 'Jour'
