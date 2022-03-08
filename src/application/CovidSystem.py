import sys
import datetime
import Configuration

from columnar import columnar

sys.path.append('..')
from model.Patient import PatientPersonalDetail
from model.Patient import PatientMedicalDetail
from model.Patient import PatientMedicalLog
from model.Patient import Patient
from service.Administration import addPatient
from service.Administration import getPatients
from service.Administration import getPatient
from service.Administration import patientScreening
from service.Administration import getCovidFacilities
from service.Administration import patientReferring

from model.HealthcareProfessional import HealthcareProfessional


def mainPage():
    while True:
        print("")
        print("----------------------------------")
        print("1) Admission:")
        print("2) Monitoring:")
        print("3) Discharge:")
        print("X) Exit")

        mainChoice = input("Enter your Choice:")

        if mainChoice == "1":
            admission()
        elif mainChoice == "2":
            monitoring()
        elif mainChoice == "3":
            discharge()
        elif mainChoice.upper() == "X":
            break


def admission():
    while True:
        print("")
        print("----------------------------------")
        print("1) Patient Registration:")
        print("2) View Patients:")
        print("3) View Patient's Medical Log:")
        print("4) Refer Patient:")
        print("B) Back to the main menu")

        mainChoice = input("Enter your Choice:")

        if mainChoice == "1":
            registration()
        elif mainChoice == "2":
            viewPatient()
        elif mainChoice == "3":
            viewPatientMedicalLog()
        elif mainChoice == "4":
            referPatient()
        elif mainChoice.upper() == "B":
            break


def monitoring():
    pass


def discharge():
    pass


def registration():
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    sex = input("Enter patient's sex (m/f): ")
    adhaarnumber = input("Enter patient's adhaarnumber: ")
    mobileNumber = input("Enter patient's mobileNumber: ")

    patientPersonalDetail = PatientPersonalDetail(name, age, sex, adhaarnumber, mobileNumber)

    registrationDate = datetime.datetime.now()
    patient = Patient(registrationDate, patientPersonalDetail)

    temperature = input("Enter patient's temperature: ")
    cough = input("Enter patient's cough: ")
    runnynose = input("Enter patient's runnynose: ")
    sorethroat = input("Enter patient's sorethroat: ")
    pneumonia = input("Enter patient's pneumonia: ")
    resprate = input("Enter patient's resprate: ")
    oxygenconcenteration = input("Enter patient's oxygenconcenteration: ")

    patientMedicalDetail = PatientMedicalDetail(temperature, cough, runnynose, sorethroat, pneumonia, resprate, oxygenconcenteration)
    screeningStatus = patientScreening(patientMedicalDetail)
    patient.screeningStatus = screeningStatus

    patientMedicalLog = PatientMedicalLog(registrationDate, "Collected during Registration", patientMedicalDetail, Configuration.healthcareProfessional)
    patient.medicalLog.append(patientMedicalLog)

    addedPatient = addPatient(patient)
    print("Patient has successfully been Registerd and Screened...!!!")
    displayPatient(addedPatient)


def viewPatient():
    patients = getPatients()
    if patients is not None:
        displayPatient(patients)
    else:
        print("No patient available")


def displayPatient(patients):
    headers = ['adhaarnumber', 'name', 'age', 'sex', 'mobileNumber', 'registrationDate', 'screeningStatus', 'covidTestStatus', 'patientStatus', 'referedCovidFacility']
    patientsData = list()
    for patient in patients.values():
        patientRow = list()
        patientRow.append(patient.patientPersonalDetail.adhaarnumber)
        patientRow.append(patient.patientPersonalDetail.name)
        patientRow.append(patient.patientPersonalDetail.age)
        patientRow.append(patient.patientPersonalDetail.sex)
        patientRow.append(patient.patientPersonalDetail.mobileNumber)
        patientRow.append(patient.registrationDate)
        patientRow.append(patient.screeningStatus)
        patientRow.append(patient.covidTestStatus)
        patientRow.append(patient.patientStatus)

        if patient.referedCovidFacility is not None:
            patientRow.append(patient.referedCovidFacility.name)
        else:
            patientRow.append(None)

        patientsData.append(patientRow)

    table = columnar(patientsData, headers, no_borders=True)
    print(table)


def viewPatientMedicalLog():
    adhaarnumber = input("Enter Patient'a Adhaar Number:")
    patient = getPatient(adhaarnumber)
    if patient is not None:
        displayPatientMedicalLog(patient)
    else:
        print("No patient available with adhaar number:", adhaarnumber)


def displayPatientMedicalLog(patient):
    headers = ['date', 'remark', 'HCP name', 'HCP covidFacilityId', 'patientMedicalDetail']
    patientsData = list()
    for patientMedicalLog in patient.medicalLog:
        patientRow = list()
        patientRow.append(patientMedicalLog.date)
        patientRow.append(patientMedicalLog.remark)
        patientRow.append(patientMedicalLog.healthcareProfessional.name)
        patientRow.append(patientMedicalLog.healthcareProfessional.covidFacilityId)
        patientRow.append(createDisplayPatientMedicalDetail(patientMedicalLog.patientMedicalDetail))
        patientsData.append(patientRow)

    table = columnar(patientsData, headers, no_borders=True, wrap_max=20)
    print(table)


def createDisplayPatientMedicalDetail(patientMedicalDetail):
        return  "temperature: " + patientMedicalDetail.temperature + \
                ", cough: " + patientMedicalDetail.cough + \
                ", runnynose: " + patientMedicalDetail.runnynose + \
                ", cough: " + patientMedicalDetail.cough + \
                ", sorethroat: " + patientMedicalDetail.sorethroat + \
                ", pneumonia: " + patientMedicalDetail.pneumonia + \
                ", resprate: " + patientMedicalDetail.resprate + \
                ", oxygenconcen: " + patientMedicalDetail.oxygenconcen


def referPatient():
    adhaarnumber = input("Enter Patient'a Adhaar Number:")
    patient = getPatient(adhaarnumber)
    if patient is None:
        print("No patient available with adhaar number:", adhaarnumber)
        return
    displayPatient({patient.patientPersonalDetail.adhaarnumber : patient})

    covidFacilities =  getCovidFacilities()
    if covidFacilities == None:
        print("No covid facility available")
        return

    print("")
    print("----------------------------------")
    print("Here are the available Covid Facilities to be assigned to patient:")
    displayCovidFacility(covidFacilities)

    selectedCovidFacilityID = input("Enter the covid facility ID which you would like to refer to " + patient.patientPersonalDetail.name + " :")

    patientReferredSuccessStatus, updatePatient = patientReferring(selectedCovidFacilityID, patient)
    if not patientReferredSuccessStatus:
        print("Covid Facility ID is incorrect!")
        return

    displayPatient(updatePatient)


def displayCovidFacility(covidFacilities):
    headers = ['id', 'name', 'address', 'type']
    covidFacilityData = list()
    for covidFacility in covidFacilities:
        covidFacilityRow = list()
        covidFacilityRow.append(covidFacility.id)
        covidFacilityRow.append(covidFacility.name)
        covidFacilityRow.append(covidFacility.address)
        covidFacilityRow.append(covidFacility.type)
        covidFacilityData.append(covidFacilityRow)

    table = columnar(covidFacilityData, headers, no_borders=True, wrap_max=20)
    print(table)
