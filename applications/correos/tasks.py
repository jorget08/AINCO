from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_task(subject, message, de, para, passw, html_email):
    send_mail(               
            subject=subject,
            message=message,
            from_email=de,
            recipient_list=[para],
            auth_user=de,
            auth_password=passw,
            html_message=html_email,
    )
    return "Se ha enviado el email"