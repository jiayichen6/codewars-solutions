=begin 
使用 (begin_number..end_number) 的 .. 表示包含尾巴，配合 .step() 設定每次間隔，
最後用 .sum 進行加總。
=end

def sequence_sum(begin_number, end_number, step)
  (begin_number..end_number).step(step).sum
end