from rest_framework.routers import SimpleRouter
from restapi.views import BookOperations
simplerouter = SimpleRouter()
simplerouter.register('book/v1', BookOperations)
urlpatterns = simplerouter.urls   #   urlpattern ye bank_app/urls.py se copy karna hai

#http://localhost:8000/api/book/v1   --->GET --->single
#http://localhost:8000/api/book/v1   --->POST --->Create
#http://localhost:8000/api/book/v1   --->DELETE--->delete and so on...
