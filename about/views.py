from django.shortcuts import render

# Create your views here.
def about_page(request):
    about_content = About.objects.first()  # Fetch the first entry in the About model
    return render(request, "about/about.html", {"about": about_content})