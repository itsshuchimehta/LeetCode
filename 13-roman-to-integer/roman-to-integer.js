/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let romanToDigit  = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    let i = 0;
    let summ = 0;
    while(i < s.length){
        if(romanToDigit[s[i]] < romanToDigit[s[i+1]]){
            summ = summ + (romanToDigit[s[i+1]] - romanToDigit[s[i]]);
            i+=2;
        }else{
            summ += romanToDigit[s[i]];
            i++;
        }
    }

    return summ;
};
//TC: O(N)
//SC: O(1)