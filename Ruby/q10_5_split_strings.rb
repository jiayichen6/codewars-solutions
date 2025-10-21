def solution(str)
  if str.size % 2 != 0
    str += "_"
  end
  
  (0...str.size).step(2).map {|s| str[s,2]}
end