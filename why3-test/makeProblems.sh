#!/bin/sh

echo "theory HelloProof"
echo "use int.Int"

for (( i=0; i <= 1000; i++ ))
do
	echo   "goal G$i: forall x,y:int. x*y < 0 <-> (x < 0 \/ y < 0) /\ (x > 0 \/ y > 0)"
done

echo "end"
