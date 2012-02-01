# -*- coding: utf-8 -*-
from applications.makebrand.modules.utils import *

@auth.requires_login()
def index():
	clients = Table(db, 'client')
	return {'clients': clients}

@auth.requires_login()
def new():
	pass

@auth.requires_login()
def profile():
	pass
