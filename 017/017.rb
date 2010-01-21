$ones     = { 1  =>3,  2  =>3,  3  =>5,  4  =>4,  5  =>4,  6  =>3,  7  =>5,  8  =>5,  9 =>4        }
$teens    = { 10 =>3,  11 =>6,  12 =>6,  13 =>8,  14 =>8,  15 =>7,  16 =>7,  17 =>9,  18=>8, 19=>8 }
$tens     = { 20 =>6,  30 =>6,  40 =>5,  50 =>5,  60 =>5,  70 =>7,  80 =>6,  90 =>6                }
$hundreds = { 100=>10, 200=>10, 300=>12, 400=>11, 500=>11, 600=>10, 700=>12, 800=>12, 900=>11      }
 
class Fixnum
  def get_count_of
      s, a  = 0, self         # temp copy
      t  = a % 100            # xx10 - xx19
      s  = ($teens[t] or 0)   # check if we are special
      a -= (s != 0) ? t : 0   # remove from total
      t  = a % 10             # xxx1 - xxx9
      s += ($ones[t] or 0)
      a -= t                  # remove from total
      t  = a % 100            # xx10 - xx90
      s += ($tens[t] or 0)
      a -= t                  # remove from total
      t  = a % 1000           # x100 - x900
      s += (t != 0 and s != 0) ? 3 : 0  # x100 'and'
      s += ($hundreds[t] or 0)
      return (a == 1000) ? 11 : s
  end
end

result = 0
1.upto(1000).each {|n| result += n.get_count_of }
puts result
