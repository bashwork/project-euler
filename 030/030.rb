class Fixnum
  #
  # given a number n and base b, return an
  # array of each nueric element in that base
  # 
  # >>> get_base_array(1234, 10)
  # [1,2,3,4]
  #
  def get_base_array(b)
    n, r = self,[]
    while n > 0
      r << n % b
      n /= b
    end
    r
  end
  
  #
  #   Basically, we know that:
  #   1. 1*9**5 = 59049  (5 digits > 1)
  #   2. 2*9**5 = 118098 (6 digits > 2)
  #   9. 9*9**5 = 531441 (6 digits < 9)
  #
  #   >>> get_max_num(5)
  #   354294 
  #
  def get_max_num
    r,t,a = 0, 0, 9**self
    while r < t.to_s.size
      r,t = r + 1, t+a
    end
    return t
  end
end

# 
#   Given a power p, this returns an iterator for
#   each number that equals the sum of its powers
#
#   >>> sum_of_power(4)
#   [1634, 8208, 9474]
# 
def sum_of_power(p)
    result = []
    powers = 0.upto(10).map {|n| n**p}
    2.upto(p.get_max_num) do |i|
        num = i.get_base_array(10).map {|n| powers[n]}
        if i == num.inject(0) {|t,n| t + n}
            result << i
        end
    end
    return result
end

puts sum_of_power(5).inject(0) {|t,n| t + n}
