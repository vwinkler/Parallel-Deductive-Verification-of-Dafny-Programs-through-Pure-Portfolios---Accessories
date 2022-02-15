method Triple(x : int) returns (r : int)
    ensures r == 3*x
{
    var y := 2*x;
    r := x + y;
}

method Quadruple(x : int) returns (r : int)
    ensures r == 4*x
{
    var y := 3*x;
    r := x + y;
}
