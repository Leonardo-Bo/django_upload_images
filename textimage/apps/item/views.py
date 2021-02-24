from django.shortcuts import render
from django.urls.base import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import ImageModel, TextModel
from .forms import CreateItemForm, UpdateItemForm
from django.contrib import messages


class HomeView(ListView):
    model = TextModel
    context_object_name = 'items'
    template_name = 'home.html'


class CreateItemView(CreateView):
    model = TextModel
    form_class = CreateItemForm
    template_name = "create_item.html"

    def get_success_url(self, *args, **kwargs):
        messages.success(self.request, 'Item created successfully')
        return reverse('edit_item', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        title = self.request.POST['title']
        if TextModel.objects.filter(title=title).exists():
            messages.error(self.request, 'Ops... Item title already exists')
        else:
            messages.error(self.request, 'Ops... Something went wrong')
        return super().form_invalid(form)


class UpdateItemView(UpdateView):
    model = TextModel
    template_name = "edit_item.html"
    form_class = UpdateItemForm

    def get_success_url(self, *args, **kwargs):
        if 'upload_images' in self.request.POST:
            url = reverse('edit_item', kwargs={'pk': self.object.pk})
        else:
            messages.success(self.request, 'Item modified successfully')
            url = reverse('detail_item', kwargs={'pk': self.object.pk})
        return url

    def form_valid(self, form):
        item_n = form.save()
        images = self.request.FILES.getlist("images")

        for i in images:
            ImageModel.objects.create(reftext=item_n, image=i)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Ops... Something went wrong')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_pk = self.kwargs['pk']
        item_images = TextModel.objects.get(pk=url_pk)       
        context['item_images'] = item_images
        return context


class DetailItemView(DetailView):
    model = TextModel
    context_object_name = 'item'
    template_name = 'detail_item.html'


class DeleteImageView(DeleteView):
    model = ImageModel

    def get_success_url(self, **kwargs):
        return reverse_lazy('edit_item', kwargs={'pk': self.object.reftext_id})

    def delete(self, request, *args, **kwargs):
        self.reftext_pk = self.get_object().reftext.pk
        return super(DeleteImageView, self).delete(request, *args, **kwargs)


class DeleteItemView(DeleteView):
    model = TextModel
    template_name = 'detail_item.html'
    success_url = reverse_lazy('home')
    success_message = 'Item removed successfully'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteItemView, self).delete(request, *args, **kwargs)