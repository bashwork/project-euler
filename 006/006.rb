puts (1..100).inject{|t,n| t + n }**2 - (1..100).inject{|t,n| t + n**2} 
