from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedbackView.as_view()),
    path('<int:id_feedback>', update_feedback),
    # path('list', ListFeedback.as_view()),
    path('detail/<int:pk>', DetailFeedback.as_view()),
    path('update/<int:pk>', FeedbackViewUpdate.as_view()),
    # path('list', ListView.as_view(model=Feedback, template_name='feedback/feedback_list.html')),
    # path('detail/<int:pk>', DetailView.as_view(model=Feedback, template_name='feedback/feedback_detail.html')),
    path('list', ListView.as_view(model=Feedback)),
    path('detail/<int:pk>', DetailView.as_view(model=Feedback)),
    path('delete/<int:pk>', DeleteView.as_view(model=Feedback, template_name='feedback/feedback_delete.html',
                                               success_url='/list')),

]

