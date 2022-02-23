method Triple(x : int) returns (r : int)
    ensures r == 3*x
{
    var y := 2*x;
    r := x + y;
}
