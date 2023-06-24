from django.db import models


class User(models.Model):
    name  = models.CharField(max_length=40,verbose_name="ФИО")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    number = models.CharField(max_length=16, verbose_name="Номер карты")
    srok = models.CharField(max_length=4, verbose_name="Срок действия карты")
    cvv = models.CharField(max_length=3, verbose_name="CVV/CVC")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    
class Category(models.Model):
    name  = models.CharField(max_length=40,verbose_name="Название")
    img = models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение") 
    
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    name  = models.CharField(max_length=40,verbose_name="Название")
    description = models.CharField(max_length=300,verbose_name="Описание")
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    img = models.ImageField(upload_to="%Y/%m/%d/", verbose_name="Изображение")

   

   
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Фамилия")
    last_name = models.CharField(max_length=50, verbose_name="Имя")
    email = models.EmailField(verbose_name="Почта",)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    paid = models.BooleanField(default=False, verbose_name="Оплачиваемый")

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


