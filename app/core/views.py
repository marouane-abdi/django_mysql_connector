from django.shortcuts import render ,  redirect
from .forms import SubmitForm

def landing_page(request):
    if request.method == 'POST':
        form = SubmitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')  # Replace 'success_page' with the appropriate URL
        else:
            print("Form errors:", form.errors)
    else:
        form = SubmitForm()
    
    context = {
        'form': form
    }

    return render(request, 'landing_page.html', context)
