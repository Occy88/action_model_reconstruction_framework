;; original sequence 1: (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 -76 -75 -74 -73 -72 -71 -70 -69 -68 -67 -66 -65 -64 -63 -62 -61 -60 -59 -58 -57 -56 -53 -52 -51 -50 -49 -39 -38 -37 28 29 30 31 32 33 34 35 40 26 27 -44 -43 -42 -41 45 46 47 48 -36 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -90 -89 -88 -87 -86 -85 -84 77 78 79 80 81 82 83 91 92 93 94 95 96 -55 -54 -105 -104 -103 -102 -101 -100 -99 -98 -97)
;; original sequence 2: (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 -76 -75 -74 -73 -72 -71 -70 -69 -68 -67 -66 -65 -64 -63 -62 -61 -56 -55 -54 -53 -60 -59 -58 -57 -27 -26 -44 -43 -42 -41 45 46 47 48 -36 -35 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -89 -88 -87 -86 -85 -84 77 78 79 80 81 82 83 90 91 92 93 94 95 96 -105 -104 -103 -102 -101 -100 -99 -98 28 29 30 31 32 33 34 -40 -39 -38 -37 49 50 51 52 -97)
;; simplified sequence 1: (106 113 -56 -53 114 115 111 35 40 117 109 108 -90 107 112 116 110 -97)
;; simplified sequence 2: (106 -56 116 -53 113 -117 109 -35 108 107 90 112 110 111 -40 115 -114 -97)
;; common subsequences: (((1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 -76 -75 -74 -73 -72 -71 -70 -69 -68 -67 -66 -65 -64 -63 -62 -61) . 106) ((-89 -88 -87 -86 -85 -84 77 78 79 80 81 82 83) . 107) ((-25 -24 -23 -22 -21 -20 -19 -18 -17 -16) . 108) ((-44 -43 -42 -41 45 46 47 48 -36) . 109) ((-105 -104 -103 -102 -101 -100 -99 -98) . 110) ((28 29 30 31 32 33 34) . 111) ((91 92 93 94 95 96) . 112) ((-60 -59 -58 -57) . 113) ((-52 -51 -50 -49) . 114) ((-39 -38 -37) . 115) ((-55 -54) . 116) ((26 27) . 117))
;; #safe insertions/deletions: 0
;; sequence 1 (names): ((NORMAL SUB1) (NORMAL SUB8) (INVERTED G56) (INVERTED G53) (NORMAL SUB9) (NORMAL SUB10) (NORMAL SUB6) (NORMAL G35) (NORMAL G40) (NORMAL SUB12) (NORMAL SUB4) (NORMAL SUB3) (INVERTED G90) (NORMAL SUB2) (NORMAL SUB7) (NORMAL SUB11) (NORMAL SUB5) (INVERTED G97))
;; sequence 2 (names): ((NORMAL SUB1) (INVERTED G56) (NORMAL SUB11) (INVERTED G53) (NORMAL SUB8) (INVERTED SUB12) (NORMAL SUB4) (INVERTED G35) (NORMAL SUB3) (NORMAL SUB2) (NORMAL G90) (NORMAL SUB7) (NORMAL SUB5) (NORMAL SUB6) (INVERTED G40) (NORMAL SUB10) (INVERTED SUB9) (INVERTED G97))

(DEFINE (PROBLEM ADENOPHORA-TO-ASYNEUMA) (:DOMAIN GENOME-EDIT-DISTANCE)
        (:OBJECTS SUB12 SUB11 SUB10 SUB9 SUB8 SUB7 SUB6 SUB5 SUB4 SUB3
            SUB2 SUB1 G97 G90 G56 G53 G40 G35)
        (:INIT (NORMAL SUB1) (NORMAL SUB8) (INVERTED G56)
               (INVERTED G53) (NORMAL SUB9) (NORMAL SUB10)
               (NORMAL SUB6) (NORMAL G35) (NORMAL G40) (NORMAL SUB12)
               (NORMAL SUB4) (NORMAL SUB3) (INVERTED G90) (NORMAL SUB2)
               (NORMAL SUB7) (NORMAL SUB11) (NORMAL SUB5)
               (INVERTED G97) (PRESENT SUB1) (PRESENT SUB8)
               (PRESENT G56) (PRESENT G53) (PRESENT SUB9)
               (PRESENT SUB10) (PRESENT SUB6) (PRESENT G35)
               (PRESENT G40) (PRESENT SUB12) (PRESENT SUB4)
               (PRESENT SUB3) (PRESENT G90) (PRESENT SUB2)
               (PRESENT SUB7) (PRESENT SUB11) (PRESENT SUB5)
               (PRESENT G97) (CW G97 SUB1) (CW SUB5 G97)
               (CW SUB11 SUB5) (CW SUB7 SUB11) (CW SUB2 SUB7)
               (CW G90 SUB2) (CW SUB3 G90) (CW SUB4 SUB3)
               (CW SUB12 SUB4) (CW G40 SUB12) (CW G35 G40)
               (CW SUB6 G35) (CW SUB10 SUB6) (CW SUB9 SUB10)
               (CW G53 SUB9) (CW G56 G53) (CW SUB8 G56) (CW SUB1 SUB8)
               (IDLE) (= (TOTAL-COST) 0))
        (:GOAL (AND (NORMAL SUB1) (INVERTED G56) (NORMAL SUB11)
                    (INVERTED G53) (NORMAL SUB8) (INVERTED SUB12)
                    (NORMAL SUB4) (INVERTED G35) (NORMAL SUB3)
                    (NORMAL SUB2) (NORMAL G90) (NORMAL SUB7)
                    (NORMAL SUB5) (NORMAL SUB6) (INVERTED G40)
                    (NORMAL SUB10) (INVERTED SUB9) (INVERTED G97)
                    (CW G97 SUB1) (CW SUB9 G97) (CW SUB10 SUB9)
                    (CW G40 SUB10) (CW SUB6 G40) (CW SUB5 SUB6)
                    (CW SUB7 SUB5) (CW G90 SUB7) (CW SUB2 G90)
                    (CW SUB3 SUB2) (CW G35 SUB3) (CW SUB4 G35)
                    (CW SUB12 SUB4) (CW SUB8 SUB12) (CW G53 SUB8)
                    (CW SUB11 G53) (CW G56 SUB11) (CW SUB1 G56)))
        (:METRIC MINIMIZE (TOTAL-COST)))
