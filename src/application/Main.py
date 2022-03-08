import Configuration
import Introduction
import CovidSystem
import sys

sys.path.append('..')
from service.Login import login
from model.HealthcareProfessional import HealthcareProfessional

Configuration.loadDefaultConfiguration()
Introduction.welcome()

username = input("Enter your username:")
password = input("Enter your password:")

loginSuccessful, healthcareProfessional = login(username, password)

if loginSuccessful:
    Configuration.healthcareProfessional = healthcareProfessional
    CovidSystem.mainPage()

Introduction.bye()