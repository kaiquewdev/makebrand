# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    return {}

def user():
    return dict(form=auth())


def download():
    return response.download(request,db)


def call():
    return service()


@auth.requires_signature()
def data():
    return dict(form=crud())

