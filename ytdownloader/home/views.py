from django.shortcuts import render, redirect
from pytube import *



def youtube(request):
    if request.method == 'POST':
        try:
            link = request.POST['link']
            video = YouTube(link)
            stream = video.streams.get_lowest_resolution()
            stream.download('C:\\Users\\lenovo\\Downloads')
            return render(request, 'home.html',{'msg':'video downloaded'})
        except:
                return render(request, 'home.html', {'msg':'Video not downloaded or wrong url'})
        
    return render(request, 'home.html')
