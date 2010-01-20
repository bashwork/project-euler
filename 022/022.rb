
class String
  #
  # Return the sum of the alphabetic positions of 
  # the letters in the self string.
  #
  def alpha_sum
    result = 0
    self.each_byte {|n| result += n - 64}
    result
  end
end

#
# Read the contents from |file| and process out the
# name fields in a sorted array
#
def clean_file(file)
  data = ''
  File.open(file, 'r') do |f|
    f.each_line {|line| data += line }
  end
  return data.delete(' "').split(',').sort
end

#
# There has to be a way to do this inline instead of
# closing over an external variable,
# i.e. puts clean_file...
#
final = 0
clean_file('names.txt').each_with_index do |val, key|
  final += key.succ * val.alpha_sum
end
puts final
