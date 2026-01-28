from django.shortcuts import render



# Create your views here.
def ip_view(request):
    
    return render(request, "fisier_randat.html", context= {
        "ip" : "3812798312798371"
    })