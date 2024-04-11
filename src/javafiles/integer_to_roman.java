class Solution {
    public String intToRoman(int num) {
        String[] one = {"" ,"I", "II" , "III" , "IV", "V" , "VI" , "VII" , "VIII", "IX" };
        String[] ten = {"","X", "XX" ,"XXX" , "XL" , "L" , "LX" , "LXX" , "LXXX" , "XC"};
        String[] hundread = {"","C" , "CC", "CCC", "CD" , "D" , "DC" , "DCC" , "DCCC" , "CM"};
        String[] thousand = {"","M","MM","MMM"};
        int remainder , length;
        int index = 0;
        String[][] r = {one,ten,hundread,thousand};
        String output = "";
        remainder = num%10;
        length = r.length;
        while (index < length){
            output = r[index][remainder] + output;
            num = num/10;
            remainder = num%10;
            index++;
        }
        return output;

    }
}