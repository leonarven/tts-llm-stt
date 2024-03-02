from os import environ

def debug( *objects ):
	if environ.get("DEBUG") == str(True):
		print( '\033[94m', *objects, '\033[0m' )
