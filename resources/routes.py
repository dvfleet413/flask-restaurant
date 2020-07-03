from .entree import EntreesApi, EntreeApi

def initialize_routes(api):
    api.add_resource(EntreesApi, '/entrees')
    api.add_resource(EntreeApi, '/entrees/<id>')