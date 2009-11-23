f = 0
1000.downto(100){|n|
   n.downto(100){|m|
   r = m * n
   s = r.to_s
   f = [r, f].max if s == s.reverse
}}
puts f

