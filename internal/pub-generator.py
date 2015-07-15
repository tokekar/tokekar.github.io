import json
import os
import errno

def createpartpub(entry,fileid):
    fileid.write("<a href=\"" + entry['id'] + ".html\">")
    fileid.write("<b>"+entry['title'].replace("{",'').replace("}",'')+"</a>.</b>")
    fileid.write("<br />\n")
    fileid.write(entry['author'].replace(" and "," &middot; ").replace("}","").replace("{","") + ". ")
    fileid.write("<br />\n")
    fileid.write("<i>"+entry.get('booktitle','')+entry.get('journal','')+"</i>, " + entry['year'])
    return


def addbibtexline(entry,key,start,end):
    bibtex = ''
    if key in entry:
        bibtex = '&nbsp;&nbsp;&nbsp;&nbsp;'
        bibtex += key + ' = ' + start + entry[key] + end
        bibtex += ',<br />'
    return bibtex


def createbibtex(entry):
    bibtex = '@' + entry['type'] + '{ ' + entry['id'] + ',<br />'
    bibtex += addbibtexline(entry,'title','\"','\"')
    bibtex += addbibtexline(entry,'author','{','}')
    bibtex += addbibtexline(entry,'booktitle','{','}')
    bibtex += addbibtexline(entry,'journal','{','}')
    bibtex += addbibtexline(entry,'year','\"','\"')
    bibtex += addbibtexline(entry,'doi','\"','\"')
    bibtex += addbibtexline(entry,'note','\"','\"')
    bibtex += '}'
    return bibtex


def createfullpub(entry,fileid,header,footer):
    fileid.write(open(header).read())
    fileid.write("<div class=\"panel\">")
    fileid.write("<h2 class=\"section\">"+entry['title'].replace("{",'').replace("}",'')+"</h2>")
    fileid.write("\n")
    fileid.write("<h3>"+entry['author'].replace(" and "," &middot; ").replace("}","").replace("{","")+"</h3>")
    fileid.write("\n")
    fileid.write("<p>")
    fileid.write("<i>"+entry.get('booktitle','')+"</i>\n")
    fileid.write("<i>"+entry.get('journal','')+"</i>\n")
    fileid.write("<i>"+entry['year']+"</i>\n")
    fileid.write("</p>")
    if 'pdf' in entry:
        fileid.write('<a href="'+entry['pdf']+'">pdf</a>')
        fileid.write(" &middot; ")
        fileid.write("\n")
    if 'slides' in entry:
        fileid.write('<a href="'+entry['slides']+'">slides</a>')
        fileid.write(" &middot; ")
        fileid.write("\n")
    if 'abstract' in entry:
        fileid.write('<h4>Abstract</h4>')
        fileid.write('<p>'+entry['abstract'].encode('utf-8')+'</p>')
    fileid.write("<blockquote>")
    fileid.write(createbibtex(entry))
    fileid.write("</blockquote>")
    if 'youtube' in entry:
        fileid.write("<div class=\"videowrapper\">")
        fileid.write(createyoutubeembed(entry['youtube']))
        fileid.write("\n")
        fileid.write("</div>")
    fileid.write("</div>")
    fileid.write(open(footer).read())
    return


def loaddata(json_file_path):
    json_file = open(json_file_path).read()
    data = json.loads(json_file)
    return data


def createyoutubeembed(url):
    value = '<iframe width="560" height="315" src="https://www.youtube.com/embed/'+url+'" frameborder="0" allowfullscreen></iframe>'
    return value


def main():

    parser = argparse.ArgumentParser('Pub Generator')
    parser.add_argument('header', help='path to the header.part file', type=str)
    parser.add_argument('footer', help='path to the footer.part file', type=str)
    parser.add_argument('pubpartdir', help='path to the directory which will contain the part files for publications', type=str)
    parser.add_argument('outdir', help='path to the output directory', type=str)
    parser.add_argument('json', help='path to the json file containing the publication data', type=str)
    args = parser.parse_args()

    data = loaddata(args.json)

    for val in data:
        key = val['id']

        fullpubfile = open(args.outdir+"/"+key+".html",'w')
        fullpub = createfullpub(val,fullpubfile,args.header,args.footer)
        fullpubfile.close()

        partpubfile = open(args.pubpartdir+"/"+key+".part",'w')
        partpub = createpartpub(val,partpubfile)
        partpubfile.close()


if __name__ == "__main__":
    main()
