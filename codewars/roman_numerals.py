#https://www.codewars.com/kata/51b66044bce5799a7f000003

class RomanNumerals:

    def to_roman(val):
        d_tr = {1:'I',2:'II',3:'III',4:'IV',5:'V',9:'IX',10:'X',
                40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}

        p = len(str(val))

        if p==1:
            if val == 4 or val == 5 or val == 9:
                return d_tr[val]
            if val < 5 :
                return d_tr[1]*val
            else:
                return d_tr[5]+d_tr[val%5]

        pp = 10**(p-1)

        if val == 4*pp or val == 5*pp or val == 9*pp:
            return d_tr[val] 
        elif val < 4*pp:
            return d_tr[pp]*(val//pp) + RomanNumerals.to_roman(val%pp)
        elif val > 4*pp and val < 5*pp:
            return d_tr[4*pp] + RomanNumerals.to_roman(val%pp)
        elif val > 5*pp and val < 9*pp:
            return d_tr[5*pp] + RomanNumerals.to_roman(val%(5*pp))
        elif val > 9*pp:
            return d_tr[9*pp] + RomanNumerals.to_roman(val%(9*pp))

    def from_roman(roman_num):
        being_lazy = 0
        while being_lazy < 4000:
            if RomanNumerals.to_roman(being_lazy) == roman_num:
                return being_lazy
            else:
                being_lazy += 1


print(RomanNumerals.to_roman(1756))
