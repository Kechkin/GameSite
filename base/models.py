from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категория Игры"""
    name = models.CharField('Категория', max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    """Жанр игры"""
    name = models.CharField('Жанр', max_length=30)
    description = models.TextField("Описание", max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Company(models.Model):
    """Разработчики/компаниия"""
    name = models.CharField('компаниия', max_length=30)
    description = models.TextField("Описание", max_length=250)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'компаниия'
        verbose_name_plural = 'компаниии'


class PersonGame(models.Model):
    """Персонаж игры"""
    name = models.CharField('Имя', max_length=20)
    age = models.PositiveSmallIntegerField('Возраст', blank=True)
    description = models.TextField("Описание", max_length=550, null=True)
    race = models.CharField('Раса', default='Человек', max_length=30)
    image = models.ImageField("Изображение", upload_to="images", blank=True)
    slug = models.SlugField(unique=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE, verbose_name='Игра')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Персонаж'
        verbose_name_plural = 'Персонажи'


class Game(models.Model):
    """Игра"""
    title = models.CharField('Игра', max_length=30)
    description = models.TextField("Описание", max_length=350)
    slug = models.SlugField(unique=True)
    image = models.ImageField("Изображение", upload_to="images", blank=True)
    year = models.PositiveSmallIntegerField('Год выхода', default=2021)
    country = models.CharField("Страна", max_length=15)
    company = models.ManyToManyField(Company, verbose_name='Компании')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    person = models.ManyToManyField(PersonGame, related_name='персонажи', blank=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse('detail_game', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class GameShorts(models.Model):
    """Кадры из игры"""
    title = models.CharField('Название', max_length=20)
    image = models.ImageField("Изображение", upload_to="images", blank=True)
    description = models.TextField("Описание")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Кадр'
        verbose_name_plural = 'Кадры'


class Review(models.Model):
    """Комментарий"""
    user = models.CharField('Юзер', max_length=20)
    text = models.TextField('Комментарий', max_length=250)
    email = models.EmailField('Email', max_length=40)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Комментрий')

    def __str__(self):
        return f"{self.user} {self.email}"

    class Meta:
        verbose_name = 'Юзер'
        verbose_name_plural = 'Юзер'
