=begin 
先用 split 把字串分割，接著用 map ＋ block 將每個元素轉成數字，最後組成字串回傳。
=end

def high_and_low(numbers)
  numbers_list = numbers.split.map {|n| n.to_i}
  "#{numbers_list.max} #{numbers_list.min}"
end