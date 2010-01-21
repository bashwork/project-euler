class Fixnum
  def is_palindrome
    (self == self.reverse(2) and self == self.reverse(10))
  end
  def reverse(base)
    result,copy = 0, self
    while copy > 0
      result = (result*base) + (copy % base)
      copy  /= base
    end
    return result
  end
end

result = 0
1.upto(1000000) do |n|
    result += n.is_palindrome ? n : 0
end
puts result
