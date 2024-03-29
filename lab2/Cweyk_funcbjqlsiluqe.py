#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: Adrian Frydmański

text = '''Jiubdsk uis vub tjpvdb bunje, lb'c jgg uosk bds fjfskc."Bssijvsk
Jkkscbsn li Tumfpbsk Tklms Ctjinjg", "Djtrsk Jkkscbsn jybsk Zjir Bjmfskliv"...
Njmi rlnc.Bdse'ks jgg jglrs.

Zpb nln eup, li eupk bdkss-flsts fcetduguve jin 1950'c bstdiuzkjli,
sosk bjrs j guur zsdlin bds sesc uy bds djtrsk?Nln eup sosk quinsk qdjb
mjns dlm bltr, qdjb yuktsc cdjfsn dlm, qdjb mje djos mugnsn dlm?
L jm j djtrsk, sibsk me qukgn...
Mlis lc j qukgn bdjb zsvlic qlbd ctduug... L'm cmjkbsk bdji mucb uy
bds ubdsk rlnc, bdlc tkjf bdse bsjtd pc zuksc ms...
Njmi pinskjtdlsosk.Bdse'ks jgg jglrs.

L'm li xpiluk dlvd uk dlvd ctduug.L'os glcbsisn bu bsjtdskc safgjli
yuk bds ylybssibd blms duq bu ksnpts j ykjtblui.L pinskcbjin lb."Iu, Mc.
Cmlbd, L nlni'b cduq me qukr.L nln lb li me dsjn..."
Njmi rln.Fkuzjzge tuflsn lb.Bdse'ks jgg jglrs.

L mjns j nlctuoske bunje.L yupin j tumfpbsk.Qjlb j cstuin, bdlc lc
tuug.Lb nusc qdjb L qjib lb bu.Ly lb mjrsc j mlcbjrs, lb'c zstjpcs L
ctksqsn lb pf.Iub zstjpcs lb nusci'b glrs ms...
Uk yssgc bdksjbsisn ze ms...
Uk bdlirc L'm j cmjkb jcc...
Uk nusci'b glrs bsjtdliv jin cdupgni'b zs dsks...
Njmi rln.Jgg ds nusc lc fgje vjmsc.Bdse'ks jgg jglrs.

Jin bdsi lb djffsisn... j nuuk ufsisn bu j qukgn... kpcdliv bdkupvd
bds fduis glis glrs dskuli bdkupvd ji jnnltb'c oslic, ji sgstbkuilt fpgcs lc
csib upb, j ksypvs ykum bds nje-bu-nje litumfsbsitlsc lc cupvdb... j zujkn lc
yupin.
"Bdlc lc lb... bdlc lc qdsks L zsguiv..."
L riuq soskeuis dsks... sosi ly L'os isosk msb bdsm, isosk bjgrsn bu
bdsm, mje isosk dsjk ykum bdsm jvjli... L riuq eup jgg...
Njmi rln.Beliv pf bds fduis glis jvjli.Bdse'ks jgg jglrs...

Eup zsb eupk jcc qs'ks jgg jglrs... qs'os zssi cfuui-ysn zjze yuun jb
ctduug qdsi qs dpivsksn yuk cbsjr... bds zlbc uy msjb bdjb eup nln gsb cglf
bdkupvd qsks fks-tdsqsn jin bjcbsgscc.Qs'os zssi numlijbsn ze cjnlcbc, uk
lviuksn ze bds jfjbdsblt.Bds ysq bdjb KUWQJG_{CpzCblbpbluiTlfdskLcQsjr} djn cumsbdliv bu bsjtd yupin pc qlgg-
liv fpflgc, zpb bducs ysq jks glrs nkufc uy qjbsk li bds nscskb.

Bdlc lc upk qukgn iuq... bds qukgn uy bds sgstbkui jin bds cqlbtd, bds
zsjpbe uy bds zjpn.Qs mjrs pcs uy j cskolts jgksjne salcbliv qlbdupb fjeliv
yuk qdjb tupgn zs nlkb-tdsjf ly lb qjci'b kpi ze fkuylbsskliv vgpbbuic, jin
eup tjgg pc tklmlijgc.Qs safguks... jin eup tjgg pc tklmlijgc.Qs cssr
jybsk riuqgsnvs... jin eup tjgg pc tklmlijgc.Qs salcb qlbdupb crli tuguk,
qlbdupb ijbluijglbe, qlbdupb ksglvlupc zljc... jin eup tjgg pc tklmlijgc.
Eup zplgn jbumlt zumzc, eup qjvs qjkc, eup mpknsk, tdsjb, jin gls bu pc
jin bke bu mjrs pc zsglsos lb'c yuk upk uqi vuun, esb qs'ks bds tklmlijgc.

Esc, L jm j tklmlijg.Me tklms lc bdjb uy tpkluclbe.Me tklms lc
bdjb uy xpnvliv fsufgs ze qdjb bdse cje jin bdlir, iub qdjb bdse guur glrs.
Me tklms lc bdjb uy upbcmjkbliv eup, cumsbdliv bdjb eup qlgg isosk yukvlos ms
yuk.

L jm j djtrsk, jin bdlc lc me mjilyscbu.Eup mje cbuf bdlc linlolnpjg,
zpb eup tji'b cbuf pc jgg... jybsk jgg, qs'ks jgg jglrs.'''

slownik = {'K': 'R',
           'k': 'r',
           'R': 'K',
           'r': 'k',
           'Q': 'W',
           'q': 'w',
           'W': 'Z',
           'w': 'z',
           'Z': 'B',
           'z': 'b',
           'B': 'T',
           'b': 't',
           'T': 'C',
           't': 'c',
           'C': 'S',
           'c': 's',
           'S': 'E',
           's': 'e',
           'E': 'Y',
           'e': 'y',
           'Y': 'F',
           'y': 'f',
           'F': 'P',
           'f': 'p',
           'P': 'U',
           'p': 'u',
           'U': 'O',
           'u': 'o',
           'X': 'J',
           'x': 'j',
           'J': 'A',
           'j': 'a',
           'O': 'V',
           'o': 'v',
           'V': 'G',
           'v': 'g',
           'G': 'L',
           'g': 'l',
           'L': 'I',
           'l': 'i',
           'I': 'N',
           'i': 'n',
           'N': 'D',
           'n': 'd',
           'D': 'H',
           'd': 'h',
           'M': 'M',
           'm': 'm',
           '.': '.',
           ',': ',',
           '\'': '\'',
           '\n': '\n',
           '{': '{',
           '}': '}',
           ' ': ' ',
           '"': '"'}
out = ''
for c in range(0, len(text)):
    x = text[c]
    if x in slownik:
        x = slownik[x]
        out += x
    else:
        out += '_'

print(out)