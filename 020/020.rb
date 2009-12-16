@memoize = Hash.new

def fact(n)
    return @memoize[n] if @memoize.has_key? n
    return 1 if n == 0
    @memoize[n] = result = n * fact(n - 1)
    return result
end
puts fact(100).to_s.bytes.inject(0) { |n, t| t + n - ?0 }

