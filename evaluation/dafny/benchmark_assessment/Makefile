find_method_runtimes=python ../../../dafnyportfolio/src/parse_runtimes.py

all : $(patsubst %.xml, %_times.txt, $(wildcard *.xml))
	
%_times.txt : %.xml
	$(find_method_runtimes) $< > $@
