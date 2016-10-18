FILES := vanDerPol.pdf
AUXFILES := $(FILES:.pdf=.aux)
LOGFILES := $(FILES:.pdf=.log)
BBLFILES := $(FILES:.pdf=.bbl)
BLGFILES := $(FILES:.pdf=.blg)
OTHERS := vanDerPolav vanDerPol.out vanDerPol.snm vanDerPol.toc vanDerPol.nav vanDerPol.pdf
PICS := $(wildcard *.png)
PYC := $(wildcard *.pyc)
main : vanDerPol.py
	python vanDerPol.py
	make pdf

pdf : $(FILES:.pdf=.tex)
	make vanDerPol.pdf

%.pdf: %.tex 
	pdflatex $<

clean:	 
	$(RM) $(AUXFILES) $(LOGFILES) $(BBLFILES) $(BLGFILES) $(OTHERS) $(PICS) $(PYC)
	