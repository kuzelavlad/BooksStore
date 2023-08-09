from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField


class BaseDateMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# class User(models.Model):
#     username = models.CharField(verbose_name="Имя", max_length=255, unique=True)
#     # password = models.CharField(verbose_name="Пароль", max_length=255)

    # def __str__(self):
    #     return self.username
    #
    # class Meta:
    #     verbose_name = "Пользователь"
    #     verbose_name_plural = "Пользователи"


class Books(models.Model):

    status_stock = (
        ("In_stock", "В наличие"),
        ("Out_of_stock", "Отсутствует"),
        ("Dev_expected", "Ожидается поставка"),

    )
    category_of_books = (

        ("F", "Fantasy"),
        ("D", "Detective"),
        ("H", "Horror"),
        ("A", "Adventures"),
        ("P", "Poetry"),
        ("PS", "Psychology"),
        ("SL", "Scientific literature"),
    )

    title = models.CharField(verbose_name='Название Книги', max_length=30)
    author = models.CharField(verbose_name='Автор', max_length=55)
    price = models.DecimalField(verbose_name='Цена', max_digits=15, decimal_places=2)
    full_description = models.TextField(verbose_name='Полное описание', max_length=255)
    status = models.CharField(verbose_name='Cостояние', max_length=16, choices=status_stock)
    category = models.CharField(verbose_name='Категория', max_length=20, choices=category_of_books)
    date = models.DateField(verbose_name='Дата поставки')
    created_time = models.DateTimeField(verbose_name='время создания', auto_now_add=True)
    modified_time = models.DateTimeField(verbose_name='время модификации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

#
# class CustomUser(AbstractUser):
#     TIERS = (
#         ("G", "Gold"),
#         ("S", "Silver"),
#         ("B", "Bronze"),
#     )
#     tier = models.CharField(max_length=1, choices=TIERS, null=True, blank=True)