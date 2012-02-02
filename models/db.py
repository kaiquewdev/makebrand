# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables()

## configure email
mail=auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################


# Signature, register datatime of the data who was create
signature = db.Table(db, 
					 'signature',
					 Field('created_on', 'datetime', default=request.now),
					 Field('created_by', db.auth_user, default=auth.user_id),			
					 Field('updated_on', 'datetime', default=request.now),
					 Field('updated_by', db.auth_user, default=auth.user_id) )

# Briefing media table
db.define_table('media', 
				Field('name', 'string'),
				Field('description', 'text'),
				Field('visibility', 'boolean'),
				Field('file', 'upload'),
				signature)
				
# Briefing client table
db.define_table('client', 
                Field('name', 'string', requires=[IS_NOT_EMPTY()]),
                Field('description', 'text', requires=[IS_NOT_EMPTY()]),
                Field('visibility', 'boolean'),
                Field('user_id', db.auth_user, default= auth.user_id),
                Field('avatar', 'upload', db.media), 
                signature)

# Briefing project table
db.define_table('project', 
				Field('name', 'string'),
				Field('description', 'text'),
				Field('terminated', 'boolean'),
				Field('client_id', db.client),
				Field('user_id', db.auth_user, default= auth.user_id),
				signature)

db.project.client_id.widget = SQLFORM.widgets.options.widget(db.project, db.project.name, requires=[IS_NOT_EMPTY])

# Briefing sub project table
db.define_table('subproject', 
				Field('name', 'string'),
				Field('description', 'text'),
				Field('visibility', 'boolean'),
				Field('project_id', db.project),
				Field('user_id', db.auth_user, default= auth.user_id),
				signature)

# Briefing question table
db.define_table('question', 
				Field('name', 'string'),
				Field('description', 'text'),
				Field('visibility', 'boolean'),
				Field('project_id', db.project),
				Field('subproject_id', db.project),
				Field('user_id', db.auth_user, default= auth.user_id),
				signature)

# Briefing answer table
db.define_table('answer', 
				Field('name', 'string'),
				Field('description', 'text'),
				Field('visibility', 'boolean'),
				Field('project_id', db.project),
				Field('subproject_id', db.subproject),
				Field('user_id', db.auth_user, default= auth.user_id),
				Field('file', db.media),
				signature)
