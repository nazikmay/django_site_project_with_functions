from django.shortcuts import render,get_object_or_404, redirect

from .models import Category, Goods, Feedback
from .forms import GoodsForm
from django.urls import reverse_lazy




def goods_list(request):
    goods = Goods.objects.all()
    return render(request, 'goods_list.html', {'goods': goods})


def get_context_data(self, **kwargs):
        context  = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')

        if category:
            category_object = Category.objects.get(name=category)
            queryset = Goods.objects.filter(category=category_object)
        else:
            queryset = Goods.objects.all()

        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset

def goods_detail(request, pk):
    goods = get_object_or_404(Goods, pk=pk)
    feedback_list = Feedback.objects.filter(goods=goods)
    return render(request, 'goods_detail.html', {'goods':goods, 'feedback_list': feedback_list})

def goods_create(request):
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            goods = form.save()
            return redirect('goods_detail',pk=goods.pk)
    else:
        form = GoodsForm()
    return render(request, 'goods_create.html',{'form':form})

def goods_update(request,pk):
    goods = get_object_or_404(Goods, pk=pk)
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES, instance=goods)
        if form.is_valid():
            goods = form.save()
            return redirect('goods_detail', pk=goods.pk)
    else:
        form = GoodsForm(instance=goods)
    return render(request, 'goods_update', {"form":form, 'goods':goods})


def goods_delete(request, pk):
    goods = get_object_or_404(Goods, pk=pk)
    goods.delete()
    return redirect('goods_list')


