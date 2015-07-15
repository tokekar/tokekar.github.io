import json
import os
import errno


def loaddata(json_file_path):
	json_file = open(json_file_path).read()
	data = json.loads(json_file)
	return data


def main():
	data = loaddata("pubs_autogen.json")
	fileid = open("abstract.txt",'w')

	for entry in data:
		fileid.write(entry['abstract'].encode('utf-8'))
	
	fileid.close()
	

if __name__ == "__main__":
	main()
