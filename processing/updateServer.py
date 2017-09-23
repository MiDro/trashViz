# updateServer.py
# ewhitsett@hmc.edu + hfang@hmc.edu 8 June 2017

# This script updates elements on the PI server
# with values from Paraodox's Content Management System

# coding: utf-8

import time
import datetime
import requests
import random
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from processing.models import TrashCan
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# basic content
BASE = "https://pilotserver.ddns.net/piwebapi"  # base repo for the web api
ELEMENT_URL = BASE + "/assetdatabases/D0dbHcahUs40KO5-Vmpl39zA8Nq5cL4I20m09GmygPkqxQV0lOLThCSU9BSlYwSEJEXFRSQVNIQ0FOU1RFU1Q/elements"
HEADERS = {'Content-Type': 'application/json', "X-Requested-With": "XML"}


def getElements():
    """ retrieve all TrashCan elements
    """
    ids = []
    response = requests.get(
        url=ELEMENT_URL,
        verify=False,
        auth=(
            "PIVisionService",
            "PilotSwag_6"),
        headers=HEADERS)

    print("Getting Elements...")
    items = dict(response.json())["Items"]
    for item in items:
        temp = item["WebId"]
        ids.append(temp)

    print("Got webIDs...")
    return ids


def attrurl(webid):
    """ returns the attribute URL
    """
    return "https://192.168.1.107/piwebapi/elements/" + webid + "/attributes"

def formatnum(num):
    if num <= 9:
        return "0" + str(num)
    return str(num)

def getWebId(url):
    """ Get the webId of the attribute url
    """
    response = requests.get(
        url=url,
        verify=False,
        auth=(
            "PIVisionServuce",
            "PilotSwag_6"),
        headers=HEADERS)

    ids = []

    items = dict(response.json())["Items"]
    for item in items:
        temp = item["Name"]
        if temp == "FillLevel":
            ids.append(item["WebId"])

    return ids[0]


def setValue(webid):
    """ modifies the value of the stream
    """
    url = BASE + "/streams/" + webid + "/value"
    # update the fill level with a random value
    data = {
        "Value": float(random.randint(0, 100))
    }
    response = requests.post(
        url=url,
        verify=False,
        auth=(
            "PIVisionServuce",
            "PilotSwag_6"),
        headers=HEADERS,
        json=data)
    return response.status_code


def updateAll():
    """  update all trash cans with random values
    """
    ids = []

    # retrieve all the trash elements IDs
    elements  = getElements()

    trashcans = TrashCan.objects.all()

    curr = 1

    # retrieve all the web Ids for each element
    for element in elements:
        name    = "TrashCan"+formatnum(curr)
        currCan = TrashCan.objects.get(name=name)
        currCan.webID = element
        currCan.save()
        curr += 1
    #     ids.append(getWebId(attrurl(element)))

    # for each in ids:
    #     print(each)
    """
    # update each fill level accordingly
    for each in ids:
        val = setValue(each)
        if not (200 <= val < 300):
            print("error")
    """

if __name__ == "__main__":
    updateAll()