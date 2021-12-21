# The last part of the example requires a QF_LIA solver to be installed.
#
#
# This example shows how to interact with files in the SMT-LIB
# format. In particular:
#
# 1. How to read a file in SMT-LIB format
# 2. How to write a file in SMT-LIB format
# 3. Formulas and SMT-LIB script
# 4. How to access annotations from SMT-LIB files
# 5. How to extend the parser with custom commands
#
from six.moves import cStringIO # Py2-Py3 Compatibility

from pysmt.smtlib.parser import SmtLibParser
from pysmt.parsing import parse


# To make the example self contained, we store the example SMT-LIB
# script in a string.
DEMO_SMTLIB=\
"""
(set-logic QF_LIA)
(declare-fun p () Int)
(declare-fun q () Int)
(declare-fun x () Bool)
(declare-fun y () Bool)
(define-fun .def_1 () Bool (! (and x y) :cost 1))
(assert (=> x (> p q)))
(check-sat)
(push)
(assert (=> y (> q p)))
(check-sat)
(assert .def_1)
(check-sat)
(pop)
(check-sat)
"""

# We read the SMT-LIB Script by creating a Parser.
# From here we can get the SMT-LIB script.
parser = SmtLibParser()

# The method SmtLibParser.get_script takes a buffer in input. We use
# cStringIO to simulate an open file.
# See SmtLibParser.get_script_fname() if to pass the path of a file.
script = parser.get_script(cStringIO(DEMO_SMTLIB))

print(type(script))
script.add("assert", args=[parse("1 < 2")])
#script.add(parser.get_formula("x < y"))

# The SmtLibScript provides an iterable representation of the commands
# that are present in the SMT-LIB file.
#
# Printing a summary of the issued commands
for cmd in script:
    print(cmd.name)
print("*"*50)

# SmtLibScript provides some utilities to perform common operations: e.g,
#
# - Checking if a command is present
assert script.contains_command("check-sat")
# - Counting the occurrences of a command
assert script.count_command_occurrences("assert") == 4
# - Obtain all commands of a particular type
decls = script.filter_by_command_name("declare-fun")
for d in decls:
    print(d)
print("*"*50)

# Most SMT-LIB scripts define a single SAT call. In these cases, the
# result can be obtained by conjoining multiple assertions.  The
# method to do that is SmtLibScript.get_strict_formula() that, raises
# an exception if there are push/pop calls.  To obtain the formula at
# the end of the execution of the Script (accounting for push/pop) we
# use get_last_formula
#
f = script.get_last_formula()
print(f)

# Finally, we serialize the script back into SMT-Lib format.  This can
# be dumped into a file (see SmtLibScript.to_file).  The flag daggify,
# specifies whether the printing is done as a DAG or as a tree.

buf_out = cStringIO()
script.serialize(buf_out, daggify=True)
print(buf_out.getvalue())

print("*"*50)
# Expressions can be annotated in order to provide additional
# information. The semantic of annotations is solver/problem
# dependent. For example, VMT uses annotations to identify two
# expressions as 1) the Transition Relation and 2) Initial Condition
#
# Here we pretend that we make up a ficticious Weighted SMT format
# and label .def1 with cost 1
#
# The class pysmt.smtlib.annotations.Annotations deals with the
# handling of annotations.
#
ann = script.annotations
print(ann.all_annotated_formulae("cost"))

print("*"*50)


