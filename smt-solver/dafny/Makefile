smt2ToProblem = ../util/makeProblem.py

all : $(patsubst %.dfy, %.problem.json, $(wildcard *.dfy))

%.problem.json : %.smt2 $(smt2ToProblem)
	python $(smt2ToProblem) --in $< --out $@

%.smt2 : %.log.smt2
	./reduceSmt.sh $< > $@

%.log.smt2 : %.bpl
	boogie $< /proverLog:$@

%.bpl : %.dfy
	dafny $< /print:$@ /noVerify
