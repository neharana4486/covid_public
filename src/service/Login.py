import sys
sys.path.append('..')
from model.HealthcareProfessional import HealthcareProfessional

healthcareProfessionals = list()


def login(username, password):
    for healthcareProfessional in healthcareProfessionals:
        if healthcareProfessional.username == username and healthcareProfessional.password == password:
            return True, healthcareProfessional

    return False

def initialHCPData():
    rajHCP = HealthcareProfessional("Raj","REG100","CV100","rajkumar","12345")
    healthcareProfessionals.append(rajHCP)
    maxHCP = HealthcareProfessional("Max","REG101","CV101","max","max123")
    healthcareProfessionals.append(maxHCP)
    testHCP = HealthcareProfessional("test","test","test","","")
    healthcareProfessionals.append(testHCP)
