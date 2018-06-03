# coding=utf-8
import os
import json
import requests
import logging
log = logging.getLogger(__name__)
facebook_api = os.environ['FACEBOOK_API']
page_token = os.environ['FACEBOOK_PAGE_TOKEN']

#@brief:
#	This function sends a normal response to the user.
#	"normal" means that it has no attachments or button.
def sendResponse(message, sender):
	message_data = {'recipient': {'id': sender}, 'message': {'text': message}}
	params = {"access_token": page_token}
	response = requests.post(facebook_api + 'messages' + '?' + 'access_token=' + page_token, params=params, json=message_data)
	print (response)
	log.debug("Messenger response Status: %s" % response.status_code)


#@brief:
#	asks facebook for the users information.
def getUserInfo(sender_id):
	params = {"access_token": page_token}
	response = requests.get('https://graph.facebook.com/' + str(sender_id) + '?' + 'access_token=' + page_token, params=params)
	log.debug("User response Status: %s" % response.status_code)
	return response.json()