DATADIR=data
OUTDIR=..
PUBPARTDIR=pubs/part
JSON=$(DATADIR)/pubs_autogen.json

all: index pub-generator pub-index-generator

index:
	cat $(DATADIR)/header.part $(DATADIR)/about.part $(DATADIR)/news.part $(DATADIR)/research.part $(DATADIR)/publications.part $(DATADIR)/teaching.part $(DATADIR)/service.part $(DATADIR)/footer.part > $(OUTDIR)/index.html

pub-generator:
	python pub-generator.py $(DATADIR)/header.part $(DATADIR)/footer.part $(PUBPARTDIR) $(OUTDIR) $(JSON)

pub-index-generator:
	#python pub-index-generator.py
