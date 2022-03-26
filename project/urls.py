from datacenter.active_passcards_view import show_active_passcards
from datacenter.passcard_info_view import show_passcard_info
from datacenter.storage_information_view import show_storage_information
from django.urls import path

urlpatterns = [
    path('', show_active_passcards, name='active_passcards'),
    path('storage_information', show_storage_information, name='storage_information'),
    path('passcard_info/<uuid:passcode>', show_passcard_info, name='passcard_info'),
]
