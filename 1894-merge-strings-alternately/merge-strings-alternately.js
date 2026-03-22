/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    const arrWord1 = word1.split("");
    const arrWord2 = word2.split("");
    let merged = [];
    const minLen = Math.min(word1.length, word2.length);
    let i = 0;
    while(i < minLen){
        merged.push(arrWord1[i])
        merged.push(arrWord2[i])
        i++;
    }
    if(arrWord1.length > minLen){
        merged.push(arrWord1.slice(minLen, arrWord1.length).join(""))
    }
    if(arrWord2.length > minLen){
        merged.push(arrWord2.slice(minLen, arrWord2.length).join(""))
    }

    return merged.join("")
};