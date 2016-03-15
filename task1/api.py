# -*- coding: utf-8 -*-


from flask import Flask
from flask import request
from flask import Response
app = Flask(__name__)
app.debug = True
# Create the appropriate app.route functions, test and see if they work, and paste your URI’s in the boxes below.

#Make an app.route() decorator here
@app.route("/puppies", methods=['GET','POST'])
def puppiesFunction():
  if request.method == 'GET':
      return getAllPuppies()#Call the method to Get all of the puppies


  elif request.method == 'POST':
      return Response(makeANewPuppy(), status=301)
    #Call the method to make a new puppy



#Make another app.route() decorator here that takes in an integer id in the
@app.route("/puppies/<int:id>", methods=['GET','PUT','DELETE'])
def puppiesFunctionId(id):
  if request.method == 'GET':
      return getPuppy(id)
    #Call the method to get a specific puppy based on their id

  if request.method == 'PUT':
    #Call the method to update a puppy
        return Response(response=updatePuppy(id), status=301)
  elif request.method == 'DELETE':
    #Call the method to remove a puppy
        return Response(deletePuppy(id), status=301)


  return "Getting All the puppies!"

def makeANewPuppy():
  return "Creating A New Puppy!"

def getPuppy(id):
    return "Getting Puppy with id %s" % id

def updatePuppy(id):
  return "Updating a Puppy with id %s" % id

def deletePuppy(id):
  return "Removing Puppy with id %s" % id


app.run()
