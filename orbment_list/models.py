from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
# Create your models here.

class Power(models.Model):
    """Model representing ATS Power."""
    name = models.CharField(max_length=10, verbose_name='Power Value')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Range(models.Model):
    """Model representing Arts Range."""
    name = models.CharField(max_length=25, verbose_name='Arts Range')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
class Element(models.Model):
    """Model representing an Orbment."""
    name = models.CharField(max_length=10, verbose_name='Element')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Attribute(models.Model):
    """Model representing an Attribute."""
    value = models.CharField(max_length=10, verbose_name='Attribute Value')
    name = models.CharField(max_length=100, verbose_name='Attribute Name')

    class Meta:
        ordering = ['name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name} {self.value}'

class Orbment(models.Model):
    """Model representing an Orbment."""
    name = models.CharField(max_length=200, verbose_name='Name')
    element = models.ForeignKey(Element, on_delete=models.CASCADE, verbose_name='Element')
    power = models.ForeignKey(Power, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Power')
    range = models.ForeignKey(Range, null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Range')
    sepith_cost = models.IntegerField(null=True, blank=True, verbose_name='Sepith Cost')
    u_material_cost = models.IntegerField(null=True, blank=True, verbose_name='U-Material Cost')
    slots_required = models.IntegerField(default=0, verbose_name='Number of Slots Required')

    # ManyToManyField used because orbment can contain many attribute types. Attribute types can belong to many orbments.
    # Orbment class has already been defined so we can specify the object above.
    attributes = models.ManyToManyField(Attribute, blank=True, related_name='attributes')

    class Meta:
        ordering = ['element', 'name']

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this orbment."""
        return reverse('orbment-detail', args=[str(self.id)])
