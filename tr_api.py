from testrail import *

api_key = "Yv.AzNCt2S/0v4Zu3..E-Jze1f8P0mMKRrei4dD8h"

# client = "https://testrail.dwos.com/"


client = APIClient('http://testrail.dwos.com/')
client.user = 'martin.carufel@dental-wings.com'
client.password = '18,Mac&Amo'

case = client.send_get('get_case/8433')
print(case)
