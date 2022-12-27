from django.contrib import messages
from django.contrib.auth.decorators import login_required
from activity.models import Comment, CommentForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# create your views here.
def index(request):
    return HttpResponse("merhaba alt uygulama")
@login_required(login_url='/login')
def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST': #form post edildiyse
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user =request.user
            data = Comment()
            data.user_id = current_user.id
            data.activity_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "yorumunuz basariyla gonderilmistir")
            return HttpResponseRedirect(url)
           #return HttpResponse("kayit islemi basarili")
        messages.error(request, "kaydedilme islemi gerceklestirilemedi")
        return HttpResponseRedirect(url)
        #return HttpResponse("kaydedilme islemi gerceklestirilemedi")