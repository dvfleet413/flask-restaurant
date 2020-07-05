from .entree import EntreesApi, EntreeApi


def initialize_routes(api):
    api.add_resource(EntreesApi, '/api/entrees')
    api.add_resource(EntreeApi, '/api/entrees/<id>')
