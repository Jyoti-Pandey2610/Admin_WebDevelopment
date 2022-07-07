from resources.user import UserApi
from resources.patient import PatientApi, PatientsApi

def initialize_routes(api):
    api.add_resource(PatientsApi, '/api/patients')
    api.add_resource(PatientApi, '/api/patient/<id>')

    api.add_resource(UserApi, '/api/user')