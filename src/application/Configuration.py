import sys

sys.path.append('..')
from service.Administration import loadPaitents
from service.Administration import initialCovidFacilityData
from service.Login import initialHCPData
from model.HealthcareProfessional import HealthcareProfessional

healthcareProfessional = None

def loadDefaultConfiguration():
    bootstrap()

def bootstrap():
    initialHCPData()
    loadPaitents()
    initialCovidFacilityData()

