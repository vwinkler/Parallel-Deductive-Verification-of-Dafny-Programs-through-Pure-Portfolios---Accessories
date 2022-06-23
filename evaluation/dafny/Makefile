PYTHON=python3
PORTFOLIO_ASSEMBLING_RESULTS=../../results/dafny/portfolio_assembling/
BOOL_PARAMS_RESULTS=../../results/dafny/bool_params/
NOASSERT_RESULTS=../../results/dafny/noassert/
VALIDATION_RESULTS=../../results/dafny/validation/
MORE_ITERATIONS=../../results/dafny/more_iterations/

evaluation_prefixes := primary noassert bool_params validation more_iterations

evaluations := $(patsubst %, %_evaluation, $(evaluation_prefixes))

all : $(evaluations)

$(evaluations) : %_evaluation : \
	%_evaluation/01.txt \
	%_evaluation/01.svg \
	%_evaluation/01_relative.svg \
	%_evaluation/01.html \
	%_evaluation/01.ods \
	%_evaluation/01_configuration_ranking.txt \
	%_evaluation/01_top_configurations_per_benchmark.txt \
	%_evaluation/01_gaps.txt \
	%_evaluation/01_heuristic_cascading_n_vbs_matrix.html \
	%_evaluation/01_heuristic_cascading_n_vbs_matrix.ods \
	%_evaluation/01_best_speedup_lineplot.svg \
	%_evaluation/01_best_speedup_boxplot.svg \
	%_evaluation/01_best_speedup.txt \
	%_evaluation/01_inverted_cactus.svg 

primary_results_list.txt : $(PORTFOLIO_ASSEMBLING_RESULTS)
	find $^ -name '*.json' > $@
	
noassert_results_list.txt : $(NOASSERT_RESULTS)
	find $^ -name '*.json' > $@
	
bool_params_results_list.txt : $(BOOL_PARAMS_RESULTS)
	find $^ -name '*.json' > $@
	
validation_results_list.txt : $(VALIDATION_RESULTS)
	find $^ -name '*.json' > $@

more_iterations_results_list.txt : $(MORE_ITERATIONS)
	find $^ -name '*.json' > $@

%_collection.h5 : %_results_list.txt
	$(PYTHON) collect.py $@ - < $<
	
%_penalized_collection.h5 : %_collection.h5
	$(PYTHON) penalize_results.py $< $@ --max-runtime 600 --penalty-runtime 1200
	
%_unpenalized_matrix.h5 : %_penalized_collection.h5
	$(PYTHON) make_matrix.py $< $@
	
%_penalized_matrix.h5 : %_unpenalized_matrix.h5
	$(PYTHON) penalize_empty_cells.py $< $@ --penalty-runtime 1200

%_evaluation/01_gaps.txt : %_unpenalized_matrix.h5
	$(PYTHON) report_empty_cells.py $< > $@

%_evaluation/01.txt : %_penalized_matrix.h5
	mkdir -p $(@D)
	$(PYTHON) print_axis_labels.py $< > $@
	
%_evaluation/01.html : %_penalized_matrix.h5
	$(PYTHON) export_html.py $< $@
	
%_evaluation/01.ods : %_penalized_matrix.h5
	$(PYTHON) export_ods.py $< $@

%_evaluation/01.svg : %_penalized_matrix.h5
	$(PYTHON) plot_matrix.py $< $@ --max-value 1200
	
%_evaluation/01_relative.svg : %_penalized_matrix.h5
	$(PYTHON) plot_matrix.py $< $@ --max-value 10 --plot-differences
	
%_evaluation/01_configuration_ranking.txt : %_penalized_matrix.h5
	$(PYTHON) rank_configurations.py $< > $@ --max-runtime 600
	
%_evaluation/01_top_configurations_per_benchmark.txt : %_penalized_matrix.h5
	$(PYTHON) print_top_configurations_per_benchmark.py $< > $@
	
%_cascading_n_vbs_matrix.h5  : %_penalized_matrix.h5
	$(PYTHON) make_n_vbs_matrix.py $< $@ 16

%_evaluation/01_heuristic_cascading_n_vbs_matrix.html : %_cascading_n_vbs_matrix.h5
	$(PYTHON) export_html.py $< $@
	
%_evaluation/01_heuristic_cascading_n_vbs_matrix.ods : %_cascading_n_vbs_matrix.h5
	$(PYTHON) export_ods.py $< $@

%_evaluation/01_best_speedup_lineplot.svg : %_penalized_collection.h5
	$(PYTHON) plot_best_speedup.py $< --plot-file $@
	
%_evaluation/01_best_speedup_boxplot.svg : %_penalized_collection.h5
	$(PYTHON) plot_best_speedup.py --boxplot $< --plot-file $@
	
%_evaluation/01_best_speedup.txt : %_penalized_collection.h5
	$(PYTHON) plot_best_speedup.py $< --info-file $@

%_evaluation/01_inverted_cactus.svg : %_penalized_collection.h5
	$(PYTHON) plot_inverted_cactus.py $< --plot-file $@

.PRECIOUS: %_collection.h5 %_penalized_matrix.h5
.PHONY: all $(evaluations)
