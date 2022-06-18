;; original sequence 1: (1 2 3 4 5 6 7 8 -36 -35 -34 -33 -32 -31 -30 -29 -28 -27 -26 -25 -24 -23 -22 -21 -20 -19 -18 -15 -14 -13 -12 -11 -10 -9 40 56 57 58 59 60 37 38 39 -44 -43 -42 -41 45 46 47 48 49 50 51 52 53 16 17 54 55 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 -96 -95 -94 -93 -92 -91 -90 -89 -88 -87 -86 -85 -84 -83 -82 -81 -80 -79 -78 -77 -105 -104 -103 -102 -101 -100 -99 -98 -97)
;; original sequence 2: (1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 -76 -75 -74 -73 -72 -71 -70 -69 -68 -67 -66 -65 -64 -63 -62 -61 -60 -59 -58 -57 -56 -53 -52 -51 -50 -49 -39 -38 -37 28 29 30 31 32 33 34 35 40 26 27 -44 -43 -42 -41 45 46 47 48 -36 -25 -24 -23 -22 -21 -20 -19 -18 -17 -16 -90 -89 -88 -87 -86 -85 -84 77 78 79 80 81 82 83 91 92 93 94 95 96 -55 -54 -105 -104 -103 -102 -101 -100 -99 -98 -97)
;; simplified sequence 1: (110 -36 111 121 109 114 40 117 118 108 116 120 119 106 115 112 113 107)
;; simplified sequence 2: (110 -114 -106 -117 -116 -118 -111 40 -121 108 -36 109 -120 112 -113 -115 -119 107)
;; common subsequences: (((61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76) . 106) ((-105 -104 -103 -102 -101 -100 -99 -98 -97) . 107) ((-44 -43 -42 -41 45 46 47 48) . 108) ((-25 -24 -23 -22 -21 -20 -19 -18) . 109) ((1 2 3 4 5 6 7 8) . 110) ((-35 -34 -33 -32 -31 -30 -29 -28) . 111) ((-90 -89 -88 -87 -86 -85 -84) . 112) ((-83 -82 -81 -80 -79 -78 -77) . 113) ((-15 -14 -13 -12 -11 -10 -9) . 114) ((-96 -95 -94 -93 -92 -91) . 115) ((49 50 51 52 53) . 116) ((56 57 58 59 60) . 117) ((37 38 39) . 118) ((54 55) . 119) ((16 17) . 120) ((-27 -26) . 121))
;; #safe insertions/deletions: 0
;; sequence 1 (names): ((NORMAL SUB5) (INVERTED G36) (NORMAL SUB6) (NORMAL SUB16) (NORMAL SUB4) (NORMAL SUB9) (NORMAL G40) (NORMAL SUB12) (NORMAL SUB13) (NORMAL SUB3) (NORMAL SUB11) (NORMAL SUB15) (NORMAL SUB14) (NORMAL SUB1) (NORMAL SUB10) (NORMAL SUB7) (NORMAL SUB8) (NORMAL SUB2))
;; sequence 2 (names): ((NORMAL SUB5) (INVERTED SUB9) (INVERTED SUB1) (INVERTED SUB12) (INVERTED SUB11) (INVERTED SUB13) (INVERTED SUB6) (NORMAL G40) (INVERTED SUB16) (NORMAL SUB3) (INVERTED G36) (NORMAL SUB4) (INVERTED SUB15) (NORMAL SUB7) (INVERTED SUB8) (INVERTED SUB10) (INVERTED SUB14) (NORMAL SUB2))

(DEFINE (PROBLEM CODONOPSIS-TO-ADENOPHORA)
        (:DOMAIN GENOME-EDIT-DISTANCE)
        (:OBJECTS SUB16 SUB15 SUB14 SUB13 SUB12 SUB11 SUB10 SUB9 SUB8
            SUB7 SUB6 SUB5 SUB4 SUB3 SUB2 SUB1 G40 G36)
        (:INIT (NORMAL SUB5) (INVERTED G36) (NORMAL SUB6)
               (NORMAL SUB16) (NORMAL SUB4) (NORMAL SUB9) (NORMAL G40)
               (NORMAL SUB12) (NORMAL SUB13) (NORMAL SUB3)
               (NORMAL SUB11) (NORMAL SUB15) (NORMAL SUB14)
               (NORMAL SUB1) (NORMAL SUB10) (NORMAL SUB7) (NORMAL SUB8)
               (NORMAL SUB2) (PRESENT SUB5) (PRESENT G36)
               (PRESENT SUB6) (PRESENT SUB16) (PRESENT SUB4)
               (PRESENT SUB9) (PRESENT G40) (PRESENT SUB12)
               (PRESENT SUB13) (PRESENT SUB3) (PRESENT SUB11)
               (PRESENT SUB15) (PRESENT SUB14) (PRESENT SUB1)
               (PRESENT SUB10) (PRESENT SUB7) (PRESENT SUB8)
               (PRESENT SUB2) (CW SUB2 SUB5) (CW SUB8 SUB2)
               (CW SUB7 SUB8) (CW SUB10 SUB7) (CW SUB1 SUB10)
               (CW SUB14 SUB1) (CW SUB15 SUB14) (CW SUB11 SUB15)
               (CW SUB3 SUB11) (CW SUB13 SUB3) (CW SUB12 SUB13)
               (CW G40 SUB12) (CW SUB9 G40) (CW SUB4 SUB9)
               (CW SUB16 SUB4) (CW SUB6 SUB16) (CW G36 SUB6)
               (CW SUB5 G36) (IDLE) (= (TOTAL-COST) 0))
        (:GOAL (AND (NORMAL SUB5) (INVERTED SUB9) (INVERTED SUB1)
                    (INVERTED SUB12) (INVERTED SUB11) (INVERTED SUB13)
                    (INVERTED SUB6) (NORMAL G40) (INVERTED SUB16)
                    (NORMAL SUB3) (INVERTED G36) (NORMAL SUB4)
                    (INVERTED SUB15) (NORMAL SUB7) (INVERTED SUB8)
                    (INVERTED SUB10) (INVERTED SUB14) (NORMAL SUB2)
                    (CW SUB2 SUB5) (CW SUB14 SUB2) (CW SUB10 SUB14)
                    (CW SUB8 SUB10) (CW SUB7 SUB8) (CW SUB15 SUB7)
                    (CW SUB4 SUB15) (CW G36 SUB4) (CW SUB3 G36)
                    (CW SUB16 SUB3) (CW G40 SUB16) (CW SUB6 G40)
                    (CW SUB13 SUB6) (CW SUB11 SUB13) (CW SUB12 SUB11)
                    (CW SUB1 SUB12) (CW SUB9 SUB1) (CW SUB5 SUB9)))
        (:METRIC MINIMIZE (TOTAL-COST)))
