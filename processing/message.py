import requests

def send_message(msg):
    token   = "6a6721e8785ce736651da2e9146515d8"
    account = "ACe54aaa99ade5b73c877fa88c750c3cbd"
    url     = "https://api.twilio.com/2010-04-01/Accounts/ACe54aaa99ade5b73c877fa88c750c3cbd/Messages"
    
    data = {
        "Body": msg,
        "From": "4158872366",
        "To": "4153686487"
    }
    return
    #resp = requests.post(url, data=data, auth=(account, token))

