def gcd(input, start=2)
    while input != start:
        while input % start == 0:
            input /= start
        end
        if input == 1:
            break
        end
        start += 1
    end
    return start
end

puts gcd 600851475143
