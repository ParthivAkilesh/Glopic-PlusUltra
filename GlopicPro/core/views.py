from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.http import HttpResponse
from PIL import Image
import os
from GlopicPro.core.paddleModel import PaddleModel
from django.conf import settings
from django.shortcuts import render



def index(request):
    return render(request, "core/index.html")


def glowit(request):
    if request.method == 'POST':
        file = request.FILES.get('ImgFile')
        if not file:
            return HttpResponse("error!")

        filename = file.name
        file_path = os.path.join(settings.MEDIA_ROOT, filename)
        with open(file_path, 'wb') as f:
            f.write(file.read())

        url_path = os.path.join("media/", filename)
        context = {'file_path': url_path}
        
        print("###################################")
        print(url_path)
        po = PaddleModel(url_path)
        po.saveRes()
        
        return HttpResponse("Success!")
        # return render(request, "core/result.html", context)


     

     