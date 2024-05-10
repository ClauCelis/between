from django.shortcuts import render
from .models import Personal_Style, Components,BigTraditions
from django.views.generic import ListView, DetailView,TemplateView,CreateView
from .forms import StyleForm,ComponentsForm,BigTradForm
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .content import Content
# Create your views here.

#Start classes with caps
class index_View(TemplateView):
    template_name = 'between_app/index.html'

class takeTestView(CreateView):
    model = Personal_Style
    form_class = StyleForm
    template_name = 'between_app/profile_test.html'
    success_url = 'between_app/results/'

    def post(self, request, *args, **kwargs):
        form = StyleForm(request.POST)
        try:
            user = get_user_model().objects.get(pk=request.user.id)
        except:
            try:
                user = get_user_model().objects.get(username='guest')
            except:
                user = get_user_model().objects.create_user(email='guest@guest.guest',username='guest' )
        if form.is_valid():
            profile_test = form.save(commit=False)
            profile_test.user = user
            profile_test.save()
            return HttpResponseRedirect(reverse_lazy('between_app:results', args=[profile_test.pk]))
        return render(request, 'between_app/profile_test.html', {'form': form})

class resultsList(LoginRequiredMixin, ListView):
    model = Personal_Style
    context_object_name = 'style_list'
    template_name = 'personalstyle_list'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(user=self.request.user.id)

class formDetailView(DetailView):
    model = Personal_Style
    context_object_name ='style_detail'
    template_name = "personal_style_detail.html"


class resultsView(DetailView):
    model = Personal_Style
    template_name = 'between_app/results.html'
    context_object_name = 'style_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        position = Content.position
        path = Content.path
        tradition = Content.tradition
        context["content"] = {'position':position,'path':path,'tradition':tradition}
        return context


class contentView(TemplateView):
    template_name = 'between_app/content.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        position = Content.position
        path = Content.path
        tradition = Content.tradition
        context["content"] = {'position':position,'path':path,'tradition':tradition}
        return context

    
#Components Views

class takeComponentstView(CreateView):
    model = Components
    form_class = ComponentsForm
    template_name = 'between_app/Components/components_test.html'
    success_url = 'between_app/results/'

    def post(self, request, *args, **kwargs):
        form = StyleForm(request.POST)
        try:
            user = get_user_model().objects.get(pk=request.user.id)
        except NameError:
                user = get_user_model().objects.get(username='guest')
        except:
                user = get_user_model().objects.create_user(email='guest@guest.guest',username='guest' )
        if form.is_valid():
            profile_test = form.save(commit=False)
            profile_test.user = user
            profile_test.save()
            return HttpResponseRedirect(reverse_lazy('between_app:index'))
        return render(request, 'between_app/Components/components_test.html', {'form': form})
    

#Big traditions Views
class takeTraditionsView(CreateView):
    model = BigTraditions
    form_class = BigTradForm
    template_name = 'between_app/BitTraditions/traditions_test.html'
    success_url = 'between_app/results/'

    def post(self, request, *args, **kwargs):
        form = StyleForm(request.POST)
        try:
            user = get_user_model().objects.get(pk=request.user.id)
        except NameError:
            user = get_user_model().objects.get(username='guest')
        except:
            user = get_user_model().objects.create_user(email='guest@guest.guest',username='guest' )
        if form.is_valid():
            profile_test = form.save(commit=False)
            profile_test.user = user
            profile_test.save()
            return HttpResponseRedirect(reverse_lazy('between_app:index'))
        return render(request, 'between_app/BitTraditions/traditions_test.html', {'form': form})
    