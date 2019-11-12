from flask import Flask
from app.services.search_service import SearchService
from app.services.crud_service import CrudService
from app.services.collections_service import CollectionsService

app = Flask(__name__)

search_service = SearchService()
crud_service = CrudService()
collections_service = CollectionsService()

from app.controllers import bulk_controller
from app.controllers import collections_controller
from app.controllers import crud_controller
from app.controllers import errors_controller
from app.controllers import search_controller
