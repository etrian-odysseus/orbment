from django.contrib import admin

from .models import Element, AttributeType, Attribute, Orbment, Power, Range

admin.site.register(Element)
admin.site.register(AttributeType)
admin.site.register(Attribute)
admin.site.register(Orbment)
admin.site.register(Power)
admin.site.register(Range)

