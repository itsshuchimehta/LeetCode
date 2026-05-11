/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    if(s.length === 0 && t.length === 0){
        return true;
    }

    if(s.length === 0 && t.length !== 0){
        return true;
    }
    
    let p = 0;
    

    for(let i = 0; i < t.length; i++){
        if(s[p] === t[i] && p === s.length - 1){
            return true;
        }
        if(s[p] === t[i]){
            p++;
        }
    }

    return false;


};