from flask import Flask, request
import uuid
import datetime
application = Flask(__name__)

# Data
incidents = {}


# functions
def addIncident(incident):
    incidentID = str(uuid.uuid4())
    incident['version'] = 1
    incident['timestamp'] =  datetime.datetime.now()
    incidentDictionary = {incidentID: incident}
    incidents.update(incidentDictionary)

def getIncidents():
    return incidents, 200

def incidentInfo(incident):
    if incident in incidents:
        return incidents.get(incident)
    else: 
        return "ID not found", 500

def incidentDelete(incident):
    if incident in incidents:
        del incidents[incident]
        return "Deleted id: " + incident
    else:
        return "Could not delete. ID not found"

def incidentPut(incident, incidentID):
    global incidents
    if incident in incidents:
        incidentID['version'] = 1
        incidentID['timestamp'] =  datetime.datetime.now()
        incidentDictionary = {incident: incidentID}
        incidents.update(incidentDictionary)
        return "Updated id: " + incident
    else:
        return ("Could not delete. ID not found", 201)
        

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/incidents", methods=['GET', 'POST'])
def incident():
    if request.method == "GET":
        return getIncidents()
    elif request.method == "POST":
        addIncident(request.json)
        return("OK", 201)

@application.route('/incidents/incident/<incidentId>', methods=['GET', 'PUT', 'DELETE'])
def specificIncident(incidentId):
    if request.method == "GET":
        return incidentInfo(incidentId)
    elif request.method == "DELETE":
        return incidentDelete(incidentId)
    elif request.method == "PUT":
        return incidentPut(incidentId, request.json)

if __name__ == "__main__":
    application.run()