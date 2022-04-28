all : $(patsubst %.dfy, %.bpl, $(wildcard *.dfy))

convert_dafny_to_boogie : 
	echo '#!/bin/sh' > $@
	echo 'dafny $$1 /print:$$2 /noVerify' >> $@
	chmod +x $@

%.bpl : %.dfy convert_dafny_to_boogie
	./convert_dafny_to_boogie $< $@
