make_job=../../dafnyportfolio/src/job_creation/make_job.py
make_cloud_job=../../dafnyportfolio/src/job_creation/make_cloud_job.py
solve_script=../../../dafnyportfolio/src/solve.py
container_image=vwinkler/dafnyportfolio-evaluation
print_result_filenames=../../dafnyportfolio/src/job_creation/print_result_filenames.py

local_run_scripts=$(patsubst %.job.json, %_run.sh, $(wildcard *.job.json))
local_container_run_scripts=$(patsubst %.job.json, %_run_cloud_dev_single.sh, $(wildcard *.job.json))
cluster_container_run_scripts=$(patsubst %.job.json, %_run_cloud_single.sh, $(wildcard *.job.json))
dev_cluster_container_run_scripts=$(patsubst %.job.json, %_run_local_container.sh, $(wildcard *.job.json))
cluster_container_target_dirs=$(patsubst %.job.json, %/, $(wildcard *.job.json))
dev_cluster_container_target_dirs=$(patsubst %.job.json, dev/%/, $(wildcard *.job.json))
cluster_container_extra_results=$(patsubst %.job.json, %_run_cloud_single_extra_results.out, $(wildcard *.job.json))
cluster_container_missing_results=$(patsubst %.job.json, %_run_cloud_single_missing_results.out, $(wildcard *.job.json))

all : \
	$(local_run_scripts) \
	$(local_container_run_scripts) \
	$(cluster_container_run_scripts) \
	$(dev_cluster_container_run_scripts)

extra: $(cluster_container_extra_results)
missing: $(cluster_container_missing_results)

%_run.sh : %.job.json $(make_job) .
	python $(make_job) --omit-existing --dfy-base-path ../../../benchmarks/dafny/ $< $(solve_script) > $@
	
%_run_cloud_dev_single.sh : %.job.json print_warning.sh $(make_cloud_job) dev/%/
	target_dir="$(patsubst %_run_cloud_dev_single.sh,%, $@)";\
	echo "#!/bin/sh" > $@;\
	echo "mkdir -p $$target_dir" >> $@;\
	cat print_warning.sh >> $@;\
	python $(make_cloud_job) --omit-existing --max-jobs 100 --results-base-path dev/$$target_dir/ --dfy-base-path ../../benchmarks/dafny/ $< dev_single vwinkler+dafnyportfolio-evaluation >> $@

%_run_cloud_single.sh : %.job.json print_warning.sh $(make_cloud_job) %/
	target_dir="$(patsubst %_run_cloud_single.sh,%, $@)";\
	echo "#!/bin/sh" > $@;\
	echo "mkdir -p $$target_dir" >> $@;\
	cat print_warning.sh >> $@;\
	python $(make_cloud_job) --omit-existing --max-jobs 100 --results-base-path $(patsubst %_run_cloud_single.sh,%, $@)/ --dfy-base-path ../../benchmarks/dafny/ $< single vwinkler+dafnyportfolio-evaluation >> $@
	
%_run_local_container.sh : %.job.json $(make_cloud_job) .
	cat print_warning.sh > $@
	python $(make_cloud_job) --omit-existing --container-framework docker --omit-sbatch --dfy-base-path ../../benchmarks/dafny/ $< single vwinkler/dafnyportfolio-evaluation >> $@

$(cluster_container_target) $(dev_cluster_container_target_dirs) :
	mkdir -p $@

%/ : 
	mkdir -p %/

%_run_cloud_single_expected_results.out : %.job.json
	target_dir="$(patsubst %_run_cloud_single_expected_results.out,%, $@)";\
	python $(print_result_filenames) $< --results-base-path $$target_dir > $@ &&\
	sort $@ -o $@

%_run_cloud_single_existing_results.out : %/
	find $< -name '*.json' > $@
	sort $@ -o $@

%_run_cloud_single_extra_results.out : %_run_cloud_single_expected_results.out %_run_cloud_single_existing_results.out
	comm -13 $^ > $@

%_run_cloud_single_missing_results.out : %_run_cloud_single_expected_results.out %_run_cloud_single_existing_results.out
	comm -23 $^ > $@


