import json

class ReadFileJson():
	def __init__(self, file):
		self.file = file
		self.full_data_from_json_file = None
		self.get_read_file_json(file)

	def get_read_file_json(self, file):
		# Opening JSON file
		f = open(file)

		# returns JSON object as a dictionary
		self.full_data_from_json_file = json.load(f)

		# Closing file
		f.close()

	def get_full_data(self):
		return self.full_data_from_json_file