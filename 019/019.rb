require 'date'

s = 0
(1901..2000).each {|y| (1..12).each {|m|
    s += (Date.new(y=y, m=m, d=1).wday == 0) ? 1 : 0
}}
puts s
