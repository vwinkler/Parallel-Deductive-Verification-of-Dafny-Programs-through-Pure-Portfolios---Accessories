find_method_runtimes=python ../../../dafnyportfolio/src/parse_runtimes.py
all_times=$(patsubst %.xml, %_times.txt, $(wildcard *.xml))

sorted-times.txt : $(all_times)
	./sort_benchmarks.sh $^ > $@
	
%_times.txt : %.xml
	$(find_method_runtimes) $< > $@
	
