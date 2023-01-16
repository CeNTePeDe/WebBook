from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=20, help_text='Введите жанр книги', verbose_name='Жанр книги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр книги'
        verbose_name_plural = 'Жанр книги'


class Language(models.Model):
    name = models.CharField(max_length=20, help_text='Введите язык книги', verbose_name='Язык книги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Язык'
        verbose_name_plural = 'Языки'


class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text='Введите имя автора', verbose_name='Имя автора')
    last_name = models.CharField(max_length=100, help_text='Введите фамилию автора', verbose_name='Фамилия автора')
    date_of_birth = models.DateField(help_text='Введите дату рождения', verbose_name='Дата рождения', null=True,
                                     blank=True)
    date_of_death = models.DateField(help_text='Введите дату смерти', verbose_name='Дата смерти', null=True, blank=True)

    def __str__(self):
        return self.last_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    title = models.CharField(max_length=200, help_text='Введите название книги', verbose_name='Название книги')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text='Выберите название жанра',
                              verbose_name='Жанр книги', null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text='Выберите язык книги',
                                 verbose_name='Язык книги', null=True)
    author = models.ManyToManyField('Author', help_text='Выберите имя автора', verbose_name='Имя автора')
    summary = models.TextField(max_length=1000, help_text='Введите краткое описание книги',
                               verbose_name='Аннотация книги')
    isbn = models.CharField(max_length=13, help_text='Должно солержать 13 символов', verbose_name='ISBN книги')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def get_absolute_url(self):
        # возращает URL-адрес для доступа к определенному экземпляру книги
        return reverse('book.detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in self.author.all()])

    display_author.short_description = 'Авторы'


class Status(models.Model):
    name = models.CharField(max_length=20, help_text='Введите статус экземпляра книги',
                            verbose_name='Статус экземпляра книги')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True, help_text='Введите инвентарный номер',
                               verbose_name='Инвентарный номер')
    imprint = models.CharField(max_length=200, help_text='Веведите издательство и год выпуска',
                               verbose_name='Издательство')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, help_text='Изменить состояние экземпляра',
                               verbose_name='Статус книги')
    due_back = models.DateField(null=True, blank=True, help_text='Введите конец срока статуса',
                                verbose_name='Дата оканчания статуса')

    def __str__(self):
        return f'{self.inv_nom} {self.book} {self.status}'

    class Meta:
        verbose_name = 'Статус книги'
        verbose_name_plural = 'Статус книги'
        ordering = ["-due_back"]
