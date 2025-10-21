def high_and_low(numbers)
  numbers_list = numbers.split().map {|n| n.to_i}
  "#{numbers_list.max} #{numbers_list.min}"
end