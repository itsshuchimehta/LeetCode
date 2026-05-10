/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let merged = "";

    let i = 0;

    while(i < word1.length && i < word2.length){
        merged += word1[i] + word2[i];
        i++;
    }

    // if(word1.length !== word2.length){

    //     if(word1.length > word2.length){
    //         merged += word1.slice(i)
    //     }else{
    //         merged += word2.slice(i)
    //     }
    // }
    merged += word1.slice(i);
    merged += word2.slice(i);


    return merged;
};