#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
- Simple Example code

import os
try:
  from SimpleHTTPServer import SimpleHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except ImportError:
  from http.server import SimpleHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server

# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('static')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()
"""
# define import library - Python Library
import os, json, urllib, requests, datetime
# define import library - Flask Library
from flask import Flask, session, escape, Response
from flask import request, redirect, url_for, render_template, jsonify, send_from_directory, make_response
from flask_cors import CORS, cross_origin
# define import library - Watson Conversation Wrapper Library
from model.conversation import ConversationModel
from crawlComponent import Crawler
local_path = os.getcwd()
execfile(local_path + '/config.py')

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
                        if "case_maxprice" in context.keys() and context["case_maxprice"] != "":
                            print("INTO THE IF CLAUSE")
                            crawler = Crawler()
                            response["output"]["text"] = crawler.getInfoByText(self.url_store["mouse"], 15000, 100000, "mouse")
                            print(response["output"]["text"])
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
	app.run(host='0.0.0.0', port=int(port)) 
