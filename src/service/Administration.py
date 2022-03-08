import sys
import json
import jsonpickle

sys.path.append('..')
from model.Patient import Patient
from model.Patient import PatientPersonalDetail
from model.Patient import PatientMedicalDetail
from model.CovidFacility import CovidFacility

patients = {}
covidFacilities = list()

def loadPaitents():
    try:
        with open('data.json', 'r') as openfile:
            patientsObject = json.load(openfile)
    except FileNotFoundError:
        return

    if(patientsObject is None):
        return
    global patients
    patients = jsonpickle.decode(patientsObject)


def getPatients():
    global patients
    return patients


def getPatient(adhaarnumber):
    global patients
    return patients.get(adhaarnumber)


def addPatient(patient):
    global patients
    patients.update({patient.patientPersonalDetail.adhaarnumber : patient})

    serilaizedPatients = jsonpickle.encode(patients)
    patients_json_object = json.dumps(serilaizedPatients, indent=4)

    with open("data.json", "w") as outfile:
        outfile.write(patients_json_object)

    return {patient.patientPersonalDetail.adhaarnumber : patient}



def patientScreening(patientMedicalDetail):
    # bussiness logic for "mild"
    return "mild"


def patientReferring(selectedCovidFacilityID, patient):
    global covidFacilities
    for covidFacility in covidFacilities:
        if covidFacility.id == selectedCovidFacilityID:
            patient.referedCovidFacility = covidFacility
            updatedPatient = addPatient(patient)
            return True, updatedPatient
    return False, None


def patientCovidTest():
    return covidTestStatus


def getCovidFacilities():
    global covidFacilities
    return covidFacilities


def initialCovidFacilityData():
    global covidFacilities
    kspHospitalCF = CovidFacility("1", "KSP Hospital", "N:245, Patil Nagar, Delhi", "Covid Center")
    covidFacilities.append(kspHospitalCF)
    davSchoolCF = CovidFacility("2", "DAV School", "245, Kamla Nagar, Delhi" , "Screening Center")
    covidFacilities.append(davSchoolCF)
    igrHospitalCF = CovidFacility("3", "IGR Hospital", "Post 232, Ram Nagar, Delhi", "Covid Center")
    covidFacilities.append(igrHospitalCF)