# -​*- coding: utf-8 -*​-
import os
import logging
import json
import requests
from datetime import datetime
from flask import Blueprint, request, Response
from flask import render_template
from .facebook import sendResponse, getUserInfo
from .response_selection import getResponse

log = logging.getLogger(__name__)

chatbot_bp = Blueprint(
    'chatbot',
    __name__,
    template_folder='templates'
)


log.debug('Welcome to EDP-Challenge Chatbot')

@chatbot_bp.route('/')
def homepage():
	return render_template('home.html')


@chatbot_bp.route('/messenger/', methods=['POST', 'GET'])
def conversations_update():
	if request.method == 'POST':
		log.debug(' POST messages ')
		request_json = request.get_json()
		messages = request_json['entry'][0]['messaging']

		for message_info in messages:
			if 'message' in message_info:
				log.debug('***** Message: {0} ****'.format(message_info['message']))
				response, link = getResponse(message_info['message']['text'], message_info['sender']['id'])
				sendResponse(message=response, sender=message_info['sender']['id'])
				if link:
					sendResponse(message="Para mais Informações pode consultar o seguinte Link: " + link, sender=message_info['sender']['id'])

		return Response(response={'message': 'received'}, status=200, mimetype='application/json')


	#if its not a POST it can only be a GET
	log.debug('**** GET messages ****')
	mode, challenge, verify = queryStringParser(str(request))
	if verify != 'No_intelligent_idea_can_gain_general_acceptance_unless_some_stupidity_is_mixed_in_with_it.-Ricardo_Reis':
		return Response(response=json.dumps({'error': 'Wrong validation token.'}), status=400, mimetype='application/json')	
	
	return Response(response=challenge, status=200, mimetype='application/json')


#---------------------------- AUXILIAR FUNCTIONS ------------------------------------------------------------------------

#@brief:
#	function to parse the query string and get the mode, challenge and verify for facebook
def queryStringParser(request_str):
	queryString = request_str.split('?')[1]
	queryString = queryString[:(len(queryString)-8)]
	parameters = queryString.split('&')
	values = ()
	for p in parameters:
		values += (p.split('=')[1],)
	log.debug(values)
	return values

def getParticipantInfo(sender_id):
	userInfo = getUserInfo(sender_id)
	print (userInfo)
	return {'name': userInfo['first_name'] + ' ' + userInfo['last_name'], 'profile_pic': userInfo['profile_pic']}

