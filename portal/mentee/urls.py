from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('mentee' , views.menteeView)
router.register('mentor' , views.mentorView)
router.register('interview' , views.interviewView)
# router.register('slot' , views.slotView)
router.register('feedback',views.feedbackView)

urlpatterns = [
	path('',include(router.urls)),
	# path('bookslot/', views.bookSlot, name='bookSlot'),
	path('allinterviews', views.allinterviews, name='allinterviews'),
	# path('scheduled', views.scheduledInterviews, name='scheduledInterviews'),
	path('slots/<int:mentor_id>', views.mentorSlots, name='mentorSlots'),
	path('myinterviews/<int:mentee_id>', views.menteeInterviews , name='menteeInterview')
]