def file_search(folder, filename):
	inner_folders    = []
	current_folder   = folder[0]

	if folder[0] == filename:
		return folder[0]

	for item in folder[1:]:
		if isinstance(item, list):
			inner_folders.append(item)
		else:
			if item == filename:
				return current_folder + "/" + filename

	for inner_folder in inner_folders:
		search_in_inner_folder = file_search(inner_folder, filename)
		if search_in_inner_folder:
			return current_folder + "/" + search_in_inner_folder

	return False

# testing
print "RESULTS:"
print "========================"
print file_search(['C:', 'backup.log', 'ideas.txt'], 'ideas.txt')
print "========================"
print file_search([ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py'], 'new folder1')
print "========================"
print file_search([ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py'], 'hereiam.py')
print "========================"
print file_search(['C:', 'backup.log', 'ideas.txt'], 'C:')
print "========================"