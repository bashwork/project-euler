puts (0..999).select {|n| n if n % 3 == 0 or n % 5 == 0}.inject(0){|s,n| s+=n}
