from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

# Create your views here.
def index(request):
    if request.method == 'POST':
        sndr_name = request.POST["name"]
        usr_email = request.POST["email"]
        sub = request.POST.get('subject', '')
        msg = request.POST["message"]
        send_mail(
            sub,  # subject
            'Name : {}\nEmail : {}\nMessage : {}'.format(sndr_name, usr_email, msg),  # message
            usr_email,  # Sender email
            ['mayankdastesting@gmail.com'],   # reciever email
            fail_silently=False,
        )
        print(sndr_name, '\n', usr_email, '\n', sub, '\n', msg)
        return render(request, "index.html", {"success_msg":"Your message sent successfully"})
    else:
        return render(request, "index.html")
    

def gui(request):
    return render(request, "portfolio-details-gui.html")

def web(request):
    return render(request, "portfolio-details-web.html")

def card(request):
    return render(request, "portfolio-details-card.html")
