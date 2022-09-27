from django.core.mail import EmailMultiAlternatives
import random
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def faculty_creation_mail(emailto, name):
    subject = 'OTP | Student Information Portal'
    to = emailto
    otp=random.randint(111111,999999)
    html_content = render_to_string('mail/faculty_creation_mail.html',{'otp_code':otp})
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(
        subject,
        text_content,
        settings.EMAIL_HOST_USER,
        [to]
    )
    email.attach_alternative(html_content,"text/html")
    email.send()
    return otp