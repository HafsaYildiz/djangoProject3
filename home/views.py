from django.http import HttpResponse
from django.shortcuts import render
from activity.models import Category, activity
# Create your views here.
def index(request):
    category = Category.objects.all()
    text = "Merhaba Dunya"
    context = {'text2': text,
             'category': category}
    return render(request, 'index.html',  context)
def category_activitys(request, id, slug):
    category = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    Activity = activity.objects.filter(category_id=id)
    context = {'selectedCategory': selectedCategory,
               'activity': Activity,
               'categoryDataAll': category}
    return render(request, 'category_activitys.html', context)
