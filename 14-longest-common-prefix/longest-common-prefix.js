/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    if(strs.length === 0) return "";
    
    let i = 0;
    let prefix = "";
    let minLength = Infinity;


    for(const s of strs){
        if(s.length < minLength){
            minLength = s.length;
        }
    }

    while(i < minLength){
        for(const s of strs){
            if(s[i] !== strs[0][i]){
                return s.slice(0,i)
            }
        }
        i+=1;
    }

    return strs[0].slice(0,i);

};