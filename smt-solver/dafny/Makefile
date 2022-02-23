smt2ToProblem = ../util/makeProblem.py
dfy_path = ../../benchmarks/dafny

all : $(patsubst %.dfy, %.problem.json, $(wildcard $(dfy_path)/*.dfy))

%.problem.json : %.smt2 $(smt2ToProblem)
	python $(smt2ToProblem) --in $< --out $@

%.smt2 : %.log.smt2
	./reduceSmt.sh $< > $@

%.log.smt2 : %.bpl
	boogie $< /proverLog:$@

%.bpl : $(dfy_path)/%.dfy
	dafny $< /print:$@ /noVerify
