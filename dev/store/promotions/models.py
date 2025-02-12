from django.db import models


class Promotion(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок акции")
    description = models.TextField(verbose_name="Описание акции")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return self.title
