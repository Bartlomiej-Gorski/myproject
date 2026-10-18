from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'hobby/home.html')
# def hobby_view(request):
#     return render(request, 'hobby/base.html')
def about_view(request):
    return render(request, 'hobby/about.html')

def gallery_view(request):
    return render(request, 'hobby/gallery.html')