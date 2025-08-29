from rest_framework import serializers
from .models import PlanningPeriod, Planning, Task

# --------------------------
# Serializer pour Task
# --------------------------
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'titre', 'duree_estimee', 'lien', 'statut']
        read_only_fields = ['id']


# --------------------------
# Serializer pour Planning (jour)
# --------------------------
class PlanningSerializer(serializers.ModelSerializer):
    taches = TaskSerializer(many=True, read_only=True)  # inclut toutes les tâches du jour

    class Meta:
        model = Planning
        fields = ['id', 'jour', 'taches']
        read_only_fields = ['id', 'taches']


# --------------------------
# Serializer pour PlanningPeriod (période)
# --------------------------
class PlanningPeriodSerializer(serializers.ModelSerializer):
    plannings = PlanningSerializer(many=True, read_only=True)  # inclut tous les jours
    est_expire = serializers.ReadOnlyField()  # True/False
    statut = serializers.ReadOnlyField()

    class Meta:
        model = PlanningPeriod
        fields = ['id', 'date_debut', 'date_fin', 'est_expire','statut', 'plannings']
        read_only_fields = ['id', 'est_expire', 'statut','plannings']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
