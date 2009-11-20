test  a = a `mod` 3 == 0 || a `mod` 5 == 0
total a = sum [x | x <- a, test x]
main = print (total [0..999])
