(set-info :smt-lib-version 2.6)
(set-logic AUFNIRA)
(set-info :source |Benchmarks from the paper: "Extending Sledgehammer with SMT Solvers" by Jasmin Blanchette, Sascha Bohme, and Lawrence C. Paulson, CADE 2011.  Translated to SMT2 by Andrew Reynolds and Morgan Deters.|)
(set-info :category "industrial")
(set-info :status unsat)
(declare-sort S1 0)
(declare-sort S2 0)
(declare-sort S3 0)
(declare-sort S4 0)
(declare-sort S5 0)
(declare-sort S6 0)
(declare-sort S7 0)
(declare-sort S8 0)
(declare-sort S9 0)
(declare-sort S10 0)
(declare-sort S11 0)
(declare-sort S12 0)
(declare-sort S13 0)
(declare-fun f1 () S1)
(declare-fun f2 () S1)
(declare-fun f3 (S2 Real) Real)
(declare-fun f4 () S2)
(declare-fun f5 () Real)
(declare-fun f6 () Real)
(declare-fun f7 () S2)
(declare-fun f8 (S3 Real) S2)
(declare-fun f9 () S3)
(declare-fun f10 () S2)
(declare-fun f11 () S3)
(declare-fun f12 () S2)
(declare-fun f13 (S4 Int) Int)
(declare-fun f14 () S4)
(declare-fun f15 (S5 Int) S4)
(declare-fun f16 () S5)
(declare-fun f17 () S2)
(declare-fun f18 () S2)
(declare-fun f19 () S2)
(declare-fun f20 (S7 S6) Real)
(declare-fun f21 () S7)
(declare-fun f22 (S8 Int) S6)
(declare-fun f23 () S8)
(declare-fun f24 (S9 S6) Int)
(declare-fun f25 () S9)
(declare-fun f26 (S10 Real) S7)
(declare-fun f27 () S10)
(declare-fun f28 (S11 Int) S9)
(declare-fun f29 () S11)
(declare-fun f30 (S12 S6) S6)
(declare-fun f31 (S13 S6) S12)
(declare-fun f32 () S13)
(declare-fun f33 () S13)
(assert (not (= f1 f2)))
(assert (not (not (= (f3 f4 f5) 0.0))))
(assert (< f6 f5))
(assert (< f5 (* 2.0 f6)))
(assert (not (= (f3 f4 (- f5 f6)) 0.0)))
(assert (< f6 f5))
(assert (< f5 (* 2.0 f6)))
(assert (< 0.0 f5))
(assert (not (= (f3 f4 (- f5 f6)) 0.0)))
(assert (< 0.0 (- f5 f6)))
(assert (< (- f5 f6) f6))
(assert (let ((?v_0 0.0)) (=> (< ?v_0 f5) (=> (< f5 f6) (not (= (f3 f4 f5) ?v_0))))))
(assert (forall ((?v0 Real)) (= (f3 f4 (- ?v0 f6)) (- (f3 f4 ?v0)))))
(assert (let ((?v_0 0.0)) (= (f3 f4 ?v_0) ?v_0)))
(assert (forall ((?v0 Real)) (<= (- 1.0) (f3 f4 ?v0))))
(assert (forall ((?v0 Real)) (<= (f3 f4 ?v0) 1.0)))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 f4 ?v0))) (<= (ite (< ?v_0 0.0) (- ?v_0) ?v_0) 1.0))))
(assert (forall ((?v0 Real)) (= (f3 f4 (- ?v0)) (- (f3 f4 ?v0)))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (=> (< ?v_0 ?v0) (=> (< ?v0 2.0) (< ?v_0 (f3 f4 ?v0)))))))
(assert (=> (= f5 f6) (not (= (f3 f7 f5) 1.0))))
(assert (= (f3 f4 f6) 0.0))
(assert (forall ((?v0 Real)) (= (f3 f4 (+ f6 ?v0)) (- (f3 f4 ?v0)))))
(assert (forall ((?v0 Real)) (= (f3 f4 (+ ?v0 f6)) (- (f3 f4 ?v0)))))
(assert (forall ((?v0 Real)) (= (f3 f4 (+ ?v0 (* 2.0 f6))) (f3 f4 ?v0))))
(assert (not (= f6 0.0)))
(assert (not (< f6 0.0)))
(assert (not (= (f3 f7 2.0) 0.0)))
(assert (< 0.0 f6))
(assert (<= 0.0 f6))
(assert (< f6 4.0))
(assert (= (f3 f7 0.0) 1.0))
(assert (= (f3 f7 f6) (- 1.0)))
(assert (forall ((?v0 Real)) (<= (- 1.0) (f3 f7 ?v0))))
(assert (forall ((?v0 Real)) (<= (f3 f7 ?v0) 1.0)))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 f7 ?v0))) (<= (ite (< ?v_0 0.0) (- ?v_0) ?v_0) 1.0))))
(assert (forall ((?v0 Real)) (= (f3 f7 (- ?v0)) (f3 f7 ?v0))))
(assert (<= 2.0 f6))
(assert (< (f3 f7 2.0) 0.0))
(assert (<= (f3 f7 2.0) 0.0))
(assert (forall ((?v0 Real)) (= (f3 f7 (+ ?v0 f6)) (- (f3 f7 ?v0)))))
(assert (forall ((?v0 Real)) (= (f3 f7 (+ ?v0 (* 2.0 f6))) (f3 f7 ?v0))))
(assert (= (f3 f7 (* 2.0 f6)) 1.0))
(assert (< (- (* 2.0 f6)) f6))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (<= 0.0 ?v0) (=> (< ?v0 ?v1) (=> (<= ?v1 f6) (< (f3 f7 ?v1) (f3 f7 ?v0)))))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (<= 0.0 ?v0) (=> (<= ?v0 ?v1) (=> (<= ?v1 f6) (<= (f3 f7 ?v1) (f3 f7 ?v0)))))))
(assert (forall ((?v0 Real)) (let ((?v_0 2.0)) (=> (< 0.0 ?v0) (=> (< ?v0 ?v_0) (< (f3 f7 (* ?v_0 ?v0)) 1.0))))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (<= (- f6) ?v0) (=> (< ?v0 ?v1) (=> (<= ?v1 0.0) (< (f3 f7 ?v0) (f3 f7 ?v1)))))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (<= (- f6) ?v0) (=> (<= ?v0 ?v1) (=> (<= ?v1 0.0) (<= (f3 f7 ?v0) (f3 f7 ?v1)))))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0) (?v_1 (f3 f7 ?v0))) (=> (= (f3 f4 ?v0) ?v_0) (= (ite (< ?v_1 ?v_0) (- ?v_1) ?v_1) 1.0)))))
(assert (forall ((?v0 Real)) (=> (= (f3 f7 ?v0) 1.0) (= (f3 f4 ?v0) 0.0))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (=> (<= ?v_0 ?v0) (=> (<= ?v0 f6) (<= ?v_0 (f3 f4 ?v0)))))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (=> (< ?v_0 ?v0) (=> (< ?v0 f6) (< ?v_0 (f3 f4 ?v0)))))))
(assert (= (f3 f4 (* 2.0 f6)) 0.0))
(assert (forall ((?v0 Real)) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (exists ((?v1 Real)) (and (and (<= 0.0 ?v1) (and (<= ?v1 f6) (= (f3 f7 ?v1) ?v0))) (forall ((?v2 Real)) (=> (and (<= 0.0 ?v2) (and (<= ?v2 f6) (= (f3 f7 ?v2) ?v0))) (= ?v2 ?v1)))))))))
(assert (exists ((?v0 Real)) (let ((?v_0 0.0)) (and (and (<= ?v_0 ?v0) (and (<= ?v0 2.0) (= (f3 f7 ?v0) ?v_0))) (forall ((?v1 Real)) (=> (and (<= ?v_0 ?v1) (and (<= ?v1 2.0) (= (f3 f7 ?v1) ?v_0))) (= ?v1 ?v0)))))))
(assert (forall ((?v0 Real)) (= (f3 f7 ?v0) (f3 f4 (- (f3 (f8 f9 f6) 2.0) ?v0)))))
(assert (forall ((?v0 Real)) (= (f3 f4 ?v0) (f3 f7 (- (f3 (f8 f9 f6) 2.0) ?v0)))))
(assert (forall ((?v0 Real)) (= (- (f3 f4 ?v0)) (f3 f7 (+ ?v0 (f3 (f8 f9 f6) 2.0))))))
(assert (forall ((?v0 Real)) (=> (<= 0.0 ?v0) (=> (<= ?v0 f6) (= (f3 f10 (f3 f7 ?v0)) ?v0)))))
(assert (forall ((?v0 Real)) (=> (<= ?v0 0.0) (=> (<= (- f6) ?v0) (= (f3 f10 (f3 f7 ?v0)) (- ?v0))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 f10 ?v0))) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (and (<= 0.0 ?v_0) (and (<= ?v_0 f6) (= (f3 f7 ?v_0) ?v0))))))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 f7 (+ ?v0 ?v1)) (- (f3 (f8 f11 (f3 f7 ?v0)) (f3 f7 ?v1)) (f3 (f8 f11 (f3 f4 ?v0)) (f3 f4 ?v1))))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 f7 (- ?v0 ?v1)) (+ (f3 (f8 f11 (f3 f7 ?v0)) (f3 f7 ?v1)) (f3 (f8 f11 (f3 f4 ?v0)) (f3 f4 ?v1))))))
(assert (forall ((?v0 Real)) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (<= 0.0 (f3 f10 ?v0))))))
(assert (= (f3 f7 (f3 (f8 f11 (f3 (f8 f9 3.0) 2.0)) f6)) 0.0))
(assert (= (f3 f4 (f3 (f8 f11 (f3 (f8 f9 3.0) 2.0)) f6)) (- 1.0)))
(assert (let ((?v_0 2.0)) (<= (f3 (f8 f9 f6) ?v_0) ?v_0)))
(assert (let ((?v_0 2.0)) (< (f3 (f8 f9 f6) ?v_0) ?v_0)))
(assert (< (- (f3 (f8 f9 f6) 2.0)) 0.0))
(assert (<= 0.0 (f3 (f8 f9 f6) 2.0)))
(assert (< 0.0 (f3 (f8 f9 f6) 2.0)))
(assert (let ((?v_0 2.0)) (not (= (f3 (f8 f9 f6) ?v_0) ?v_0))))
(assert (not (= (f3 (f8 f9 f6) 2.0) 0.0)))
(assert (forall ((?v0 Real)) (=> (<= (ite (< ?v0 0.0) (- ?v0) ?v0) 1.0) (= (f3 f7 (f3 f10 ?v0)) ?v0))))
(assert (forall ((?v0 Real)) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (= (f3 f7 (f3 f10 ?v0)) ?v0)))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 f10 ?v0))) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (and (<= 0.0 ?v_0) (<= ?v_0 f6)))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 f10 ?v0))) (=> (< (- 1.0) ?v0) (=> (< ?v0 1.0) (and (< 0.0 ?v_0) (< ?v_0 f6)))))))
(assert (forall ((?v0 Real)) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (<= (f3 f10 ?v0) f6)))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (=> (<= (- ?v_0) ?v0) (=> (<= ?v0 ?v_0) (<= 0.0 (f3 f7 ?v0)))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (=> (< (- ?v_0) ?v0) (=> (< ?v0 ?v_0) (< 0.0 (f3 f7 ?v0)))))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (=> (< ?v_0 ?v0) (=> (< ?v0 (f3 (f8 f9 f6) 2.0)) (< ?v_0 (f3 f7 ?v0)))))))
(assert (= (f3 f7 (f3 (f8 f9 f6) 3.0)) (f3 (f8 f9 1.0) 2.0)))
(assert (= (f3 f7 (f3 (f8 f9 f6) 2.0)) 0.0))
(assert (= (f3 f4 (f3 (f8 f9 f6) 2.0)) 1.0))
(assert (= (f3 f4 (f3 (f8 f9 f6) 6.0)) (f3 (f8 f9 1.0) 2.0)))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (=> (< ?v_0 ?v0) (=> (< ?v0 (f3 (f8 f9 f6) 2.0)) (< ?v_0 (f3 f4 ?v0)))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (=> (<= (- ?v_0) ?v0) (=> (<= ?v0 ?v1) (=> (<= ?v1 ?v_0) (<= (f3 f4 ?v0) (f3 f4 ?v1))))))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (=> (< (f3 (f8 f9 (- f6)) 2.0) ?v0) (=> (< ?v0 ?v_0) (< (f3 f4 ?v0) ?v_0))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 f7 ?v0)) (?v_1 (f3 f4 ?v0))) (= (+ (f3 (f8 f11 ?v_0) ?v_0) (f3 (f8 f11 ?v_1) ?v_1)) 1.0))))
(assert (forall ((?v0 Real)) (let ((?v_0 2.0)) (= (f3 f4 (* ?v_0 ?v0)) (f3 (f8 f11 (* ?v_0 (f3 f4 ?v0))) (f3 f7 ?v0))))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 f4 (- ?v0 ?v1)) (- (f3 (f8 f11 (f3 f4 ?v0)) (f3 f7 ?v1)) (f3 (f8 f11 (f3 f7 ?v0)) (f3 f4 ?v1))))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 f4 (- ?v0 ?v1)) (- (f3 (f8 f11 (f3 f7 ?v1)) (f3 f4 ?v0)) (f3 (f8 f11 (f3 f4 ?v1)) (f3 f7 ?v0))))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 f4 (+ ?v0 ?v1)) (+ (f3 (f8 f11 (f3 f4 ?v0)) (f3 f7 ?v1)) (f3 (f8 f11 (f3 f7 ?v0)) (f3 f4 ?v1))))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 f7 (- ?v0 ?v1)) (+ (f3 (f8 f11 (f3 f7 ?v1)) (f3 f7 ?v0)) (f3 (f8 f11 (f3 f4 ?v1)) (f3 f4 ?v0))))))
(assert (forall ((?v0 Real)) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (exists ((?v1 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (and (and (<= (- ?v_0) ?v1) (and (<= ?v1 ?v_0) (= (f3 f4 ?v1) ?v0))) (forall ((?v2 Real)) (=> (and (<= (- ?v_0) ?v2) (and (<= ?v2 ?v_0) (= (f3 f4 ?v2) ?v0))) (= ?v2 ?v1))))))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 (f8 f11 ?v0))) (= (f3 (f8 f9 (f3 ?v_0 ?v1)) (f3 ?v_0 ?v0)) (f3 (f8 f9 ?v1) ?v0)))))
(assert (forall ((?v0 S2) (?v1 Real) (?v2 Real)) (let ((?v_0 (f3 ?v0 ?v1)) (?v_1 (f3 ?v0 ?v2))) (let ((?v_2 (f8 f11 (f3 (f8 f9 (- ?v_1 ?v_0)) (- ?v2 ?v1))))) (= (- ?v_0 (f3 ?v_2 ?v1)) (- ?v_1 (f3 ?v_2 ?v2)))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real) (?v3 Real)) (= (f3 (f8 f11 (f3 (f8 f9 ?v0) ?v1)) (f3 (f8 f9 ?v2) ?v3)) (f3 (f8 f9 (f3 (f8 f11 ?v0) ?v2)) (f3 (f8 f11 ?v1) ?v3)))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 (f8 f11 ?v0))) (= (f3 ?v_0 (f3 (f8 f9 ?v1) ?v2)) (f3 (f8 f9 (f3 ?v_0 ?v1)) ?v2)))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (< ?v0 0.0) (exists ((?v2 Real) (?v3 Real)) (let ((?v_0 (f8 f11 ?v2))) (and (= ?v1 (f3 ?v_0 (f3 f7 ?v3))) (= ?v0 (f3 ?v_0 (f3 f4 ?v3)))))))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (< 0.0 ?v0) (exists ((?v2 Real) (?v3 Real)) (let ((?v_0 (f8 f11 ?v2))) (and (= ?v1 (f3 ?v_0 (f3 f7 ?v3))) (= ?v0 (f3 ?v_0 (f3 f4 ?v3)))))))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 f12 (f3 (f8 f11 ?v0) ?v1)) (f3 (f8 f11 (f3 f12 ?v0)) (f3 f12 ?v1)))))
(assert (forall ((?v0 Int) (?v1 Int)) (= (f13 f14 (f13 (f15 f16 ?v0) ?v1)) (f13 (f15 f16 (f13 f14 ?v0)) (f13 f14 ?v1)))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 f12 ?v0))) (= (f3 (f8 f11 ?v_0) ?v_0) (f3 (f8 f11 ?v0) ?v0)))))
(assert (forall ((?v0 Int)) (let ((?v_0 (f13 f14 ?v0))) (= (f13 (f15 f16 ?v_0) ?v_0) (f13 (f15 f16 ?v0) ?v0)))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 f12 (f3 (f8 f9 ?v0) ?v1)) (f3 (f8 f9 (f3 f12 ?v0)) (f3 f12 ?v1)))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (= (not (< ?v_0 (f3 (f8 f11 ?v0) ?v0))) (= ?v0 ?v_0)))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 2.0) (?v_1 (f8 f9 ?v1))) (= (= ?v0 (f3 ?v_1 (* ?v_0 ?v2))) (= (* ?v_0 ?v0) (f3 ?v_1 ?v2))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 2.0)) (= (- (f3 (f8 f9 (+ ?v0 ?v1)) ?v_0) ?v0) (f3 (f8 f9 (- ?v1 ?v0)) ?v_0)))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 2.0)) (= (- (f3 (f8 f9 (+ ?v0 ?v1)) ?v_0) ?v1) (f3 (f8 f9 (- ?v0 ?v1)) ?v_0)))))
(assert (forall ((?v0 Real) (?v1 Real)) (exists ((?v2 Real) (?v3 Real)) (let ((?v_0 (f8 f11 ?v2))) (and (= ?v0 (f3 ?v_0 (f3 f7 ?v3))) (= ?v1 (f3 ?v_0 (f3 f4 ?v3))))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 f17 ?v0))) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (and (<= (- (f3 (f8 f9 f6) 2.0)) ?v_0) (and (<= ?v_0 f6) (= (f3 f4 ?v_0) ?v0))))))))
(assert (forall ((?v0 Real)) (let ((?v_1 (f3 (f8 f9 f6) 2.0)) (?v_0 (f3 f17 ?v0))) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (and (<= (- ?v_1) ?v_0) (and (<= ?v_0 ?v_1) (= (f3 f4 ?v_0) ?v0))))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (=> (<= (- ?v_0) ?v0) (=> (<= ?v0 ?v_0) (= (f3 f17 (f3 f4 ?v0)) ?v0))))))
(assert (forall ((?v0 Real)) (let ((?v_1 2.0)) (let ((?v_0 (f3 (f8 f9 f6) ?v_1)) (?v_2 (* ?v_1 ?v0))) (=> (< (- ?v_0) ?v0) (=> (< ?v0 ?v_0) (= (f3 f18 ?v0) (f3 (f8 f9 (f3 f4 ?v_2)) (+ (f3 f7 ?v_2) 1.0)))))))))
(assert (let ((?v_0 0.0)) (= (f3 f18 ?v_0) ?v_0)))
(assert (forall ((?v0 Real)) (= (f3 f18 (- ?v0)) (- (f3 f18 ?v0)))))
(assert (forall ((?v0 Real)) (= (f3 f18 (+ ?v0 (* 2.0 f6))) (f3 f18 ?v0))))
(assert (forall ((?v0 Real)) (= (f3 f18 (+ ?v0 f6)) (f3 f18 ?v0))))
(assert (= (f3 f18 f6) 0.0))
(assert (forall ((?v0 Real)) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (= (f3 f4 (f3 f17 ?v0)) ?v0)))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (=> (< (f3 (f8 f9 (- f6)) 2.0) ?v0) (=> (< ?v0 ?v_0) (< (f3 f18 ?v0) ?v_0))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (let ((?v_1 (- ?v_0))) (=> (< ?v_1 ?v0) (=> (< ?v0 ?v_0) (=> (< ?v_1 ?v1) (=> (< ?v1 ?v_0) (= (< ?v0 ?v1) (< (f3 f18 ?v0) (f3 f18 ?v1)))))))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (=> (< (- ?v_0) ?v0) (=> (< ?v0 ?v1) (=> (< ?v1 ?v_0) (< (f3 f18 ?v0) (f3 f18 ?v1))))))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0)) (=> (< ?v_0 ?v0) (=> (< ?v0 (f3 (f8 f9 f6) 2.0)) (< ?v_0 (f3 f18 ?v0)))))))
(assert (forall ((?v0 Real)) (= (f3 (f8 f9 1.0) (f3 f18 ?v0)) (f3 f18 (- (f3 (f8 f9 f6) 2.0) ?v0)))))
(assert (= (f3 f18 (f3 (f8 f9 f6) 4.0)) 1.0))
(assert (forall ((?v0 Real)) (let ((?v_1 (f3 (f8 f9 f6) 2.0)) (?v_0 (f3 f17 ?v0))) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (and (<= (- ?v_1) ?v_0) (<= ?v_0 ?v_1)))))))
(assert (forall ((?v0 Real)) (let ((?v_1 (f3 (f8 f9 f6) 2.0)) (?v_0 (f3 f17 ?v0))) (=> (< (- 1.0) ?v0) (=> (< ?v0 1.0) (and (< (- ?v_1) ?v_0) (< ?v_0 ?v_1)))))))
(assert (forall ((?v0 Real)) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (<= (- (f3 (f8 f9 f6) 2.0)) (f3 f17 ?v0))))))
(assert (forall ((?v0 Real)) (=> (<= (- 1.0) ?v0) (=> (<= ?v0 1.0) (<= (f3 f17 ?v0) (f3 (f8 f9 f6) 2.0))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 0.0) (?v_1 (f3 f7 ?v0)) (?v_2 (f3 f7 ?v1))) (=> (not (= ?v_1 ?v_0)) (=> (not (= ?v_2 ?v_0)) (= (- 1.0 (f3 (f8 f11 (f3 f18 ?v0)) (f3 f18 ?v1))) (f3 (f8 f9 (f3 f7 (+ ?v0 ?v1))) (f3 (f8 f11 ?v_1) ?v_2))))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 0.0) (?v_1 (+ ?v0 ?v1)) (?v_2 (f3 f18 ?v0)) (?v_3 (f3 f18 ?v1))) (=> (not (= (f3 f7 ?v0) ?v_0)) (=> (not (= (f3 f7 ?v1) ?v_0)) (=> (not (= (f3 f7 ?v_1) ?v_0)) (= (f3 f18 ?v_1) (f3 (f8 f9 (+ ?v_2 ?v_3)) (- 1.0 (f3 (f8 f11 ?v_2) ?v_3))))))))))
(assert (forall ((?v0 Real)) (= (f3 f18 ?v0) (f3 (f8 f9 (f3 f4 ?v0)) (f3 f7 ?v0)))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 0.0) (?v_1 (f3 f7 ?v0)) (?v_2 (f3 f7 ?v1))) (=> (not (= ?v_1 ?v_0)) (=> (not (= ?v_2 ?v_0)) (= (+ (f3 f18 ?v0) (f3 f18 ?v1)) (f3 (f8 f9 (f3 f4 (+ ?v0 ?v1))) (f3 (f8 f11 ?v_1) ?v_2))))))))
(assert (forall ((?v0 Real)) (exists ((?v1 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (and (< (- ?v_0) ?v1) (and (< ?v1 ?v_0) (= (f3 f18 ?v1) ?v0)))))))
(assert (forall ((?v0 Real)) (exists ((?v1 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (and (and (< (- ?v_0) ?v1) (and (< ?v1 ?v_0) (= (f3 f18 ?v1) ?v0))) (forall ((?v2 Real)) (=> (and (< (- ?v_0) ?v2) (and (< ?v2 ?v_0) (= (f3 f18 ?v2) ?v0))) (= ?v2 ?v1))))))))
(assert (forall ((?v0 Real)) (=> (< 0.0 ?v0) (exists ((?v1 Real)) (and (< 0.0 ?v1) (and (< ?v1 (f3 (f8 f9 f6) 2.0)) (< ?v0 (f3 f18 ?v1))))))))
(assert (forall ((?v0 Real)) (=> (<= 0.0 ?v0) (exists ((?v1 Real)) (and (<= 0.0 ?v1) (and (< ?v1 (f3 (f8 f9 f6) 2.0)) (= (f3 f18 ?v1) ?v0)))))))
(assert (forall ((?v0 Real)) (=> (< (ite (< ?v0 0.0) (- ?v0) ?v0) 1.0) (exists ((?v1 Real)) (let ((?v_0 (f3 (f8 f9 f6) 4.0))) (and (< (- ?v_0) ?v1) (and (< ?v1 ?v_0) (= (f3 f18 ?v1) ?v0))))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f3 (f8 f9 f6) 2.0))) (=> (< (- ?v_0) ?v0) (=> (< ?v0 ?v_0) (= (f3 f19 (f3 f18 ?v0)) ?v0))))))
(assert (forall ((?v0 Real)) (let ((?v_1 (f3 (f8 f9 f6) 2.0)) (?v_0 (f3 f19 ?v0))) (and (< (- ?v_1) ?v_0) (and (< ?v_0 ?v_1) (= (f3 f18 ?v_0) ?v0))))))
(assert (forall ((?v0 S6)) (= (f3 f7 (f3 (f8 f9 (f3 (f8 f11 f6) (f20 f21 (f22 f23 (+ (* 2 (f24 f25 ?v0)) 1))))) 2.0)) 0.0)))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 2.0)) (= (f3 f7 (+ ?v0 (f3 (f8 f9 (f3 (f8 f11 (f20 f21 (f22 f23 (+ (f24 f25 ?v1) 1)))) f6)) ?v_0))) (- (f3 f4 (+ ?v0 (f3 (f8 f9 (f3 (f8 f11 (f20 f21 ?v1)) f6)) ?v_0))))))))
(assert (forall ((?v0 Real)) (not (= (f3 f7 (f3 f19 ?v0)) 0.0))))
(assert (forall ((?v0 S6)) (= (* (f20 f21 ?v0) 4.0) (f20 f21 (f22 f23 (* 4 (f24 f25 ?v0)))))))
(assert (forall ((?v0 S6)) (let ((?v_0 (* 2 (f24 f25 ?v0)))) (=> (not (= ?v0 (f22 f23 0))) (= (f22 f23 (+ (f24 f25 (f22 f23 (- ?v_0 1))) 1)) (f22 f23 ?v_0))))))
(assert (forall ((?v0 S6)) (let ((?v_0 (* 4 (f24 f25 ?v0)))) (=> (not (= ?v0 (f22 f23 0))) (= (f22 f23 (+ (+ (f24 f25 (f22 f23 (- ?v_0 2))) 1) 1)) (f22 f23 ?v_0))))))
(assert (forall ((?v0 S6)) (let ((?v_0 (* 2 (f24 f25 ?v0)))) (=> (not (= ?v0 (f22 f23 0))) (= (f22 f23 (+ (+ (f24 f25 (f22 f23 (- ?v_0 2))) 1) 1)) (f22 f23 ?v_0))))))
(assert (let ((?v_0 0.0)) (= (f3 f19 ?v_0) ?v_0)))
(assert (forall ((?v0 Real)) (= (f3 f19 (- ?v0)) (- (f3 f19 ?v0)))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (< ?v0 ?v1) (< (f3 f19 ?v0) (f3 f19 ?v1)))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (<= ?v0 ?v1) (<= (f3 f19 ?v0) (f3 f19 ?v1)))))
(assert (forall ((?v0 Real)) (= (f3 f18 (f3 f19 ?v0)) ?v0)))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 0.0) (?v_1 1.0)) (=> (<= (ite (< ?v0 ?v_0) (- ?v0) ?v0) ?v_1) (=> (< (ite (< ?v1 ?v_0) (- ?v1) ?v1) ?v_1) (= (+ (f3 f19 ?v0) (f3 f19 ?v1)) (f3 f19 (f3 (f8 f9 (+ ?v0 ?v1)) (- ?v_1 (f3 (f8 f11 ?v0) ?v1))))))))))
(assert (forall ((?v0 Real)) (let ((?v_1 (f3 (f8 f9 f6) 2.0)) (?v_0 (f3 f19 ?v0))) (and (< (- ?v_1) ?v_0) (< ?v_0 ?v_1)))))
(assert (let ((?v_0 4.0) (?v_1 (f8 f9 1.0))) (= (f3 (f8 f9 f6) ?v_0) (- (* ?v_0 (f3 f19 (f3 ?v_1 5.0))) (f3 f19 (f3 ?v_1 239.0))))))
(assert (forall ((?v0 Real)) (< (- (f3 (f8 f9 f6) 2.0)) (f3 f19 ?v0))))
(assert (forall ((?v0 Real)) (< (f3 f19 ?v0) (f3 (f8 f9 f6) 2.0))))
(assert (= (f3 f19 1.0) (f3 (f8 f9 f6) 4.0)))
(assert (forall ((?v0 S6)) (= (f3 f7 (f3 (f8 f11 (* 2.0 (f20 f21 ?v0))) f6)) 1.0)))
(assert (forall ((?v0 S6)) (= (f3 f4 (f3 (f8 f11 (* 2.0 (f20 f21 ?v0))) f6)) 0.0)))
(assert (forall ((?v0 S6)) (= (f3 f4 (f3 (f8 f11 (f20 f21 ?v0)) f6)) 0.0)))
(assert (forall ((?v0 S6)) (= (f3 f4 (f3 (f8 f11 f6) (f20 f21 ?v0))) 0.0)))
(assert (forall ((?v0 S6)) (= (f3 f18 (f3 (f8 f11 (f20 f21 ?v0)) f6)) 0.0)))
(assert (forall ((?v0 Real) (?v1 S6)) (= (f3 f18 (+ ?v0 (f3 (f8 f11 (f20 f21 ?v1)) f6))) (f3 f18 ?v0))))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 2.0)) (= (f3 f4 (+ ?v0 (f3 (f8 f9 (f3 (f8 f11 (f20 f21 (f22 f23 (+ (f24 f25 ?v1) 1)))) f6)) ?v_0))) (f3 f7 (+ ?v0 (f3 (f8 f9 (f3 (f8 f11 (f20 f21 ?v1)) f6)) ?v_0)))))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (f20 f21 (f22 f23 (f13 (f15 f16 (f24 f25 ?v0)) (f24 f25 ?v1)))) (f3 (f8 f11 (f20 f21 ?v0)) (f20 f21 ?v1)))))
(assert (forall ((?v0 S6)) (<= 0.0 (f20 f21 ?v0))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 0.0)) (=> (< ?v_0 ?v0) (=> (<= ?v_0 ?v1) (exists ((?v2 S6)) (and (<= (f3 (f8 f11 (f20 f21 ?v2)) ?v0) ?v1) (< ?v1 (f3 (f8 f11 (f20 f21 (f22 f23 (+ (f24 f25 ?v2) 1)))) ?v0)))))))))
(assert (forall ((?v0 S6)) (= (f3 f4 (f3 (f8 f9 (f3 (f8 f11 (f20 f21 (f22 f23 (+ (* 2 (f24 f25 ?v0)) 1)))) f6)) 2.0)) (f20 (f26 f27 (- 1.0)) ?v0))))
(assert (forall ((?v0 S6) (?v1 Int)) (let ((?v_0 (f24 f25 ?v0)) (?v_1 (f28 f29 ?v1))) (=> (< 0 ?v_0) (= (f13 (f15 f16 (f24 ?v_1 (f22 f23 (- ?v_0 1)))) ?v1) (f24 ?v_1 ?v0))))))
(assert (forall ((?v0 S6) (?v1 Real)) (let ((?v_0 (f24 f25 ?v0)) (?v_1 (f26 f27 ?v1))) (=> (< 0 ?v_0) (= (f3 (f8 f11 (f20 ?v_1 (f22 f23 (- ?v_0 1)))) ?v1) (f20 ?v_1 ?v0))))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f24 f25 ?v0)) (?v_1 (f31 f33 ?v1))) (=> (< 0 ?v_0) (= (f30 (f31 f32 (f30 ?v_1 (f22 f23 (- ?v_0 1)))) ?v1) (f30 ?v_1 ?v0))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 Int)) (let ((?v_0 (f24 f25 ?v1)) (?v_1 (f24 f25 ?v0)) (?v_2 (f28 f29 ?v2))) (=> (<= ?v_1 ?v_0) (= (f24 ?v_2 (f22 f23 (- (+ ?v_0 1) ?v_1))) (f13 (f15 f16 (f24 ?v_2 (f22 f23 (- ?v_0 ?v_1)))) ?v2))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 Real)) (let ((?v_0 (f24 f25 ?v1)) (?v_1 (f24 f25 ?v0)) (?v_2 (f26 f27 ?v2))) (=> (<= ?v_1 ?v_0) (= (f20 ?v_2 (f22 f23 (- (+ ?v_0 1) ?v_1))) (f3 (f8 f11 (f20 ?v_2 (f22 f23 (- ?v_0 ?v_1)))) ?v2))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_0 (f24 f25 ?v1)) (?v_1 (f24 f25 ?v0)) (?v_2 (f31 f33 ?v2))) (=> (<= ?v_1 ?v_0) (= (f30 ?v_2 (f22 f23 (- (+ ?v_0 1) ?v_1))) (f30 (f31 f32 (f30 ?v_2 (f22 f23 (- ?v_0 ?v_1)))) ?v2))))))
(assert (forall ((?v0 S6)) (< (f20 f21 ?v0) (f20 (f26 f27 2.0) ?v0))))
(assert (forall ((?v0 S6)) (<= 1.0 (f20 (f26 f27 2.0) ?v0))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 (f22 f23 2))) (<= (- (f20 (f26 f27 ?v0) ?v_0)) (f20 (f26 f27 ?v1) ?v_0)))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_1 0.0) (?v_0 (f22 f23 2))) (= (= (+ (f20 (f26 f27 ?v0) ?v_0) (f20 (f26 f27 ?v1) ?v_0)) ?v_1) (and (= ?v0 ?v_1) (= ?v1 ?v_1))))))
(assert (forall ((?v0 Real)) (let ((?v_0 1.0)) (=> (< (ite (< ?v0 0.0) (- ?v0) ?v0) ?v_0) (< (f20 (f26 f27 ?v0) (f22 f23 2)) ?v_0)))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f22 f23 2))) (= (* 4.0 (f20 (f26 f27 ?v0) ?v_0)) (f20 (f26 f27 (* 2.0 ?v0)) ?v_0)))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f22 f23 2))) (= (f3 f7 (* 2.0 ?v0)) (- (f20 (f26 f27 (f3 f7 ?v0)) ?v_0) (f20 (f26 f27 (f3 f4 ?v0)) ?v_0))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f22 f23 2))) (= (f20 (f26 f27 (f3 f7 ?v0)) ?v_0) (- 1.0 (f20 (f26 f27 (f3 f4 ?v0)) ?v_0))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f22 f23 2))) (= (f20 (f26 f27 (f3 f4 ?v0)) ?v_0) (- 1.0 (f20 (f26 f27 (f3 f7 ?v0)) ?v_0))))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f22 f23 2))) (= (+ (f20 (f26 f27 (f3 f7 ?v0)) ?v_0) (f20 (f26 f27 (f3 f4 ?v0)) ?v_0)) 1.0))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f22 f23 2))) (= (+ (f20 (f26 f27 (f3 f4 ?v0)) ?v_0) (f20 (f26 f27 (f3 f7 ?v0)) ?v_0)) 1.0))))
(assert (forall ((?v0 Real)) (let ((?v_1 (f22 f23 2)) (?v_0 (- ?v0))) (= (+ (f20 (f26 f27 (+ (f3 f4 ?v_0) (f3 f4 ?v0))) ?v_1) (f20 (f26 f27 (- (f3 f7 ?v_0) (f3 f7 ?v0))) ?v_1)) 0.0))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_5 (f22 f23 2)) (?v_3 (f8 f11 (f3 f4 ?v0))) (?v_2 (f3 f7 ?v1)) (?v_1 (f8 f11 (f3 f7 ?v0))) (?v_4 (f3 f4 ?v1)) (?v_0 (+ ?v0 ?v1))) (= (+ (f20 (f26 f27 (- (f3 f4 ?v_0) (+ (f3 ?v_3 ?v_2) (f3 ?v_1 ?v_4)))) ?v_5) (f20 (f26 f27 (- (f3 f7 ?v_0) (- (f3 ?v_1 ?v_2) (f3 ?v_3 ?v_4)))) ?v_5)) 0.0))))
(assert (forall ((?v0 Real)) (let ((?v_0 0.0) (?v_2 2.0)) (let ((?v_1 (* ?v_2 ?v0)) (?v_3 (f3 f18 ?v0))) (=> (not (= (f3 f7 ?v0) ?v_0)) (=> (not (= (f3 f7 ?v_1) ?v_0)) (= (f3 f18 ?v_1) (f3 (f8 f9 (* ?v_2 ?v_3)) (- 1.0 (f20 (f26 f27 ?v_3) (f22 f23 2)))))))))))
(assert (forall ((?v0 Real) (?v1 Real)) (<= (- (f3 (f8 f11 ?v0) ?v0)) (f3 (f8 f11 ?v1) ?v1))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 (f8 f11 ?v0) ?v1) (f3 (f8 f11 ?v1) ?v0))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 (f8 f11 ?v0))) (= (f3 (f8 f11 (f3 ?v_0 ?v1)) ?v2) (f3 ?v_0 (f3 (f8 f11 ?v1) ?v2))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (= (f3 (f8 f11 (+ ?v0 ?v1)) ?v2) (+ (f3 (f8 f11 ?v0) ?v2) (f3 (f8 f11 ?v1) ?v2)))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 0.0)) (= (= (+ (f3 (f8 f11 ?v0) ?v0) (f3 (f8 f11 ?v1) ?v1)) ?v_0) (and (= ?v0 ?v_0) (= ?v1 ?v_0))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (=> (not (= ?v0 0.0)) (= (= (f3 (f8 f11 ?v1) ?v0) (f3 (f8 f11 ?v2) ?v0)) (= ?v1 ?v2)))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 (f8 f11 ?v0))) (=> (not (= ?v0 0.0)) (= (= (f3 ?v_0 ?v1) (f3 ?v_0 ?v2)) (= ?v1 ?v2))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (=> (< 0.0 ?v0) (= (< (f3 (f8 f11 ?v1) ?v0) (f3 (f8 f11 ?v2) ?v0)) (< ?v1 ?v2)))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (=> (< 0.0 ?v0) (= (<= (f3 (f8 f11 ?v1) ?v0) (f3 (f8 f11 ?v2) ?v0)) (<= ?v1 ?v2)))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 (f8 f11 ?v0))) (=> (< 0.0 ?v0) (= (<= (f3 ?v_0 ?v1) (f3 ?v_0 ?v2)) (<= ?v1 ?v2))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 0.0)) (=> (< ?v_0 ?v0) (=> (< ?v_0 ?v1) (< ?v_0 (f3 (f8 f11 ?v0) ?v1)))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 (f8 f11 ?v0))) (=> (< 0.0 ?v0) (=> (< ?v1 ?v2) (< (f3 ?v_0 ?v1) (f3 ?v_0 ?v2)))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 0.0)) (= (<= ?v_0 (f3 (f8 f9 ?v0) ?v1)) (and (or (<= ?v0 ?v_0) (<= ?v_0 ?v1)) (or (<= ?v_0 ?v0) (<= ?v1 ?v_0)))))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (< ?v0 ?v1) (< ?v0 (f3 (f8 f9 (+ ?v0 ?v1)) 2.0)))))
(assert (forall ((?v0 Real) (?v1 Real)) (=> (< ?v0 ?v1) (< (f3 (f8 f9 (+ ?v0 ?v1)) 2.0) ?v1))))
(assert (forall ((?v0 S6)) (not (< (f20 f21 ?v0) 0.0))))
(assert (forall ((?v0 S6)) (< 0.0 (f20 f21 (f22 f23 (+ (f24 f25 ?v0) 1))))))
(assert (= (f20 f21 (f22 f23 1)) 1.0))
(assert (= (f20 f21 (f22 f23 0)) 0.0))
(assert (= (f20 f21 (f22 f23 (+ 0 1))) 1.0))
(assert (forall ((?v0 S6)) (let ((?v_0 (f20 f21 ?v0))) (= (ite (< ?v_0 0.0) (- ?v_0) ?v_0) ?v_0))))
(assert (forall ((?v0 S6)) (= (f20 f21 (f22 f23 (+ (f24 f25 ?v0) 1))) (+ (f20 f21 ?v0) 1.0))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (f20 f21 (f22 f23 (+ (f24 f25 ?v0) (f24 f25 ?v1)))) (+ (f20 f21 ?v0) (f20 f21 ?v1)))))
(assert (forall ((?v0 S6)) (= (< 0.0 (f20 f21 ?v0)) (< 0 (f24 f25 ?v0)))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (<= (f24 f25 ?v0) (f24 f25 ?v1)) (< (f20 f21 ?v0) (+ (f20 f21 ?v1) 1.0)))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (< (f24 f25 ?v0) (f24 f25 ?v1)) (<= (+ (f20 f21 ?v0) 1.0) (f20 f21 ?v1)))))
(assert (forall ((?v0 S6)) (= (= (f20 f21 ?v0) 0.0) (= ?v0 (f22 f23 0)))))
(assert (forall ((?v0 S6)) (= (<= (f20 f21 ?v0) 0.0) (= ?v0 (f22 f23 0)))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (= (f20 f21 ?v0) (f20 f21 ?v1)) (= ?v0 ?v1))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (< (f20 f21 ?v0) (f20 f21 ?v1)) (< (f24 f25 ?v0) (f24 f25 ?v1)))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (<= (f20 f21 ?v0) (f20 f21 ?v1)) (<= (f24 f25 ?v0) (f24 f25 ?v1)))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f24 f25 ?v1)) (?v_1 (f24 f25 ?v0))) (=> (<= ?v_1 ?v_0) (= (f20 f21 (f22 f23 (- ?v_0 ?v_1))) (- (f20 f21 ?v1) (f20 f21 ?v0)))))))
(assert (forall ((?v0 S6)) (= (f3 f7 (f3 (f8 f11 (f20 f21 ?v0)) f6)) (f20 (f26 f27 (- 1.0)) ?v0))))
(assert (forall ((?v0 S6)) (= (f3 f7 (f3 (f8 f11 f6) (f20 f21 ?v0))) (f20 (f26 f27 (- 1.0)) ?v0))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_1 (f22 f23 2)) (?v_0 (f8 f11 ?v0))) (= (+ (f20 (f26 f27 (f3 ?v_0 (f3 f7 ?v1))) ?v_1) (f20 (f26 f27 (f3 ?v_0 (f3 f4 ?v1))) ?v_1)) (f20 (f26 f27 ?v0) ?v_1)))))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 1.0)) (=> (<= 0.0 ?v0) (<= (+ (f3 (f8 f11 (f20 f21 ?v1)) ?v0) ?v_0) (f20 (f26 f27 (+ ?v0 ?v_0)) ?v1))))))
(assert (forall ((?v0 Int) (?v1 S6)) (let ((?v_0 (f28 f29 ?v0))) (let ((?v_1 (f24 ?v_0 ?v1))) (= (f24 ?v_0 (f22 f23 (* 2 (f24 f25 ?v1)))) (f13 (f15 f16 ?v_1) ?v_1))))))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 (f26 f27 ?v0))) (let ((?v_1 (f20 ?v_0 ?v1))) (= (f20 ?v_0 (f22 f23 (* 2 (f24 f25 ?v1)))) (f3 (f8 f11 ?v_1) ?v_1))))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f31 f33 ?v0))) (let ((?v_1 (f30 ?v_0 ?v1))) (= (f30 ?v_0 (f22 f23 (* 2 (f24 f25 ?v1)))) (f30 (f31 f32 ?v_1) ?v_1))))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (f20 f21 (f30 (f31 f33 ?v0) ?v1)) (f20 (f26 f27 (f20 f21 ?v0)) ?v1))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (f20 (f26 f27 (f20 f21 ?v0)) ?v1) (f20 f21 (f30 (f31 f33 ?v0) ?v1)))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6) (?v3 S6)) (let ((?v_0 (f31 f32 ?v0))) (= (f30 (f31 f32 (f30 ?v_0 ?v1)) (f30 (f31 f32 ?v2) ?v3)) (f30 (f31 f32 (f30 ?v_0 ?v2)) (f30 (f31 f32 ?v1) ?v3))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real) (?v3 Real)) (let ((?v_0 (f8 f11 ?v0))) (= (f3 (f8 f11 (f3 ?v_0 ?v1)) (f3 (f8 f11 ?v2) ?v3)) (f3 (f8 f11 (f3 ?v_0 ?v2)) (f3 (f8 f11 ?v1) ?v3))))))
(assert (forall ((?v0 Int) (?v1 Int) (?v2 Int) (?v3 Int)) (let ((?v_0 (f15 f16 ?v0))) (= (f13 (f15 f16 (f13 ?v_0 ?v1)) (f13 (f15 f16 ?v2) ?v3)) (f13 (f15 f16 (f13 ?v_0 ?v2)) (f13 (f15 f16 ?v1) ?v3))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6) (?v3 S6)) (let ((?v_1 (f31 f32 (f30 (f31 f32 ?v0) ?v1))) (?v_0 (f31 f32 ?v2))) (= (f30 ?v_1 (f30 ?v_0 ?v3)) (f30 ?v_0 (f30 ?v_1 ?v3))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real) (?v3 Real)) (let ((?v_1 (f8 f11 (f3 (f8 f11 ?v0) ?v1))) (?v_0 (f8 f11 ?v2))) (= (f3 ?v_1 (f3 ?v_0 ?v3)) (f3 ?v_0 (f3 ?v_1 ?v3))))))
(assert (forall ((?v0 Int) (?v1 Int) (?v2 Int) (?v3 Int)) (let ((?v_1 (f15 f16 (f13 (f15 f16 ?v0) ?v1))) (?v_0 (f15 f16 ?v2))) (= (f13 ?v_1 (f13 ?v_0 ?v3)) (f13 ?v_0 (f13 ?v_1 ?v3))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6) (?v3 S6)) (let ((?v_0 (f31 f32 ?v0)) (?v_1 (f30 (f31 f32 ?v2) ?v3))) (= (f30 (f31 f32 (f30 ?v_0 ?v1)) ?v_1) (f30 ?v_0 (f30 (f31 f32 ?v1) ?v_1))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real) (?v3 Real)) (let ((?v_0 (f8 f11 ?v0)) (?v_1 (f3 (f8 f11 ?v2) ?v3))) (= (f3 (f8 f11 (f3 ?v_0 ?v1)) ?v_1) (f3 ?v_0 (f3 (f8 f11 ?v1) ?v_1))))))
(assert (forall ((?v0 Int) (?v1 Int) (?v2 Int) (?v3 Int)) (let ((?v_0 (f15 f16 ?v0)) (?v_1 (f13 (f15 f16 ?v2) ?v3))) (= (f13 (f15 f16 (f13 ?v_0 ?v1)) ?v_1) (f13 ?v_0 (f13 (f15 f16 ?v1) ?v_1))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_0 (f31 f32 ?v0))) (= (f30 (f31 f32 (f30 ?v_0 ?v1)) ?v2) (f30 (f31 f32 (f30 ?v_0 ?v2)) ?v1)))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 (f8 f11 ?v0))) (= (f3 (f8 f11 (f3 ?v_0 ?v1)) ?v2) (f3 (f8 f11 (f3 ?v_0 ?v2)) ?v1)))))
(assert (forall ((?v0 Int) (?v1 Int) (?v2 Int)) (let ((?v_0 (f15 f16 ?v0))) (= (f13 (f15 f16 (f13 ?v_0 ?v1)) ?v2) (f13 (f15 f16 (f13 ?v_0 ?v2)) ?v1)))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_0 (f31 f32 ?v0))) (= (f30 (f31 f32 (f30 ?v_0 ?v1)) ?v2) (f30 ?v_0 (f30 (f31 f32 ?v1) ?v2))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 (f8 f11 ?v0))) (= (f3 (f8 f11 (f3 ?v_0 ?v1)) ?v2) (f3 ?v_0 (f3 (f8 f11 ?v1) ?v2))))))
(assert (forall ((?v0 Int) (?v1 Int) (?v2 Int)) (let ((?v_0 (f15 f16 ?v0))) (= (f13 (f15 f16 (f13 ?v_0 ?v1)) ?v2) (f13 ?v_0 (f13 (f15 f16 ?v1) ?v2))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_0 (f31 f32 ?v0))) (= (f30 ?v_0 (f30 (f31 f32 ?v1) ?v2)) (f30 (f31 f32 (f30 ?v_0 ?v1)) ?v2)))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_0 (f8 f11 ?v0))) (= (f3 ?v_0 (f3 (f8 f11 ?v1) ?v2)) (f3 (f8 f11 (f3 ?v_0 ?v1)) ?v2)))))
(assert (forall ((?v0 Int) (?v1 Int) (?v2 Int)) (let ((?v_0 (f15 f16 ?v0))) (= (f13 ?v_0 (f13 (f15 f16 ?v1) ?v2)) (f13 (f15 f16 (f13 ?v_0 ?v1)) ?v2)))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_1 (f31 f32 ?v0)) (?v_0 (f31 f32 ?v1))) (= (f30 ?v_1 (f30 ?v_0 ?v2)) (f30 ?v_0 (f30 ?v_1 ?v2))))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 Real)) (let ((?v_1 (f8 f11 ?v0)) (?v_0 (f8 f11 ?v1))) (= (f3 ?v_1 (f3 ?v_0 ?v2)) (f3 ?v_0 (f3 ?v_1 ?v2))))))
(assert (forall ((?v0 Int) (?v1 Int) (?v2 Int)) (let ((?v_1 (f15 f16 ?v0)) (?v_0 (f15 f16 ?v1))) (= (f13 ?v_1 (f13 ?v_0 ?v2)) (f13 ?v_0 (f13 ?v_1 ?v2))))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (f30 (f31 f32 ?v0) ?v1) (f30 (f31 f32 ?v1) ?v0))))
(assert (forall ((?v0 Real) (?v1 Real)) (= (f3 (f8 f11 ?v0) ?v1) (f3 (f8 f11 ?v1) ?v0))))
(assert (forall ((?v0 Int) (?v1 Int)) (= (f13 (f15 f16 ?v0) ?v1) (f13 (f15 f16 ?v1) ?v0))))
(assert (forall ((?v0 Int)) (= (f24 (f28 f29 ?v0) (f22 f23 1)) ?v0)))
(assert (forall ((?v0 Real)) (= (f20 (f26 f27 ?v0) (f22 f23 1)) ?v0)))
(assert (forall ((?v0 S6)) (= (f30 (f31 f33 ?v0) (f22 f23 1)) ?v0)))
(assert (forall ((?v0 Int)) (= (f13 (f15 f16 ?v0) ?v0) (f24 (f28 f29 ?v0) (f22 f23 2)))))
(assert (forall ((?v0 Real)) (= (f3 (f8 f11 ?v0) ?v0) (f20 (f26 f27 ?v0) (f22 f23 2)))))
(assert (forall ((?v0 S6)) (= (f30 (f31 f32 ?v0) ?v0) (f30 (f31 f33 ?v0) (f22 f23 2)))))
(assert (forall ((?v0 Int) (?v1 S6)) (let ((?v_0 (f28 f29 ?v0))) (= (f24 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1))) (f13 (f15 f16 ?v0) (f24 ?v_0 ?v1))))))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 (f26 f27 ?v0))) (= (f20 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1))) (f3 (f8 f11 ?v0) (f20 ?v_0 ?v1))))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f31 f33 ?v0))) (= (f30 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1))) (f30 (f31 f32 ?v0) (f30 ?v_0 ?v1))))))
(assert (forall ((?v0 Int) (?v1 S6)) (let ((?v_0 (f28 f29 ?v0))) (= (f13 (f15 f16 ?v0) (f24 ?v_0 ?v1)) (f24 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1)))))))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 (f26 f27 ?v0))) (= (f3 (f8 f11 ?v0) (f20 ?v_0 ?v1)) (f20 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1)))))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f31 f33 ?v0))) (= (f30 (f31 f32 ?v0) (f30 ?v_0 ?v1)) (f30 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1)))))))
(assert (forall ((?v0 Int) (?v1 S6)) (let ((?v_0 (f28 f29 ?v0))) (= (f13 (f15 f16 (f24 ?v_0 ?v1)) ?v0) (f24 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1)))))))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 (f26 f27 ?v0))) (= (f3 (f8 f11 (f20 ?v_0 ?v1)) ?v0) (f20 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1)))))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f31 f33 ?v0))) (= (f30 (f31 f32 (f30 ?v_0 ?v1)) ?v0) (f30 ?v_0 (f22 f23 (+ (f24 f25 ?v1) 1)))))))
(assert (forall ((?v0 Int) (?v1 Int) (?v2 S6)) (= (f24 (f28 f29 (f13 (f15 f16 ?v0) ?v1)) ?v2) (f13 (f15 f16 (f24 (f28 f29 ?v0) ?v2)) (f24 (f28 f29 ?v1) ?v2)))))
(assert (forall ((?v0 Real) (?v1 Real) (?v2 S6)) (= (f20 (f26 f27 (f3 (f8 f11 ?v0) ?v1)) ?v2) (f3 (f8 f11 (f20 (f26 f27 ?v0) ?v2)) (f20 (f26 f27 ?v1) ?v2)))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (= (f30 (f31 f33 (f30 (f31 f32 ?v0) ?v1)) ?v2) (f30 (f31 f32 (f30 (f31 f33 ?v0) ?v2)) (f30 (f31 f33 ?v1) ?v2)))))
(assert (forall ((?v0 Int) (?v1 S6) (?v2 S6)) (let ((?v_0 (f28 f29 ?v0))) (= (f13 (f15 f16 (f24 ?v_0 ?v1)) (f24 ?v_0 ?v2)) (f24 ?v_0 (f22 f23 (+ (f24 f25 ?v1) (f24 f25 ?v2))))))))
(assert (forall ((?v0 Real) (?v1 S6) (?v2 S6)) (let ((?v_0 (f26 f27 ?v0))) (= (f3 (f8 f11 (f20 ?v_0 ?v1)) (f20 ?v_0 ?v2)) (f20 ?v_0 (f22 f23 (+ (f24 f25 ?v1) (f24 f25 ?v2))))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_0 (f31 f33 ?v0))) (= (f30 (f31 f32 (f30 ?v_0 ?v1)) (f30 ?v_0 ?v2)) (f30 ?v_0 (f22 f23 (+ (f24 f25 ?v1) (f24 f25 ?v2))))))))
(assert (forall ((?v0 Int) (?v1 S6) (?v2 S6)) (let ((?v_0 (f28 f29 ?v0))) (= (f24 (f28 f29 (f24 ?v_0 ?v1)) ?v2) (f24 ?v_0 (f22 f23 (f13 (f15 f16 (f24 f25 ?v1)) (f24 f25 ?v2))))))))
(assert (forall ((?v0 Real) (?v1 S6) (?v2 S6)) (let ((?v_0 (f26 f27 ?v0))) (= (f20 (f26 f27 (f20 ?v_0 ?v1)) ?v2) (f20 ?v_0 (f22 f23 (f13 (f15 f16 (f24 f25 ?v1)) (f24 f25 ?v2))))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_0 (f31 f33 ?v0))) (= (f30 (f31 f33 (f30 ?v_0 ?v1)) ?v2) (f30 ?v_0 (f22 f23 (f13 (f15 f16 (f24 f25 ?v1)) (f24 f25 ?v2))))))))
(assert (forall ((?v0 Real) (?v1 Real)) (let ((?v_0 (f22 f23 2))) (= (f20 (f26 f27 (+ ?v0 ?v1)) ?v_0) (+ (+ (f20 (f26 f27 ?v0) ?v_0) (f20 (f26 f27 ?v1) ?v_0)) (f3 (f8 f11 (* 2.0 ?v0)) ?v1))))))
(assert (forall ((?v0 Int) (?v1 S6)) (let ((?v_0 (f28 f29 ?v0))) (let ((?v_1 (f24 ?v_0 ?v1))) (= (f24 ?v_0 (f22 f23 (+ (* 2 (f24 f25 ?v1)) 1))) (f13 (f15 f16 ?v0) (f13 (f15 f16 ?v_1) ?v_1)))))))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 (f26 f27 ?v0))) (let ((?v_1 (f20 ?v_0 ?v1))) (= (f20 ?v_0 (f22 f23 (+ (* 2 (f24 f25 ?v1)) 1))) (f3 (f8 f11 ?v0) (f3 (f8 f11 ?v_1) ?v_1)))))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f31 f33 ?v0))) (let ((?v_1 (f30 ?v_0 ?v1))) (= (f30 ?v_0 (f22 f23 (+ (* 2 (f24 f25 ?v1)) 1))) (f30 (f31 f32 ?v0) (f30 (f31 f32 ?v_1) ?v_1)))))))
(assert (forall ((?v0 Int) (?v1 S6)) (let ((?v_0 (f28 f29 ?v0))) (= (f24 ?v_0 (f22 f23 (+ (* 2 (f24 f25 ?v1)) 1))) (f13 (f15 f16 ?v0) (f24 (f28 f29 (f24 ?v_0 ?v1)) (f22 f23 2)))))))
(assert (forall ((?v0 Real) (?v1 S6)) (let ((?v_0 (f26 f27 ?v0))) (= (f20 ?v_0 (f22 f23 (+ (* 2 (f24 f25 ?v1)) 1))) (f3 (f8 f11 ?v0) (f20 (f26 f27 (f20 ?v_0 ?v1)) (f22 f23 2)))))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f31 f33 ?v0))) (= (f30 ?v_0 (f22 f23 (+ (* 2 (f24 f25 ?v1)) 1))) (f30 (f31 f32 ?v0) (f30 (f31 f33 (f30 ?v_0 ?v1)) (f22 f23 2)))))))
(assert (forall ((?v0 Int) (?v1 S6) (?v2 S6)) (let ((?v_0 (f28 f29 ?v0))) (= (f24 ?v_0 (f22 f23 (f13 (f15 f16 (f24 f25 ?v1)) (f24 f25 ?v2)))) (f24 (f28 f29 (f24 ?v_0 ?v1)) ?v2)))))
(assert (forall ((?v0 Real) (?v1 S6) (?v2 S6)) (let ((?v_0 (f26 f27 ?v0))) (= (f20 ?v_0 (f22 f23 (f13 (f15 f16 (f24 f25 ?v1)) (f24 f25 ?v2)))) (f20 (f26 f27 (f20 ?v_0 ?v1)) ?v2)))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_0 (f31 f33 ?v0))) (= (f30 ?v_0 (f22 f23 (f13 (f15 f16 (f24 f25 ?v1)) (f24 f25 ?v2)))) (f30 (f31 f33 (f30 ?v_0 ?v1)) ?v2)))))
(assert (forall ((?v0 S6) (?v1 S6)) (= (< 0 (f24 f25 (f30 (f31 f33 ?v0) ?v1))) (or (< 0 (f24 f25 ?v0)) (= ?v1 (f22 f23 0))))))
(assert (forall ((?v0 S6)) (let ((?v_0 (f22 f23 (+ 0 1)))) (= (f30 (f31 f33 ?v_0) ?v0) ?v_0))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f22 f23 (+ 0 1)))) (= (= (f30 (f31 f33 ?v0) ?v1) ?v_0) (or (= ?v1 (f22 f23 0)) (= ?v0 ?v_0))))))
(assert (forall ((?v0 S6) (?v1 S6) (?v2 S6)) (let ((?v_0 (f31 f33 ?v0))) (=> (< 0 (f24 f25 ?v0)) (=> (< (f24 f25 (f30 ?v_0 ?v1)) (f24 f25 (f30 ?v_0 ?v2))) (< (f24 f25 ?v1) (f24 f25 ?v2)))))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (+ 0 1))) (=> (<= ?v_0 (f24 f25 ?v0)) (<= ?v_0 (f24 f25 (f30 (f31 f33 ?v0) ?v1)))))))
(assert (forall ((?v0 Int) (?v1 S6)) (= (f13 f14 (f24 (f28 f29 ?v0) ?v1)) (f24 (f28 f29 (f13 f14 ?v0)) ?v1))))
(assert (forall ((?v0 Real) (?v1 S6)) (= (f3 f12 (f20 (f26 f27 ?v0) ?v1)) (f20 (f26 f27 (f3 f12 ?v0)) ?v1))))
(assert (forall ((?v0 Int)) (let ((?v_0 (f24 (f28 f29 ?v0) (f22 f23 2)))) (= (f13 f14 ?v_0) ?v_0))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f20 (f26 f27 ?v0) (f22 f23 2)))) (= (f3 f12 ?v_0) ?v_0))))
(assert (forall ((?v0 Int)) (= (f24 (f28 f29 ?v0) (f22 f23 1)) ?v0)))
(assert (forall ((?v0 Real)) (= (f20 (f26 f27 ?v0) (f22 f23 1)) ?v0)))
(assert (forall ((?v0 S6)) (= (f30 (f31 f33 ?v0) (f22 f23 1)) ?v0)))
(assert (forall ((?v0 Int)) (let ((?v_0 (f22 f23 2))) (= (f24 (f28 f29 (f13 f14 ?v0)) ?v_0) (f24 (f28 f29 ?v0) ?v_0)))))
(assert (forall ((?v0 Real)) (let ((?v_0 (f22 f23 2))) (= (f20 (f26 f27 (f3 f12 ?v0)) ?v_0) (f20 (f26 f27 ?v0) ?v_0)))))
(assert (forall ((?v0 S6) (?v1 S6)) (let ((?v_0 (f22 f23 0)) (?v_2 (f24 f25 ?v0)) (?v_1 (f24 f25 ?v1))) (= (f22 f23 (f13 (f15 f16 ?v_2) ?v_1)) (ite (= ?v0 ?v_0) ?v_0 (f22 f23 (+ ?v_1 (f13 (f15 f16 (f24 f25 (f22 f23 (- ?v_2 1)))) ?v_1))))))))
(assert (forall ((?v0 S6)) (let ((?v_0 (f24 f25 ?v0))) (= (f22 f23 (* ?v_0 2)) (f22 f23 (+ ?v_0 ?v_0))))))
(assert (forall ((?v0 S6)) (= (f22 f23 (f24 f25 ?v0)) ?v0)))
(assert (forall ((?v0 Int)) (=> (<= 0 ?v0) (= (f24 f25 (f22 f23 ?v0)) ?v0))))
(assert (forall ((?v0 Int)) (=> (< ?v0 0) (= (f24 f25 (f22 f23 ?v0)) 0))))
(check-sat)
(exit)