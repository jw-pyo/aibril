#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os, json, urllib, requests, datetime
from flask import Flask, session, escape, Response
from flask import request, redirect, url_for, render_template, jsonify, send_from_directory, make_response
from flask_cors import CORS, cross_origin
from model.conversation import ConversationModel
import pprint
#from crawling.crawlComponent import Crawler

local_path = os.getcwd()
execfile('data/data.py')
execfile(local_path + '/config.py')

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
                        if "comp" in context.keys() and "price" in context.keys() and "usage" in context.keys() and context["isSpec"]=="false":
                            if context["comp"] == "Desktop":
                                """
                                obj =data["Desktop"][context["usage"]][str(context["price"])]
                                ret = "CPU: "+obj["CPU"]+"<br />\n" + \
                                      "RAM: "+obj["RAM"]+"<br />\n" + \
                                      "GPU: "+obj["GPU"]+"<br />\n" + \
                                      "메인보드: "+obj["mainboard"]+"<br />\n" + \
                                      "저장장치: "+obj["disk"]+"<br />\n" + \
                                      "파워: "+obj["power"]+"<br />\n" + \
                                      "가격 : "+obj["price"]+"<br />\n" + \
                                      "이메일을 기재하시면 본 견적서를 발송해드리겠습니다."
                                      #"케이스: "+obj["case"]+"<br />\n" + \
                                
                                response["output"]["text"] = ret
                                #response["output"]["text"] = #"CPU: "+obj["CPU"]+"<br />\n" + \
                                                             #"RAM: "+obj["RAM"]+"<br />\n" + \
                                                             #"GPU: "+obj["GPU"]+"<br />\n" + \
                                                             #"메인보드: "+obj["mainboard"]+"<br />\n" + \
                                                             #"저장장치: "+obj["disk"]+"<br />\n" + \
                                                             #"파워: "+obj["power"]+"<br />\n" + \
                                                             #"케이스: "+obj["case"]+"<br />\n" + \
                                                             #"모니터: "+obj["monitor"]+"<br />\n" + \
                                                             #"키보드: "+obj["keyboard"]+"<br />\n" + \
                                                             #"마우스: "+obj["mouse"]+"<br />\n" + \
                                                             #"가격 : "+obj["price"]+"<br />\n" + \
                                                             #"이메일을 기재하시면 본 견적서를 발송해드리겠습니다."
                                """
                                response["output"]["text"] = MyPrettyPrinter().pformat(data["Desktop"][context["usage"]][str(context["price"])]) + "<br />\n 이메일을 기재하시면 해당 견적서를 보내드리겠습니다."
                            else:
                                response["output"]["text"] = MyPrettyPrinter().pformat(data["Notebook"][context["usage"]][str(context["price"])])+ "<br />\n 이메일을 기재하시면 해당 견적서를 보내드리겠습니다."
                            context["isSpec"] = "true"
                            #print(context["comp"])
                            #print(context["price"])
                            #print(context["usage"])
                        
                        """ 
                        if "email" not in context.keys() and "case_maxprice" in context.keys() and context["case_maxprice"] != "":
                            print("INTO THE IF CLAUSE")
                            total_price = { "CPU" : context["CPU_maxprice"], \
                                            "RAM" : context["RAM_maxprice"],\
                                            "GPU" : context["GPU_maxprice"],\
                                            "disk" : context["disk_maxprice"],\
                                            "monitor" : context["monitor_maxprice"],\
                                            "power" : context["power_maxprice"],\
                                            "keyboard" : context["keyboard_maxprice"],\
                                            "mouse" : context["mouse_maxprice"],\
                                            "case" : context["case_maxprice"], \
                                            u"총 가격" : int(context["first_price"]) - int(context["price"])
                                            }
                            #crawler = Crawler()
                            #response["output"]["text"] = crawler.getInfoByText(self.url_store["mouse"], 15000, 100000, "mouse")
                            response["output"]["text"] = str(total_price) + "\n 해당 가격대에서 최적의 부품을 선택 후, 견적을 보내드리겠습니다. 이메일 주소를 입력해 주세요"
                            print(response["output"]["text"])
			"""
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
