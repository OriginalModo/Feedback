from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import *
from .models import *


from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})


# # Переменная для шаблона по дефолту будет form
# class FeedbackView(FormView):
#     form_class = FeedbackForm
#     template_name = 'feedback/feedback.html'
#     success_url = '/done'
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)

# Для создания записей в БД через Форму

# Переменная для шаблона html по дефолту будет  form
class FeedbackView(CreateView):
    model = Feedback
    # form_class = FeedbackForm
    fields = '__all__'
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedbackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

class FeedbackViewDelete(DeleteView):
    model = Feedback
    success_url = reverse_lazy('/list')
    template_name = 'feedback/feedback_delete.html'


def index(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Sasya A.S.'
        context['date'] = '28.07.2024'
        return context


# def done(request):
#     return render(request, 'feedback/done.html', context={'got_error': False})


# class ListFeedback(TemplateView):
#     template_name = 'feedback/feedback_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedbacks = Feedback.objects.all()
#         context['feedbacks'] = feedbacks
#         return context

# class DetailFeedback(TemplateView):
#     template_name = 'feedback/feedback_detail.html'
#
#     def get_context_data(self, **kwargs):
#         id_feedback = kwargs['id_feedback']
#         context = super().get_context_data(**kwargs)
#         feedback = Feedback.objects.get(id=id_feedback)
#         context['feedback'] = feedback
#         return context


# from django.views.generic import TemplateView, ListView, DetailView
# Django Находить одну запись и сохраняет её по модели в нижнем регистре
class DetailFeedback(DetailView):
    template_name = 'feedback/feedback_detail.html'  # По дефолту будет шаблон   имя приложения / имя модели_detail.html
    model = Feedback  # Переписывает для шаблона html в нижний регистр feedback
    context_object_name = 'fee'  # По дефолту будет переменная object



class ListFeedback(ListView):
    template_name = 'feedback/feedback_list.html'  # По дефолту будет шаблон      имя приложения / имя модели_list.html
    model = Feedback
    context_object_name = 'feedbacks'  # По дефолту будет переменная object_list

    # Фильтрация записей
    def get_queryset(self):
        qs = super().get_queryset()
        filter_qs = qs.filter(rating__gt=2)
        return filter_qs


def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect(f'/{id_feedback}')
    else:
        form = FeedbackForm(instance=feed)
    return render(request, 'feedback/feedback.html', context={'form': form})

















