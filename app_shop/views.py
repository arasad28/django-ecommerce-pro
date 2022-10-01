# from audioop import reverse
import django
from django.urls import reverse,reverse_lazy
from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import ListView,DetailView,UpdateView,CreateView
from app_order.models import Comment
from .models import Product,Slider
from .forms import CommentForm,ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


#import models
from app_shop.models import Product
# Create your views here.
class Home(ListView):
    model = Product
    template_name = 'app_shop/index.html'
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slider'] = Slider.objects.filter(slide=True)
        context['deal'] = Product.objects.filter(q_deal=True)
        return context


def Post(request,pk):
    object = Product.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.prod = object
        comment.save()
        return HttpResponseRedirect(reverse('app_shop:product',kwargs={'pk':pk}))
    return render(request,'app_shop/product.html',context={'object':object,'comment':comment_form})

class Createview(CreateView,LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'app_shop/create.html'

    def form_valid(self,form):
        prod_obj = form.save(commit=False)
        prod_obj.author = self.request.user
        prod_obj.save()
        return HttpResponseRedirect(reverse('app_shop:home'))


class Updateview(UpdateView,LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = 'app_shop/edit.html'


    def get_success_url(self,**kwargs):
        print(self.object.pk)
        return reverse_lazy('app_shop:product',kwargs={'pk':self.object.pk})