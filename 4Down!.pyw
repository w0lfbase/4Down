"""

This tool was developed by w0lfbase
    w0lfbase.com

This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""



import Tkinter, tkFileDialog,re,os,urllib2,sys,getpass,base64
from Tkinter import *
user = getpass.getuser()
ext_list = ['jpg','png','webm','gif']
dirname = "c:\\users\\{0}\\pictures".format(user).title()
urllist = []
debug = False

#base64 source of icon

icon = \
""" AAABAAQAEBAAAAAAIABoBAAARgAAACAgAAAAACAAqBAAAK4EAAAwMAAAAAAgAKglAABWFQAAQEAA
AAAAIAAoQgAA/joAACgAAAAQAAAAIAAAAAEAIAAAAAAAQAQAAAAAAAAAAAAAAAAAAAAAAAD///8B
////Af///wEveT0JJ281BxNpF3MUbBiR////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wEYaB8bHHAf4xduGtUbcx3/GHMa/w5mEj////8B////ARFnFIEhdyXXHHEfoRdq
IQ3///8B////Af///wH///8BFW4ZhxV1GP8kfyn/Cm4O/xR1GP8PbhJp////ARZqG3MZcxz/AGMA
/xZyGP8JZQt5////Af///wH///8B////ARlwHJk2k0X/MY9A/zGQQf82kkT/DGgQYVOYbAMkfSrl
H4Ap/yGBK/8vhjb/D2UTgf///wH///8B////Af///wEPYxVFQ5pU/1mydf9ZsnT/SKBb/xBmFjcO
ZxUvRJ1V/1Cqaf9Qqmn/T6pp/0qgXP8KYw5h////Af///wH///8B////ARZpG3dQpGT9cMiU/zqR
SeVJi14DC2IQW2a6gf9xyJX/cMiU/3HIlP9NoWD9DWMTQ////wH///8B////Af///wH///8BD2IV
Myl+Ma0ZbR9z////ARptJRcLYw5vI3kqpSWALrMcciGTDmEVNf///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////ATp/VAf///8B////Af///wH///8B////Af//
/wH///8BEWYeExhvHY0geCPNH3cj0R92I6cNZBJZQoViBf///wEXcBuVHHQf4RlwHocQZhwX////
Af///wH///8B////ARlxHr8PbRH/AGMB/wBkAf8FZwb/GnUc/yJ1NRv///8BGXQc3wBjAP8ObRD/
HHIf5RBjGCf///8B////Af///wEVbBqZKIQw/yKDLf8igyz/IYIs/yJ9KeH///8BM35OER56I/8b
fSL/G30i/x+AJ/8ccyG3////Af///wH///8BRIhlAxNqGMNPpWP/Uaxs/1OsbP8bcSCP////ASh7
PCM0jkL/Qp5X/0OeWP9Cnlb/LoQ55f///wH///8B////Af///wEwgzvVcciV/3DHkv81iUHvFGge
G////wE3f1MPQ5tV/Wa/iP9CmFH/Z7yE/yN5Kqv///8B////Af///wH///8BD2AbJRpyIKUWbhur
DWMXL////wH///8B////AS2COcFluoH/GW8hoQtiDpkaaScb////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wESZxwjAV0CjSh9PAv///8B////Af///wH///8BAAD//wAA
//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD//wAA//8AAP//AAD/
/ygAAAAgAAAAQAAAAAEAIAAAAAAAgBAAAAAAAAAAAAAAAAAAAAAAAAD///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////ARdrH0kLZw9nM3dCEf///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wEveT0jJ281Gf///wEYZR+FEGoR/x93Iv8JXwzP////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8BEmAZkRBsEv8GXgf1Kn01XxtuHP8m
eyr/FW0W/yR6J/8RbBdZ////Af///wH///8B////Af///wH///8BF2sdVQxhD6sLXg6zDWMSgTZ+
Rhf///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////ARhoH2kmeSn/I3Um
/y+HM/8IXgn/K4Mv/wBiAP8AYgD/J4Iq/wxjEKH///8B////Af///wH///8BVZVuAwpeDq0UbBb/
L4Yz/zGINv8rhC7/EGMT6RdqIS////8B////Af///wH///8B////Af///wH///8B////Af///wFY
lWwDC2gN6SF7JP8BZQL/GXQc/zKJN/8EZAX/AWcC/wFnAv8adRz/D28Ty////wH///8B////Af//
/wETYhmZJ3sq/yB4JP8AYQD/AGAA/wNhA/8uhjP/CmIM2f///wH///8B////Af///wH///8B////
Af///wH///8B////ATB6QS8acRz/HX0j/xN3Gf8XeR3/LIcy/xF1F/8Tdxn/E3cZ/yKBKf8PbhHX
////Af///wH///8BKn43MRVrFv8edyH/AWQB/wFmAf8BZgH/AGIA/yh+LP8FZQb/SItgC////wH/
//8B////Af///wH///8B////Af///wH///8BLX86QRtyHv8vjTz/KIg0/yeHM/8mhjL/KIg0/yiI
NP8oiDP/NI8//wxrD9H///8B////Af///wELXxCjMow4/w5zFP8Udxv/FHcb/xR3G/82jD3/F2wZ
/xNmGYf///8B////Af///wH///8B////Af///wH///8B////Af///wE2fksjDWgM/0WeWP87mE7/
O5hO/zuYTv87mE7/O5hO/zuXTf9Em1L/DGMQs////wH///8BU5hsCRFsEfU4k0b/LYw7/y2MO/8t
jDv/LYw8/zuTR/81izz/DWcP9Q5hFYf///8B////Af///wH///8B////Af///wH///8B////Af//
/wELXhDRSZ5W/0+qaP9PqWf/T6pn/0+qZ/9Pqmf/Tqln/0GaTf8IXgqL////Af///wEkdjJFJn4r
/0eiXP9EoFn/RKBZ/0SgWf9EoFn/Q59Y/0KfV/9TqGb/G3Ed/xZmHov///8B////Af///wH///8B
////Af///wH///8B////ARtyJ0UOZA//Z7uC/2O7g/9ju4L/Y7uC/2O7gv9pwIr/KH0v/x91LE3/
//8B////AQJeBXlGnlL/XLV7/1y1ev9ctXr/XLV6/1y1ev9ctXr/XLV6/1u0ef9esnT/A2EE8///
/wH///8B////Af///wH///8B////Af///wH///8B////ARNfHHcWbhj/bsKL/3DJlv9uxpH/bsaR
/3LHk/8KZgvzSYteCf///wH///8BDGARpWG1ef9uxpL/bsaR/27Gkf9uxpH/bsaR/27Gkf9uxpH/
cMmW/16xcv8JXg7R////Af///wH///8B////Af///wH///8B////Af///wH///8B////ARlpIWUP
YRH1UKJd/3TLl/9xy5j/TqRe/wxdEJ////8B////Af///wEKYw/HV6ln/3HFkP91y5n/csqY/3LK
l/9yypf/dMuZ/3TIlf9Vp2T/DmAR8xxyJzf///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////ASh3OCMKXg6pF20Y/U6iW/8Zbxz/IXMyL////wH///8B////ARptJVcLXhG7
CWYJ9yB2I/8sgzT/Mo07/zCIOv8nfC3/D2kP9wpdD6shczMl////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wEndD8pCF0OjxZnH53///8B////Af//
/wH///8B////Af///wE4eksNJHI0OxFqG10GYgtpDGgUZR5xLEcrc0MP////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////ATp/VBf///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8BRoljBxxwLE0GXwmLCV4NpwRdCakIXg2ZCWUOayx5QTH/
//8B////Af///wH///8B////Af///wFWl3cHCWQL8xBuEuUJXw2jF2snR////wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////ARFmHkcLYw3jIngk/y+HM/8uhzH/LIYx
/zCIM/8ogir/HnIg/wxmD90OYhaDQoViFf///wH///8B////ARdwJFUieyT/H3Ui/zCHNP8lfCj/
DGQQ1xBmHFX///8B////Af///wH///8B////Af///wH///8B////Af///wEvgEc3D2QR/TKIN/8L
aAz/AGAA/wBhAP8AYQD/AGAA/wBjAP8Ubhb/K4Iw/xt0HP8dci5P////Af///wH///8BC2ARoSmE
LP8AYgD/AGEA/wpnCv8whTX/HHMd/xBjGZn///8B////Af///wH///8B////Af///wH///8B////
AQljDskrhS7/AV8B/wFnAv8BZwL/AWcC/wFnAv8BZwL/AWcC/wFnAv8HaQj/GXUa/zR/UBf///8B
////Af///wENbhDfG3Ye/wBlAP8AZgD/AGYA/wBiAP8ZdBr/Jnop/xBiGJn///8B////Af///wH/
//8B////Af///wH///8BFWwfkx92If8hgCj/FHcb/xV4HP8VeBz/FXgc/xV4HP8VeBz/FXgc/yWD
Lf8RbxPh////Af///wH///8BP4ZcExZvFv8beyH/EXQW/xF0Fv8RdBb/EXQW/w5yE/8ohC7/EWYS
/yh9Nz3///8B////Af///wH///8B////Af///wFkoogHB14Lyyx/MP8/mEz/L48//y6NPP8ujTz/
Lo08/y6NPP8sjDr/PJRG/w1hE6P///8B////Af///wEvfEgxHnYg/yqJNv8lhi//JYYv/yWGL/8l
hi//JYYv/yCDLP8vijX/CV8Pn////wH///8B////Af///wH///8B////Af///wFEiGUJDWEXgQ1m
Dv02hzr/TKNf/0eiXP9Holz/R6Jc/0qlYv8pfi3/GnMoT////wH///8B////ASh6PEUieif/O5lO
/zmVSv85lUr/OZVK/zmWSv85lUr/OJVJ/0OaUP8LYRLN////Af///wH///8B////Af///wH///8B
////Af///wESZhyLHnYh/1+0eP9dtnz/XLd8/123fP9ct3z/YLR3/wthDudRknQF////Af///wH/
//8BKXw9RSV7Kv9Qqmn/TKdk/0ynZP9Lp2P/Uahn/0ynY/9Mp2P/T6Vg/wxiFMf///8B////Af//
/wH///8B////Af///wH///8B////AQleENtitXj/b8eT/2/Gkv9vxpL/bsaS/3fLmv8fcyL/FGge
Z////wH///8B////Af///wE0fE4tIXcl/2a+h/9fuH//X7h//2a+hv83jDr/Zr6I/2C7gv9Emk//
CF8Mjf///wH///8B////Af///wH///8B////Af///wH///8BF2gieyp+Lv91yZf/csqZ/3TLmf9w
w47/Kn0u/wheDr3///8B////Af///wH///8B////AUmPbgkOag35dcqX/27Gkf9uxpL/ar2D/wBb
AP9itXj/csSP/xBmEv0qfEEl////Af///wH///8B////Af///wH///8B////Af///wH///8BD2Ab
kw9nDv8rgzL/J34s/whhCP8LYhSxLXZOC////wH///8B////Af///wH///8B////AQteErlitnj/
bseS/3bMm/8sfzH/EmwfoQVfBP8IYQj/Gmknaf///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8BJHI+LwhlEmsHZg9xInM4P////wH///8B////Af///wH///8B////Af//
/wH///8BGHEmSRltG/9sv4f/RJhQ/wddC9tnpZgFHm0yOyRyPi3///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8BEWccgwBfAPMDWwTZKH08K////wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wEfdzAFAV4BQQRdByX///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoAAAAMAAAAGAA
AAABACAAAAAAAIAlAAAAAAAAAAAAAAAAAAAAAAAA////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////ASZyNQ0TahorBmMJNR5wJyEzd0IF
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BI3Uv
ExFmGH0HXwrVA2EE6QpdDcEjby1B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////ATuA
Tg0tdzpBJ281N////wH///8BJHAsgQVbBvEieyX/M4g3/xRrFv8MZA/ZcayMA////wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8BGmkkTQpgDdUKYgv/BF0F9xRnGoM0gz9HCVoJ/zKHNv8sfzD/GHAa/zSK
Of8SZhT/HHQlc////wH///8B////Af///wH///8B////Af///wH///8B////ASt1Ng8RaRYzGWog
eRRlGZMXZx6LF2gfWRxwJSc2fkYH////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wE4hUcxEF4V4yJ4Jf82izv/H3kh/wtiDuML
YQ/bKIAr/yZ8Kf8DXwP/AGAA/xlxG/8phSv/A10Eu0qOWwv///8B////Af///wH///8B////Af//
/wH///8BH3IrHxFlFo0HXgnjC2kM/xhwGv8acBz/EGsR+QphDckYZyBr////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////AWGffQ0LXA6t
IXgj/y2EMf8RYRL/MIk0/xltG/8SaxT/NIo6/wViBf8AZAD/AGQA/wdoB/8uiDL/BV8H0ziCSSn/
//8B////Af///wH///8B////Af///wFVlW4HBlsKvQhhCvcnfSr/OIw9/zKIN/8whjT/N4w7/yqA
Lv8MXg7vF2khaf///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////ARJrGmEIYwnvM4k2/wRjBP8AZQH/DWoP/yqCLv8zijj/CWgK/wBjAf8AZgH/
AGYB/wBiAP8ngCv/Cm4M4xxwKEn///8B////Af///wH///8B////ATF+QRMSZRixEmQU/zeNPf8m
fCr/AGAA/wBdAP8AXQD/Al4C/yB6I/80izn/B1oI5SR4L03///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8BOoBLCwdfCpMbeBz/J4Ar/wVoB/8IbQv/CmoN
/0KVSP8wiDX/BGYH/whtDP8IbQv/CG0M/wVqCP8ogi3/DW8P6RZtHlX///8B////Af///wH///8B
WZZwBRZnHGkJXArxOI08/xpzHP8BXwH/AGUA/wBlAP8AZQD/AGQA/wBfAP8sgjH/B2sH/QRhB4VE
iFsF////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BLnk+Gw1h
ErUogCv/J4Qu/xJ2GP8WeRz/FXgc/ymFL/8cfCL/FXgb/xZ5HP8WeRz/Fnkc/xF3GP8wijf/DG4N
6xRtGln///8B////Af///wH///8BJXwyIw1gEcMpfy3/IHsj/wJhAv8BZgL/AWcC/wFnAv8CZwL/
AGIA/w5qEf83jDz/A2IE/whnDIlNj2YF////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8BL4E8IxBkFMEpgC7/M48//yKELv8lhjD/JYYw/yGDLP8khS//JYYw/yWG
MP8lhjD/JYYw/yOELv85kkT/B2oI6RpwJFP///8B////Af///wH///8BFmgeYxNtE/82jjz/B20K
/xB1Fv8RdBf/EXQX/xB0Fv8QcxX/J4Iu/zyOQv8Wbhj/Cl0Nw0KIVCX///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8BK3g6HQ1fErckeyb/QptS/y6OP/8x
kEH/MZBB/zGQQf8xj0H/MZBB/zGQQf8xj0H/MY9B/zORQ/9BmE3/BWYH4R1wLEX///8B////Af//
/wH///8BEWoXvyZ9Kf8siTf/HoAo/yCBK/8ggSr/IIEq/x1/KP8ohzP/S5tT/yJ3Jf8IYQj/CGEM
xQ9mGU8vfEIN////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
P4RVDwthDpsNbQz/TqNf/z2aUf8+mlH/PppQ/z6ZUP8+mlD/PppQ/z6ZUP8+mlD/PZlQ/0OeWP9C
mE3/BFwG1y16PS////8B////Af///wFTmGwTC2MM9ziQP/8xkEH/MI8//zCOP/8wjj//MI4//zCO
P/8vjj//NpJF/0GZTv9ClUv/HXQe+wJbBOcNYBSfaaWGA////wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////ARJuHWEDWAXvQ5hN/1atbv9Mp2T/TKdk/0ynZP9Mp2T/
TKdk/0ynZP9Mp2T/TKdk/1Wtbf82kD3/A1kFx02NZBX///8B////Af///wErezxZEmoU/0ifV/9C
nlf/QZ1V/0GdVf9BnVX/QZ1V/0GdVf9BnVX/QJxV/zuaUP9AnVX/Valn/zmOQP8JXQn/GGsgpTqD
TQ////8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////AUGIVhsJXQ7BHXIf
/1uvb/9ctXn/WrJ0/1qzdP9asnT/WrN0/1qzdP9asnT/WrN1/160eP8feyP/C2cQo2KefQP///8B
////Af///wEMZxORH30i/1etbv9Rq2r/UKtp/1Cqaf9Qq2n/UKtp/1Cqaf9Qq2n/UKpp/1Cqaf9Q
qmj/T6pp/1yyc/82jDz/BVcG5x1zJ1H///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wEsfj1HBFsF/zSIO/9swIr/Zr6J/2S8hf9lvIX/ZbyF/2S9hf9lvIX/aMCK
/1+zdv8TZxX/JHcyZ////wH///8B////AUuMZAcBXAK5OJE+/2e9hv9ft37/X7d+/1+3ff9ft33/
X7d+/1+3ff9ft33/X7d+/1+3ff9ft33/Xrd9/2O8hP9esHH/AGMB+wNiBHf///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8BG2gncwJXA+0yhjf/c8iT/3LL
mP9ux5P/bsaR/27Gkf9uxpH/c8qY/0eeVP8HYQj3SYpdEf///wH///8B////ATuFUCMEWQbRUKRf
/3XLmv9txZH/bcWQ/23FkP9txZD/bcWQ/23FkP9txZD/bcWQ/23FkP9txZD/bsaS/3bMm/9ZrGr/
AlsE7w5qFl////8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8BInA1DxZoIHUDWwTrMIE2/2W2ev92y5n/cMmV/27Gkv9uxpH/cMWQ/yh8L/8RaRi5////Af//
/wH///8B////ASl4OzUEXQfZZbZ6/3jPoP9wyZb/b8eT/27Hkv9uxpH/bsaR/27Gkf9uxpH/bsaS
/2/Ik/9wypb/d8ya/2a4e/8hdST/Dl8Uuz2IUR3///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////AUWKWw0caydTC14P6RdqFv9KnFT/dciT/3bNm/9z
zZz/XrJz/wtlCv8VZhxf////Af///wH///8B////ARluJk8EXwbnP5RH/2Kydv9zxJD/ecyb/3bM
nP90zJv/dMya/3TMmv90zJr/ds2c/3nNm/9zxI//T6Ba/xtvG/8LXRDlI3YwL////wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
KHc4Gw9lFZUEWAfbGXIY/0SWT/9uvoX/MYQ2/wlcDr8bcCwh////Af///wH///8B////ATuDUCsR
ZhiZBVcH1wRgBO8RbRD9LYIx/zuPRP9EmFD/SZ9Z/0qgWv9Hm1X/PZBH/y2BMf8QbA35BVcH3Q1i
FJshczMd////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////AUSGXwckdDU7B1wMmQdgC9kXbhj7C2QN9RNpG3FRkmwF
////Af///wH///8B////Af///wFDhV4DLXlAMQ1mFl8HXQuNC18QtQlhDs8GYgvfBGQG6QNkBekG
YwnhCmIOywpdD60DXgh9J3U6OzZ/VAn///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BLnhG
DxBnHS8TYx1tFGMenzuJTyX///8B////Af///wH///8B////Af///wH///8B////Af///wE4eksJ
J3M4GxluJikQahkxB2MNNQZjDDUOaRYxG3AnJyh0Oxcrc0MF////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////AVCUbw0yeEspTY1sA////wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BRoljAzN+
TBMWbSQrDGMSTRhpI28OYxd9BFwMfxNlH3cSZRxhBmIKOxxxKSkuekYV////Af///wH///8B////
Af///wH///8B////Af///wH///8BVpd2AxNuHXMGXgj3C2kO4xJpGqkRZBpnEmkgKSlyQQ3///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wFBgmQFE2ceWwtfEKMJZg7VEm8T+RlxG/8bdB3/G3Ye/xtyHP8XcBf/DWwO7wtm
D9ELXRGpCGQQZyx6Pjc/hlkJ////Af///wH///8B////Af///wH///8BNYFNFQxhEqceeB//L4ky
/yB5If8bcxz/DGgQ0QddDpEYbSZNP4BeBf///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////AUGGYw8LYRSNCF0J6yJ6I/80iDj/NYk4/y6FMf8o
giv/JoIq/yuEL/8xiDX/NIo4/zOHN/8qfyz/DGoN8wVZB9sNYxWlQoViL////wH///8B////Af//
/wH///8BEGwaMQxrEN8vhzP/D2UR/xh0Gv8whjT/N4s7/yF6JPsIXQrlCGERmS55RSP///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BPYlaEw1iFZsLYQ39
O5BB/yuBMP8JaAr/AFwA/wBeAP8AXwD/AF8A/wBeAP8AXQD/AGAA/wprC/8jeib/Noo8/zOJOP8K
ZAv/GnAphf///wH///8B////Af///wH///8BFWcfYRhwGf8ngir/AF4A/wBkAP8AXQD/B2YI/yuB
Lv89kEP/EmwS/w5gE9sXaiNT////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8BInYxbQtkD+svhDP/GHIb/wBfAP8AYwD/AGUA/wBlAP8AZQD/AGUA/wBlAP8AZQD/
AGUA/wBjAP8AXwD/BGQE/yeCK/8QbxH/KXlCSf///wH///8B////Af///wH///8BF28jpx54IP8V
dBf/AGMA/wBlAP8AZQD/AGMA/wBgAP8TaxX/MYc1/yZ6KP8MXhDpDGUXT////wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8BDGQTtQ9tEP8xiTX/AF0A/wJoA/8CaAP/AmgD
/wJoA/8CaAP/AmcD/wJnA/8CaAP/AmcD/wJnA/8CaAP/BWcG/yWBKP8MaA3/N4BUG////wH///8B
////Af///wH///8BC2sR2SSAJf8NaA7/AGYA/wBmAP8AZgD/AGYA/wBmAP8AZAD/CGUJ/y6GM/8j
eSb/CFgN0zCEQzv///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BG3AphwVj
B/UziDf/G30i/w5zFf8SdRj/EnUY/xJ1GP8SdRj/EnUY/xJ1GP8SdRj/EnUY/xJ1GP8SdRj/E3YZ
/y2HMP8LaQ/f////Af///wH///8B////Af///wFDiWMVCmQK/yyGMP8OcRL/DXES/w1xEv8NcRL/
DXES/w1xEv8NcRL/C3AQ/wpvDv87kUH/EGgQ/w1fEqk1hUkX////Af///wH///8B////Af///wH/
//8B////Af///wH///8BMH5FIwtfEbMQZhH/QZVJ/y+MOv8ggiv/IYMs/yKDLf8igy3/IoMt/yKD
Lf8igy3/IoMt/yKDLf8hgyz/K4k2/yR9KP8XcCKn////Af///wH///8B////Af///wE3f1EzDWYO
/zKMOf8cfiT/G30j/xt9I/8bfSP/G30j/xt9I/8bfSP/G30j/xd6H/8jgyz/Mog3/whiCe8TaxxB
////Af///wH///8B////Af///wH///8B////Af///wH///8BZKKIAx5wLTcIYAzXFWkX/z6SRP9J
nlf/NpRH/y6PPv8xjz//MY9A/zGPQP8xj0D/MY9A/zGPQP8sjTz/QppP/xlwGf8abCZn////Af//
/wH///8B////Af///wEte0ZPD2kQ/zeQQf8oiDX/J4gy/yeIMv8niDL/J4gy/yeIMv8niDL/J4gy
/yeHMv8ggyz/PJRG/xBpEP8XaCZ9////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wFEiGUVCl8VmwNfBOkccx7/O45D/0ueWP9En1n/RJ9Y/0SfWP9En1j/RJ9Y/0OfWP9G
ol3/QJRJ/wpnDtsSbh0v////Af///wH///8B////Af///wEoezxlEGoT/z+YTf83lUj/NpNH/zaT
R/82k0f/NpNH/zaTR/82lEf/NpNH/zaTR/80kkX/RJxT/x5zIf8XayOx////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8BJHc5IQxmE70EWwP/L4Ez/1WlY/9TrW3/
Uaxr/1Gsa/9RrGv/Uatr/1GsbP9gtXr/IHgh/wtdEJ84hFER////Af///wH///8B////Af///wEp
ejxrEmsU/0ifWf9En1n/Q51X/0OdV/9DnVf/Q51X/0OeV/9Dnlj/Q51X/0OdV/9DnVb/S6Ne/yJ6
Jv8PZxq1////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BGWsm
gwdfB/U7j0P/aLyG/2C5gf9guYH/X7qB/2C6gf9guoH/X7mB/2jAi/9WqWT/CFkK7RtxKV3///8B
////Af///wH///8B////Af///wEpfT1jEmkV/1GnZP9Rq2r/Tqln/06pZv9OqWf/Tqlm/1CqaP9V
qmv/Talm/06pZv9OqWb/Vq1s/yJ2Jv8Xayan////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8BDWUWzSBzIv9yxJD/b8iV/2/Gkf9vxpL/b8aS/2/Gkf9uxpL/dMua
/2e4fv8WbBf/CV8NrV6egwn///8B////Af///wH///8B////Af///wEweklJEWgT/1itbP9guX//
XLZ7/1y2e/9ctnv/X7l+/1WpZ/9ClUj/Zb2F/1y3e/9duX//XK9v/xFqEf0ZayVl////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8BGGonmRVoFv9ouX//c8yb/27H
k/9uxpH/bseS/2/IlP90zJv/bL2G/yt9L/8IWgzzL4JGNf///wH///8B////Af///wH///8B////
Af///wFAh2IpDGMN/1araP9txZH/acGL/2nBi/9owIv/bsWS/0CXTf8RbhD/c8WS/23Hlf90y5r/
QpVM/wdgCt8OaBcx////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8BJHU1PQ5gEt8pfSz/csKN/3nNnf90zJz/ds2c/3nLmv9mt3v/I3gl/wRZBPsSZx15////Af//
/wH///8B////Af///wH///8B////Af///wFJj20HBWIF8UaeUv9yy5j/bsaR/27Gkf9ux5P/csWP
/yd8K/8AWQD/SJxT/3vLmf9ltnn/DGQO/QdeDZMxgEkL////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////ARVqJkcIWA7NDWkL/zSHOf9Dl07/PpJH/yd8Kf8G
YQb/BVsK4RBpHG0sdU4J////Af///wH///8B////Af///wH///8B////Af///wH///8BEmgfqSl9
Lv9xxZH/bsaS/27Gkf92zZz/TJ5Y/whiC+cLaRTJA10D/xRtEv8GYAb/C10Rr0+Xcxv///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wEmdz41
CV8PowdeDtMDYQftAmEF8wdfDN0LYhKzGGwpS0iHdAf///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8BFmcjVw5lD/dZqmr/eM+f/3fNnP9tv4b/FGsU/wtdE59Fi2slCWAPrwpd
EcsIXw6fOYZYJf///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8BLXlLERJoIysGZQ83CWgSPRBqHS8ndkEb////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8BKHs9GwtcErUVbBX/YLFy/12ub/8j
eif/BVcI4yN2NktmpJgDInA5GRxsMCcpdkYR////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////AS2ARjkJXQ7DAF4A9wFfAPsCWQPlKH08X////wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wEXbyQzAFsArQBeALkMZRNl////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wEedzADAFwA
HwFeASMLYxAN////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8BAAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAA
AP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA
//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD/
/wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//
AAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8A
AAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAA
AAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//AAAAAAAA//8AAAAAAAD//wAAAAAAAP//KAAA
AEAAAACAAAAAAQAgAAAAAAAAQgAAAAAAAAAAAAAAAAAAAAAAAP///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8BJnI1XRBpFsMCYQPbF24evzN3
QkX///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8BI3UvlwBZAP8AWAD/AGMA/wBWAP8AUgD/TJNhQ////wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8BO4FOIyx3OGknbzVh////Af///wH///8BPIlKgQBLAP8GZwb/PJJA/0mZT/82jTz/AFoA
/wxmEPlxrIwF////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8BIG0sjQBaAP8AVQD/AFgA/xVqHNX///8BYqR0
KwBMAP8UbRT/Tp9W/zKFN/8Ybhr/PJJB/zqQP/8ATgD/LX86f////wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////ATx/T0EtdzZrHmwmcTF8P2FB
g1gz////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BI3Qw
tQBMAP8SdBP/MY02/wdqB/8AUQD/NoZEkRZuHcMDXAL/VaVb/xt1Hf8AVAD/AGAA/wBWAP9ClUn/
FXcV/wJjBef///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8BLHU2cw1nEeEAXQD/AFYA/wBXAP8AVAD/AFgA/xJrGM82fkZb////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8BOIZHgwBJAP8uhDD/SpxR/0KNR/9Km0//DGsN/wBZAP8AVQD/
QJdG/yiDLP8AVgD/AGcA/wBmAP8AWwD/I38m/zeQO/8AVgD/So5cK////wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wE/f1YRGG8hwwBXAP8AVwD/EHIQ/yyHMP81jDr/NIw4/yWD
Jv8AYgD/AE4A/yBxK6n///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BYZ99HwBTAP8deR7/
T6FW/wJhA/8ATAD/KIQr/z+VRf8ATwD/IX4k/0SYTP8AWgD/AGUA/wBmAP8AZgD/AGMA/whsCP86
kD//AF4A/zaBR1////8B////Af///wH///8B////Af///wH///8B////Af///wFVlW4NBlwL3wBT
AP8RbxP/QJNG/0eVTf85jT//LoQy/zCFNP8+kEP/SZtP/ymBLP8AUQD/F2ohuf///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////ARtyJ6sAWQD/RZhK/wprC/8AXQD/AGYA/wBgAP89kUP/C2sN/0CURv8Q
cBL/AF0A/wBmAP8AZQD/AGUA/wBlAP8AXwD/Now6/wZtBv8fciyJ////Af///wH///8B////Af//
/wH///8B////Af///wH///8BF3Af1wBMAP8lfif/UaJa/yh/Lf8AYQD/AFkA/wBbAP8AWwD/AFkA
/wxoDf9LnlL/LoYy/wBPAP89iE15////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////AViVbAkAXgD/GHsX/ziNPP8A
XAD/A2oF/wNpBf8AXQD/KYMu/1GgWP8vhzP/AFsA/wNqBf8DaQX/A2kF/wNpBf8DaQX/AGEA/zOJ
OP8McQv/GG0hpf///wH///8B////Af///wH///8B////Af///wH///8BMn9CiwBIAP8kfib/VKRb
/wpnC/8AWAD/AGUA/wBmAP8AZgD/AGYA/wBnAP8AXgD/AGIA/0KVSP8GaAX/AGAC8UyJZAX///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wE3fkhJAFcA/zGKNP8wiTb/A2kG/w5yE/8OchP/AmkG/yiDLv9nr27/FXUa/wZs
C/8OchP/DnIT/w5yE/8OchP/DnIT/wRsCP83jj//DG8M/xZuHa////8B////Af///wH///8B////
Af///wH///8BWpZxGwBWAP8ObA7/U6Ja/wpnCv8AWgD/AGYA/wBlAP8AZQD/AGUA/wBlAP8AZQD/
AGYA/wBWAP82izz/D3cP/wBeAP9EiFoj////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8BLXk9dQBXAP83jzz/L4o4/xN4
Gv8ZfCD/GXwg/xd7IP8dfSP/IoEo/xR4G/8afSH/GXwg/xl8IP8ZfCD/GXwg/xl8IP8ReBn/PZNF
/wtvCv8UbRqx////Af///wH///8B////Af///wH///8B////ASN7L6sAUQD/RppM/x17IP8AWwD/
AmkD/wJoA/8CaAP/AmgD/wJoA/8DaAT/AGUA/wBZAP8ohC7/Q5ZI/wBbAP8FZwn/WZh1C////wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////ATGEPocAVQD/OJA//zeRQv8egSj/I4Qt/yOELf8khS7/IIIq/xt/Jf8jhC3/I4Qt
/yOELf8jhC3/I4Qt/yOELf8jhC3/HoEp/0GXS/8EagP/G3Ikq////wH///8B////Af///wH///8B
////AWKffRcAWQD/HHwc/0KWSv8AZgD/DXMS/w5yE/8OchP/DnIT/w5yE/8PcxT/CG0M/w5xE/8/
lEj/UJ9Y/w1qDv8BVAH5QohUX////wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wEqejd/AFUA/zeOPP9Dm1L/J4k2
/y2MO/8tjDv/LYw7/y2MO/8tjDv/LYw7/y2MO/8tjDv/LYw7/y2MO/8tjDv/LYw6/yyMO/9FmlD/
A2kC/xlsJpn///8B////Af///wH///8B////Af///wEue0F7AFMA/0SXSf8phzP/E3gc/xt9I/8a
fCP/Gnwj/xp8I/8afCP/E3gc/ymGMf9apWL/NIc4/wBVAP8AVQD/FW8dx////wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8BLXdAYwBUAP8qhCv/UaZi/zCQRP83lEj/NpRI/zaUSP82lEj/NpRI/zaUSP82lEj/
NpRI/zaUSP82lEj/NpRI/zaTR/89mVD/R5pQ/wBgAP8kdjR7////Af///wH///8B////Af///wH/
//8BCmgP1wtuCf9LnVb/HoEr/yeHNP8nhzP/J4cz/yeHM/8nhzP/J4cz/yGDLv8zkED/T6BZ/zGG
NP8mfSj/CmkJ/wBZAPsCXQjbL3xCY////wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////AVCRaCcAXAD/Cm4I/1anZf9Anlf/
QZxV/0GcVP9BnFT/QZxU/0GcVP9BnFT/QZxU/0GcVP9BnFT/QZxU/0GcVP8/m1P/T6hm/z6TRf8A
VwD/MnxCVf///wH///8B////Af///wH///8BU5hsIQBWAP8uhy//TKFb/yyOPv80kkT/NJFE/zSR
RP80kUT/NJFE/zSRRP81kkX/Lo4//yyMPf9BnFL/UqZh/1OiXv8ziDX/AF0A/wBVAP8RZBy5aaWG
A////wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8BDGsV3wBUAP9GmE7/XbN2/0ikYP9KpWH/SqVh/0qlYf9KpWH/SqVh/0qlYf9K
pWH/SqVh/0qlYf9KpWH/SKRg/16zdv8viTL/AFQA/02NYzP///8B////Af///wH///8B////ATaB
SmUAWAD/RJhL/0iiXP89mlL/PppS/z6aUv8+mlL/PppS/z6aUv8+mlL/PppS/z+bUv8+mlL/OplO
/zSVSf9BnVX/Xa9v/1KgW/8LaAn/AE4A/yF3LMX///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////AUGJV2UATQD/F3YW/2u4fv9X
snT/VK5s/1Wubv9Vr23/Va9t/1Wvbf9Vr23/Va9t/1Wvbf9Vr23/Va5t/1OvcP9mt3v/FHYS/wBf
AfFinn0H////Af///wH///8B////Af///wEacSWrAWMA/1WmY/9MqGT/S6Zh/0qmYf9KpmH/SqZh
/0qmYf9KpmH/SqZh/0qmYf9KpmH/SqZh/0qlYf9LpmH/SaVf/0OiWv9csnT/Wall/wtoCf8ATgD/
O4NNa////wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8BDWkV4QBOAP85jzv/dMWS/1+6gf9ftnr/X7d8/1+3fP9ft3z/X7d8/1+3
fP9ft3z/X7d8/1+3e/9mvof/XK1u/wBdAP8YciO/////Af///wH///8B////Af///wH///8BAWAF
2RV3Ef9mt3z/VrF1/1ewcv9XsHL/V7By/1ewcv9XsHL/V7By/1ewcv9XsHL/V7By/1ewcv9XsHL/
V7By/1ewcv9XsHL/U69w/2q+hv9FmEv/AFYA/w9sFdv///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////AV6hfTEBWgP/AFoA/1Gh
Wf96zZ7/asOQ/2e+iP9nv4n/Z7+J/2e/if9nv4n/Z7+J/2i/if9nwIv/eMyb/0eaT/8AUgD/K3o7
d////wH///8B////Af///wH///8BS4xkEQBaAPsshiz/csSQ/2K8hf9iuoL/YrqC/2K6gv9iuoL/
YrqC/2K6gv9iuoL/YrqC/2K6gv9iuoL/YrqC/2K6gv9iuoL/YrqC/2G6gv9pwo7/YrFz/wBoAP8A
XwDx////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8BMX5GaQBMAP8AXgD/Wqhi/4LVpv9yzpz/bseS/27Gkf9uxpL/bsaS
/27Gkv9uxpL/ccuZ/33NnP8hfR7/AFYA/0mLXh////8B////Af///wH///8B////AUGIWD0AVgD/
PZJD/3zOn/9ux5P/bcWQ/23FkP9txZD/bcWQ/23FkP9txZD/bcWQ/23FkP9txZD/bcWQ/23FkP9t
xZD/bcWQ/23FkP9sxZH/fdOm/1yta/8AWwD/B2UN2f///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wEicDV3AFkA
/wBaAP9Imk//fs2b/3jRof9vyZb/bsaR/2/Gkf9vx5L/bsaR/3fQn/9mtXr/AF8A/wppD9P///8B
////Af///wH///8B////Af///wExf0NbAFYA/1CiXv991Kb/b8iU/2/Hkv9vx5L/b8eT/2/Hkv9v
x5L/b8eS/2/Hkv9vx5L/b8eS/2/Hkv9vx5L/b8eS/2/Hkv9wyZX/etOk/37Klv8hfSH/AEwA/z2I
UW////8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////AUWKW2EAVwD/AFEA/y+CLv9vu4D/gNGj/3POm/9uyJT/
bsaR/27Ik/9/0qP/PJFC/wBMAP88iU5x////Af///wH///8B////Af///wH///8BI3Q1dQBeAP9o
tnj/hNaq/3TNnf9xy5n/b8mW/2/Ik/9ux5L/bsaR/27Gkf9uxpH/bsaR/23Gkv9uxpL/b8iT/3DK
l/9zzpz/f9Kj/3bCiv8rgSv/AE0A/xlwItH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
RIdeNQ9nGNcATQD/CmYD/0qZUP91xI3/fdKh/3XOnf910KD/c8KN/wtuB/8AWAD/UJJxEf///wH/
//8B////Af///wH///8B////ARdtI6sAXAD/JoAn/02bVf9otXr/eceT/33Nnf97zqD/eM+g/3fP
n/92z57/ds+d/3bPnv93z57/edCf/3zQoP99zZv/cb6G/0+dVv8Tbg3/AFAA/xBkG9FinYIN////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8BKHc4iQBbAPkAUgD/FXEQ/0mZUP9t
vIP/jNmu/1CgWv8AUQD/GG4on////wH///8B////Af///wH///8B////Af///wE8g1FxCmIP5wBT
AP8AVgD/BGcA/x55HP85jTz/SpxT/1WmY/9drm//YrN2/2O2ef9js3j/Xq9w/1WmY/9JmlL/MYcx
/wtqBf8AUgD/AFcA/yFzM5P///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wFEhmAbI3MzkQBZAPsAUgD/BWYA/zuQPf8WdRb/AFgA/1GSbB////8B////Af//
/wH///8B////Af///wH///8B////AUOFXgU6gE9PHG8qnQNhCd8AVwD/AFYA/wBZAP8AWwD/AF0A
/wBjAP8EaQD/AGIA/wBdAP8AWwD/AFYA/wBUAP8CYQfjJnU4jzd/VCP///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wFBg14bI3I5hQRh
C+UAUwD/AFIA/yd9Nqn///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8BOHpLLyt1PGEgcTCNFGwfrw9qGMcKZRDTAl8H0wpnEdMQaxm/GW8koyd2N3crc0M9
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wFQi24DLHZAUxhmJKdam3Yn////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wFRlG8jLXNFO02NbAX///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////AT+CWA06glUzOYRSTRVmJVUAUw5VJXE8VTB7TUE3flQnP4BWBf///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
GXUl0QBTAP8AXwPpFGogryh1O2s2f1Mh////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wFGiWMbL3xHdRFqHb8AXQDxAFkA/wBVAP8AWwD/AF8A
/wBZAP8AVwD/AFoA/wBfAusTbBy/KXk8hTN7TkH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8BVpd3HQBbAP8PcQ7/J4Uo/wZrAv8AWgD/AFcA/w9oG7sp
c0Ff////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////AUGCZA0bbCuVAFwA
+wBRAP8CaAD/IH8h/y+JM/83jjr/N488/zePPf84jzz/NYw3/yyHLf8cexv/A2kA/wBXAP8AVAD/
AmAJ3yR2M5k/hlpD////Af///wH///8B////Af///wH///8B////Af///wH///8B////AS59RIEA
VAD/QpZG/0KWSP86jUD/QJNF/zSNNv8Mbgn/AFQA/wNgC+MldTd/P4FeDf///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////AUGGYykHXw/nAFMA/xh3GP9DlUf/RpVM/z6OQv8xhzb/KIEq/yJ+JP8gfST/
JIAo/yyEMP81ijr/PpBD/0OUSv9ElEn/NIw3/xN0Ef8AVAD/AFUA/xJpHMlChWJR////Af///wH/
//8B////Af///wH///8B////Af///wEKaRLVDXMM/zqPQP8AUgD/AGIA/xh0Gv82iTv/SJhP/0OX
Sf8VdBP/AFIA/wNeCesuekVd////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////AV6fhBUHYAz3AFYA/zuPQP9MnlT/
KX8s/wNkBP8AWgD/AFoA/wBdAP8AXgD/AF4A/wBdAP8AXAD/AFoA/wBcAP8CZQL/G3cd/zaKO/9G
lk3/R5dO/x55H/8AVwD/GG8lw////wH///8B////Af///wH///8B////Af///wFHimYZAFcA/y2I
Lv8rhC//AFsA/wBmAP8AYQD/AFkA/wBgAP8ogCv/TJtS/0OVSf8EYwH/AFIA/yV1N5////8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////AWWkkBckeDixAE4A/zaNO/9Cl0n/AFwA/wBaAP8AZQD/AGYA/wBmAP8AZgD/AGYA/wBmAP8A
ZgD/AGYA/wBmAP8AZgD/AGUA/wBfAP8AWQD/AF4A/yF+Jf9OnlT/AmQA/yZ3PXv///8B////Af//
/wH///8B////Af///wH///8BN4NTawBYAP89kkH/EXMT/wBhAP8AZgD/AGYA/wBnAP8AZQD/AFoA
/wBdAP80iTn/T6BW/x93IP8AUQD/Fmwjwzx8XAX///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wEufj99AGAA/xFzEf9DlEn/AFoA/wBhAP8A
ZgD/AGUA/wBlAP8AZQD/AGUA/wBlAP8AZQD/AGUA/wBlAP8AZQD/AGUA/wBlAP8AZQD/AGUA/wBi
AP8AZAD/MYk1/wFkAP8xfk1F////Af///wH///8B////Af///wH///8B////ARt0KacCZwH/O5BB
/wBiAP8AZAD/AGUA/wBlAP8AZQD/AGUA/wBmAP8AZAD/AFYA/xBsEf9So1j/J38q/wBPAP8MZRbL
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8BDWQVpwBbAP8kgyX/NIo5/wBaAP8EagT/A2kF/wNpBf8DaQX/A2kF/wNpBf8DaQX/A2kF/wNp
Bf8DaQX/A2kF/wNpBf8DaQX/A2kF/wNpBf8AYgD/H30j/zSMNv8AWwD/PoRcF////wH///8B////
Af///wH///8B////Af///wEEZQvZGXoW/zSLOP8AWwD/AWcB/wFnAf8BZwH/AWcB/wFnAf8BZwH/
AWcB/wBoAf8AXQD/AmQC/1OiW/8feSL/AE0A/zCEQ53///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////ASp5QYEAYAD/CGoI/0qbUf8PdRX/CW8O/xBz
Ff8PcxT/D3MU/w9zFP8PcxT/D3MU/w9zFP8PcxT/D3MU/w9zFP8PcxT/D3MU/w9zFP8PcxT/AWkF
/zmRQv8lgSP/AF8F4////wH///8B////Af///wH///8B////Af///wFLj3ATAFsA/yiDJ/8viDb/
AGYC/wtvD/8Lbw//C28P/wtvD/8Lbw//C28P/wtvD/8Lbw//C3AP/wBmA/8TdRf/UaBX/wllCP8A
VAD/WJl2Mf///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wFSknUXHXIrswBQAP8rhC3/VaRf/xd7If8Weh//HX4m/xx+Jf8cfiX/HH4l/xx+Jf8cfiX/HH4l
/xx+Jf8cfiX/HH4l/xx+Jf8cfiX/HH4l/xR5Hv9HmlH/CW4H/xZwI6f///8B////Af///wH///8B
////Af///wH///8BO4NWNQBZAP8xiDP/L4s4/w51Ff8XeR3/F3kd/xd5Hf8XeR3/F3kd/xd5Hf8X
eR3/F3kd/xd5Hf8Yex7/BW4M/ziQQP88kkD/AE4A/xx2KMH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////AWSiiBkCXQb/AFMA/zSJN/9bqmf/NJJD
/yCELv8niDP/KYk1/ymJNf8piTX/KYk1/ymJNf8piTX/KYk1/ymJNf8piTX/KYk1/yeIM/8zkUH/
Q5ZK/wBXAP85h1Jt////Af///wH///8B////Af///wH///8B////ATV+T1UAWwD/OpA+/zGNO/8d
gCb/IIIq/yCCKv8ggir/IIIq/yCCKv8ggir/IIIq/yCCKv8ggir/IIIq/x+BKf8bfib/SJtS/wlu
B/8AXQD/QoNmF////wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8BQIheNwhjDPkAUgD/IXoi/1WjXf9VqGX/P5tS/y+RQv8xkUL/NZJE/zSSRP80kkT/
NJJE/zSSRP80kkT/NJJE/zSSRP8tjz7/T6Vh/y2HLP8AVgD/WJt9If///wH///8B////Af///wH/
//8B////Af///wEse0RvAF0A/z6TRf8zkEL/KIk1/yqKNf8qijX/Koo1/yqKNf8qijX/Koo1/yqK
Nf8qijX/Koo1/yqKNf8qijb/H4Qr/0adVP8ogyr/AFMA/zB7TWX///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wFEiGUjDWIctQBWAP8DZAL/
Moc2/0ibUv9OoVv/RZ5Y/z+cVP9BnVX/QZ1V/0GdVf9BnVX/QZ1V/0GdVf9BnVX/P51W/1mqaP8H
aQT/DGsVzf///wH///8B////Af///wH///8B////Af///wH///8BKHw8hQBcAP9Clkv/OphM/zOS
Q/80kkT/NJJE/zSSRP80kkT/NJJE/zSSRP80kkT/NJJE/zSSRP80kkT/NJJE/zCQQf9Hn1j/OpBA
/wBSAP8qfD6V////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wE5glhRAGIA+wBOAP8AVwD/Qow+/2Csbf9MqGb/Tadk/02nZP9N
p2T/Tadk/02nZP9Np2T/SqZj/2C1ev9FmEv/AFAA/zWDTW////8B////Af///wH///8B////Af//
/wH///8B////ASh5PI8AXQD/RppR/0OgWf8+mlH/PplR/z6ZUf8+mVH/PplR/z6ZUf8+mVH/PppR
/z6aUf8+mVH/PplR/z6ZUf8+mVD/SaJe/0OXS/8AXQD/Fmskn////wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BG3IsrQBZAP0M
aAn/SZlP/1uub/9YsXT/VrJ0/1axc/9WsXP/VrFz/1axc/9WsXP/VbBy/1m2ev9suoL/EXEO/wBY
AP9RknQR////Af///wH///8B////Af///wH///8B////Af///wEqfD2PAFoA/0qdVf9PqGf/SKJe
/0iiXv9Iol7/SKJe/0iiXv9Iol7/SKJd/0ijYP9Io2D/SKJd/0iiXv9Iol7/SKJd/1Ora/9Im1D/
AFsA/xtwLpv///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8BKnpAgQBVAP8MaQr/YrBx/3fKmv9jv4n/Y7yF/2S8hv9jvYb/ZL2G/2S9
hv9kvYb/Y7yF/2O/if95y5v/Q5dH/wBLAP8ofj6d////Af///wH///8B////Af///wH///8B////
Af///wH///8BKX4+gQBYAP9LnVb/W7R3/1Gsav9QrGr/Uaxq/1Gsav9RrGr/Uaxq/06sav9arm//
Wq1v/0+sav9RrGr/Uaxq/1Csav9gt3v/RJhM/wBTAP8rfUSF////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////ARBsHMMAUwD/QJRE/4PV
qf9vyZf/b8aS/2/Gkv9vxpL/b8aS/2/Gkv9vxpL/b8aS/2/IlP9+06f/Z7R2/wNgAP8AVwD/Xp6D
F////wH///8B////Af///wH///8B////Af///wH///8B////AS54RWkAWQD/SJxT/2i/h/9atXj/
WrV4/1q1eP9atXj/WrV4/1q1d/9kvIT/TZ1V/06eVv9jvIP/WrV4/1q1d/9Ztnv/cMGL/y2GLf8A
VAD/RI5jQ////wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wEfdzSpAE4A/0SXSv+E1ar/b8mV/2/Gkf9vx5L/b8eS/2/Hkv9vx5L/b8aR
/27IlP9706X/d8GL/xVxE/8ASAD/L4JGif///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wE9hF1JAFYA/z2URP9zx5b/Zb6I/2S8hv9kvIb/ZLyG/2S8hv9lv4r/d8iW/x54Hf8k
fSP/ecqb/2S/i/9kvIX/asWT/268hf8GaAL/AF4D8f///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BRY9rRQBPAP8ScBD/dsOM
/3zUp/9vypf/bseT/27Gkf9ux5L/b8iU/3HMmv9+1Kf/dL+I/yF2H/8ATgD/Em0d4f///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8BSY9uIwBWAP8qhCr/fs6f/2/Jlf9u
xpH/bsaR/27Gkf9txZD/ds+e/268g/8AYQD/AmEA/3G9hf981Kf/c86e/4XVqf9Bl0b/AE0A/yd6
PIv///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wEpfzqpAE4A/yF4H/9suH7/gNCh/3rPof91zp//d8+f/37QoP96yZb/
V6Vh/xVuEv8AVAD/AFoC81iYgh////8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wEAXgPlDXEI/3bGkP9yzZv/b8eS/2/Hkv9vx5L/b8mV/4HTpP9El0j/AFYA/wBX
AP8mfyf/eMSO/4HOnv9Rolr/AFkA/wFcBflgoIcL////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////ARVqJr0ATgD/
BmUA/ziMO/9To13/XK1s/1ipZv9Gl0z/I3oi/wBdAP8AVAD/CWYR8S12Tiv///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8BGXErowBYAP9erm3/etCi/27G
kf9uxpH/bcaQ/3fPn/9yv4j/C2kI/wNfCO8HaQ73AFkA/xRxEv8ieyD/AFoA/wBTAP9Pl3RH////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8BJnc+jQBbAP8AUwD/AFwA/wBgAP8AXwD/AFoA/wBUAP8A
XAD/FmsmvUiIdBv///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////AUGIYkcATgD/L4ku/4LSpP9wy5n/bsaQ/3HMmv+D0qT/No03/wBKAP8zglNtT5B4
NQBcAP8AVwD/AFMA/wBcAf85hlhf////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wFB
h2YtHGwyjQxmGcUFZQ3lBWYL6whmEtMccS2nMHpQUf///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BCWcR4QBXAP9cq2j/g9ap
/3rSo/+E06X/UKFY/wBZAP8AXQP/Z6WYE////wEpdUVLGWoqnyBwN401flsl////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////AUWLbQf///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////AUuTb0UATQD/CGUE/1CgWf9mtHj/P5FD/wBdAP8AUAD/O4hZbf///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BLYFGmQBUAP8AXgD/
A2UA/wBbAP8AVQD/KH08qf///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wEWbyN1AFoA2wBgAPcAXADlFWwgf////wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8BH3cwEQBZAG8C
YwORAFkAex50LBn///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B
////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH/
//8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af//
/wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////Af///wH///8B////
Af///wEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
AAAAAA==
"""

icondata= base64.b64decode(icon)
## The temp file is icon.ico
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()

class Application(Frame):
    def get_dir(self):
        global dirname
        dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
        self.dirtext.delete('1.0',END)
        self.dirtext.insert('1.0', dirname)
        if debug:
            print dirname

    def download_func(self):
        global urllist
        
        del urllist[:]
        urllist = self.urltext.get('1.0',END)
        urllist = urllist.split("\n")
        if debug:   
            print urllist
        try:
            x = len(os.listdir(sys.argv[2]))
        except:
            x = 0
        for i in urllist:
            try:
                response = urllib2.urlopen(i)
                source = response.read()
                            
                if "4chan" in i.lower():
                    imgUrls = re.findall('a class="fileThumb" .*?href="(.*?)"', source)
                if debug:
                    print imgUrls
                        
                for imgUrl in imgUrls:
                    try:
                        if imgUrl.split('.')[-1] in ext_list:
                            if "4chan" in i.lower() or "4cdn" in i.lower():
                                if 's' in imgUrl:
                                    imgUrl = imgUrl.replace('s','')
                                imgLink = "http://" + imgUrl[2:]
                
                            if debug:
                                print imgLink
                        
                            
                            imgData = urllib2.urlopen(imgLink).read()
                            if debug:
                                print imgLink + " downloading as " + str(x)
                            if imgUrl.split('.')[-1] == 'webm':
                                filename = "VIDEO %d.%s" % (x,imgUrl.split('.')[-1])
                            else:
                                filename = "IMAGE %d.%s" % (x,imgUrl.split('.')[-1])
                            if debug:
                                print dirname
                            output = open(dirname + "\ "+ filename,'wb+')
                            x+=1
                            output.write(imgData)
                            output.close()
                            
                    except Exception as e:
                        if debug:
                            print "skipping %s" % (imgUrl)
                            print str(e)
                        continue
            except:
                if debug:
                    print "Failed: Thread probably closed going to next one"
                
        if debug:
            print "\n\n DOWNLOADING DONE..."
        
    def createWidgets(self):        
        
        self.labelDIRBOX = Label(self,text = "Directory")
        self.labelDIRBOX.grid(row=0)

        self.dirtext = Text(self,height = 2,width=23)
        self.dirtext.grid(row=1,column=0)
        self.dirtext.insert('1.0', dirname)

        self.browse = Button(self,text = "Browse..",height = 1,width=25)
        self.browse["command"] = self.get_dir
        self.browse.grid(row=2,column=0)

        self.labelURLBOX = Label(self, text= "Url(s)")
        self.labelURLBOX.grid(row=3)

        self.urltext = Text(self, height = 2, width = 23)
        self.urltext.grid(row=4,column=0,sticky=W)

        self.download = Button(self,text = "Download",height = 1,width=25)
        self.download["command"] = self.download_func
        self.download.grid(row=7,column=0)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

root = Tkinter.Tk()
root.resizable(width=FALSE, height=FALSE)
root.geometry("190x175")
root.title("4Down!")
root.wm_iconbitmap(tempFile)
os.remove(tempFile)
app = Application(master=root)
app.mainloop()
root.destroy()
