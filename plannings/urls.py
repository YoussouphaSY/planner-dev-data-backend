from django.urls import path
from . import views

urlpatterns = [
    # ---------------------------
    # PlanningPeriod (périodes)
    # ---------------------------
    path('periodes/', views.PlanningPeriodListCreateView.as_view(), name='period_list_create'),
    path('periodes/<int:pk>/', views.PlanningPeriodDetailView.as_view(), name='period_detail'),
    path('periodes/user/<int:user_id>/', views.user_periods, name='user_periods'),

    # ---------------------------
    # Planning (jours) d'une période
    # ---------------------------
    path('periodes/<int:period_id>/plannings/', views.PlanningListCreateView.as_view(), name='planning_list_create'),
    path('periodes/<int:period_id>/plannings/<int:pk>/', views.PlanningDetailView.as_view(), name='planning_detail'),

    # ---------------------------
    # Task (tâches) d'un planning/jour
    # ---------------------------
    path('plannings/<int:planning_id>/tasks/', views.TaskListCreateView.as_view(), name='task_list_create'),
    path('plannings/<int:planning_id>/tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
]
