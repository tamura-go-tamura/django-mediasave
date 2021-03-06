from django.shortcuts import render, redirect
from post.models import FILENAME

from django.contrib import messages
from django.db.models import Q


# Create your views here.
def index(request):
    files = None
    keyword = request.GET.get('keyword')
    if keyword:
        files = FILENAME.objects.all()
        files = files.filter(
                 Q(file_name__icontains=keyword)
               )
        messages.success(request, '「{}」の検索結果'.format(keyword))
    return render(request, 'index.html', {'files': files, 'admin': False  })

def auth(request):
    pic = request.GET.get('pic')
    messages.success(request, '「{}」のパスワードを入力'.format(pic))
    return render(request, 'picAuth.html', {'picture': pic })

def show(request):
    try:
        pwd = request.POST["pwd"]
        pic = request.POST["pic"]
    except:
        pwd = None
        return redirect(request.build_absolute_uri()[:-6])

    if pic == "admin" and pwd == "adminPassword":
        messages.error(request, '全ての画像を表示します')
        files = FILENAME.objects.all()
        return render(request, 'index.html', {'files': files, 'admin': True })

    try:
        selected_file = FILENAME.objects.get(pwd = pwd)
        if pic == selected_file.file_name:
            return redirect(request.build_absolute_uri()[:-6] + '/media/' + pwd + selected_file.file_name)
        else:
            messages.error(request, 'パスワードが間違っています')
            files = None
            return render(request, 'index.html', {'files': files, 'admin': False })
    except:
        messages.error(request, 'パスワードが間違っています')
        files = None
        return render(request, 'index.html', {'files': files, 'admin': False  })
        