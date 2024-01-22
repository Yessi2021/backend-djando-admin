from typing import List

from django.core.mail import send_mail

from .build_template import build_html_for_mail


def send_mail_to(asunto: str, content: str, to_list: List[str], fail_silently: bool = True):
    message_content = build_html_for_mail(asunto, content)
    send_mail(asunto, "", "admin@bi360.com.co", to_list, fail_silently=fail_silently, html_message=message_content)
