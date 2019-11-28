from flask import Flask

from app.injection.dependency_injections_service import DependencyInjectionsService
from app.services.collections_service import CollectionsService
from app.services.crud_service import CrudService
from app.services.database_service import DatabaseService
from app.services.search_service import SearchService

app = Flask(__name__)

collections_service = DependencyInjectionsService.get_instance().get_service(CollectionsService)
crud_service = DependencyInjectionsService.get_instance().get_service(CrudService)
database_service = DependencyInjectionsService.get_instance().get_service(DatabaseService)
search_service = DependencyInjectionsService.get_instance().get_service(SearchService)

from app.controllers import bulk_controller
from app.controllers import collections_controller
from app.controllers import crud_controller
from app.controllers import database_controller
from app.controllers import errors_controller
from app.controllers import search_controller
