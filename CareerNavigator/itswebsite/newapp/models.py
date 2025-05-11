from django.db import models


class Professions(models.Model):
    title = models.CharField('Профессия', max_length=50, default='Профессия')
    anons = models.CharField('Анонс', max_length=200)
    full_text = models.TextField('Описание профессии')
    demand = models.TextField('Востребованность профессии')
    studying = models.TextField('Направления обучения')
    unis = models.TextField('Вузы')
    exams = models.TextField('Предметы ЕГЭ')
    date = models.DateField('Дата обновления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
