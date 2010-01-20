ones     = { 1:3, 2:3, 3:5, 4:4,  5:4, 6:3, 7:5, 8:5, 9:4 }
teens    = { 10:3, 11:6, 12:6, 13:8, 14:8,  15:7, 16:7, 17:9, 18:8, 19:8 }
tens     = { 20:6, 30:6, 40:5, 50:5,  60:5,  70:7, 80:6, 90:6 }
hundreds = { 100:10, 200:10, 300:12, 400:11, 500:11, 600:10, 700:12, 800:12, 900:11 }

def get_count_of(n):
    a  = n                  # temp copy
    t  = a % 100            # xx10 - xx19
    s  = teens.get(t, 0)    # check if we are special
    a -= t if s else 0      # remove from total
    t  = a % 10             # xxx1 - xxx9
    s += ones.get(t, 0)
    a -= t                  # remove from total
    t  = a % 100            # xx10 - xx90
    s += tens.get(t, 0)
    a -= t                  # remove from total
    t  = a % 1000           # x100 - x900
    if t and s: s += 3      # x100 'and'
    s += hundreds.get(t, 0)
    return len('onethousand') if (a == 1000) else s

print sum(get_count_of(i) for i in xrange(1,1001))
