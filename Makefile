OUT=output/pdf

.PHONY: all clean check

all:
	mkdir -p $(OUT)
	xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUT) main.tex
	bibtex $(OUT)/main.aux
	xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUT) main.tex
	xelatex -interaction=nonstopmode -halt-on-error -output-directory=$(OUT) main.tex

check:
	python3 scripts/check_book.py

clean:
	rm -f $(OUT)/main.{aux,bbl,bcf,blg,log,out,run.xml,toc,lof,lot,fdb_latexmk,fls,pdf}
