from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.

class Element(models.Model):
    """Model representing an Orbment."""
    name = models.CharField(max_length=10, verbose_name='Element')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class AttributeType(models.Model):
    """Model representing an AttributeType."""
    description = models.CharField(max_length=100, verbose_name='Attribute Description')

    def __str__(self):
        """String for representing the Model object."""
        return self.attribute_type.description
    
class Attribute(models.Model):
    """Model representing an Orbment."""
    value = models.IntegerField(verbose_name='Value', null=True, blank=True)
    attribute_type = models.ForeignKey(AttributeType, on_delete=models.CASCADE, verbose_name='Attribute Type')

    def __str__(self):
        """String for representing the Model object."""
        return self.attribute_type.description

class Orbment(models.Model):
    """Model representing an Orbment."""
    name = models.CharField(max_length=200, verbose_name='Name')
    element = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name='Element')
    power = models.CharField(max_length=5, null=True, blank=True, verbose_name='Power')
    range = models.CharField(max_length=20, null=True, blank=True, verbose_name='Range')
    sepith_cost = models.IntegerField(null=True, blank=True, verbose_name='Sepith Cost')
    u_material_cost = models.IntegerField(null=True, blank=True, verbose_name='U-Material Cost')
    slots_required = models.IntegerField(default=1, verbose_name='Number of Slots Required')

    # ManyToManyField used because genre can contain many attribute types. Attribute types can belong to many orbments.
    # Genre class has already been defined so we can specify the object above.
    attribute_type = models.ManyToManyField(Attribute)

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this orbment."""
        return reverse('orbment-detail', args=[str(self.id)])
