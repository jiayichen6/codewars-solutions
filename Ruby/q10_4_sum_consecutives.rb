=begin 
使用 prev_number 記住前一個數字，且從第二個數字開始比對的方式
在前後數字相同時計數 count + 1，不同時將數字乘上 count 並加進 result
最後重置 prev_number 和 count。
=end

def sum_consecutives(s)
  result = []
  prev = s.first
  count = 1
  
  s[1..].each do |num|
    if num == prev
      count += 1
    else
      result << prev * count
      prev = num
      count = 1
    end
  end
      
  result << prev * count
end