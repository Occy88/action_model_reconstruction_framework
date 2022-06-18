;; original sequence 1: (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 -76 -75 -74 -73 -72 -71 -70 -69 -68 -67 -66 -65 -64 -63 -62 -61 -60 -59 -58 -57 -56 -53 -52 -51 -50 -49 -39 -38 -37 40 -35 -34 -33 -32 -31 -30 -29 -28 -27 -26 -44 -43 -42 -41 45 46 47 48 -36 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -90 -89 -88 -87 -86 -85 -84 77 78 79 80 81 82 83 91 92 93 94 95 96 -55 -54 -105 -104 -103 -102 -101 -100 -99 -98 -97)
;; original sequence 2: (1 2 3 4 5 6 7 8 9 10 11 -60 -59 -58 -57 -56 -53 -52 -51 -50 -49 37 38 39 40 -35 -34 -33 -32 -31 -30 -29 -28 12 13 14 15 -76 -75 -74 -73 -72 -71 -70 -69 -68 -67 -66 -65 -64 -63 -62 -61 -27 -26 -44 -43 -42 -41 45 46 47 48 -36 54 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -90 -89 -88 -87 -86 -85 -84 77 78 79 80 81 82 83 91 92 93 94 95 96 -55 -105 -104 -103 -102 -101 -100 -99 -98 -97)
;; simplified sequence 1: (109 107 110 113 112 108 106 -54 111)
;; simplified sequence 2: (109 110 -113 112 107 108 54 106 111)
;; common subsequences: (((-25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -90 -89 -88 -87 -86 -85 -84 77 78 79 80 81 82 83 91 92 93 94 95 96 -55) . 106) ((12 13 14 15 -76 -75 -74 -73 -72 -71 -70 -69 -68 -67 -66 -65 -64 -63 -62 -61) . 107) ((-27 -26 -44 -43 -42 -41 45 46 47 48 -36) . 108) ((1 2 3 4 5 6 7 8 9 10 11) . 109) ((-60 -59 -58 -57 -56 -53 -52 -51 -50 -49) . 110) ((-105 -104 -103 -102 -101 -100 -99 -98 -97) . 111) ((40 -35 -34 -33 -32 -31 -30 -29 -28) . 112) ((-39 -38 -37) . 113))
;; #safe insertions/deletions: 0
;; sequence 1 (names): ((NORMAL SUB4) (NORMAL SUB2) (NORMAL SUB5) (NORMAL SUB8) (NORMAL SUB7) (NORMAL SUB3) (NORMAL SUB1) (INVERTED G54) (NORMAL SUB6))
;; sequence 2 (names): ((NORMAL SUB4) (NORMAL SUB5) (INVERTED SUB8) (NORMAL SUB7) (NORMAL SUB2) (NORMAL SUB3) (NORMAL G54) (NORMAL SUB1) (NORMAL SUB6))

(DEFINE (PROBLEM CAMPANULA-TO-WAHLENBERGIA)
        (:DOMAIN GENOME-EDIT-DISTANCE)
        (:OBJECTS SUB8 SUB7 SUB6 SUB5 SUB4 SUB3 SUB2 SUB1 G54)
        (:INIT (NORMAL SUB4) (NORMAL SUB2) (NORMAL SUB5) (NORMAL SUB8)
               (NORMAL SUB7) (NORMAL SUB3) (NORMAL SUB1) (INVERTED G54)
               (NORMAL SUB6) (PRESENT SUB4) (PRESENT SUB2)
               (PRESENT SUB5) (PRESENT SUB8) (PRESENT SUB7)
               (PRESENT SUB3) (PRESENT SUB1) (PRESENT G54)
               (PRESENT SUB6) (CW SUB6 SUB4) (CW G54 SUB6)
               (CW SUB1 G54) (CW SUB3 SUB1) (CW SUB7 SUB3)
               (CW SUB8 SUB7) (CW SUB5 SUB8) (CW SUB2 SUB5)
               (CW SUB4 SUB2) (IDLE) (= (TOTAL-COST) 0))
        (:GOAL (AND (NORMAL SUB4) (NORMAL SUB5) (INVERTED SUB8)
                    (NORMAL SUB7) (NORMAL SUB2) (NORMAL SUB3)
                    (NORMAL G54) (NORMAL SUB1) (NORMAL SUB6)
                    (CW SUB6 SUB4) (CW SUB1 SUB6) (CW G54 SUB1)
                    (CW SUB3 G54) (CW SUB2 SUB3) (CW SUB7 SUB2)
                    (CW SUB8 SUB7) (CW SUB5 SUB8) (CW SUB4 SUB5)))
        (:METRIC MINIMIZE (TOTAL-COST)))
