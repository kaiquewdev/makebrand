# -*- coding: utf-8 -*-
from applications.makebrand.modules.utils import *

@auth.requires_login()
def index():
	projects = Table(db, 'project')
    
	return {'projects': projects}

@auth.requires_login()
def new():
	form = SQLFORM(db.project, fields=['name', 'description', 'client_id'])
	
	form.vars.terminated = False
	if form.accepts(request, session):
		response.flash = T('New project was created!')
	elif form.errors:
		response.flash = T('Please, verify the errors.')
	else:
		response.flash = T('Fill, the fields.')
	
	return {'form': form}

@auth.requires_login()
def profile():
	#if not request.args: redirect(URL('project', 'index'))
	
	return {}
