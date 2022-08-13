import json

class ReadFileJson():
	def __init__(self, file):
		self.file = file
		self.data = None
		self.getReadFileJson(file)

	def getReadFileJson(self, file):
		# Opening JSON file
		f = open(file)

		# returns JSON object as a dictionary
		self.data = json.load(f)

		# Closing file
		f.close()

	def getData(self):
		return self.data