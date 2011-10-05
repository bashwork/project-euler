fibevensum  :: (Integral a) => a -> a
fibevensum m = last . takeWhile (<m) . scanl1 (+) . filter even $ fibonacci
    where fibonacci = map fst $ iterate (\(a,b) -> (b, a + b)) (0,1)
main = print $ fibevensum 5000000
