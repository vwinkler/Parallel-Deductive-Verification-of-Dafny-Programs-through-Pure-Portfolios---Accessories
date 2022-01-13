smt2ToProblem = ../util/makeProblem.py

all : $(patsubst %.smt2, %.problem.json, $(wildcard *.smt2))

%.problem.json : %.smt2 $(smt2ToProblem)
	python $(smt2ToProblem) --in $< --out $@
	
