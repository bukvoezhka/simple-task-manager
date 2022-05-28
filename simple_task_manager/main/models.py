from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория события'
        verbose_name_plural = 'Категории событий'


class ArchiveReport(models.Model):
    start_date = models.DateField(verbose_name="Начало периода", blank=True, null=True)
    end_date = models.DateField(verbose_name="Конец периода", blank=True, null=True)

    def __str__(self):
        return 'Отчет за период: {0} - {1}'.format(self.start_date, self.end_date)

    class Meta:
        verbose_name = 'Отчет за период'
        verbose_name_plural = 'Отчеты за период'


class Event(models.Model):
    description = models.TextField(verbose_name='Описание')
    category = models.ForeignKey(
        to=Category,
        verbose_name='Категория события',
        on_delete=models.SET_NULL,
        null=True,
        help_text='Выбор категории события.',
        related_name='related_category_events',
    )
    archive_report = models.ForeignKey(
        to=ArchiveReport,
        verbose_name='Отчет за период',
        on_delete=models.SET_DEFAULT,
        default=None,
        blank=True,
        null=True,
        related_name='related_archive_events',
    )
    created_at = models.DateField(verbose_name="Cоздано", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Обновлено", auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
