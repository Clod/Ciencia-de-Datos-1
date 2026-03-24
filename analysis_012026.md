# Analysis of Worksheet 012026

This document extracts formulas from column B and identifies their dependencies with labels from the adjacent cells (Column C).

## Cell B30
**Formula:** `=(B27)/12`

| Dependency | Label (Content to its right) |
| --- | --- |
| B27 | =B27 |

## Cell B31
**Formula:** `=+B27+B30`

| Dependency | Label (Content to its right) |
| --- | --- |
| B27 | =B27 |
| B30 | =(C27)/12 |

## Cell B37
**Formula:** `=B33+B27`

| Dependency | Label (Content to its right) |
| --- | --- |
| B33 | Empty |
| B27 | =B27 |

## Cell B39
**Formula:** `=-B5*11%`

| Dependency | Label (Content to its right) |
| --- | --- |
| B5 | Empty |

## Cell B40
**Formula:** `=-B5*3%`

| Dependency | Label (Content to its right) |
| --- | --- |
| B5 | Empty |

## Cell B41
**Formula:** `=-B5*3%`

| Dependency | Label (Content to its right) |
| --- | --- |
| B5 | Empty |

## Cell B43
**Formula:** `=SUM(B39:B42)`

| Dependency | Label (Content to its right) |
| --- | --- |
| B39 | =-C27*11% |
| B42 | Empty |

## Cell B45
**Formula:** `=B27++B33`

| Dependency | Label (Content to its right) |
| --- | --- |
| B27 | =B27 |
| B33 | Empty |

## Cell B47
**Formula:** `=+B28/12`

| Dependency | Label (Content to its right) |
| --- | --- |
| B28 | Empty |

## Cell B49
**Formula:** `=SUM(B47:B48)`

| Dependency | Label (Content to its right) |
| --- | --- |
| B47 | =$B$47+B47 |
| B48 | Empty |

## Cell B52
**Formula:** `=B45+B47`

| Dependency | Label (Content to its right) |
| --- | --- |
| B45 | =C27+B45 |
| B47 | =$B$47+B47 |

## Cell B54
**Formula:** `=-B30+B61`

| Dependency | Label (Content to its right) |
| --- | --- |
| B30 | =(C27)/12 |
| B61 | =((C30*0.17)) |

## Cell B55
**Formula:** `=B54`

| Dependency | Label (Content to its right) |
| --- | --- |
| B54 | =-C30+C61 |

## Cell B57
**Formula:** `=B48+B43`

| Dependency | Label (Content to its right) |
| --- | --- |
| B48 | Empty |
| B43 | =SUM(C39:C42) |

## Cell B59
**Formula:** `=B43`

| Dependency | Label (Content to its right) |
| --- | --- |
| B43 | =SUM(C39:C42) |

## Cell B61
**Formula:** `=+(($B$5/12*0.17))`

| Dependency | Label (Content to its right) |
| --- | --- |
| $B$5 | Empty |

## Cell B62
**Formula:** `=B27+B47+B43+B48-B54+B33`

| Dependency | Label (Content to its right) |
| --- | --- |
| B27 | =B27 |
| B47 | =$B$47+B47 |
| B43 | =SUM(C39:C42) |
| B48 | Empty |
| B54 | =-C30+C61 |
| B33 | Empty |

## Cell B64
**Formula:** `=B62`

| Dependency | Label (Content to its right) |
| --- | --- |
| B62 | =C27+C47+C43+C48-C54+C33 |

## Cell B69
**Formula:** `=B83*5/100`

| Dependency | Label (Content to its right) |
| --- | --- |
| B83 | =C64-C77+C68 |

## Cell B71
**Formula:** `='Tablas '!B3`

| Dependency | Label (Content to its right) |
| --- | --- |
| 'Tablas '!B3 | =+$N$3/12*C2 |

## Cell B72
**Formula:** `='Tablas '!B4`

| Dependency | Label (Content to its right) |
| --- | --- |
| 'Tablas '!B4 | =+$N$4/12*C2 |

## Cell B76
**Formula:** `=SUM(B71:B75)/12`

| Dependency | Label (Content to its right) |
| --- | --- |
| B71 | ='Tablas '!C3 |
| B75 | Empty |

## Cell B77
**Formula:** `=SUM(B71:B76)`

| Dependency | Label (Content to its right) |
| --- | --- |
| B71 | ='Tablas '!C3 |
| B76 | =SUM(C71:C75)/12 |

## Cell B83
**Formula:** `=B64-B77+B68`

| Dependency | Label (Content to its right) |
| --- | --- |
| B64 | =C45+C47-C55+C57+B59 |
| B77 | =SUM(C71:C76) |
| B68 | Empty |

## Cell B84
**Formula:** `=B64-B77`

| Dependency | Label (Content to its right) |
| --- | --- |
| B64 | =C45+C47-C55+C57+B59 |
| B77 | =SUM(C71:C76) |

## Cell B85
**Formula:** `=B84`

| Dependency | Label (Content to its right) |
| --- | --- |
| B84 | =IF((C64-C77)>=0,C64-C77,0) |

## Cell B86
**Formula:** `=B85`

| Dependency | Label (Content to its right) |
| --- | --- |
| B85 | =C62 |

## Cell B90
**Formula:** `=IF(B86>0,(VLOOKUP(B86,Escalas!$A$19:$E$27,3)),0)`

| Dependency | Label (Content to its right) |
| --- | --- |
| B86 | =C84 |
| Escalas!$A$19 | 166669.17 |
| $E$27 | =E27 |

## Cell B91
**Formula:** `=IF(B86>0,VLOOKUP(B86,Escalas!$A$19:$E$27,4),0)`

| Dependency | Label (Content to its right) |
| --- | --- |
| B86 | =C84 |
| Escalas!$A$19 | 166669.17 |
| $E$27 | =E27 |

## Cell B92
**Formula:** `=IF(B86>0,(VLOOKUP(B$86,Escalas!$A$19:$E$27,5)*B89),0)`

| Dependency | Label (Content to its right) |
| --- | --- |
| B86 | =C84 |
| B$86 | =C84 |
| Escalas!$A$19 | 166669.17 |
| $E$27 | =E27 |
| B89 | 2 |

## Cell B94
**Formula:** `=IF(B86>0,+B86-B92,0)`

| Dependency | Label (Content to its right) |
| --- | --- |
| B86 | =C84 |
| B92 | =IF(C86>0,(VLOOKUP(C$86,Escalas!A29:E37,5)),0) |

## Cell B95
**Formula:** `=+B91*B94`

| Dependency | Label (Content to its right) |
| --- | --- |
| B91 | =IF(C86>0,VLOOKUP(C86,Escalas!A29:E37,4),0) |
| B94 | =IF(C86>0,+C86-C92,0) |

## Cell B97
**Formula:** `=+B90+B95`

| Dependency | Label (Content to its right) |
| --- | --- |
| B90 | =IF(C86>0,(VLOOKUP(C86,Escalas!A29:E37,3)),0) |
| B95 | =+C91*C94 |

## Cell B99
**Formula:** `=+B103`

| Dependency | Label (Content to its right) |
| --- | --- |
| B103 | =IF(C27<>0,C97-B99,0) |

## Cell B103
**Formula:** `=+B97`

| Dependency | Label (Content to its right) |
| --- | --- |
| B97 | =+C90+C95 |

