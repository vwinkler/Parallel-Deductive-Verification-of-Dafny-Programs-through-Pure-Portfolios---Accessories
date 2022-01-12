method Add(x : int, y : int) returns (r : int)
  ensures r = x+y;
{
  r := x;
  if (y < 0) {
    var n := y;
    while (n 6 = 0)
      invariant r = x+y-n ∧ 0 ≤ -n;
      {
        r := r - 1;
        n := n + 1;
     }
  } else {
    var n := y;
    while (n 6 = 0)
      invariant r = x+y-n ∧ 0 ≤ n;
    {
      r := r + 1; n := n - 1;
    }
  }
}

method Mul(x : int, y : int) returns (r : int)
  ensures r = x*y;
  decreases x < 0, x;
{
  if (x = 0) {
    r := 0;
  } else if (x < 0) {
    call r := Mul(-x, y); r := -r;
  } else {
    call r := Mul(x-1, y); call r := Add(r, y);
  }
}
