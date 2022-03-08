
class ScreeningResult:
    def __init__(self, screeningStatus, healthcareProfessionalDetail, date, covidFacility):
        self.screeningStatus= screeningStatus
        self.healthcareProfessionalDetail= healthcareProfessionalDetail
        self.date= date
        self.covidFacility= covidFacility



class CovidTest:
    def __init__(self, covidStatus, healthcareProfessionalDetail, date):
        self.covidStatus= covidStatus
        self.healthcareProfessionalDetail= healthcareProfessionalDetail
        self.date= date

class CovidConfirmCaseMonitoring:
    def __init__(self, hospitalTestHistory, startDate, endDate, temperature, pulseOximetry, healthcareProfessionalDetail):
        self.hospitalTestHistory= hospitalTestHistory
        self.temperature= temperature
        self.pulseOximetry= pulseOximetry
        self.startDate= startDate
        self.endDate= endDate
        self.healthcareProfessionalDetail= healthcareProfessionalDetail

class HospitalTestHistory:
    def __init__(self, screeningResult, covidTest, covidConfirmCaseMonitoring):
        self.screeningResult= screeningResult
        self.covidTest= covidTest
        self.covidConfirmCaseMonitoring= covidConfirmCaseMonitoring