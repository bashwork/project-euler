def fib
    a,b,c = 1,0,0
    while true
       a,b,c = b,a+b,c+1
       return c if yield(b)
    end
end

puts fib {|n| n.to_s.length == 1000 }

