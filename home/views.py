from django.http import HttpResponse
from django.shortcuts import render
from activity.models import Category, activity
from home.models import message, comment


# Create your views here.
def index(request):
    deger = 0
    a = activity.objects.all()
    for i in a:
        deger += 100
    data = {
        "activity": activity.objects.all(),
        "deger": deger
    }

    return render(request, 'index.html', data)


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


def about(request):
    return render(request, 'about.html')


def teacher(request):
    return render(request, 'teacher.html')


def courses(request):
    return render(request, 'courses.html')


def blog(request):
    return render(request, 'blog.html')


def blog_single(request):
    if request.method == "POST":
        c = comment()
        c.name = request.POST["name"]
        c.email = request.POST["email"]
        c.title = request.POST["title"]
        c.comment = request.POST["comment"]
        c.save()
        return render(request, 'blog-single.html')
    else:
        return render(request, 'blog-single.html')