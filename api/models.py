from django.db import models
from django.db.models import Q
from django.conf import settings


class NoteQuerySet(models.QuerySet):
    def search(self, query, user=None):
        lookup = Q(title__icontains=query)  # | Q(note__icontains=query)
        qs = self.filter(lookup)
        if user is not None:
            qs2 = qs.filter(owner=user).filter(lookup)
            qs = qs2.distinct()
        return qs


class NoteManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return NoteQuerySet(self.model, using=self.db)

    def search(self, query, user=None):
        return self.get_queryset().search(query, owner=user)


# Priority_choices = [{
#     1 :"high",
#     2 : "medium"
#     3 : "low"
# }]
class Note(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    note = models.TextField()

    objects = NoteManager()
