class PatientPersonalDetail:
    def __init__(self, name, age, sex, adhaarnumber, mobileNumber):
        self.name= name
        self.age= age
        self.sex= sex
        self.adhaarnumber= adhaarnumber
        self.mobileNumber= mobileNumber

class PatientMedicalDetail:
    def __init__(self, temperature, cough, runnynose, sorethroat, pneumonia, resprate, oxygenconcenteration):
        self.temperature = temperature
        self.cough = cough
        self.runnynose = runnynose
        self.sorethroat = sorethroat
        self.pneumonia = pneumonia
        self.resprate = resprate
        self.oxygenconcen = oxygenconcenteration

class PatientMedicalLog:
    def __init__(self, date, remark, patientMedicalDetail, healthcareProfessional):
        self.date = date
        self.remark = remark
        self.patientMedicalDetail= patientMedicalDetail
        self.healthcareProfessional = healthcareProfessional

class Patient:
    def __init__(self, registrationDate, patientPersonalDetail):
        self.registrationDate = registrationDate
        self.patientPersonalDetail= patientPersonalDetail
        self.screeningStatus = None
        self.covidTestStatus = None
        self.patientStatus = None
        self.medicalLog = list()
        self.referedCovidFacility = None

