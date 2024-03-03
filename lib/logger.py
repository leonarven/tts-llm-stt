from os import environ

def debug( *objects ):
	if environ.get("VERBOSE") == str(True):
		print( '\033[94m', *objects, '\033[0m' )
