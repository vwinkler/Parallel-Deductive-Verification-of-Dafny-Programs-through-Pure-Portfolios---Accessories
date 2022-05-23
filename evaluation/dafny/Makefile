PYTHON=python3
PORTFOLIO_ASSEMBLING_RESULTS=../../results/dafny/portfolio_assembling/
BOOL_PARAMS_RESULTS=../../results/dafny/bool_params/
NOASSERT_RESULTS=../../results/dafny/noassert/

evaluation_prefixes := primary noassert

evaluations := $(patsubst %, %_evaluation, $(evaluation_prefixes))

all : $(evaluations)

$(evaluations) : %_evaluation : \
	%_evaluation/01.txt \
	%_evaluation/01.svg \
	%_evaluation/01_relative.svg \
	%_evaluation/01.html \
	%_evaluation/01.ods \
	%_evaluation/01_configuration_ranking.txt \
	%_evaluation/01_top_configurations_per_benchmark.txt


primary_results_list.txt : $(PORTFOLIO_ASSEMBLING_RESULTS) $(BOOL_PARAMS_RESULTS)
	find $^ -name '*.json' > $@
	
noassert_results_list.txt : $(NOASSERT_RESULTS)
	find $^ -name '*.json' > $@

%_collection.h5 : %_results_list.txt
	$(PYTHON) collect.py $@ - < $<
	
%_penalized_collection.h5 : %_collection.h5
	$(PYTHON) penalize_results.py $< $@ --max-runtime 600 --penalty-runtime 1200
	
%_matrix.h5 : %_penalized_collection.h5
	$(PYTHON) make_matrix.py $< $@ --penalty-runtime 1200

%_evaluation/01.txt : %_matrix.h5
	mkdir -p $(@D)
	$(PYTHON) print_axis_labels.py $< > $@
	
%_evaluation/01.html : %_matrix.h5
	$(PYTHON) export_html.py $< $@
	
%_evaluation/01.ods : %_matrix.h5
	$(PYTHON) export_ods.py $< $@

%_evaluation/01.svg : %_matrix.h5
	$(PYTHON) plot_matrix.py $< $@ --max-value 1200
	
%_evaluation/01_relative.svg : %_matrix.h5
	$(PYTHON) plot_matrix.py $< $@ --max-value 10 --plot-differences
	
%_evaluation/01_configuration_ranking.txt : %_matrix.h5
	$(PYTHON) rank_configurations.py $< > $@ --max-runtime 600
	
%_evaluation/01_top_configurations_per_benchmark.txt : %_matrix.h5
	$(PYTHON) print_top_configurations_per_benchmark.py $< > $@

.PRECIOUS: %.h5
.PHONY: all $(evaluations)
