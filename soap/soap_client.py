from zeep import Client

client = Client(wsdl = 'http://www.dneonline.com/calculator.asmx?wsdl')
print(client.service.Add(5,5))


# from zeep import Client
# from zeep.transports import Transport
# from requests import Session
# from requests.auth import HTTPBasicAuth
# wsdl = <wsdl_url>
# session = Session()
# session.auth = HTTPBasicAuth(<username>, <password>)

# client=Client(wsdl,transport=Transport(session=session))

# request_data={'SAPUsername' : SAP_username ,
#               'SAPPassword' : SAP_password}

# response=client.service.xxxxxxx(**request_data)