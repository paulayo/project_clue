
from django.db import models


from oscar.apps.catalogue.abstract_models import (AbstractProduct, AbstractProductClass,
                                                  AbstractCategory,AbstractProductRecommendation,
                                                   AbstractProductAttribute, AbstractProductImage,
                                                   AbstractOption)
from oscar.core.loading import  get_classes

from clue import settings


ProductManager, BrowsableProductManager = get_classes(
    'catalogue.managers', ['ProductManager', 'BrowsableProductManager'])
import catalogue



class ShirtProductClass(AbstractProductClass):

    name = models.CharField(name='tshirt_type', max_length=128)



class ShirtAttribute(AbstractProductAttribute):

    product_class = models.ForeignKey(
        ShirtProductClass,
        on_delete=models.CASCADE,
        )

    name = models.CharField('Name', max_length=128) 
    type = models.CharField('text', max_length=20)
    option_group = models.ForeignKey(
        'AttributeOptionGroup',
        on_delete=models.CASCADE,
        )

class ShirtCategory(AbstractCategory):
    name = models.CharField('shirt', max_length=200)
    description = models.TextField('shirt_desc')
    


class ShirtRecommendation(AbstractProductRecommendation):
    primary = models.ForeignKey(
        'ShirtProduct',
        on_delete=models.CASCADE,
        related_name='primary_recommendations')

    recommendation = models.ForeignKey(
        'ShirtProduct',
        on_delete=models.CASCADE)


class ShirtOption(AbstractOption):

    pass

class ShirtProduct(AbstractProduct):
    
    structure = models.CharField('standalone', max_length=10)
    slug = models.SlugField('t-shirts', max_length=255, unique=False)
    description = models.TextField('Description', blank=True)
    product_class = models.ForeignKey(ShirtProductClass, 
                                        on_delete=models.PROTECT,
                                        null = True,
                                        blank = True,
                                        verbose_name = 'product type',
                                        related_name = 'products'
                                        )
    title = models.CharField('title', max_length=255, blank=True)   

    date_updated = models.DateTimeField('Date updated', 
                                        auto_now=True,
                                        db_index=True)
    attributes = models.ManyToManyField(ShirtAttribute)
    recommended_products = models.ManyToManyField( 
        to="self",
        symmetrical=False,
        related_name=None,
        )
    categories = models.ManyToManyField(ShirtCategory)
    product_options = models.ManyToManyField(ShirtOption, blank=True)

    objects = ProductManager()
    browsable = BrowsableProductManager()







from oscar.apps.catalogue.models import *