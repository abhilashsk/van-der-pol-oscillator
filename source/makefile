FILES := 130010006.pdf
AUXFILES := $(FILES:.pdf=.aux)
LOGFILES := $(FILES:.pdf=.log)
BBLFILES := $(FILES:.pdf=.bbl)
BLGFILES := $(FILES:.pdf=.blg)

OTHERS := 130010006.nav 130010006.out 130010006.snm 130010006.toc 130010006.nav 
PICS := $(wildcard *.png)
PYC := $(wildcard *.pyc)
main : vanDerPol.py
	python vanDerPol.py
	make pdf
	python html.py

pdf : $(FILES:.pdf=.tex)
	make 130010006.pdf

%.pdf: %.tex 
	pdflatex $<
	bibtex `echo $< |cut -d "." -f1`.aux
	pdflatex $<
	pdflatex $<
	mv 130010006.pdf ../output/130010006.pdf

test : tests.py
	python tests.py
	
clean:	 
	$(RM) $(AUXFILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) $(OTHERS) $(PICS) $(PYC)
	rm -rf __pycache__
	