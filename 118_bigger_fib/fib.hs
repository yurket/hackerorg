import Text.Printf (printf)

-- fib 0 = 1
-- fib 1 = 1
-- fib n = fib (n-1) + fib (n-2)




-- fib :: Integer -> Integer
-- fib n = go n (0,1)
--   where
--     go !n (!a, !b) | n==0      = a
--                    | otherwise = go (n-1) (b, a+b)

-- fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
-- fib2 n = fibs!!n

-- fib n = round $ phi ** fromIntegral n / sq5
--   where
--     sq5 = sqrt 5 :: Double
--     phi = (1 + sq5) / 2



import Data.List
import Data.Bits
 
fib :: Int -> Integer
fib n = snd . foldl' fib' (1, 0) . dropWhile not $
            [testBit n k | k <- let s = bitSize n in [s-1,s-2..0]]
    where
        fib' (f, g) p
            | p         = (f*(f+2*g), ss)
            | otherwise = (ss, g*(2*f-g))
            where ss = f*f+g*g


a =  (logBase 2.0 . fromIntegral) (fib 150000000)
-- main = printf "%.2g" a
-- main = printf "%.2d" a
main = print a
