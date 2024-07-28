from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import *
from django.views import View
from .forms import *
from django.views.generic import CreateView, ListView

class ListGallery(ListView):
    model = Gallery
    template_name = 'gallery/gallery_list.html'

class CreateGalleryView(CreateView):
    model = Gallery
    template_name = 'gallery/load_file.html'
    fields = '__all__'
    success_url = 'load_image'


# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm()
#         return render(request, 'gallery/load_file.html', context={'form': form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             new_image = Gallery(image=form.cleaned_data['image'])
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/load_file.html', context={'form': form})

