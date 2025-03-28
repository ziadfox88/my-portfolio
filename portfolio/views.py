from django.shortcuts import render,redirect
from .models import Contact,myPersonalInfo
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

# def home(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             Contact.objects.create(
#                 name=form.cleaned_data['name'],
#                 email=form.cleaned_data['email'],
#                 phone_number=form.cleaned_data['phone_number'],
#                 another_phone=form.cleaned_data['another_phone'],
#                 description=form.cleaned_data['description']
#             )
#             messages.success(request, 'Thank you! Your message has been sent.')
#             return redirect('home')  # Redirect to the home page after success
#     else:
#         form = ContactForm()  # Create a new form for GET requests
#     return render(request, 'home.html', {'form': form})
def home(request):
    # Get the first myPersonalInfo object or None
    info = myPersonalInfo.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the Contact model
            try:
                # Send email with form data
                send_mail(
                    subject='New Contact Submission',
                    message=(
                        f'Name: {form.cleaned_data["name"]}\n'
                        f'Email: {form.cleaned_data["email"]}\n'
                        f'Phone: {form.cleaned_data["phone_number"]}\n'
                        f'Message: {form.cleaned_data["description"]}'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you! Your message has been sent.')
            except Exception as e:
                # Handle email sending errors
                messages.error(request, f'Failed to send message: {str(e)}')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'home.html', {'form': form, 'info': info})