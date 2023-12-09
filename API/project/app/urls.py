from django.urls import path
from .views import *

urlpatterns = [
    path('getData/', SubmitDataView.as_view(), name='submit_data'),
    path('getSubmission/<int:id>/', GetSingleSubmissionView.as_view(), name='get_submission'),
    path('patchSubmission/<int:id>/', PatchSubmissionView.as_view(), name='patch_submission'),
    path('getUserSubmissions/', GetUserSubmissionsView.as_view(), name='get_user_submissions'),
]