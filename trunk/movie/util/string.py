def list2str(l, jstr=''):
	if type(l)==list:
		return jstr.join(l)
	else:
		return l