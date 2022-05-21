PORTFOLIO_ASSEMBLING_RESULTS=../../results/dafny/portfolio_assembling/
BOOL_PARAMS_RESULTS=../../results/dafny/bool_params/
NOASSERT_RESULTS=../../results/dafny/noassert/

all : primary_evaluation noassert_evaluation

primary_results_list.txt : $(PORTFOLIO_ASSEMBLING_RESULTS) $(BOOL_PARAMS_RESULTS)
	find $^ -name '*.json' > $@
	
noassert_results_list.txt : $(NOASSERT_RESULTS)
	find $^ -name '*.json' > $@

%_collection.h5 : %_results_list.txt collect.py
	python collect.py $@ - < $<
	
%_penalized_collection.h5 : %_collection.h5
	python penalize_results.py $< $@

%_evaluation : %_penalized_collection.h5 make_matrix.py
	mkdir -p $@
	python make_matrix.py $< --target-dir $@
	touch $@ # make sure timestamp is updated

.PRECIOUS: %_collection.h5
