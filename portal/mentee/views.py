from django.template import loader
from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework.request import Request
# ,generics,filters
# from django_filters.rest_framework import DjangoFilterBackend
from .models import mentee, mentor, interview, feedback
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .serializers import menteeSerializer, interviewSerializer, mentorSerializer, feedbackSerializer


class menteeView(viewsets.ModelViewSet):
	queryset = mentee.objects.all()
	serializer_class = menteeSerializer
	#permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
	# serializer_class.is_valid(raise_exception=True)

class mentorView(viewsets.ModelViewSet):
	queryset = mentor.objects.all()
	serializer_class = mentorSerializer


class interviewView(viewsets.ModelViewSet):
	queryset = interview.objects.all()
	serializer_class = interviewSerializer

class feedbackView(viewsets.ModelViewSet):
	queryset = feedback.objects.all()
	serializer_class = feedbackSerializer

def allinterviews(request):
	all_interviews_list = interview.objects.all()
	serializer_class = interviewSerializer
	output = ' <br>'.join([str(q.mentor)+" - "+str(q.slot) for q in all_interviews_list])
	return HttpResponse(output)

def mentorSlots(request, mentor_id):
	availableSlots_list = interview.objects.filter(mentor__id=mentor_id).filter(isVacant=True)
	# serializer_class = interviewSerializer
	# serializer_context = {
	# 	'request': Request(request),
	# }
	serializer = interviewSerializer(availableSlots_list, many=True)
		# , context=serializer_context)
	output = ' <br>'.join([str(q.mentor)+" - "+str(q.slot) for q in availableSlots_list])
	return HttpResponse(output)
	# return HttpResponse(serializer.data)

def menteeInterviews(request, mentee_id):
	mentee_interviews = interview.objects.filter(mentee_id=mentee_id)
	serializer_class = interviewSerializer
	output = ' <br>'.join([str(q.mentee)+" - "+str(q.slot) for q in mentee_interviews])
	return HttpResponse(output)

def scheduledInterviews(request):
	sch_int = interview.objects.filter(isVacant=False)
	output = ' <br>'.join([str(q.mentor)+" - "+str(q.mentee)+" : "+str(q.slot) for q in sch_int])
	return HttpResponse(output)

# def bookSlot(request):
# 	return "self.mentee_name"

# def create(request):
#     if request.method == 'POST':
#         form = CreatePollForm(request.POST)
#     else:
#         form = CreatePollForm()

#     context = {'form' : form}
#     return "SUCCESS"


# def list(self, request):
#     queryset = User.objects.all()
#     serializer = UserSerializer(queryset, many=True)
#     return Response(serializer.data)