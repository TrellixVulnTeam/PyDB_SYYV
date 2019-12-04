from flask import Flask, request, abort, make_response, jsonify

from app.controllers import app
from app.controllers import crud_service
from app.controllers import search_service
from app.exceptions.app_exception import AppException
from app.threads.searching_stack import SearchingStack
from app.tools.collection_meta_data import CollectionMetaData
from app.tools.search_context import SearchContext

@app.route('/<collection>/', methods=['POST'])
def create(collection):
    if not request.json:
        abort(405)
    return crud_service.create(CollectionMetaData(collection), request.json)

@app.route('/<collection>/<id>')
def get(collection, id):
    search_id = SearchingStack.get_instance().push_search(collection, {"$filter":{"id":int(id)}})
    result = SearchingStack.get_instance().pop_results(search_id)
    if len(result) != 1:
        raise AppException('Unable to find document {}'.format(id), 404)
    return result[0]

@app.route('/<collection>/<id>', methods=['PUT'])
def update(collection, id):
    if not request.json:
        abort(405)
    result = crud_service.update(CollectionMetaData(collection), int(id), request.json)
    if result is None:
        raise AppException('Unable to find document {}'.format(id), 404)
    return result

@app.route('/<collection>/<id>', methods=['DELETE'])
def delete(collection, id):
    result = crud_service.delete(CollectionMetaData(collection), int(id))
    if result is None:
        raise AppException('Unable to find document {}'.format(id), 404)
    return result
