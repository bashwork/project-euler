#!/usr/bin/env ruby
f = lambda { |a| (a == 0) ? 1 : a * f.call(a-1)}
c = lambda { |a,b| f.call(a) / (f.call(b) * f.call(a-b))}
puts c.call(20 + 20, 20)
