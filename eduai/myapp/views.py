from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def subject_detail_view(request):
    return render(request, 'subject_detail.html')

# ADD THIS NEW FUNCTION:
def ask_view(request):
    return render(request, 'ask.html')