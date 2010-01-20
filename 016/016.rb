puts (2**1000).to_s.split('').inject(0) {|t, n| t += n.to_i}
