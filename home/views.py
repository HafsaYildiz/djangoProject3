from django.http import HttpResponse
from django.shortcuts import render
from activity.models import Category, activity
from home.models import message


# Create your views here.
def index(request):
    category = Category.objects.all()
    text = "Merhaba Dunya"
    context = {'text2': text,
               'category': category}
    return render(request, 'index.html', context)


def category_activitys(request, id, slug):
    category = Category.objects.all()
    selectedCategory = Category.objects.filter(pk=id)
    Activity = activity.objects.filter(category_id=id)
    context = {'selectedCategory': selectedCategory,
               'activity': Activity,
               'categoryDataAll': category}
    return render(request, 'category_activitys.html', context)

def contact(request):
    if request.method == "POST":
        m = message()
        m.name = request.POST["name"]
        m.email = request.POST["email"]
        m.title = request.POST["title"]
        m.message = request.POST["message"]
        m.save()
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')



def activity_detail(request, id, slug):
    category = Category.objects.all()
    context = {'category': category}
    return render(request, 'activity_detail.html', context)

    return None


def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def teacher(request):
    return render(request, 'teacher.html')
def courses(request):
    return render(request, 'courses.html')
def blog(request):
    return render(request, 'blog.html')
def blog_single(request):
    return render(request, 'blog-single.html')