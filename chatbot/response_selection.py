# -​*- coding: utf-8 -*​-
import os
import logging
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from .facebook import getUserInfo
import numpy as np

def getResponse(message, sender_id):
	faq_response, faq_link, score = select_most_similar(message)
	sender_name = getUserInfo(sender_id)['first_name']

	message_lowercased = message.lower()

	#greetings
	greetings = ""
	if "bom dia" in message_lowercased :
		greetings = "Bom dia {0}! ".format(sender_name)
	elif "boa tarde" in message_lowercased :
		greetings = "Boa tarde {0}! ".format(sender_name)
	elif "boa noite" in message_lowercased:
		greetings = "Boa noite {0}! ".format(sender_name)

	#FAQ Response trigger?
	if score > 0.5:
		return greetings + faq_response, faq_link

	#small talk activation
	faq_link = None
	print (message_lowercased)
	if 'olá' in message_lowercased or 'ola' in message_lowercased:
		return "Olá {0}! Como posso ser útil?".format(sender_name), faq_link
	elif 'obrigado' in message_lowercased:
		return "De nada! Qualquer dúvida não hesite em contactar-nos!", faq_link
	else:
		return "Desculpe, não compreendi. Pode reformular?", faq_link


def json_to_doc():
	json_file = open('faq.json')
	data = json.loads(json_file.read())
	
	documents = []
	questions = []
	answers = []
	links = []
	for i in range(len(data)):
		for j in range(data['FAQ' + str(i+1)]['size']):
			for k in range(data['FAQ' + str(i+1)]['subFAQ' + str(j+1)]['size']):
				documents.append(data['FAQ' + str(i+1)]['subFAQ' + str(j+1)]['question'+str(k+1)])
				documents.append(data['FAQ' + str(i+1)]['subFAQ' + str(j+1)]['answer'+str(k+1)])
				answers.append(data['FAQ' + str(i+1)]['subFAQ' + str(j+1)]['answer'+str(k+1)])
				questions.append(data['FAQ' + str(i+1)]['subFAQ' + str(j+1)]['question'+str(k+1)])
				links.append(data['FAQ' + str(i+1)]['subFAQ' + str(j+1)]['link'+str(k+1)])
	return (documents, questions, answers, links)

def cosine_sim(v1, v2):
    return np.dot(v1, v2) / (np.sqrt(np.sum(v1**2)) * np.sqrt(np.sum(v2**2)))


def select_most_similar(question):
	documents, questions, answers, links = json_to_doc()
	file = open('stopwords.txt', 'r')
	stopwords = list(file.read().split('\n'))
	vectorizer = TfidfVectorizer(analyzer='word', stop_words=stopwords)
	X = vectorizer.fit_transform(documents)
	
	#bigram_vectorizer = TfidfVectorizer(ngram_range=(1, 2), token_pattern=r'\b\w+\b', min_df=1)
	#X_2 = bigram_vectorizer.fit_transform(documents)

	question_tfidf = vectorizer.transform([question]).toarray()[0]
	max_index = 0
	score = 0  
	for i in range(len(questions)):
		if score < cosine_sim(question_tfidf, vectorizer.transform([questions[i]]).toarray()[0]):
			score = cosine_sim(question_tfidf, vectorizer.transform([questions[i]]).toarray()[0])
			max_index = i

	return answers[max_index], links[max_index], score
