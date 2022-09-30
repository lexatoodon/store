from celery import shared_task
from django.core.mail import send_mail
from .models import Order
from django.template.loader import render_to_string
from datetime import date, timedelta

@shared_task
def daily_report():
    time_period = date.today() - timedelta(days=7)
    orders = Order.objects.filter(created__gte = time_period).prefetch_related('items')
    subject = f'Daily Report for the last week from {time_period} to {date.today()}'
    context = {
        'orders': orders
    }
    message = render_to_string('emails/weekly_report.html', context)
    mail_sent = send_mail(subject, message, 'lexa@gmail.com', ['admin@gmail.com'])
    return mail_sent

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    context = {
        'name': order.first_name,
        'id': order.id
    }
    message = render_to_string('emails/order_receipt.html', context)
    mail_sent = send_mail(subject, message, 'lexa@gmail.com', [order.email])
    return mail_sent