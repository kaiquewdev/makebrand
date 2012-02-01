# -*- coding: utf-8 -*-
from applications.makebrand.modules.utils import *

@auth.requires_login()
def index():
	projects = Table(db, 'project')
    
	return {'projects': projects}

@auth.requires_login()
def new():
	form = SQLFORM(db.project)
	
	return {'form': form}

@auth.requires_login()
def profile():
	#if not request.args: redirect(URL('project', 'index'))
	
	return {}
