from django.shortcuts import render, redirect
from .forms import IndiaModelForm
import requests
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ListenIN
import subprocess

def calling_listenIndia(request):
    video_model_id = request.session.get('video_model_id')
    print(video_model_id)
    if video_model_id:
        # Use the ID to retrieve the YourModel instance
        model_instance = ListenIN.objects.get(pk=video_model_id)
        print(model_instance)
    try:
        result = subprocess.run(r'python /home/ravish/Desktop/Listen_India/Listen_India.py /home/ravish/Desktop/Listen_India/ListenIndia/'+str(model_instance.video_file), shell=True, capture_output=True, text=True)
        print(result)
        print("Command output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Command failed with error:", e)

@csrf_exempt
def home(request):
    if request.method == 'POST':
        
        form = IndiaModelForm(request.POST, request.FILES)
        if form.is_valid():
            listen_in_instance = form.save(commit=False)
            title = form.cleaned_data['title']
            video_file = form.cleaned_data['video_file']
            language = form.cleaned_data['language']
            # Create a ListenIN model instance
            listen_in_instance = ListenIN.objects.create(title=title, video_file=video_file, language=language)
            print('here si the code',listen_in_instance.id)
            request.session['video_model_id'] = listen_in_instance.id
            calling_listenIndia(request)
            
            return render(request, 'base.html')
        else:
            form = IndiaModelForm()
    else:
            print("No file uploaded")
    return render(request, "base.html",{'form': form})
