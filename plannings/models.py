from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

class PlanningPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='periodes')
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Période {self.date_debut} → {self.date_fin} ({self.user.username})"

    @property
    def est_expire(self):
        return timezone.now().date() > self.date_fin

    @property
    def statut(self):
        """
        Retourne l'état de la période :
        - "actif" : si la date n’est pas expirée
        - "termine" : si expirée et toutes les tâches sont terminées
        - "en_retard" : si expirée et certaines tâches ne sont pas terminées
        """
        today = timezone.now().date()

        # Si pas encore expiré → actif
        if today <= self.date_fin:
            return "actif"

        # Si expiré → vérifier les tâches
        toutes_taches = Task.objects.filter(planning__period=self)
        if toutes_taches.exists() and all(t.statut == "termine" for t in toutes_taches):
            return "termine"
        return "retard"


class Planning(models.Model):
    JOUR_CHOICES = [
        ('lundi', 'Lundi'),
        ('mardi', 'Mardi'),
        ('mercredi', 'Mercredi'),
        ('jeudi', 'Jeudi'),
        ('vendredi', 'Vendredi'),
    ]

    period = models.ForeignKey(
        PlanningPeriod,
        on_delete=models.CASCADE,
        related_name='plannings'
    )
    jour = models.CharField(max_length=10, choices=JOUR_CHOICES)

    class Meta:
        # Un jour ne peut être choisi qu'une seule fois par période
        unique_together = ('period', 'jour')
        # ou bien, en Django 3.2+ tu peux écrire :
        constraints = [
            models.UniqueConstraint(fields=['period', 'jour'], name='unique_jour_per_period')
        ]

    def __str__(self):
        return f"{self.jour} ({self.period})"


class Task(models.Model):
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE, related_name='taches')
    titre = models.CharField(max_length=200)
    duree_estimee = models.PositiveIntegerField(help_text="Durée en minutes")
    lien = models.URLField(blank=True, null=True)
    statut = models.CharField(
        max_length=15,
        choices=[('a_faire', 'À faire'), ('en_cours', 'En cours'), ('termine', 'Terminé')],
        default='a_faire'
    )

    def __str__(self):
        return f"{self.titre} ({self.planning.jour})"
