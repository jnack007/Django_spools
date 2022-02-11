from django.views.generic import TemplateView, ListView

from .models import Spool


from django.db.models import Q


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Spool
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Spool.objects.filter(
            Q(tag=query) | Q(level=query)
        )
        return  object_list
        # to add an or filter see below example:
        # Q(tag='AS-L00-050') | Q(level='Level 00')
