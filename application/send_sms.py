import africastalking
from django.conf import settings


africastalking.initialize(username=settings.AFRICASTALKING_USERNAME, api_key=settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_sms_alert(customer_phone, message):
    response = sms.send(message, [str(customer_phone)])
    return response
 