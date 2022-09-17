# Parallel-Deductive-Verification-of-Dafny-Programs-through-Pure-Portfolios---Accessories

This repository contains the source code, benchmarks, results and means to generate the figures
of my thesis "Parallel Deductive Verification of Dafny Programs through Pure Portfolios"
(2022, Karlsruhe Institute of Technology).
It deals with the composition of a pure portfolio of parallel running instances
of the [Dafny verification tool](https://github.com/dafny-lang/dafny)
and aims to reduce the wall-clock time to verifiy Dafny programs.
The portfolio is selected based on about 40 benchmarks
and evaluated using six additional benchmarks for validation.

* **benchmarks/** contains the benchmarks used for the selection and evaluation
* **containers/** facilitates the generation of a Docker container for the selection and evaluation
* **dafnyportfolio/** contains the source code of the portfolio and the evaluation
* **evaluation/** facilitates the generation of the evaluation
* **excerpts/** contains excerpts of relevant papers
* **expose/** holds the expose made prior to work on the thesis
* **reports/** contains specific investigations done during the work on the thesis
* **results/** contains benchmarking results of the portfolio used in the evaluation
