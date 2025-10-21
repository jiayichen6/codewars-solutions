=begin 
一開始先判斷是否為奇數，若是則補 "_"。
透過 map + block 對 (0...str.size).step(2) range 物件做操作取得結果。
=end

def solution(str)
  if str.size % 2 != 0
    str += "_"
  end
  
  (0...str.size).step(2).map {|s| str[s,2]}
end