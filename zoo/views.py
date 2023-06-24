from django.shortcuts import render, get_object_or_404
from zoo.models import Category, Product
from django.views.generic import ListView
from django.core.paginator import Paginator
from zoo.forms import ZooSearchForm


   
class CategoryListView(ListView):
    model = Product
    template_name = 'catalog.html'
    context_object_name = 'products'
    
    paginate_by = 12
    
    
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['object-count'] = self.model.objects.count()
        paginator = Paginator(self.model.object_list, self.paginate_by)
        try:
            page = self.request.GET.get('page')
        except:
            page = 1
            
        try:
            context[self.context_object_name] = paginator.page(page)
        except:
            context[self.context_object_name] = paginator.page(1)
            
        context['object-count'] = self.model.objects.count()
        context['paginator'] = paginator
        return context
   
    def get_context_data(self,*,object_list=None, **kwargs):
         context = super().get_context_data(object_list=object_list, **kwargs)
         
         form = ZooSearchForm(self.request.GET)
         if form.is_valid():
             pass
         
         else:
             form = ZooSearchForm()
             
         context['form'] = form
         return context
         
    def get(self, request, *args, **kwargs):
        form = ZooSearchForm(self.request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            product = self.model.objects.filter(name__icontains=cd['search'])
        else:
            product = self.model.objects.all()
        return render(request, self.template_name, self.get_context_data(object_list=product))
    

   
class ZooView (ListView):
   model = Product
   context_object_name = 'product'
   template_name = 'main.html'
   
class Zoo2View (ListView):
   model = Category
   context_object_name = 'category'
   template_name = 'tov.html'
   
def uslygi_view(request):
    context = {'page':'uslygi'}
    return render(request, 'uslygi.html',context)


