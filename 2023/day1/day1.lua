File = "input.txt"
Sum = 0

for line in io.lines(File) do

  -- Grab the first digit
  local l = string.find(line, "%d")
  local rev = string.reverse(line)
  local r = string.find(rev, "%d")

  if(l == nil) then
    break
  end

  if(r == nil) then
    l = r
  end

  local left =  string.sub(line, l, l)
  local right =  string.sub(rev, r, r)

  local consider = left .. right

  Sum = Sum + consider

end

print(Sum)

