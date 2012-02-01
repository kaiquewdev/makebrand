# -*- coding: utf-8 -*-
from applications.makebrand.modules.utils import *

@auth.requires_login()
def index():
	clients = Table(db, 'client')
	return {'clients': clients}

@auth.requires_login()
def new():
	form = SQLFORM(db.client, fields=['name', 'description', 'avatar'])
	
	form.vars.visibility = True
	if form.accepts(request, session):
		response.flash = T('New client was inserted!')
	elif form.errors:
		response.flash = T('Please, verify the errors.')
	else:
		response.flash = T('Fill, the fields. Avatar is optional!')
	
	return {'form': form}

@auth.requires_login()
def profile():
	if not request.args: redirect(URL('client', 'index'))
	
	# Get information of this client, refencied by id in request args
	profileClient = Table(db, 'client').get({'id': request.args[0], 'visibility': True})[0]
	# Get name of all projects, created for this client
	projectsByThisClient = Table(db, 'project').get({'client_id': profileClient.id, 'visibility': True})
	
	return {'profileClient': profileClient,
			'projectsByThisClient': projectsByThisClient}
