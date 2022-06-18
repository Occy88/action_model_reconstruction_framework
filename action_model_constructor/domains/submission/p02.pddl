(define (problem test)
(:domain GRIDWORLD)
(:objects
    x0 x1 x2 x3 x4 - xc
    y0 y1 y2 y3 y4 - yc
    v0 v1 v2 v3 v4 - v

)
(:init


(inc v0 v1)
(inc v1 v2)
(inc v2 v3)
(inc v3 v4)

(gx x0 x1)
(gx x0 x2)
(gx x0 x3)
(gx x0 x4)
(gx x1 x2)
(gx x1 x3)
(gx x1 x4)
(gx x2 x3)
(gx x2 x4)
(gx x3 x4)

(gy y0 y1)
(gy y0 y2)
(gy y0 y3)
(gy y0 y4)
(gy y1 y2)
(gy y1 y3)
(gy y1 y4)
(gy y2 y3)
(gy y2 y4)
(gy y3 y4)

(conn  x0 y0  x0 y1 )
(conn  x0 y0  x1 y0 )
(conn  x0 y1  x0 y2 )
(conn  x0 y1  x0 y0 )
(conn  x0 y1  x1 y1 )
(conn  x0 y2  x0 y3 )
(conn  x0 y2  x0 y1 )
(conn  x0 y2  x1 y2 )
(conn  x0 y3  x0 y4 )
(conn  x0 y3  x0 y2 )
(conn  x0 y3  x1 y3 )
(conn  x0 y4  x0 y3 )
(conn  x0 y4  x1 y4 )
(conn  x1 y0  x1 y1 )
(conn  x1 y0  x0 y0 )
(conn  x1 y0  x2 y0 )
(conn  x1 y1  x1 y2 )
(conn  x1 y1  x1 y0 )
(conn  x1 y1  x0 y1 )
(conn  x1 y1  x2 y1 )
(conn  x1 y2  x1 y3 )
(conn  x1 y2  x1 y1 )
(conn  x1 y2  x0 y2 )
(conn  x1 y2  x2 y2 )
(conn  x1 y3  x1 y4 )
(conn  x1 y3  x1 y2 )
(conn  x1 y3  x0 y3 )
(conn  x1 y3  x2 y3 )
(conn  x1 y4  x1 y3 )
(conn  x1 y4  x0 y4 )
(conn  x1 y4  x2 y4 )
(conn  x2 y0  x2 y1 )
(conn  x2 y0  x1 y0 )
(conn  x2 y0  x3 y0 )
(conn  x2 y1  x2 y2 )
(conn  x2 y1  x2 y0 )
(conn  x2 y1  x1 y1 )
(conn  x2 y1  x3 y1 )
(conn  x2 y2  x2 y3 )
(conn  x2 y2  x2 y1 )
(conn  x2 y2  x1 y2 )
(conn  x2 y2  x3 y2 )
(conn  x2 y3  x2 y4 )
(conn  x2 y3  x2 y2 )
(conn  x2 y3  x1 y3 )
(conn  x2 y3  x3 y3 )
(conn  x2 y4  x2 y3 )
(conn  x2 y4  x1 y4 )
(conn  x2 y4  x3 y4 )
(conn  x3 y0  x3 y1 )
(conn  x3 y0  x2 y0 )
(conn  x3 y0  x4 y0 )
(conn  x3 y1  x3 y2 )
(conn  x3 y1  x3 y0 )
(conn  x3 y1  x2 y1 )
(conn  x3 y1  x4 y1 )
(conn  x3 y2  x3 y3 )
(conn  x3 y2  x3 y1 )
(conn  x3 y2  x2 y2 )
(conn  x3 y2  x4 y2 )
(conn  x3 y3  x3 y4 )
(conn  x3 y3  x3 y2 )
(conn  x3 y3  x2 y3 )
(conn  x3 y3  x4 y3 )
(conn  x3 y4  x3 y3 )
(conn  x3 y4  x2 y4 )
(conn  x3 y4  x4 y4 )
(conn  x4 y0  x4 y1 )
(conn  x4 y0  x3 y0 )
(conn  x4 y1  x4 y2 )
(conn  x4 y1  x4 y0 )
(conn  x4 y1  x3 y1 )
(conn  x4 y2  x4 y3 )
(conn  x4 y2  x4 y1 )
(conn  x4 y2  x3 y2 )
(conn  x4 y3  x4 y4 )
(conn  x4 y3  x4 y2 )
(conn  x4 y3  x3 y3 )
(conn  x4 y4  x4 y3 )
(conn  x4 y4  x3 y4 )



(black x0 y3)

(black x1 y3)
(value x1 y3 v0)
(black x3 y3)
(value x3 y3 v0)
(black x4 y1)

(black x4 y1)
(value x4 y1 v0)
(black x4 y2)
(value x4 y2 v0)


)
(:goal
(and
(value x1 y3 v1)
(value x3 y3 v3)
(value x4 y1 v0)
(value x4 y2 v1)

(lit x0 y0)
(lit x1 y0)
(lit x2 y0)
(lit x3 y0)
(lit x4 y0)

(lit x0 y1)
(lit x1 y1)
(lit x2 y1)
(lit x3 y1)

(lit x0 y2)
(lit x1 y2)
(lit x2 y2)
(lit x3 y2)

(lit x2 y3)
(lit x4 y3)

(lit x0 y4)
(lit x1 y4)
(lit x2 y4)
(lit x3 y4)
(lit x4 y4)


)))
