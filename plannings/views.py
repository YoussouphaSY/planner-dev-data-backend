from django.utils import timezone
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import PlanningPeriod, Planning, Task
from .serializers import PlanningPeriodSerializer, PlanningSerializer, TaskSerializer

# ---------------------------
# Utilitaires
# ---------------------------

def update_planning_statut(planning):
    """Met à jour le statut des tâches si le planning est expiré"""
    if planning.period.date_fin and timezone.now().date() > planning.period.date_fin:
        for task in planning.taches.all():
            if task.statut != 'termine':
                task.statut = 'a_faire'  # ou 'en_cours' selon logique
                task.save()

def update_period_statut(period):
    """Met à jour tous les plannings et tâches d'une période"""
    for planning in period.plannings.all():
        update_planning_statut(planning)


# ---------------------------
# PlanningPeriod
# ---------------------------
class PlanningPeriodListCreateView(generics.ListCreateAPIView):
    serializer_class = PlanningPeriodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = PlanningPeriod.objects.filter(user=self.request.user).order_by('date_debut')
        for period in queryset:
            update_period_statut(period)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PlanningPeriodDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlanningPeriodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = PlanningPeriod.objects.filter(user=self.request.user)
        for period in queryset:
            update_period_statut(period)
        return queryset


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_periods(request, user_id):
    periods = PlanningPeriod.objects.filter(user_id=user_id).order_by('date_debut')
    for period in periods:
        update_period_statut(period)
    serializer = PlanningPeriodSerializer(periods, many=True)
    return Response(serializer.data)


# ---------------------------
# Planning (jours)
# ---------------------------
class PlanningListCreateView(generics.ListCreateAPIView):
    serializer_class = PlanningSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        period = get_object_or_404(PlanningPeriod, id=self.kwargs.get('period_id'), user=self.request.user)
        return period.plannings.all()

    def perform_create(self, serializer):
        period = get_object_or_404(PlanningPeriod, id=self.kwargs.get('period_id'), user=self.request.user)
        serializer.save(period=period)


class PlanningDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlanningSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        period = get_object_or_404(PlanningPeriod, id=self.kwargs.get('period_id'), user=self.request.user)
        return period.plannings.all()


# ---------------------------
# Task
# ---------------------------
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        planning = get_object_or_404(Planning, id=self.kwargs.get('planning_id'), period__user=self.request.user)
        return planning.taches.all()

    def perform_create(self, serializer):
        planning = get_object_or_404(Planning, id=self.kwargs.get('planning_id'), period__user=self.request.user)
        serializer.save(planning=planning)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        planning = get_object_or_404(Planning, id=self.kwargs.get('planning_id'), period__user=self.request.user)
        return planning.taches.all()
