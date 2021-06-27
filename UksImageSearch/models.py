from django.db import models

class Product(models.Model):

    name = models.CharField('Група товара',max_length=250)
    ukr_name = models.CharField("Група товара Укр.",max_length=250)
    article = models.CharField('Полный артикул',max_length=250)
    product_code = models.CharField('Сокращеный артикул',max_length=250)
    color_name = models.CharField('Название цвета',max_length=250)
    color_code = models.CharField("Код цвета",max_length=100)
    img_link = models.URLField('Сылка на изображения')

    def __str__(self):
        return self.ukr_name
        

    
        

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class Logo(models.Model):
    name = models.CharField('Название бренда',max_length=100)
    svg_code = models.TextField('Код svg',default='')
    image = models.ImageField('Изображение логотипа',upload_to='logo/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Логотип'
        verbose_name_plural = 'Логотипи'