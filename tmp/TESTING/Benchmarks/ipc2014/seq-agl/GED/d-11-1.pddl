;; original sequence 1: (1 2 3 4 5 6 7 8 28 -36 -35 -34 -33 -32 -31 -30 -29 -27 -26 40 56 57 58 59 60 37 38 39 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -44 -43 -42 -41 45 46 47 48 -55 -54 -53 -52 -51 -50 -49 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 -105 -104 -103 -102 -101 -100 -99 -98 -97)
;; original sequence 2: (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 -76 -75 -74 -73 -72 -71 -70 -69 -68 -67 -66 -65 -64 -63 -62 -61 -60 -59 -58 -57 -56 -53 -52 -51 -50 -49 37 38 39 40 -35 -34 -33 -32 -31 -30 -29 -28 -27 -26 -44 -43 -42 -41 45 46 47 48 -36 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -90 -89 -88 -87 -86 -85 -84 77 78 79 80 81 82 83 91 92 93 94 95 96 -55 -54 -105 -104 -103 -102 -101 -100 -99 -98 -97)
;; simplified sequence 1: (110 28 -36 112 120 40 117 118 107 114 109 119 116 106 111 113 115 108)
;; simplified sequence 2: (110 -114 -106 -117 116 118 40 112 -28 120 109 -36 107 -113 111 115 119 108)
;; common subsequences: (((61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76) . 106) ((-25 -24 -23 -22 -21 -20 -19 -18 -17 -16) . 107) ((-105 -104 -103 -102 -101 -100 -99 -98 -97) . 108) ((-44 -43 -42 -41 45 46 47 48) . 109) ((1 2 3 4 5 6 7 8) . 110) ((77 78 79 80 81 82 83) . 111) ((-35 -34 -33 -32 -31 -30 -29) . 112) ((84 85 86 87 88 89 90) . 113) ((-15 -14 -13 -12 -11 -10 -9) . 114) ((91 92 93 94 95 96) . 115) ((-53 -52 -51 -50 -49) . 116) ((56 57 58 59 60) . 117) ((37 38 39) . 118) ((-55 -54) . 119) ((-27 -26) . 120))
;; #safe insertions/deletions: 0
;; sequence 1 (names): ((NORMAL SUB5) (NORMAL G28) (INVERTED G36) (NORMAL SUB7) (NORMAL SUB15) (NORMAL G40) (NORMAL SUB12) (NORMAL SUB13) (NORMAL SUB2) (NORMAL SUB9) (NORMAL SUB4) (NORMAL SUB14) (NORMAL SUB11) (NORMAL SUB1) (NORMAL SUB6) (NORMAL SUB8) (NORMAL SUB10) (NORMAL SUB3))
;; sequence 2 (names): ((NORMAL SUB5) (INVERTED SUB9) (INVERTED SUB1) (INVERTED SUB12) (NORMAL SUB11) (NORMAL SUB13) (NORMAL G40) (NORMAL SUB7) (INVERTED G28) (NORMAL SUB15) (NORMAL SUB4) (INVERTED G36) (NORMAL SUB2) (INVERTED SUB8) (NORMAL SUB6) (NORMAL SUB10) (NORMAL SUB14) (NORMAL SUB3))

(DEFINE (PROBLEM CYANANTHUS-TO-TRACHELIUM)
        (:DOMAIN GENOME-EDIT-DISTANCE)
        (:OBJECTS SUB15 SUB14 SUB13 SUB12 SUB11 SUB10 SUB9 SUB8 SUB7
            SUB6 SUB5 SUB4 SUB3 SUB2 SUB1 G40 G36 G28)
        (:INIT (NORMAL SUB5) (NORMAL G28) (INVERTED G36) (NORMAL SUB7)
               (NORMAL SUB15) (NORMAL G40) (NORMAL SUB12)
               (NORMAL SUB13) (NORMAL SUB2) (NORMAL SUB9) (NORMAL SUB4)
               (NORMAL SUB14) (NORMAL SUB11) (NORMAL SUB1)
               (NORMAL SUB6) (NORMAL SUB8) (NORMAL SUB10) (NORMAL SUB3)
               (PRESENT SUB5) (PRESENT G28) (PRESENT G36)
               (PRESENT SUB7) (PRESENT SUB15) (PRESENT G40)
               (PRESENT SUB12) (PRESENT SUB13) (PRESENT SUB2)
               (PRESENT SUB9) (PRESENT SUB4) (PRESENT SUB14)
               (PRESENT SUB11) (PRESENT SUB1) (PRESENT SUB6)
               (PRESENT SUB8) (PRESENT SUB10) (PRESENT SUB3)
               (CW SUB3 SUB5) (CW SUB10 SUB3) (CW SUB8 SUB10)
               (CW SUB6 SUB8) (CW SUB1 SUB6) (CW SUB11 SUB1)
               (CW SUB14 SUB11) (CW SUB4 SUB14) (CW SUB9 SUB4)
               (CW SUB2 SUB9) (CW SUB13 SUB2) (CW SUB12 SUB13)
               (CW G40 SUB12) (CW SUB15 G40) (CW SUB7 SUB15)
               (CW G36 SUB7) (CW G28 G36) (CW SUB5 G28) (IDLE)
               (= (TOTAL-COST) 0))
        (:GOAL (AND (NORMAL SUB5) (INVERTED SUB9) (INVERTED SUB1)
                    (INVERTED SUB12) (NORMAL SUB11) (NORMAL SUB13)
                    (NORMAL G40) (NORMAL SUB7) (INVERTED G28)
                    (NORMAL SUB15) (NORMAL SUB4) (INVERTED G36)
                    (NORMAL SUB2) (INVERTED SUB8) (NORMAL SUB6)
                    (NORMAL SUB10) (NORMAL SUB14) (NORMAL SUB3)
                    (CW SUB3 SUB5) (CW SUB14 SUB3) (CW SUB10 SUB14)
                    (CW SUB6 SUB10) (CW SUB8 SUB6) (CW SUB2 SUB8)
                    (CW G36 SUB2) (CW SUB4 G36) (CW SUB15 SUB4)
                    (CW G28 SUB15) (CW SUB7 G28) (CW G40 SUB7)
                    (CW SUB13 G40) (CW SUB11 SUB13) (CW SUB12 SUB11)
                    (CW SUB1 SUB12) (CW SUB9 SUB1) (CW SUB5 SUB9)))
        (:METRIC MINIMIZE (TOTAL-COST)))
