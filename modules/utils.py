# Class table tools
class Table( object ):
    # Define db and tablename
	def __init__(self, db, tablename):
		self.db = db
		self.tablename = tablename
	
	# Mount a query
	def setQuery(self, fields={}):
		try:
			db = self.db
			table = db.get(self.tablename)
			if fields:
				query = (table)
				for field in fields:
					if table.has_key(field):
						query = query and ( table.get(field) == fields[field] )
				
				return query
			else:
				return False
						
		except Exception:
			return False
	
    # Get informations of table by fields or all informations
	def get(self, fields={}, order=''):
		try:
			db = self.db
			table = db.get(self.tablename)
			query = self.setQuery(fields)
			
			if query:
				if order:	
					return db( query ).select( table.ALL, orderby=~table.get(order))
				elif not order:
					return db( query ).select()
			else:
				if order:
					return db().select( table.ALL, orderby=~table.get(order) )
				elif not order:
					return db().select( table.ALL )
		except Exception:
			return False
	
	# Get counter of all rows or rows by specified fields
	def score(self, fields={}):
		try:
			db = self.db
			table = db.get(self.tablename)
			query = self.setQuery(fields)
			
			if query:
				return db(query).count()
			else:
				return db(table).count()
		except Exception:
			return False

# Create html elements, based on fields table of the db
class HTMLstick( object ):
	# Define a default properties, for create a element
	def __init__(self, db, tablename=''):
		self.db = db
		self.tablename = tablename
	
	# get information of table for mout structure of a future element
	def struct(self, value='', label=''):
		db = self.db
		table = db.get(self.tablename)
		
		try:
			if value and label:
				options = []
				
				if not options:
					selection = db(table).select()
					if selection: 
						for row in :
							if row.has_key(value) and row.has_key(label):
								item = {'value': row.get(value), 'label': row.get(label)}
							
								if not item in options:
									options.append(item)
							else:
								return False
						return options
					else:
						return False
				else:
					return False
			else:
				return False
		except Exception:
			return False
	
	# This function mount a html element
	def picker(self, fields={}, select={}, options={}):
		# select => for the picker
		# options => for all options in this select
		try:
			if fields and select and options:
				pickerSelect = SELECT()
				
				
		except Exception:
			return False
