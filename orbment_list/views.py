from django.shortcuts import render
from django.views import generic
from .models import Element, Attribute, Orbment, Power, Range
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_orbments = Orbment.objects.all().count()

    context = {
        'num_orbments': num_orbments,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class OrbmentListView(generic.ListView):
    model = Orbment
    paginate_by = 50

    def get_orbment_table_data():
        orb_dict = {}
        attr_dict = {}
        for orbment in Orbment.objects.all():
            for atts in list(orbment.attributes.all().values('name', 'value')):
                attr_dict[atts['name']] = atts['value']
            #atts = orbment.attributes.all().values('name', 'value')
            orb_dict[orbment.name] = attr_dict
            attr_dict = {}
        print("orb_dict: ", orb_dict)
        attributes = Attribute.objects.all().distinct('name')
        
        for key in orb_dict:
            for attr in attributes:
                if orb_dict[key].get(attr.name) == None:
                    orb_dict[key][attr.name] = ''

        for key in orb_dict:
            orb_dict[key] = sorted(orb_dict[key].items())
        
        print("sorted: ", orb_dict)

        return orb_dict

            
        
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(OrbmentListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the Attributes
        context['attributes'] = Attribute.objects.all().distinct('name')
        context['orb_attrs'] = OrbmentListView.get_orbment_table_data()
        return context
            

class OrbmentDetailView(generic.DetailView):
    model = Orbment

#             {% for orb_attribute in orbment.attributes.all %}
            # {% for attribute in attributes %}
            # {% if orb_attribute.name == attribute.name %}
            # <td>{{ attribute.value }}</td>
            # {% else %}
            # <td>0</td>
            # {% endif %}
            # {% endfor %}
            # {% endfor %}