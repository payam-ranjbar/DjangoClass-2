from django.urls import path

from MyAccounts.views import myfuncview, myclassview

urlpatterns = [
    path('myclass/', myclassview.as_view(), name='myclass'),
    path('byfunc/', myfuncview, name='myfunction')

]
