from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

from .forms import ContactForm


def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print('form is valid')
            subject = f'Message form {form.cleaned_data["topic"]}'
            message = form.cleaned_data["message"]
            contact_email = form.cleaned_data["contact_email"]
            sender = ["loken070707@gmail.com"]
            recipients = ['mateusz.gralak1@wp.pl']
            try:
                send_mail(subject, "Message: {},\n\n Contact:{}".format(message, contact_email), sender, recipients,
                          fail_silently=True)
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return HttpResponse("Email sended")
    return render(request, 'user_contact/contact.html', {'form': form})
