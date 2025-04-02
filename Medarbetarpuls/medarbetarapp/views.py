from django.shortcuts import render
import logging
import models

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Testing")
    logger.warning("Testing warning!")
    logger.error("Testing error!!!")

    return render(request, "index.html")

def create_acc_view(request):
    if request.method == 'POST':
        if request.headers.get('HX-Request'):
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            models.CustomUserManager(email,name,password)
            models.EmailList(email=email)

    return render(request, 'create_acc.html')

