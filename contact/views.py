from django.core.mail import send_mail, BadHeaderError

from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import render, redirect

from django.template.loader import render_to_string

from .forms import ContactForm

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			from_email = form.cleaned_data['from_email']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']

			html = render_to_string('contact/emails/contact_form.html', {
				'name':name,
				'from_email':from_email,
				'subject':subject,
				'message':message
			})

			try:
				send_mail(subject, message, from_email, ['christian.delmor@gmail.com'], html_message=html)
			except BadHeaderError:
				return HttpResponse('Invalid Header Found!')
			return redirect('success')
	form = ContactForm()
	context = {'form':form,}
	return render(request, 'contact/contact.html', context)

def success(request):
	return render(request, 'contact/success.html')