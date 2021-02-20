from django.shortcuts import render
from .forms import EmailHistoryForm
from .models import EmailHistory


def send_email(request):
    form = EmailHistoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        model: EmailHistory = form.save()
        print('send email : {}'.format(model.send_to))
        context = {'email': model.send_to}
        return render(request, 'sender/complete.html', context=context)
    context = {'form': form}
    return render(request, 'sender/index.html', context)

