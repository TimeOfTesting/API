from django.urls import path
from .views import *

urlpatterns = [
    path('get_data/', SubmitDataView.as_view(), name='submit_data'),
    path('get_submitData/<int:id>/', GetSingleSubmissionView.as_view(), name='get_submission'),
    path('patch_submitData/<int:id>/', PatchSubmissionView.as_view(), name='patch_submission'),
    path('get_submitData/', GetUserSubmissionsView.as_view(), name='get_user_submissions'),
]