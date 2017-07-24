from processing.models import TrashCan
import os
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

TRASH_URL = "https://pilotserver.ddns.net/piwebapi/elements/"  # + webID

# (os.environ['user'], os.environ['pass'])
auth = ("PIVisionService", "PilotSwag_6")
HEADERS = {'Content-Type': 'application/json', "X-Requested-With": "XML"}
DEBUG = True


def setValue(webid, val):
    """ modifies the value of the stream
    """
    url = "https://pilotserver.ddns.net/piwebapi/streams/" + webid + "/value"
    # update the fill level with a random value
    data = {
        "Value": val
    }
    response = requests.post(
        url=url,
        verify=False,
        auth=auth,
        headers=HEADERS,
        json=data)
    return response.status_code


def getWebId(url, attr):
    """ Get the webId of the attribute url
    """
    response = requests.get(
        url=url,
        verify=False,
        auth=auth,
        headers=HEADERS)

    attr_id = ""

    items = dict(response.json())["Items"]

    for item in items:
        temp = item["Name"]
        if temp == attr:
            attr_id = item["WebId"]

    return attr_id


def format_date(date):
    date_str = "{}/{}/{} {}:{}:{} AM".format(
        date.month, date.day, date.year, date.hour, date.minute, date.second)
    return date_str


def update_trashcan(trashcan):
    curr_url = TRASH_URL + trashcan.webID + "/attributes"

    data = {
        "BN": 			trashcan.bn,
        "BT": 			trashcan.bt,
        "Version": 		trashcan.v,
        "LastEmptied":	format_date(trashcan.lastEmptied),
        "LastUpdated":  format_date(trashcan.lastUpdated),
        "FillLevel":	float(trashcan.fillLevel),
        "Sensor1":      float(trashcan.sensor1),
        "Sensor2":		float(trashcan.sensor2),
        "Sensor3":		float(trashcan.sensor3),
        "FillStatus":	trashcan.fillStatus,
        "Info":			trashcan.info,
        "MessageID":	trashcan.messageID,
        "Percent":		float(trashcan.percent),
        "Status":		trashcan.status
    }

    for attr in data:
        print(attr, end="     ")
        r = setValue(getWebId(curr_url, attr), data[attr])
        print("Done")


def update_trashcans():

    trashcans = TrashCan.objects.all()

    for trashcan in trashcans:
        curr_url = TRASH_URL + trashcan.webID + "/attributes"

        data = {
            "BN": 			trashcan.bn,
            "BT": 			trashcan.bt,
            "Version": 		trashcan.v,
            "LastEmptied":	format_date(trashcan.lastEmptied),
            "LastUpdated":  format_date(trashcan.lastUpdated),
            "FillLevel":	float(trashcan.fillLevel),
            "Sensor1":      float(trashcan.sensor1),
            "Sensor2":		float(trashcan.sensor2),
            "Sensor3":		float(trashcan.sensor3),
            "FillStatus":	bool(trashcan.fillStatus),
            "Info":			trashcan.info,
            "MessageID":	trashcan.messageID,
            "Percent":		float(trashcan.percent),
            "Status":		bool(trashcan.status)
        }

        for attr in data:
            r = setValue(getWebId(curr_url, attr), data[attr])


if __name__ == "__main__":
    update_trashcans()
