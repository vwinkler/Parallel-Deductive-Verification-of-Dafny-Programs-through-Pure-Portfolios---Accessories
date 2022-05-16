#/bin/sh

#sed 's/assert\([^; ]*\( \+\([^;b ]\|b[^y;]\)\)\?\)*\(;\| \+;\| \+b;\| \+by *{[^}]*}\)/assert true;/'
#sed 's/assert\([^; v]*\(var[^;]*\|\( \+\([^;b ]\|b[^y;]\)\)\?\)\)*\(;\| \+;\| \+b;\| \+by *{[^}]*}\)/assert true;/'
#sed 's#^\(\s*\)assert#\1//assert#g'
#sed 's#\(assert\([^;]*;\s*\([^$/]\|/[^/]\)\)*;\s*\)\($\|//\)#\1#g'
sed 's#assert\(\s*\(var [^;]*;\)*[^;]*;\)#assert true;#g'
