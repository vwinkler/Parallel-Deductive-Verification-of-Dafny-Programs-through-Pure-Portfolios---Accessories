all : $(patsubst %.dfy, %.bpl, $(wildcard *.dfy))

%.bpl : %.dfy
	dafny $< /print:$@ /noVerify
