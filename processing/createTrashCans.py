t
# removeAll.py
# ewhitsett@hmc.edu + hfang@hmc.edu 8 June 2017

# This script removes all elements from the PI Server
# and it removes all PI Points as well

# coding: utf-8

import requests

# Silence warning from not having a SSL certificate. Don't worry,
# it's our server.
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Endpoints for to access points and trashcans
point_url = "https://pilotserver.ddns.net/piwebapi/dataservers/s0_WTkn63TY0yI0MwBHyvDTwV0lOLThCSU9BSlYwSEJE/points"
trash_url = "https://pilotserver.ddns.net/piwebapi/assetdatabases/D0dbHcahUs40KO5-Vmpl39zA8Nq5cL4I20m09GmygPkqxQV0lOLThCSU9BSlYwSEJEXFRSQVNIQ0FOU1RFU1Q/elements"

# Username. Password
creds = ("PIVisionService", "PilotSwag_6")
PI_POINTS = {"BT": "Int32", "FillLevel": "Float64", "LastEmptied": "Timestamp",
             "MaxFill": "Float64", "Percent": "Float64", "Status": "Digital",
             "FillStatus":"Digital", "Info":"String","LastEmptied":"Timestamp",
             "LastUpdated":"Timestamp","Percent":"Float64", "Sensor1":"Float64",
             "Sensor2":"Float64","Sensor3":"Float64", "Version":"Int32"}

# Headers required to interact with server. X-Requested-With prevents the
# server from thinking we are attempting a CSRF attack. We're not
headers = {'Content-Type': 'application/json', "X-Requested-With": "XML"}

# Makes making a request a little easier as headers, creds, and verify
# never change.
def makeRequest(retype, url, data):
    if retype == "get":
        return requests.get(url, verify=False, auth=creds, headers=headers)
    return requests.post(
        url,
        verify=False,
        auth=creds,
        headers=headers,
        json=data)

# Format Trashcan Number we're adding. want a two digit number 09, 19, etc
def formatnum(num):
    if num <= 9:
        return "0" + str(num)
    return str(num)


# Basic point. Change name and pointtype to be what we want.
point_default = {
    #"Name": "TrashCan##.<POINT_NAME>,
    "Descriptor": "Default Point",
    "PointClass": "classic",
    #"PointType": PI_POINT[<POINT_NAME>],
    "EngineeringUnits": "",
    "Step": False,
    "Future": False
}

# Makes the required PI Points given a number.
def makePoints(num):
    for pt in PI_POINTS:
        # Updates the Pi Point to match this trash can and makes request
        # If we don't get the right status code, print which point fails
        point_default["Name"] = "TrashCan" + formatnum(num) + "." + pt
        point_default["PointType"] = PI_POINTS[pt]
        response = makeRequest("post", point_url, point_default)


data = {
    #"Name": "TrashCan##",
    "Description": "Data representation of trashcan",
    "TemplateName": "TrashCanTemplate"
}


def makeTrash(num):
    # Make PI Points
    makePoints(num)
    data["Name"] = "TrashCan" + formatnum(num)
    makeRequest("post", trash_url, data)


def main(cans):
    for i in range(1, cans):
        makeTrash(i)


if __name__ == "__main__":
    main(40)
