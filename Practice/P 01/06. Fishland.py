midi = 7.5
skumria = float(input())
caca = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input()) * midi
palamud_prc = palamud_kg * (skumria + (skumria * 0.6))
safrid = safrid_kg * (caca + (caca * 0.8))


price = midi_kg + palamud_prc + safrid
print("%0.2f" % price)