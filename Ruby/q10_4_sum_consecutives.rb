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