boogie \
/infer:j \
/proverOpt:O:auto_config=false \
/proverOpt:O:type_check=true \
/proverOpt:O:smt.case_split=3 \
/proverOpt:O:smt.qi.eager_threshold=100 \
/proverOpt:O:smt.delay_units=true \
/proverOpt:O:smt.arith.solver=2 \
$@
