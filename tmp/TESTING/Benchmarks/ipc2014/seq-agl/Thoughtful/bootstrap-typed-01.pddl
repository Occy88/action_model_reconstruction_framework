(define (problem thoughtful-s5-t4)
(:domain thoughtful-typed)
(:objects
    C0 CA C2 C3 C4 C5 
    D0 DA D2 D3 D4 D5 
    H0 HA H2 H3 H4 H5 
    S0 SA S2 S3 S4 S5 
 - card
    COLN0 COLN1 COLN2 COLN3 COLN4
 - colnum
    N0 N1 N2 N3 N4 N5
 - num
    C D H S
 - suittype
)
(:init
(VALUE C0 N0)
(VALUE D0 N0)
(VALUE H0 N0)
(VALUE S0 N0)
(VALUE CA N1)
(VALUE DA N1)
(VALUE HA N1)
(VALUE SA N1)
(VALUE C2 N2)
(VALUE D2 N2)
(VALUE H2 N2)
(VALUE S2 N2)
(VALUE C3 N3)
(VALUE D3 N3)
(VALUE H3 N3)
(VALUE S3 N3)
(VALUE C4 N4)
(VALUE D4 N4)
(VALUE H4 N4)
(VALUE S4 N4)
(VALUE C5 N5)
(VALUE D5 N5)
(VALUE H5 N5)
(VALUE S5 N5)
(COLSUCCESSOR COLN1 COLN0)
(COLSUCCESSOR COLN2 COLN1)
(COLSUCCESSOR COLN3 COLN2)
(COLSUCCESSOR COLN4 COLN3)
(SUCCESSOR N1 N0)
(SUCCESSOR N2 N1)
(SUCCESSOR N3 N2)
(SUCCESSOR N4 N3)
(SUCCESSOR N5 N4)
(SUIT C0 C)
(SUIT D0 D)
(SUIT H0 H)
(SUIT S0 S)
(SUIT CA C)
(SUIT DA D)
(SUIT HA H)
(SUIT SA S)
(SUIT C2 C)
(SUIT D2 D)
(SUIT H2 H)
(SUIT S2 S)
(SUIT C3 C)
(SUIT D3 D)
(SUIT H3 H)
(SUIT S3 S)
(SUIT C4 C)
(SUIT D4 D)
(SUIT H4 H)
(SUIT S4 S)
(SUIT C5 C)
(SUIT D5 D)
(SUIT H5 H)
(SUIT S5 S)
(KING C5)
(KING D5)
(KING H5)
(KING S5)
(CANSTACK C2 D3)
(CANSTACK C2 H3)
(CANSTACK S2 D3)
(CANSTACK S2 H3)
(CANSTACK D2 C3)
(CANSTACK D2 S3)
(CANSTACK H2 C3)
(CANSTACK H2 S3)
(CANSTACK C3 D4)
(CANSTACK C3 H4)
(CANSTACK S3 D4)
(CANSTACK S3 H4)
(CANSTACK D3 C4)
(CANSTACK D3 S4)
(CANSTACK H3 C4)
(CANSTACK H3 S4)
(CANSTACK C4 D5)
(CANSTACK C4 H5)
(CANSTACK S4 D5)
(CANSTACK S4 H5)
(CANSTACK D4 C5)
(CANSTACK D4 S5)
(CANSTACK H4 C5)
(CANSTACK H4 S5)
(COLSPACE COLN0)
(BOTTOMCOL HA)
(CLEAR HA)
(FACEUP HA)
(BOTTOMCOL H5)
(ON C4 H5)
(CLEAR C4)
(FACEUP C4)
(BOTTOMCOL D2)
(ON H3 D2)
(ON S5 H3)
(CLEAR S5)
(FACEUP S5)
(BOTTOMCOL D4)
(ON C3 D4)
(ON SA C3)
(ON CA SA)
(CLEAR CA)
(FACEUP CA)
(BOTTOMTALON S3)
(ONTALON D3 S3)
(ONTALON D5 D3)
(ONTALON H4 D5)
(ONTALON C2 H4)
(ONTALON S4 C2)
(ONTALON DA S4)
(ONTALON C5 DA)
(ONTALON S2 C5)
(ONTALON H2 S2)
(TOPTALON H2)
(TALONPLAYABLE D5)
(HOME C0)
(HOME D0)
(HOME H0)
(HOME S0)
)
(:goal
(and
(HOME C5)
(HOME D5)
(HOME H5)
(HOME S5)
)
)
)
