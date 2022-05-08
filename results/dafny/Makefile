make_job=../../dafnyportfolio/src/job_creation/make_job.py
make_cloud_job=../../dafnyportfolio/src/job_creation/make_cloud_job.py
solve_script=../../../dafnyportfolio/src/solve.py
container_image=vwinkler/dafnyportfolio-evaluation


local_run_scripts=$(patsubst %.job.json, %_run.sh, $(wildcard *.job.json))
local_container_run_scripts=$(patsubst %.job.json, %_run_cloud_dev_single.sh, $(wildcard *.job.json))
cluster_container_run_scripts=$(patsubst %.job.json, %_run_cloud_single.sh, $(wildcard *.job.json))
dev_cluster_container_run_scripts=$(patsubst %.job.json, %_run_local_container.sh, $(wildcard *.job.json))

all : \
	$(local_run_scripts) \
	$(local_container_run_scripts) \
	$(cluster_container_run_scripts) \
	$(dev_cluster_container_run_scripts)

%_run.sh : %.job.json $(make_job)
	python $(make_job) --dfy-base-path ../../../benchmarks/dafny/ $< $(solve_script) > $@
	
%_run_cloud_dev_single.sh : %.job.json print_warning.sh $(make_cloud_job)
	target_dir="$(patsubst %_run_cloud_dev_single.sh,%, $@)";\
	echo "#!/bin/sh" > $@;\
	echo "mkdir -p $$target_dir" >> $@;\
	cat print_warning.sh >> $@;\
	python $(make_cloud_job) --max-jobs 200 --results-base-path dev/$$target_dir/ --skip-existing --dfy-base-path ../../benchmarks/dafny/ $< dev_single vwinkler+dafnyportfolio-evaluation >> $@

%_run_cloud_single.sh : %.job.json print_warning.sh $(make_cloud_job)
	target_dir="$(patsubst %_run_cloud_single.sh,%, $@)";\
	echo "#!/bin/sh" > $@;\
	echo "mkdir -p $$target_dir" >> $@;\
	cat print_warning.sh >> $@;\
	python $(make_cloud_job) --max-jobs 200 --results-base-path $(patsubst %_run_cloud_single.sh,%, $@)/ --skip-existing --dfy-base-path ../../benchmarks/dafny/ $< single vwinkler+dafnyportfolio-evaluation >> $@
	
%_run_local_container.sh : %.job.json $(make_cloud_job)
	cat print_warning.sh > $@
	python $(make_cloud_job) --container-framework docker --skip-existing --omit-sbatch --dfy-base-path ../../benchmarks/dafny/ $< single vwinkler/dafnyportfolio-evaluation >> $@
