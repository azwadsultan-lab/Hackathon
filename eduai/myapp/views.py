from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def subject_detail_view(request):
    return render(request, 'subject_detail.html')

# ADD THIS NEW FUNCTION:
def ask_view(request):
    # This grabs the subject from the URL. If someone just types /ask/, it defaults to compsci.
    selected_subject = request.GET.get('subject', 'compsci') 
    
    # We pass that subject into the HTML template so it knows what to display!
    return render(request, 'ask.html', {'subject': selected_subject})
def verify_view(request):
    return render(request, 'verify.html')
def profile_view(request):
    return render(request, 'profile.html')
def resources_view(request):
    return render(request, 'resources.html')