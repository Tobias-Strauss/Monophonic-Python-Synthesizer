# Monophonic-Python-Synthesizer

This script only runs on Windows!  I rely on the winsound import for this build.  I am planning a universal script down the road, but it will not be any time soon.

To use the synth: remove the "sheet music" at the bottom of the script and replace with your own.  Think of it like a piano roll.  I've done the math and assigned variables for the pitches a PC speaker can reproduce, as well as common durations (whole note, half note, etc).

The synth defaults to 120 BPM.  If you want to change that, alter the duration variables.  Example: If I wanted 100 BPM, I'd divide 60,000 msec by 100 and get 600 for a beat (aka quarter note).  You can do the math if you want this. :)
