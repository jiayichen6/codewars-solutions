=begin 
先判斷字串長度，若字串長度小於或等於 4 時直接回傳原字串，
否則用 "#" * (str.length - 4) + str[-4..-1] 產生遮罩。
=end

def maskify(cc)
  return cc if cc.size <= 4
  "#" * (cc.size - 4) + cc[-4..-1]
end