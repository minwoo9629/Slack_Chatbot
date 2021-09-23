from django.core.exceptions import AppRegistryNotReady
from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
# Create your views here.

class HelloView(APIView):
    def post_message(self, token, channel, text):
        response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ token},
        data={"channel": channel,"text": text}
        )
        print(response)

    def post(self, request):
        
        # 요청이 어떻게 들어오나 찍어보기
        print(request.body, "request body \n")
        client_msg_id = request.data.get('event').get('client_msg_id', None)
        # body에서 challenge 필드만 빼오기
        challenge = request.data.get('challenge')
        if client_msg_id is not None:
            user = request.data.get('event').get('user')
            text = request.data.get('event').get('text')
            print("사용자 :", user, "| 메시지 :", text)
            self.post_message("xoxb-2470194170337-2493625179457-X4JemkrFwA4rGQkTRN638CLa", "#민우", "싫엉")


        # 응답 데이터로 { challenge : challenge } 주기
        return Response(status=200, data=dict(challenge=challenge))
