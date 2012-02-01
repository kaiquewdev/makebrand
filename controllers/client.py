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
	pass
