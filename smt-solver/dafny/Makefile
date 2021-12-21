all : $(patsubst %.dfy, %.problem.json, $(wildcard *.dfy))

%.problem.json : %.smt2 makeProblem.py
	python makeProblem.py --in $< --out $@

%.smt2 : %.log.smt2
	./reduceSmt.sh $< > $@

%.log.smt2 : %.bpl
	boogie $< /proverLog:$@

%.bpl : %.dfy
	dafny $< /print:$@ /noVerify
