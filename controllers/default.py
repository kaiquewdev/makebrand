# -*- coding: utf-8 -*-
from applications.makebrand.modules.utils import *

@auth.requires_login()
def index():
	clients = Table(db, 'client')
    
	return {'clients': clients}

def user():
    return dict(form=auth())


def download():
    return response.download(request,db)


def call():
    return service()


@auth.requires_signature()
def data():
    return dict(form=crud())

