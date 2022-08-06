#REST FRAMEWORK API Router
from api.viewsets import userviewsets
from rest_framework import routers

router = routers.DefaultRouter()
#router.register('cuentas_usuario', userviewsets, base_name ='user_api')
