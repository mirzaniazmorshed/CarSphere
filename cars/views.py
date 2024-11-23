from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import DetailView
from .models import CarModel
from . import forms
from django.contrib import messages

# Create your views here.

#car details show
class CarDetailView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = car
                messages.success(self.request, 'Commented successfull')
                new_comment.save()
                return self.get(request, *args, **kwargs)
        else:
             messages.warning(self.request, 'OOPS! May be this email user already commented')
             return redirect('car_details',self.kwargs.get('id'))
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car'] = CarModel.objects.get(pk=self.kwargs.get('id'))
        car = self.object
        comments = car.comments.all()
        
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['form'] = comment_form 
        return context


class CarBuy(View):
     def get(self,request,*args, **kwargs):
        id = kwargs.get('id')
        buy_car = CarModel.objects.get(pk=id)
        buy_car.quantity -= 1
        buy_car.save()
        if request.session.get('carts'):
            carts =  request.session.get('carts')
            new_buy_product = {
                       'name': buy_car.name,
                       'title': buy_car.title,
                       'price': buy_car.price,
                       'quantity': buy_car.quantity,
                       'image': buy_car.image.url,
                       'description': buy_car.description,
                       'brand': buy_car.brand.brand_name
                  }
            carts.append(new_buy_product)
            request.session['carts'] = carts

        else:
             carts = [
                  {
                       'name': buy_car.name,
                       'title': buy_car.title,
                       'price': buy_car.price,
                       'quantity': buy_car.quantity,
                       'image': buy_car.image.url,
                       'description': buy_car.description,
                       'brand': buy_car.brand.brand_name
                  }
             ]
             request.session['carts'] = carts
            
        return redirect('user_profile')