PYTHON=python3
EVAL_SCRIPTS=../../dafnyportfolio/src/evaluation/
PORTFOLIO_ASSEMBLING_RESULTS=../../results/dafny/portfolio_assembling/
BOOL_PARAMS_RESULTS=../../results/dafny/bool_params/
NOASSERT_RESULTS=../../results/dafny/noassert/
NOASSERT_MORE_ITERATIONS_RESULTS=../../results/dafny/noassert_more_iterations/
VALIDATION_RESULTS=../../results/dafny/validation/
MORE_ITERATIONS=../../results/dafny/more_iterations/
PARALLEL_VCS=../../results/dafny/parallel_vcs/
N_VBS_IRL=../../results/dafny/n-vbs_irl/
N_VBS_IRL_VALIDATION=../../results/dafny/n-vbs_irl_validation
DEFAULT=../../results/dafny/default_config
SELECTION=../../results/dafny/selection

evaluation_prefixes := primary noassert noassert_more_iterations bool_params validation \
                       more_iterations parallel_vcs n-vbs_irl n-vbs_irl_validation default \
                       selection

evaluations := $(patsubst %, %_evaluation, $(evaluation_prefixes))
ps := 1 2 3 4 5 6 7 8
n-vbs_h5 := $(patsubst %, vbs_%_vbs.h5, $(ps))
n-vbs_html := $(patsubst %, vbs_comparison/%_vbs.html, $(ps))

all : $(evaluations) misc

$(evaluations) : %_evaluation : \
	%_evaluation/01.txt \
	%_evaluation/01.svg \
	%_evaluation/01_correlation_start_time.svg \
	%_evaluation/01_correlation_call_number.svg \
	%_evaluation/01_correlation_job_number.svg \
	%_evaluation/01_correlation_call_in_job_number.svg \
	%_evaluation/01_correlation_median_runtime.svg \
	%_evaluation/01_relative.svg \
	%_evaluation/01.html \
	%_evaluation/01.ods \
	%_evaluation/01_configuration_ranking.txt \
	%_evaluation/01_top_configurations_per_benchmark.txt \
	%_evaluation/01_gaps.txt \
	%_evaluation/01_heuristic_cascading_n_vbs_matrix.html \
	%_evaluation/01_heuristic_cascading_n_vbs_matrix.ods \
	%_evaluation/01_best_speedup_lineplot.svg \
	%_evaluation/01_best_speedup_by_benchmark_lineplot.svg \
	%_evaluation/01_best_speedup_boxplot.svg \
	%_evaluation/01_best_speedup.txt \
	%_evaluation/01_inverted_cactus.svg \
	%_evaluation/01_top_config_latex_table.tex

misc : vbs_comparison/cactus_with_vbs.svg \
	vbs_comparison/cactus_with_n-vbs.svg \
	$(n-vbs_html) \
	vbs_n-vbs_portfolio_comparison/cactus_with_vbs.svg \
	vbs_n-vbs_portfolio_comparison/cactus_with_n-vbs.svg \
	external_comparison/cactus_1.svg \
	external_comparison/cactus_8.svg \
	external_comparison/cactus_c.svg \
	external_comparison/cactus_optk_1.svg \
	external_comparison/cactus_optk_8.svg \
	external_comparison/cactus_optk_c.svg

primary_results_list.txt : $(PORTFOLIO_ASSEMBLING_RESULTS)
	find $^ -name '*.json' > $@
	
noassert_results_list.txt : $(NOASSERT_RESULTS)
	find $^ -name '*.json' > $@
	
noassert_more_iterations_results_list.txt : $(NOASSERT_MORE_ITERATIONS_RESULTS)
	find $^ -name '*.json' > $@
	
bool_params_results_list.txt : $(BOOL_PARAMS_RESULTS)
	find $^ -name '*.json' > $@
	
validation_results_list.txt : $(VALIDATION_RESULTS)
	find $^ -name '*.json' > $@

more_iterations_results_list.txt : $(MORE_ITERATIONS)
	find $^ -name '*.json' > $@
	
parallel_vcs_results_list.txt : $(PARALLEL_VCS)
	find $^ -name '*.json' > $@
	
n-vbs_irl_results_list.txt : $(N_VBS_IRL)
	find $^ -name '*.json' > $@
	
n-vbs_irl_validation_results_list.txt : $(N_VBS_IRL_VALIDATION)
	find $^ -name '*.json' > $@
	
default_results_list.txt : $(DEFAULT)
	find $^ -name '*.json' > $@
	
selection_results_list.txt : $(SELECTION)
	find $^ -name '*.json' > $@

%_collection.h5 : %_results_list.txt
	$(PYTHON) $(EVAL_SCRIPTS)/collect.py $@ - < $<
	
%_penalized_collection.h5 : %_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/penalize_results.py $< $@ --max-runtime 600 --penalty-runtime 1200
	
%_unpenalized_matrix.h5 : %_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/make_matrix.py $< $@
	
%_std_matrix.h5 : %_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/make_matrix.py --agg std $< $@
	
%_penalized_matrix.h5 : %_unpenalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/penalize_empty_cells.py $< $@ --penalty-runtime 1200

%_evaluation/01_correlation_start_time.svg : %_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_correlation.py $< --with start_time --plot-file $@

%_evaluation/01_correlation_call_number.svg : %_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_correlation.py $< --with call_number --plot-file $@

%_evaluation/01_correlation_job_number.svg : %_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_correlation.py $< --with job_number --plot-file $@

%_evaluation/01_correlation_call_in_job_number.svg : %_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_correlation.py $< --with call_in_job_number --plot-file $@

%_evaluation/01_correlation_median_runtime.svg : %_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_correlation.py $< --with call_in_job_number --plot-file $@

%_evaluation/01_gaps.txt : %_unpenalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/report_empty_cells.py $< > $@

%_evaluation/01.txt : %_penalized_matrix.h5
	mkdir -p $(@D)
	$(PYTHON) $(EVAL_SCRIPTS)/print_axis_labels.py $< > $@
	
%_evaluation/01.html : %_penalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/export_html.py $< $@
	
%_evaluation/01_std.html : %_std_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/export_html.py $< $@

%_evaluation/01.ods : %_penalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/export_ods.py $< $@

%_evaluation/01.svg : %_penalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_matrix.py $< $@ --max-value 1200
	
%_evaluation/01_relative.svg : %_penalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_matrix.py $< $@ --max-value 10 --plot-differences
	
%_evaluation/01_configuration_ranking.txt : %_penalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/rank_configurations.py $< > $@ --max-runtime 600
	
%_evaluation/01_top_configurations_per_benchmark.txt : %_penalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/print_top_configurations_per_benchmark.py $< > $@
	
%_cascading_n_vbs_matrix.h5  : %_penalized_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/make_n_vbs_matrix.py $< $@ 16

%_evaluation/01_heuristic_cascading_n_vbs_matrix.html : %_cascading_n_vbs_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/export_html.py $< $@
	
%_evaluation/01_heuristic_cascading_n_vbs_matrix.ods : %_cascading_n_vbs_matrix.h5
	$(PYTHON) $(EVAL_SCRIPTS)/export_ods.py $< $@

%_evaluation/01_best_speedup_lineplot.svg : %_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_best_speedup.py $< --plot-file $@
	
%_evaluation/01_best_speedup_by_benchmark_lineplot.svg  : %_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_best_speedup_benchmark_lines.py $< --plot-file $@ --errorbars
	
%_evaluation/01_best_speedup_boxplot.svg : %_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_best_speedup.py --boxplot $< --plot-file $@
	
%_evaluation/01_best_speedup.txt : %_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_best_speedup.py $< --info-file $@

%_evaluation/01_inverted_cactus.svg : %_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_inverted_cactus.py $< --plot-file $@

vbs_comparison_collection.h5 : more_iterations_penalized_collection.h5 primary_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/combine_results.py $^ $@ --param source -1 portfolio -2 all
	
vbs_comparison/cactus_with_vbs.svg : vbs_comparison_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_inverted_cactus_with_vbs.py $< --plot-file $@
	
vbs_comparison/cactus_with_n-vbs.svg : vbs_comparison_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_inverted_cactus_with_n-vbs.py $< --plot-file $@
	
$(n-vbs_h5) : vbs_%_vbs.h5 : selection_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/make_n-vbs.py $^ $@ $(patsubst vbs_%_vbs.h5, %, $@)
	
$(n-vbs_html) : vbs_comparison/%_vbs.html : vbs_%_vbs.h5
	$(PYTHON) $(EVAL_SCRIPTS)/export_html.py $< $@

vbs_n-vbs_portfolio_comparison_collection.h5 : n-vbs_irl_penalized_collection.h5 selection_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/combine_results.py $^ $@ --param source -1 portfolio -2 all
	
vbs_n-vbs_portfolio_comparison/cactus_with_vbs.svg : vbs_n-vbs_portfolio_comparison_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_inverted_cactus_with_vbs.py $< --plot-file $@

vbs_n-vbs_portfolio_comparison/cactus_with_n-vbs.svg : vbs_n-vbs_portfolio_comparison_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/plot_inverted_cactus_with_n-vbs.py $< --plot-file $@
	
external_comparison.h5 : more_iterations_penalized_collection.h5 parallel_vcs_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/combine_results.py $^ $@ --param source -1 more_iterations -2 parallel_vcs

external_comparison/cactus_1.svg : external_comparison.h5
	mkdir -p $(@D)
	$(PYTHON) $(EVAL_SCRIPTS)/plot_n_vcs_cactus.py $< --plot-file $@ --approach 's=p'

external_comparison/cactus_8.svg : external_comparison.h5
	mkdir -p $(@D)
	$(PYTHON) $(EVAL_SCRIPTS)/plot_n_vcs_cactus.py $< --plot-file $@ --approach 's=8p'

external_comparison/cactus_c.svg : external_comparison.h5
	mkdir -p $(@D)
	$(PYTHON) $(EVAL_SCRIPTS)/plot_n_vcs_cactus.py $< --plot-file $@ --approach 's=const>>p'
	
external_comparison_optk.h5 : n-vbs_irl_penalized_collection.h5 parallel_vcs_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/combine_results.py $^ $@ --param source -1 more_iterations -2 parallel_vcs

external_comparison/cactus_optk_1.svg : external_comparison_optk.h5
	mkdir -p $(@D)
	$(PYTHON) $(EVAL_SCRIPTS)/plot_n_vcs_cactus.py $< --plot-file $@ --approach 's=p'

external_comparison/cactus_optk_8.svg : external_comparison_optk.h5
	mkdir -p $(@D)
	$(PYTHON) $(EVAL_SCRIPTS)/plot_n_vcs_cactus.py $< --plot-file $@ --approach 's=8p'

external_comparison/cactus_optk_c.svg : external_comparison_optk.h5
	mkdir -p $(@D)
	$(PYTHON) $(EVAL_SCRIPTS)/plot_n_vcs_cactus.py $< --plot-file $@ --approach 's=const>>p'
	
%_evaluation/01_top_config_latex_table.tex : %_penalized_collection.h5
	$(PYTHON) $(EVAL_SCRIPTS)/print_vbs_latex_table.py --prefix '\dafnycl{' --suffix '}' $< > $@

.PRECIOUS: %_collection.h5 %_penalized_matrix.h5
.PHONY: all $(evaluations) misc
