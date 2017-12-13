#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, json, urllib, requests, datetime
from flask import Flask, session, escape, Response
from flask import request, redirect, url_for, render_template, jsonify, send_from_directory, make_response
from flask_cors import CORS, cross_origin
from model.conversation import ConversationModel
import pprint
import trollius as asyncio
from trollius import From
from threading import Thread
#from crawling.crawlComponent import Crawler

local_path = os.getcwd()
execfile('data/data.py')
execfile(local_path + '/config.py')

import smtplib
from email.mime.text import MIMEText

isSend = False
contents_buf = ""
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()      # say Hello
smtp.starttls()  # TLS 사용시 필요
smtp.login('id', 'password') 
msg = MIMEText("a")
#msg = MIMEText("dd")
#msg = MIMEText("test")
#msg['Subject'] = '[컴퓨터 견적서]'
#msg['To'] = 'wjddn1801@gmail.com'
#smtp.sendmail('wjddn1801@gmail.com', 'jhlee@kdb.snu.ac.kr', msg.as_string())
 
#smtp.quit()
def sendMessage(contents, fr, to, msg=msg):
    msg['Subject'] = '[컴퓨터견적서]'
    msg['To'] = to
    msg['From'] = fr
    smtp.sendmail(fr, to, msg.as_string())
    smtp.quit()

class MyPrettyPrinter(pprint.PrettyPrinter):
    def format(self, _object, context, maxlevels, level):
        if isinstance(_object, unicode):
            return "'%s'" % _object.encode('utf8'), True, False
        elif isinstance(_object, str):
            _object = unicode(_object,'utf8')
            return "'%s'" % _object.encode('utf8'), True, False
        return pprint.PrettyPrinter.format(self, _object, context, maxlevels, level)

def Make_Conversation():
	model_v1 = None
	print '--- Conversation Service Credentials info ---'
	print '  > End-Point : {}'.format(endpoint_url)
	print '  > Username : {}'.format(conversation_username)
	print '  > Password : {}'.format(conversation_password)
	print '--------------------------------------------- '
	model_v1 = ConversationModel(endpoint_url, conversation_username, conversation_password)
	return model_v1

def Conversation_Message(model_obj, workspace_id, message, context, alternate_intents):
	if isinstance(model_obj, ConversationModel) == False:
		return "Not found Conversation Model", {}
	response, response_watson = model_obj.send_message(message=message, \
			workspace_id=workspace_id, context=context, alternate_intents=alternate_intents)
	text = response["message"]
	intents = []
	for idx in range(len(response["intents"])):
		item = (response["intents"][idx]["intent"], response["intents"][idx]["confidence"])
		intents.append(item)
	return text, intents, response["context"], response_watson

def makeError(code, error, url):
	message = {	"errorCode": str(code), "error": error + " : " + url }
	resp = jsonify(message)
	resp.status_code = code
	return resp

app = Flask(__name__)  
CORS(app)

conversation_model_v1 = Make_Conversation()

@app.route("/")
def index():
	return render_template('index.html')

@app.errorhandler(404)
@cross_origin()
def not_found(error=None):
	message = {	"errorCode": "404", "error": "Not Found : " + request.url }
	resp = jsonify(message)
	resp.status_code = 404
	return resp

@app.errorhandler(500)
@cross_origin()
def not_found(error=None):
	message = {	"errorCode": "500", "error": "Internal Server Error : " + request.url }
	resp = jsonify(message)
	resp.status_code = 500
	return resp

@app.route('/api/message', methods=['POST'])
@cross_origin()
def apiMessage():
	# workspace route test
	status_ret = "400"
	message_ret = "Bad Reques"
	if request.method == 'POST':
		try:
			message = ""
			context = {}
			params = json.loads(json.dumps(request.json))
			if "input" in params.keys():
				if "text" in params["input"].keys():
					message = params["input"]["text"]
			
			workspace_id = workspace_main
			if "context" in params.keys():
				context = params["context"]
				if "workspace_id" in context.keys():
					workspace_id = context["workspace_id"]
					if len(workspace_id) < 1:
						workspace_id = workspace_main

			output_text, _, context, response = Conversation_Message(conversation_model_v1, \
					workspace_id, message, context, True)
                        print(output_text)
                        #if "email" in context.keys() and context["email"] != "" and isSend is False:
                         #   sendMessage("test", "wjddn1801@gmail.com", context["email"], msg)
                         #   isSend = True
                        if "comp" in context.keys() and "price" in context.keys() and "usage" in context.keys() and context["isSpec"]=="false":
                            if context["comp"] == "Desktop":
                                if context["price"] <= 600000: context["price"] = 600000
                                elif context["price"] <= 800000: context["price"] = 800000
                                elif context["price"] <= 1000000 and context["usage"] == "game": context["price"] = 1000000
                                elif context["price"] <= 1200000 and context["usage"] == "game": context["price"] = 1200000
                                else: context["price"] = "other"
                                response["output"]["text"] = MyPrettyPrinter().pformat(data["Desktop"][context["usage"]][str(context["price"])]) + "<br />\n 이메일을 기재하시면 해당 견적서를 보내드리겠습니다."
                                contents_buf = MyPrettyPrinter().pformat(data["Desktop"][context["usage"]][str(context["price"])])
                            else:
                                if context["price"] <= 500000: context["price"] = 500000
                                elif context["price"] > 1500000: context["price"] = "other"
                                else: context["price"] = context["price"] % 100000 == 0 and context["price"]/100000*100000 or context["price"]/100000*100000+100000
                                response["output"]["text"] = MyPrettyPrinter().pformat(data["Notebook"][context["usage"]][str(context["price"])])+ "<br />\n 이메일을 기재하시면 해당 견적서를 보내드리겠습니다."
                                contents_buf = MyPrettyPrinter().pformat(data["Notebook"][context["usage"]][str(context["price"])])
                            context["isSpec"] = "true"
                        
                        if len(context["conversation_id"]) > 0:
				if "workspace_id" in context.keys():
					next_workspace_id = context["workspace_id"]
					if workspace_id != next_workspace_id and len(next_workspace_id) != 0:
						_, _, context, response = Conversation_Message(conversation_model_v1, \
								next_workspace_id, message, context, True)
						if len(context["conversation_id"]) > 0:
							return jsonify(json.loads(json.dumps(response, indent=2)))
					if len(next_workspace_id) < 1:
						response["context"] = {}
                                return jsonify(json.loads(json.dumps(response, indent=2)))
			else:
				return makeError(404, "Conversation Not Found", request.url)
		except:
			return makeError(500, "Internal Server Error", request.url)
	return makeError(400, "Bad Request", request.url)

port = os.getenv('PORT', '8000')  

if __name__ == "__main__":  
	total_price = {}
        app.run(host='0.0.0.0', port=int(port))
