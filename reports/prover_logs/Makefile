logging_z3=../../smt-solver/util/logged_z3.sh
logs=test_dafny_prover_log_intercepted\
     test_dafny_prover_log_prover-option\
     test_boogie_prover_log_intercepted\
     test_boogie_prover_log_prover-option\
     test_boogie_prover_log_boogie-option
difference_of_prover_logs_tex=difference_of_prover_logs.tex

all: difference_of_prover_logs.pdf $(logs)

%.bpl : %.dfy
	dafny /print:$@ $< /noVerify

%_dafny_prover_log_intercepted : %.dfy
	dafny /proverOpt:PROVER_PATH=$(logging_z3) $<
	mv logfile $@

%_dafny_prover_log_prover-option : %.dfy
	dafny /proverOpt:LOG_FILE=$@ $<

%_boogie_prover_log_intercepted : %.bpl
	boogie /proverOpt:PROVER_PATH=$(logging_z3) $<
	mv logfile $@

%_boogie_prover_log_prover-option : %.bpl
	boogie /proverOpt:LOG_FILE=$@ $<

%_boogie_prover_log_boogie-option : %.bpl
	boogie /proverLog:$@ $<

wc_of_logs.txt : $(logs)
	wc -l $^ > $@

wc_of_logs_definitions.tex : wc_of_logs.txt
	cat $< | sed -rn "s/^\s+([0-9]+)\s+([a-zA-Z0-9_-]+)$$/\\\def\\\\\2{\1}/p" \
		| sed "s/[_-]//g" > $@

difference_of_prover_logs_wrapper.tex : wc_of_logs_definitions.tex
	cp $< $@
	printf "\n" >> $@
	printf "\\input{$(difference_of_prover_logs_tex)}" >> $@
	printf "\n" >> $@

difference_of_prover_logs.pdf : \
	difference_of_prover_logs_wrapper.tex $(difference_of_prover_logs_tex)
	latexmk -pdf -jobname=$(basename $@) $<


