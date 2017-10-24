#!/usr/bin/env python
from itty import *
import json
import pprint
import jimmy
import requests
from bs4 import BeautifulSoup
import urllib.request


# api info website for Canvas https://canvas.instructure.com/courses/785215
# api documentation for Canvas https://canvas.instructure.com/doc/api/index.html
# general format for requesting url: https://canvas.instructure.com/api/v1/ + path
# example: https://canvas.instructure.com/api/v1/courses?include[]=total_scores  for the request for user's grades

def Authorization():
	# send an account linking button to the user
	# note: https://discuss.api.ai/t/authenticate-user-on-facebook-messenger/2917
	#       https://developers.facebook.com/docs/messenger-platform/send-messages/buttons
	
	url = "https://developers.facebook.com/apps/1531277306967086/webhooks/"
	# not sure about the format
	data = {
		'type':'account_linking',
		'url':'canvas login url'}

	requests.post(url, data = data)




def get_announcement():
	url = "https://canvas.instructure.com/api/v1/announcements"
	params = {
		'context_codes':'',
		'start_date':'',
		'end_date':'',
		'active_only':''}

	r = requests.get(url, params = params,headers = {"Authorization":access_token} )
	data = json.loads(r.text)
	title = data['title'], message = data['message']
	output = 'reply message'

def get_classes():

	course_ids = []
	classes = []
    url = 'https://sjsu.instructure.com/'
    content = urllib.request.urlopen(url).read()
    soup=BeautifulSoup(content,'html.parser')
    tag=soup.body.find(class_="ic-NavMenu-list-item__link")
    for string in tag.strings
        print(string)
	classes_data = {'classes':classes, 'course id': course_ids}


	return classes_data



def get_grades():

    classes_data = get_classes() # gets a dict of class data from get_classes()
    ids = classes_data['course id'] # the ids of the classes as a list
    courses = classes_data['classes'] # the class names in a list
    class_and_grade={} # an empty dict for class:grade pairs
    
    for i, cid in enumerate(ids):
        grade_url = 'https://sjsu.instructure.com/courses/%s/grades' % ids[i]
        content = urllib.request.urlopen(grade_url).read()
        soup=BeautifulSoup(content,'html.parser')
        tag=soup.body.find(class_="student_assignment final_grade")
        grade=""
        for string in tag.stripped_strings
            grade+=(repr(string))
        grade=grade[9]+grade[10]+'%' #orig str is 'total:__%', this returns __%
        class_and_grade[courses[i]]=grade #adds a class:grade pair

    return class_and_grade # returns a dict of class:grade pairs

@post('/')
def index(request):
	r = json.loads(request.body)
	if not r:
	    return "True"

	pprint.pprint(r)
	return "true"

	action = r['result']['action']

	if action == 'get_grades':
		get_grades()

	if action == 'classes':
		get_classes()

	if action == 'get_announcement':
		get_announcement()

# triggered by canvas login URL callback
@post('/')
def authentication(request):
	global access_token;
	r = json.loads(request.body)
	access_token = r[???]

	# call intended function





if __name__ == "__main__":

	run_itty(server='wsgiref', host='0.0.0.0', port=8080)
