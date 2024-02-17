from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from django.http import HttpResponse


# Create your views here.

@api_view(['POST'])
def upload_image(request):
    print(request.data)
    print(request.FILES)
    print(request.POST)
    # if request.method == 'POST' and request.FILES.get('image'):
    #     uploaded_image = request.FILES['image']
    #     fs = FileSystemStorage()
    #     filename = fs.save(uploaded_image.name, uploaded_image)
    #     image_url = fs.url(filename)  # URL to access the saved image
    #     return render(request, 'image_upload_success.html', {'image_url': image_url})
    # return render(request, 'image_upload_form.html')
    return HttpResponse("HELLO WORLD!")