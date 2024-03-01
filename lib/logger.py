import lib.const as const

def debug( *objects ):
	if const.DEBUG:
		print( '\033[94m', *objects, '\033[0m' )