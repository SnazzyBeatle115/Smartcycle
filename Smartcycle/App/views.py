from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.core.files.storage import default_storage
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# TEST: create the img upload form page
def handler(request):
    html_file = open("./Smartcycle/App/test.html", "r")
    return HttpResponse(html_file.read())

# handle the form submission of img
@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['img']
        image_name = default_storage.save(image.name, image)
        image_url = default_storage.url(image_name)
        return HttpResponse("Upload Success")
    return HttpResponse('This is GET, not POST')