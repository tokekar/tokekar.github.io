PART=part.html

all: index pub-generator pub-index-generator

index:
	cat header.$(PART) about.$(PART) news.$(PART) research.$(PART) publications.$(PART) teaching.$(PART) service.$(PART) footer.$(PART) > index.html

pub-generator:
	python pub-generator.py

pub-index-generator:
	python pub-index-generator.py
