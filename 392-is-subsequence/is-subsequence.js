/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isSubsequence = function(s, t) {
    if(s.length === 0){
        return true;
    }
    if(s.length > t.length){
        return false;
    }

    let p = 0;
    

    for(let i = 0; i < t.length; i++){
        if(s[p] === t[i]){
            if(p === s.length - 1){
                return true;
            }
            p++;
        }
    }

    return false;


};