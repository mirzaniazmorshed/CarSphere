from django.views.generic import TemplateView
from cars.models import CarModel
from brands.models import BrandModel

# home view page
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = CarModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['search'] = 'all'
        return context

# home view page
class BrandSearchView(TemplateView):
    template_name = 'index.html'
    k_url_kwarg = 'id'
   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = CarModel.objects.filter(brand=kwargs.get('id'))
        context['brands'] = BrandModel.objects.all()
        get_brand_name = BrandModel.objects.get(pk=kwargs.get('id'))
        context['search'] = str(get_brand_name.brand_name)
        
        return context
  
