from django.shortcuts import render
from django.views import generic
from .models import Element, AttributeType, Attribute, Orbment, Power, Range
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
    paginate_by = 10

class OrbmentDetailView(generic.DetailView):
    model = Orbment
