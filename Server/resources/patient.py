from importlib.resources import Resource
from flask import Response, request, jsonify
from flask_restful import Resource
from .db import mysql

class PatientsApi(Resource):
    def __init__(self) -> None:
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
        
    def get(self):
        self.cursor.execute("SELECT * FROM patient")
        data = self.cursor.fetchall()

        patients = []
        for d in data: patients.append({ "id":d[0], "name": d[1], "number": d[3], "city": d[2]})
        return patients, 200

    def post(self):
        body = request.get_json()
        print(body)
        self.cursor.execute('INSERT INTO patient (name, city, number) VALUES (%s, %s, %s)', (body['name'], body['city'], body['number']))
        self.connection.commit()
        return { "id": "" }, 200

    def put(self):
        body = request.get_json()
        print(body)
        self.cursor.execute("UPDATE patient SET name = %s, city = %s, number = %s WHERE id = %s", (body['name'], body['city'], body['number'], body['id']))
        self.connection.commit()
        return { "id": "" }, 200

class PatientApi(Resource):
    def __init__(self) -> None:
        self.connection = mysql.connect()
        self.cursor = self.connection.cursor()
    
    def get(self, id):
        self.cursor.execute("SELECT * FROM patient WHERE id = %s", id)
        data = self.cursor.fetchone()
        return data, 200

    def delete(self, id):
        self.cursor.execute("DELETE FROM patient WHERE id = %s", id)
        self.connection.commit()
        return "", 200
    
