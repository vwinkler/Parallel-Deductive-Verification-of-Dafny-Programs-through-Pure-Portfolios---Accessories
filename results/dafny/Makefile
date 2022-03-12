make_job=../../dafnyportfolio/src/job_creation/make_job.py
solve_script=../../../dafnyportfolio/src/solve.py

run.sh : $(make_job) job.json
	python $(make_job) job.json $(solve_script) > $@
