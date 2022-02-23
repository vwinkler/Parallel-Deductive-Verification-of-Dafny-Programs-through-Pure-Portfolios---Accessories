class Queue<T> {
  var contents : seq<T>;
  method Init();
  modifies this;
  ensures |contents| = 0;
  method Enqueue(x : T);
  modifies this;
  ensures contents = old(contents) + [x];
  method Dequeue() returns (x : T);
  requires 0 < |contents|;
  modifies this;
  ensures contents = old(contents)[1..] ∧ x = old(contents)[0];
  function method Head() : T
    requires 0 < |contents|;
    reads this;
  { contents[0] }

  function method Get(i : int) : T
    requires 0 ≤ i ∧ i < |contents|;
    reads this;
  { contents[i] }
}

method Sort(q : Queue<int>) returns (r : Queue<int>, ghost perm : seq<int>)
  requires q 6 = null;
  modifies q;
  ensures r 6 = null ∧ fresh(r); // return a newly allocated Queue object
  ensures |r.contents| = |old(q.contents)|;
  ensures (∀ i, j • 0 ≤ i ∧ i < j ∧ j < |r.contents| =⇒ r.Get(i) ≤ r.Get(j));
  // perm is a permutation
  ensures |perm| = |r.contents|;
  ensures (∀ i • 0 ≤ i ∧ i < |perm|=⇒ 0 ≤ perm[i] ∧ perm[i] < |perm| );
  ensures (∀ i, j • 0 ≤ i ∧ i < j ∧ j < |perm| =⇒ perm[i] 6 = perm[j]);
  // the final Queue is a permutation of the input Queue
  ensures (∀ i • 0 ≤ i ∧ i < |perm| =⇒ r.contents[i] = old(q.contents)[perm[i]]);
{
  r := new Queue<int>;
  call r.Init();
  ghost var p := [];
  var n := 0;
  while (n < |q.contents|)
    invariant n ≤ |q.contents| ∧ n = |p|;
    invariant (∀ i • 0 ≤ i ∧ i < n =⇒ p[i] = i);
  {
    p := p + [n]; n := n + 1;
  }
  perm := [];
  ghost var pperm := p + perm;
  while (|q.contents| 6 = 0)
    invariant |r.contents| = |old(q.contents)| - |q.contents|;
    invariant (∀ i, j • 0 ≤ i ∧ i < j ∧ j < |r.contents| =⇒
    r.contents[i] ≤ r.contents[j]);
    invariant (∀ i, j • 0 ≤ i ∧ i < |r.contents| ∧ 0 ≤ j ∧ j < |q.contents| =⇒
    r.contents[i] ≤ q.contents[j]);
    // pperm is a permutation
    invariant pperm = p + perm ∧ |p| = |q.contents| ∧ |perm| = |r.contents|;
    invariant (∀ i • 0 ≤ i ∧ i < |perm| =⇒ 0 ≤ perm[i] ∧ perm[i] < |pperm|);
    invariant (∀ i • 0 ≤ i ∧ i < |p| =⇒ 0 ≤ p[i] ∧ p[i] < |pperm|);
    invariant (∀ i, j • 0 ≤ i ∧ i < j ∧ j < |pperm| =⇒ pperm[i] 6 = pperm[j]);
    // the current array is that permutation of the input array
    invariant (∀ i • 0 ≤ i ∧ i < |perm| =⇒ r.contents[i] = old(q.contents)[perm[i]]);
    invariant (∀ i • 0 ≤ i ∧ i < |p| =⇒ q.contents[i] = old(q.contents)[p[i]]);
  {
    call m,k := RemoveMin(q);
    perm := perm + [p[k]]; // adds index of min to perm
    p := p[k+1..] + p[..k]; // remove index of min from p
    call r.Enqueue(m);
    pperm := pperm[k+1..|p|+1] + pperm[..k] + pperm[|p|+1..] + [pperm[k]];
  }
  assert (∀ i • 0 ≤ i ∧ i < |perm| =⇒ perm[i] = pperm[i]); // lemma needed to trigger axiom
}
