from django.db import models 

class MainImages(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(main=True)
    