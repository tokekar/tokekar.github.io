import json
import os
import errno


def loaddata(json_file_path):
	json_file = open(json_file_path).read()
	data = json.loads(json_file)
	return data


def main():
	data = loaddata("pubs_autogen.json")
	fileid = open("publications.html",'w')
	fileid.write(open('header.part.html','r').read())
	fileid.write("<div class=\"panel\">")

	for val in data:
		fileid.write("<p>")
		fileid.write(open(val['id']+'.part.html','r').read())
		fileid.write("</p>")

	fileid.write("</div>")
	fileid.write(open('footer.part.html','r').read())


if __name__ == "__main__":
	main()
