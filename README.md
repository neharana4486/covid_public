# covid_public
patient admission and discharge system
This Python based project is to produce a covid patient discharge system as per public guidelines of ministry of health & family welfare, India.

It has a source directory (src) which further has three main modules: application, model, service.

![High level Use Cases - Discharge](https://github.com/neharana4486/covid_public/blob/main/Slide4.JPG?raw=true)


MVP: complete the process for mild cases, from admission to discharge

1. Patient goes to fever clinic/COVID reception. 
2. Health Care Professional at COVID reception/fever clinic REGISTERS the Patient to the Patient System.   [function: register_patient(), input patient detail and medical detail and register the patient. The registered patient info should be ADDED somewhere, may be in a file or a list. So function add_patient()]
3. Healthcare Professional SCREENS the patient. [screening function which returns screening status based on Patient Medical Detail. 
4. Healthcare Professional REFERS the patient to the needed COVID facility based on the screening status (keep patient facility history separate)
5. Patient goes to referred COVID facility (covid care centre [CCC] in case of screening result (mild).
6. HCP takes COVID test at CCC reception.
7. HCP puts the patient under ‘suspected patients’ section.
8. HCP refers the patient to allotted room.
9. Based on the COVID test result (FUNCTION): a) HCP gives instructions to COVID -ve patients and send them home. b) HCP puts the COVID +ve patients under ‘COVID confirmed cases’.
10. COVID confirmed cases are monitored for 10 days.
11. HCP discharges (function) the patient if pulse oximetry is normal and there is no fever since last 3 days.


![Software Development Process](https://github.com/neharana4486/covid_public/blob/main/SD_process.jpg?raw=true)
