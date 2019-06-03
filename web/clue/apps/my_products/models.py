from django.db import models
from clue import settings

from oscar.apps.catalogue.models import (ProductImage, Product,
                                                  Category, ProductAttributeValue,
                                                  ProductClass, ProductRecommendation,
                                                  ProductAttribute
                                                  )

from oscar.models.fields import AutoSlugField
# Create your models here
 

class TShirtProductClass(ProductClass):

    name = models.CharField(name='tshirt_type', max_length=128)

    pass
class TShirtProduct(Product):
    
    structure = models.CharField('standalone', max_length=10)
    slug = models.SlugField('t-shirts', max_length=255, unique=False)
    description = models.TextField('Description', blank=True)
    product_class = models.ForeignKey(TShirtProductClass, on_delete=models.PROTECT,
                                        null = True,
                                        blank = True,
                                        verbose_name = 'product type',
                                        related_name = 'products'
                                        )
    title = models.CharField('title', max_length=255, blank=True)   

    date_updated = models.DateTimeField('Date updated', 
                                        auto_now=True,
                                        db_index=True)
    # categories = models.ManyToManyField(TShirtCategory,
    #                                     through='TShirtCategory',
    #                                     verbose_name='T-Shirt Category')
    pass


class TShirtAttributeValue(ProductAttributeValue):
    product = models.ForeignKey(
        'TShirtProduct',
        on_delete=models.CASCADE,
        related_name='attribute_values',
        verbose_name="Product"
    )
    value_text = models.TextField('Text', blank=True, null=True)
    value_integer = models.IntegerField('Integer', blank=True, null=True)
    value_boolean = models.NullBooleanField('Boolean', blank=True)
    value_float = models.FloatField('Float', blank=True, null=True)
    value_richtext = models.TextField('Richtext', blank=True, null=True)
    value_date = models.DateField('Date', blank=True, null=True)
    value_datetime = models.DateTimeField('DateTime', blank=True, null=True)
    value_file = models.FileField(
        upload_to=settings.OSCAR_IMAGE_FOLDER, max_length=255,
        blank=True, null=True)
    value_image = models.ImageField(
        upload_to='media/product_image/', max_length=255,
        blank=True, null=True)
    pass

class TShirtCategory(Category):
    name = models.CharField('Name', max_length=255, db_index=True)
    description = models.TextField('Description', blank=True)
    pass

class TShirtRecommendation(ProductRecommendation):
    pass




class TshirtImage(ProductImage):
    product = models.ForeignKey(TShirtProduct, on_delete=models.CASCADE,
                            related_name='tshirt_images',
                            verbose_name='tshirt_product')
    original = models.ImageField('original', upload_to='./media/product/product_image/',
                                max_length=255)
    display_order = models.PositiveIntegerField('display order', default=1)
    caption = models.CharField('caption', max_length=200)

    def is_primary(self):
        """
        Return bool if image display order is 0
        """
        return self.display_order == 1



from oscar.apps.catalogue.abstract_models import *