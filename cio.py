def lock(filename):
	from os import system
	system(f'chmod -r+w-x {filename}')
def ulock(filename):
	from os import system
	system(f'chmod +r+x+w {filename}')
def get_settings(filename):
	from ast import literal_eval
	ulock(filename)
	with open(filename,'r') as inf:
		settings = literal_eval(inf.read())
	lock(filename)
	return settings