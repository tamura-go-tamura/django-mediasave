from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .models import FILENAME
#パスワード生成
import string
import secrets
from upload import settings

# Create your views here.
@csrf_exempt
def get_img(request):
    
    if request.method == "POST":
        # ← 受け取ったPOST画像データを保存
        if request.FILES["image_file"].name == "reset_data.jpeg":
            ret = {"url": "全データ削除完了","pwd": settings.MEDIA_URL}
            # JSONに変換して戻す
            return JsonResponse(ret)
        else:
            pwd = pass_gen()
            res, file_name = save(request.FILES["image_file"], pwd)
            res = request.build_absolute_uri(res)
            print(res)
            #データベースに保存
            new_data = FILENAME(file_name = file_name, pwd = pwd)
            new_data.save()
    
    else:  # ← methodが'POST'ではない = 最初のページ表示時の処理
        return render(request, "howto.html")

    ret = {"url": res,"pwd": pwd}

    # JSONに変換して戻す
    return JsonResponse(ret)

def save(data,pwd):
        file_name = default_storage.save(pwd + data.name, data)
        return default_storage.url(file_name), data.name

def pass_gen(size=12):
   chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
   # 記号を含める場合
   # chars += '%&$#()'

   return ''.join(secrets.choice(chars) for x in range(size))