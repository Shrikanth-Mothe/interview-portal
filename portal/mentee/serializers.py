from rest_framework import serializers
from .models import mentee, mentor, interview, feedback


class menteeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = mentee
		fields = ('url' , 'mentee_name' , 'email')

class mentorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = mentor
		fields = ('url' , 'mentor_name' , 'email' , 'bio')

class interviewSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = interview
		fields = ('url' , 'mentor' , 'mentee' ,'slot', 'isVacant')

class feedbackSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = feedback
		fields = ('url', 'feedback_id', 'verdict', 'comments','rating')


		