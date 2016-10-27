# Monophonic Python Organ
# By Tobias Strauss

import winsound

# An equally tempered scale is based on the constant A440 and the following formula:
# fn=f0*(a)^n
# f0 = 440 (A440, 4th octave A)
# a = 2^(1/12)
# n = the number of halfsteps up or down (an octave is 12 halfsteps)
#
# A4-G#5 from a basic chart, we'll calculate octaves as fx*octave (2, 3, .5, etc)

A4=440
Asharp4=466
B4=493
C5=523
Csharp5=554
D5=587
Dsharp5=622
E5=659
F5=699
Fsharp5=739
G5=784
Gsharp5=831

A3=A4/2
Asharp3=Asharp4/2
B3=B4/2
C4=C5/2
Csharp4=Csharp5/2
D4=D5/2
Dsharp4=Dsharp5/2
E4=E5/2
F4=F5/2
Fsharp4=Fsharp5/2
G4=G5/2
Gsharp4=Gsharp5/2

A2=A3/2
Asharp2=Asharp3/2
B2=B3/2
C3=C4/2
Csharp3=Csharp4/2
D3=D4/2
Dsharp3=Dsharp4/2
E3=E4/2
F3=F4/2
Fsharp3=Fsharp4/2
G3=G4/2
Gsharp3=Gsharp4/2

A1 = A2/2
Asharp1=Asharp2/2
B1=B2/2
C2=C3/2
Csharp2=Csharp3/2
D2=D3/2
Dsharp2=Dsharp3/2
E2=E3/2
F2=F3/2
Fsharp2=Fsharp3/2
G2=G3/2
Gsharp2=Gsharp3/2

Dsharp1=Dsharp2/2
E1=E2/2
F1=F2/2
Fsharp1=Fsharp2/2
G1=G2/2
Gsharp1=Gsharp2/2

# 120 BPM
# 60,000 msec/ minute
# Therefore, 500 msec/ beat

Whole=2000
Half=1000
Quarter=500
DottedEighth=375
Eighth=250
Sixteenth=125

# This is a sound test
# It is boring
# Uncomment at your own peril

##winsound.Beep(Gsharp5, Sixteenth)
##winsound.Beep(G5, Sixteenth)
##winsound.Beep(Fsharp5, Sixteenth)
##winsound.Beep(F5, Sixteenth)
##winsound.Beep(E5, Sixteenth)
##winsound.Beep(Dsharp5, Sixteenth)
##winsound.Beep(D5, Sixteenth)
##winsound.Beep(Csharp5, Sixteenth)
##winsound.Beep(C5, Sixteenth)
##winsound.Beep(B4, Sixteenth)
##winsound.Beep(Asharp4, Sixteenth)
##winsound.Beep(A4, Sixteenth)
##
##winsound.Beep(Gsharp4, Sixteenth)
##winsound.Beep(G4, Sixteenth)
##winsound.Beep(Fsharp4, Sixteenth)
##winsound.Beep(F4, Sixteenth)
##winsound.Beep(E4, Sixteenth)
##winsound.Beep(Dsharp4, Sixteenth)
##winsound.Beep(D4, Sixteenth)
##winsound.Beep(Csharp4, Sixteenth)
##winsound.Beep(C4, Sixteenth)
##winsound.Beep(B3, Sixteenth)
##winsound.Beep(Asharp3, Sixteenth)
##winsound.Beep(A3, Sixteenth)
##
##winsound.Beep(Gsharp3, Sixteenth)
##winsound.Beep(G3, Sixteenth)
##winsound.Beep(Fsharp3, Sixteenth)
##winsound.Beep(F3, Sixteenth)
##winsound.Beep(E3, Sixteenth)
##winsound.Beep(Dsharp3, Sixteenth)
##winsound.Beep(D3, Sixteenth)
##winsound.Beep(Csharp3, Sixteenth)
##winsound.Beep(C3, Sixteenth)
##winsound.Beep(B2, Sixteenth)
##winsound.Beep(Asharp2, Sixteenth)
##winsound.Beep(A2, Sixteenth)
##
##winsound.Beep(Gsharp2, Sixteenth)
##winsound.Beep(G2, Sixteenth)
##winsound.Beep(Fsharp2, Sixteenth)
##winsound.Beep(F2, Sixteenth)
##winsound.Beep(E2, Sixteenth)
##winsound.Beep(Dsharp2, Sixteenth)
##winsound.Beep(D2, Sixteenth)
##winsound.Beep(Csharp2, Sixteenth)
##winsound.Beep(C2, Sixteenth)
##winsound.Beep(B1, Sixteenth)
##winsound.Beep(Asharp1, Sixteenth)
##winsound.Beep(A1, Sixteenth)
##
##winsound.Beep(Gsharp1, Sixteenth)
##winsound.Beep(G1, Sixteenth)
##winsound.Beep(Fsharp1, Sixteenth)
##winsound.Beep(F1, Sixteenth)
##winsound.Beep(E1, Sixteenth)
##winsound.Beep(Dsharp1, Sixteenth)

##winsound.Beep(A4, Whole)
##winsound.Beep(A4, Half)
##winsound.Beep(A4, Quarter)
##winsound.Beep(A4, DottedEighth)
##winsound.Beep(A4, Eighth)
##winsound.Beep(A4, Sixteenth)

# Song goes down here
# This is Bach's Prelude and Fugue in B Flat Major
# Arr. Tobias Strauss

winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(D5, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(Dsharp5, Sixteenth)
winsound.Beep(D5, Sixteenth)
winsound.Beep(F5, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(C5, Sixteenth)

winsound.Beep(Asharp3, Sixteenth)
winsound.Beep(D4, Sixteenth)
winsound.Beep(C4, Sixteenth)
winsound.Beep(Dsharp4, Sixteenth)
winsound.Beep(D4, Sixteenth)
winsound.Beep(F4, Sixteenth)
winsound.Beep(F5, Sixteenth)
winsound.Beep(Dsharp5, Sixteenth)

# Bar 2
winsound.Beep(D5, Sixteenth)
winsound.Beep(Dsharp5, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(Dsharp5, Sixteenth)
winsound.Beep(D5, Sixteenth)
winsound.Beep(Dsharp5, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(C5, Sixteenth)

winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(F3, Sixteenth)
winsound.Beep(Gsharp3, Sixteenth)

#Bar 3

winsound.Beep(G4, Sixteenth)
winsound.Beep(Gsharp4, Sixteenth)
winsound.Beep(F4, Sixteenth)
winsound.Beep(Gsharp4, Sixteenth)
winsound.Beep(G4, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(C5, Sixteenth)

winsound.Beep(A4, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(G4, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(D5, Sixteenth)

#Bar 4

winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(D5, Sixteenth)
winsound.Beep(Dsharp5, Sixteenth)

winsound.Beep(C5, Sixteenth)
winsound.Beep(D5, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(D5, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(D5, Sixteenth)
winsound.Beep(Dsharp5, Sixteenth)
winsound.Beep(F5, Sixteenth)

#Bar 5

winsound.Beep(D5, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(G4, Sixteenth)
winsound.Beep(F4, Sixteenth)
winsound.Beep(E4, Sixteenth)
winsound.Beep(D4, Sixteenth)

winsound.Beep(C4, Sixteenth)
winsound.Beep(Asharp3, Sixteenth)
winsound.Beep(A3, Sixteenth)
winsound.Beep(G3, Sixteenth)
winsound.Beep(F3, Sixteenth)
winsound.Beep(E3, Sixteenth)
winsound.Beep(D3, Sixteenth)
winsound.Beep(C3, Sixteenth)

#Bar 6

winsound.Beep(B2, Sixteenth)
winsound.Beep(D3, Sixteenth)
winsound.Beep(G3, Sixteenth)
winsound.Beep(B3, Sixteenth)
winsound.Beep(D4, Sixteenth)
winsound.Beep(G4, Sixteenth)
winsound.Beep(G3, Sixteenth)
winsound.Beep(B3, Sixteenth)

winsound.Beep(D4, Sixteenth)
winsound.Beep(G4, Sixteenth)
winsound.Beep(B4, Sixteenth)
winsound.Beep(D5, Sixteenth)
winsound.Beep(B3, Sixteenth)
winsound.Beep(D4, Sixteenth)
winsound.Beep(G4, Sixteenth)
winsound.Beep(F5, Sixteenth)

#Bar 7

winsound.Beep(E5, Sixteenth)
winsound.Beep(G5, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(C5, Sixteenth)
winsound.Beep(F4, Sixteenth)
winsound.Beep(A4, Sixteenth)

winsound.Beep(Asharp4, Sixteenth)
winsound.Beep(Asharp3, Sixteenth)
winsound.Beep(A4, Sixteenth)
winsound.Beep(G4, Sixteenth)
winsound.Beep(G4, DottedEighth)
winsound.Beep(F4, Sixteenth)


#Bar 8

winsound.Beep(F5, Quarter)
winsound.Beep(F3, Quarter)

#Sound Check


