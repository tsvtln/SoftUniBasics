groups = int(input())
l_1 = 0
l_2 = 0
l_3 = 0
l_4 = 0
l_5 = 0
tnop = 0

for _ in range(groups):
    ppl_in_group = int(input())
    if ppl_in_group <= 5:
        l_1 += ppl_in_group
        tnop += ppl_in_group
    elif ppl_in_group <= 12:
        l_2 += ppl_in_group
        tnop += ppl_in_group
    elif ppl_in_group <= 25:
        l_3 += ppl_in_group
        tnop += ppl_in_group
    elif ppl_in_group <= 40:
        l_4 += ppl_in_group
        tnop += ppl_in_group
    elif ppl_in_group >= 41:
        l_5 += ppl_in_group
        tnop += ppl_in_group

# formula: 'num of ppl in grp' / 'total number of ppl' * 100 = %

# prc ppl grp 1
prc_grp_1 = l_1 / tnop * 100
# prc ppl grp 2
prc_grp_2 = l_2 / tnop * 100
# prc ppl grp 3
prc_grp_3 = l_3 / tnop * 100
# prc ppl grp 4
prc_grp_4 = l_4 / tnop * 100
# prc ppl grp 5
prc_grp_5 = l_5 / tnop * 100

print(f'{prc_grp_1:.2f}%\n{prc_grp_2:.2f}%\n{prc_grp_3:.2f}%\n{prc_grp_4:.2f}%\n{prc_grp_5:.2f}%')
