# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from apitest.models import User,Task
from apitest.serializer import UserSerializer,TaskSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

# Create your views here.


class UserView(APIView):
	renderer_classes = (TemplateHTMLRenderer,)
	template_name = 'user_list.html'

	def get(self,request,format=None,pk=None):
		userdata =  User.objects.all()
		serializer = UserSerializer(userdata,many=True)
		return Response({'users':serializer.data},template_name='user_list.html')
		#return Response({'users':serializer.data},status=status.HTTP_200_OK)

	def post(self,request,format=None,pk=None):
		if request.POST.__contains__('username'):
			username = request.POST.get('username')
			userdata = User.objects.create(username=username)
		if userdata:
			userlist = User.objects.all()
	                serializer = UserSerializer(userlist,many=True)
			return Response({'users':serializer.data},template_name='user_list.html')
		#else:
		#	return Response({'users':serializer.data},template_name='user_list.html')


class TaskView(APIView):
        renderer_classes = (TemplateHTMLRenderer,)
        template_name = 'task_list.html'

        def get(self,request,format=None,pk=None):
                taskdata =  Task.objects.all()
                serializer = TaskSerializer(taskdata,many=True)
                return Response({'tasks':serializer.data},status=status.HTTP_200_OK)

        def post(self,request,format=None,pk=None):
                if request.POST.__contains__('taskname'):
                        userid = request.POST.get('userid')
			userobj = User.objects.get(userid=userid)
			taskname = request.POST.get('taskname')
                        taskdata = Task.objects.create(taskname=taskname,userid=userobj)
                if str(request.POST.get('action')) == 'stop':
			userid = request.POST.get('userid')
			taskid = request.POST.get('taskid')
			taskobj = Task.objects.get(userid=userid,taskid=taskid)
			if str(taskobj.status) != 'stop':
				tz_info = taskobj.starttime.tzinfo
				taskobj.endtime = datetime.now(tz_info)
				seconds = (taskobj.endtime-taskobj.starttime).seconds
				taskobj.duration = seconds
				taskobj.status = 'stop'
				taskobj.save()
			else:
				return Response({'message':"You cannot stop an already ended task"},status=status.HTTP_400_BAD_REQUEST)

	
		#if taskdata:
                tasklist = Task.objects.all()
                serializer = TaskSerializer(tasklist,many=True)
                return Response({'tasks':serializer.data},template_name='task_list.html')
