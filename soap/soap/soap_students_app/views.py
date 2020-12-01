from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from spyne.application import Application
from spyne.decorator import rpc
from spyne.model.primitive import Unicode, Integer
from spyne.protocol.soap import Soap11
from spyne.server.django import DjangoApplication
from spyne.service import ServiceBase
from .models import Student


class SoapService(ServiceBase):
    @rpc(Integer(nillable=False), _returns=Unicode)
    def student_details(ctx, admission_no):
        return_value = "Student doesn't exist."
        try:
            student_info = Student.objects.get(admission=admission_no)
            return_value = 'Name: {}\nEmail: {}\nPhone Number: {}\nAddress: {}\nEntry points: {}\nRegistration Date: {}'.format(student_info.full_name, student_info.email, student_info.phone_number, student_info.address, student_info.entry_points, student_info.reg_date)
        except: 
            print("Doesn't work!")
        return return_value

soap_app = Application(
    [SoapService],
    tns='django.soap.example',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11(),
)

django_soap_application = DjangoApplication(soap_app)
my_soap_application = csrf_exempt(django_soap_application)
