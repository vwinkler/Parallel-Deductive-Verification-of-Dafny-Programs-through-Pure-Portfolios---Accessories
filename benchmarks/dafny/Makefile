assert_dfys = $(filter-out $(wildcard *.noassert.dfy), $(wildcard *.dfy))
tmp_noassert_dfys = $(patsubst %.dfy, _%.noassert.dfy, $(assert_dfys))
noassert_dfys = $(patsubst %.dfy, %.noassert.dfy, $(assert_dfys))

all: $(noassert_dfys)
	
_%.noassert.dfy : %.dfy
	#test -s $@.patch || cp $< $@ && patch -o $@ $< $@.patch
	if [[ -s $@.patch ]];\
	then\
		patch -o $@ $< $@.patch;\
	else\
		cp $< $@;\
	fi

__%.noassert.dfy : _%.noassert.dfy
	./remove_assertions.sh < $< > $@

%.noassert.dfy : __%.noassert.dfy
	dafny /noVerify /compile:0 /noIncludes $< ; [ $$? -ne 2 ] && cp $< $@

clean:
	-$(RM) $(tmp_noassert_dfys)
