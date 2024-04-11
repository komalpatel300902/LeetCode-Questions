class Solution:
    def intToRoman(self, num: int) -> str:
        one = ["" ,"I", "II" , "III" , "IV", "V" , "VI" , "VII" , "VIII", "IX" ]
        ten = ["","X", "XX" ,"XXX" , "XL" , "L" , "LX" , "LXX" , "LXXX" , "XC"]
        hundread = ["","C" , "CC", "CCC", "CD" , "D" , "DC" , "DCC" , "DCCC" , "CM"]
        thousand = ["","M","MM","MMM"]
        output = ""
        val = num
        remainder = val%10
        index = 0
        r = [one,ten,hundread,thousand]
        while index < len(r):
            output = r[index][remainder]  + output
            val = val //10
            remainder = val%10
            index += 1
        return output


