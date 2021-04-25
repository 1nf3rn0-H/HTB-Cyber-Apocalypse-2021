x = "}a:Vh|}a:g}8j=}89gV<p<}:dV8<Vg9}V<9V<:j|{:"
k = 9
ans = ""
for i in x:
	ans += chr(ord(i) ^ k)
print(ans)