make_job=../../dafnyportfolio/src/job_creation/make_job.py
make_cloud_job=../../dafnyportfolio/src/job_creation/make_cloud_job.py
solve_script=../../../dafnyportfolio/src/solve.py
container_image=vwinkler/dafnyportfolio-evaluation

all : run.sh run_cloud_dev_single.sh run_cloud_single.sh run_local_container.sh

run.sh : $(make_job) job.json
	python $(make_job) --dfy-base-path ../../../benchmarks/dafny/ job.json $(solve_script) > $@
	
run_cloud_dev_single.sh : print_warning.sh $(make_cloud_job) job.json
	cat print_warning.sh > $@
	python $(make_cloud_job) --results-base-path dev/ --dfy-base-path ../../benchmarks/dafny/ job.json dev_single vwinkler+dafnyportfolio-evaluation >> $@

run_cloud_single.sh : print_warning.sh $(make_cloud_job) job.json
	cat print_warning.sh > $@
	python $(make_cloud_job) --results-base-path experiments/ --dfy-base-path ../../benchmarks/dafny/ job.json single vwinkler+dafnyportfolio-evaluation >> $@
	
run_local_container.sh : $(make_cloud_job) job.json
	cat print_warning.sh > $@
	python $(make_cloud_job) --container-framework docker --omit-sbatch --dfy-base-path ../../benchmarks/dafny/ job.json single vwinkler/dafnyportfolio-evaluation >> $@
