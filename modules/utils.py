# Class table tools
class Table( object ):
    # Define db and tablename
	def __init__(self, db, tablename=''):
		self.db = db
		self.tablename = tablename
	
    # Get informations of table by fields or all informations
	def get(self, fields={}, order=''):
		try:
			db = self.db
			table = db.get(self.tablename)
	
			if fields:
				query = ( table )
				
				for field in fields:
					query = query and ( table[field] == fields[field] )
	
				return db( query ).select()
			else:
				return db().select( table.ALL )
		except Exception:
			return False
	
	# Get counter of all rows or rows by specified fields
	def score(self, fields={}):
		try:
			db = self.db
			table = db.get(self.tablename)

			if fields:
				query = ( table )

				for field in fields:
					query = query and ( table[field] == fields[field] )

				return db( query ).count()
			else:
				return db( table ).count()
		except Exception:
			return False
