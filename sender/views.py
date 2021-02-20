from django.http import HttpResponse
from django.shortcuts import render
from .forms import EmailHistoryForm
from .models import EmailHistory
from PIL import Image
from hashlib import md5


def send_email(request):
    form = EmailHistoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        model: EmailHistory = form.save()
        print('send email : {}'.format(model.send_to))
        sid = create_secret_key(model)
        link = create_image_link(request, sid, model.pk)
        context = {'email': model.send_to, 'link': link}
        return render(request, 'sender/complete.html', context=context)
    context = {'form': form}
    return render(request, 'sender/index.html', context)


def add_opened_email_history(request):
    response = HttpResponse(content_type='image/png')
    empty_image = Image.new('RGBA', (1, 1))
    empty_image.save(response, 'png')
    response['Content-Disposition'] = 'attachment; filename="footer.png"'

    if "sid" not in request.GET or "eid" not in request.GET:
        return response

    eid = request.GET["eid"]
    histories = EmailHistory.objects.filter(id=eid)
    if len(histories) != 1:
        return response
    history: EmailHistory = histories[0]
    sid = request.GET["sid"]
    if create_secret_key(history) == sid:
        history.is_opened = True
        history.save()
    return response


def create_secret_key(model: EmailHistory):
    salt = "{}-{}".format(model.pk, model.created_at)
    return md5(salt.encode('utf-8')).hexdigest()


def create_image_link(request, sid, eid):
    return "{}/image/?sid={}&eid={}".format(request._current_scheme_host, sid, eid)

