from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_restful import reqparse
from flask import jsonify
from flask_cors import CORS, cross_origin

#from pymongo import MongoClient
import pymongo
from bson import Binary, Code
from bson.json_util import dumps
from bson.objectid import ObjectId

import datetime

import json
import urllib


import timeit

app = FlaskAPI(__name__)
CORS(app)

client = pymongo.MongoClient('localhost', 27017)
db = client['waseem_mongodb']
businessdb = db['yelp.business']
reviewdb = db['yelp.review']
userdb = db['yelp.user']
tipdb = db['yelp.tip']

parser = reqparse.RequestParser()

"""=================================================================================="""
"""=================================================================================="""
"""=================================================================================="""


@cross_origin() # allow all origins all methods.
@app.route("/", methods=['GET'])
def index():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return func_list

   
"""=================================================================================="""
@app.route("/find_zips/<args>", methods=['GET'])
def find_zips(args):
    args = myParseArgs(args)
    
    zip = []
    zip = args['zip']
    data = []
  
    # if 'start' in args.keys():
        # args['start'] = int(args['start'])
    # if 'limit' in args.keys():
        # args['limit'] = int(args['limit'])
    
    # if 'start' in args.keys() and 'limit' in args.keys():
	    # result = businessdb.find({},{"full_address":1,"_id":0}).skip(args['start']).limit(args['limit'])
    # elif 'start' in args.keys():
        # result = businessdb.find({},{"full_address":1,"_id":0}).skip(args['start'])
    # elif 'limit' in args.keys():
        # result = businessdb.find({},{"full_address":1,"_id":0}).limit(args['limit'])
    # else:
     #   result = businessdb.find({},{"full_address":1,"_id":0}).limit(20)        
    
    result = businessdb.find({},{"full_address":1,"_id":0})
    for r in result:
        parts = r['full_address'].split(' ')
        target = parts[-1]
        if target in zip:
            data.append(r['full_address'])
    return {"data":data}
   
   
"""=================================================================================="""


"""=================================================================================="""
@app.route("/rest_city/<args>", methods=['GET'])
def rest_city(args):

    args = myParseArgs(args)
    data = []
    city = args['city']
	
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])
		
	if 'start' in args.keys() and 'limit' in args.keys():
           result = businessdb.find({"city": city},{"name":1,"city":city,"_id":0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
          result = businessdb.find({"city": city},{"name":1,"city":city,"_id":0}).skip(args['start'])
    elif 'limit' in args.keys():
          result = businessdb.find({"city": city},{"name":1,"city":city,"_id":0}).limit(args['limit'])
    else:
          result = businessdb.find({"city": city},{"name":1,"city":city,"_id":0}).limit(20)  	
		
    #return city	
   #  result = businessdb.find({"city": city},{"name":1,"city":city,"_id":0})
    #return result
    for r in result :
	    #if r['city']== city :
	    data.append(r)
    return {"data":data}


"""=================================================================================="""

"""=================================================================================="""
@app.route("/closest/<args>", methods=['GET'])
def closest(args):
	"""Find all closest restaurants with lon and lat."""
	args = myParseArgs(args)	
	if 'start' in args.keys():
		args['start'] = int(args['start'])
	if 'limit' in args.keys():
		args['limit'] = int(args['limit'])
	data = []
	
	if 'start' in args.keys() and 'limit' in args.keys():
		result = businessdb.find({ 'loc' : { '$geoWithin' : { '$centerSphere': [ [-80.839186,35.226504] , 5 / 3963.2 ] } } },{"name":1, "_id":0}).skip(args['start']).limit(args['limit'])
	elif 'start' in args.keys():
		result = businessdb.find({ 'loc' : { '$geoWithin' : { '$centerSphere': [ [-80.839186,35.226504] , 5 / 3963.2 ] } } },{"name":1, "_id":0}).skip(args['start'])
	elif 'limit' in args.keys():
		result = businessdb.find({ 'loc' : { '$geoWithin' : { '$centerSphere': [ [-80.839186,35.226504] , 5 / 3963.2 ] } } },{"name":1, "_id":0}).limit(args['limit'])
	else:
		result = businessdb.find({ 'loc' : { '$geoWithin' : { '$centerSphere': [ [-80.839186,35.226504] , 5 / 3963.2 ]} } },{"name":1, "_id":0, "full_address":1}).limit(10)

	for r in result:
		data.append(r)
	
	return {"data":data}

"""=================================================================================="""
@app.route("/reviews/<args>", methods=['GET'])
def reviews(args):

    args = myParseArgs(args)    
    data = []
    id = args['id']
	
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])
		
		
    if 'start' in args.keys() and 'limit' in args.keys():
           result = reviewdb.find({"business_id":id},{"business_id":1,"_id":0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
          result = reviewdb.find({"business_id":id},{"business_id":1,"_id":0}).skip(args['start'])
    elif 'limit' in args.keys():
          result = reviewdb.find({"business_id":id},{"business_id":1,"_id":0}).limit(args['limit'])
    else:
          result = reviewdb.find({"business_id":id},{"business_id":1,"_id":0}).limit(20)  		
	
   ## result = reviewdb.find({},{"business_id":1,"_id":0})
    for r in result:
	    
		    data.append(r)  
    return {"data":data}
"""==================================================================================="""


"""=================================================================================="""
@app.route("/reviews_5stars/<args>", methods=['GET'])
def reviews_5stars(args):

    args = myParseArgs(args)    
    data = []
    id = args['id']	
    star = int(args['num_stars'])
	
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])
		
		
    if 'start' in args.keys() and 'limit' in args.keys():
           result = reviewdb.find({"stars":star , "business_id":id }, {"business_id" :1,"stars":1,"_id":0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
          result = reviewdb.find({"stars":star , "business_id":id }, {"business_id" :1,"stars":1,"_id":0}).skip(args['start'])
    elif 'limit' in args.keys():
          result = reviewdb.find({"stars":star , "business_id":id }, {"business_id" :1,"stars":1,"_id":0}).limit(args['limit'])
    else:
          result = reviewdb.find({"stars":star , "business_id":id }, {"business_id" :1,"stars":1,"_id":0}).limit(20) 
	
   ## result = reviewdb.find({"stars":star , "business_id":id }, {"business_id" :1,"stars":1,"_id":0})
    for r in result:
	    #if r['business_id']== id:
		data.append(r)  
    return {"data":data}
"""==================================================================================="""

@app.route("/yelping/", methods=['GET'])
def yelping():
	data = []		
	# if 'skip' in args.keys():
	    # args['skip'] = int(args['skip'])
	# if 'limit' in args.keys():
		# args['limit'] = int(args['limit'])
	
	# if 'start' in args.keys() and 'limit' in args.keys():
        # result = userdb.find({ "yelping_since" : {"$lte":"2012-01"}}, {"yelping_since":1,"_id":0}).limit(args['limit'])
	# elif 'start' in args.keys():
        # result = userdb.find({ "yelping_since" : {"$lte":"2012-01"}}, {"user_id":1,"_id":0}).skip(args['start'])
    # elif 'limit' in args.keys():
        # result = userdb.find({ "yelping_since" : {"$lte":"2012-01"}}, {"user_id":1,"_id":0}).limit(args['limit'])
    # else:

	result = userdb.find({"yelping_since":{"$lte":"2012-01"}},{"yelping_since":1,"_id":0})
	for r in result:
	    data.append(r)

	return {"data":data}



"""=================================================================================="""
@app.route("/most_likes/<args>", methods=['GET'])
def most_likes(args):

    args = myParseArgs(args)    
    data = []
	
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])
	
	if 'start' in args.keys() and 'limit' in args.keys():
           result = tipdb.find({},{"business_id":1,"_id" :0}).sort("likes",-1).limit(1).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
          result = tipdb.find({},{"business_id":1,"_id" :0}).sort("likes",-1).limit(1).skip(args['start'])
    elif 'limit' in args.keys():
          result = tipdb.find({},{"business_id":1,"_id" :0}).sort("likes",-1).limit(1).limit(args['limit'])
    else:
          result = tipdb.find({},{"business_id":1,"_id" :0}).sort("likes",-1).limit(1).limit(20) 
		  
		  
   ## result = tipdb.find({},{"business_id":1,"_id" :0}).sort("likes",-1).limit(1)
    for r in result: 
	  	data.append(r)  
    return {"data":data}
"""==================================================================================="""
"""==================================================================================="""

@app.route("/review_count/", methods=['GET'])
def review_count():
    
    data = []
		
    result = userdb.aggregate([{'$group':{"_id":"$user_id",'averageReviewCount':{'$avg':"$review_count"}}}])
    
    for r in result:
        data.append(r)
    

    return {"data":data}


"""=================================================================================="""
"""=================================================================================="""
@app.route("/elite/<args>", methods=['GET'])
def elite(args):

    args = myParseArgs(args)    
    data = []
	
    if 'start' in args.keys():
        args['start'] = int(args['start'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])
	
	
	if 'start' in args.keys() and 'limit' in args.keys():
           result = userdb.find({},{"user_id":1, "name":1, "_id" :0}).skip(args['start']).limit(args['limit'])
    elif 'start' in args.keys():
          result = userdb.find({},{"user_id":1, "name":1, "_id" :0}).skip(args['start'])
    elif 'limit' in args.keys():
          result = userdb.find({},{"user_id":1, "name":1, "_id" :0}).limit(args['limit'])
    else:
          result = userdb.find({},{"user_id":1, "name":1, "_id" :0}).limit(20) 
		  
	
     ##result = userdb.find({},{"user_id":1, "name":1, "_id" :0})
    for r in result:		
		data.append(r)  
    return {"data":data}
"""==================================================================================="""

"""==================================================================================="""
@app.route("/long_elite/<args>", methods=['GET'])
def long_elite(args):
	
	args = myParseArgs(args)
    
	if 'start' in args.keys():
		args['start'] = int(args['start'])
	if 'limit' in args.keys():
		args['limit'] = int(args['limit'])

	data = []
	# if 'start' in args.keys() and 'limit' in args.keys():
		# result = userdb.aggregate([{'$project': {'elitesize': { '$size': "$elite" }}},{ '$group':{"_id": "$user_id",'maxelite': { '$max': "$elitesize" }}}]).skip(args['start']).limit(args['limit'])
	# elif 'start' in args.keys():
		# result = userdb.aggregate([{'$project': {'elitesize': { '$size': "$elite" }}},{ '$group':{"_id": "$user_id",'maxelite': { '$max': "$elitesize" }}}]).skip(args['start'])
	# elif 'limit' in args.keys():
		# result = userdb.aggregate([{'$project': {'elitesize': { '$size': "$elite" }}},{ '$group':{"_id": "$user_id",'maxelite': { '$max': "$elitesize" }}}]).limit(args['limit'])
	# else:
		# result = userdb.aggregate([{'$project': {'elitesize': { '$size': "$elite" }}},{ '$group':{"_id": "$user_id",'maxelite': { '$max': "$elitesize" }}}]).limit(1)
		
	result = userdb.aggregate([{'$project': {'elitesize': { '$size': "$elite" }}},{ '$group':{"_id": "$name",'maxelite': { '$max': "$elitesize" }}}])	
		
	for r in result:
		data.append(r)


	return {"data":data}


"""==================================================================================="""
@app.route("/avg_elite/", methods=['GET'])
def avg_elite():
    
    data = []
		
    result = userdb.aggregate([{'$project': {'elitesize': { '$size': "$elite" }}},{ '$group':{"_id": 0,'avg_elite_yrs': { '$avg': "$elitesize" }}}])
    
    for r in result:
        data.append(r)
    

    return {"data":data}

"""==================================================================================="""


"""==================================================================================="""

@app.route("/user/<args>", methods=['GET'])
def user(args):

    args = myParseArgs(args)
    
    if 'skip' in args.keys():
        args['skip'] = int(args['skip'])
    if 'limit' in args.keys():
        args['limit'] = int(args['limit'])

    data = []
    
    #.skip(1).limit(1)
    
    if 'skip' in args.keys() and 'limit' in args.keys():
        result = userdb.find({},{'_id':0}).skip(args['skip']).limit(args['limit'])
    elif 'skip' in args.keys():
        result = userdb.find({},{'_id':0}).skip(args['skip'])
    elif 'limit' in args.keys():
        result = userdb.find({},{'_id':0}).limit(args['limit'])
    else:
        result = userdb.find({},{'_id':0}).limit(10)  

    for row in result:
        data.append(row)


    return {"data":data}
    


@app.route("/business/<args>", methods=['GET'])
def business(args):

    args = myParseArgs(args)
    
    data = []
    
    result = businessdb.find({},{'_id':0}).limit(100)
    
    for row in result:
        data.append(row)
    

    return {"data":data}
"""=================================================================================="""
def snap_time(time,snap_val):
    time = int(time)
    m = time % snap_val
    if m < (snap_val // 2):
        time -= m
    else:
        time += (snap_val - m)
        
    if (time + 40) % 100 == 0:
        time += 40
        
    return int(time)

"""=================================================================================="""
def myParseArgs(pairs=None):
    """Parses a url for key value pairs. Not very RESTful.
    Splits on ":"'s first, then "=" signs.
    
    Args:
        pairs: string of key value pairs
        
    Example:
    
        curl -X GET http://cs.mwsu.edu:5000/images/
        
    Returns:
        json object with all images
    """
    
    if not pairs:
        return {}
    
    argsList = pairs.split(":")
    argsDict = {}

    for arg in argsList:
        key,val = arg.split("=")
        argsDict[key]=str(val)
        
    return argsDict
    

if __name__ == "__main__":
    app.run(debug=True,host='107.170.48.163',port=5000)
