from flask import Response, request
from flask_restful import Resource
from database.models import Entree

class EntreesApi(Resource):
    def get(self):
        entrees = Entree.objects().to_json()
        return Response(entrees, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        entree = Entre(**body).save()
        id = entree.id
        return {'id': str(id)}, 200

class EntreeApi(Resource):
    def get(self, id):
        entree = Entree.objects().get(id=id).to_json()
        return Response(entree, mimetype="application/json", status=200)
    
    def put(self, id):
        body = request.get_json()
        Entree.objects().get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        Entree.objects().get(id=id).delete()
        return '', 200