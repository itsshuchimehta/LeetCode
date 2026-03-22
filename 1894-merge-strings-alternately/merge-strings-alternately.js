/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    // const arrWord1 = word1.split("");
    // const arrWord2 = word2.split("");
    // let merged = [];
    // const minLen = Math.min(word1.length, word2.length);

    // // Loop through the overlapping part
    // for(let i = 0; i < minLen; i++) {
    //     merged.push(word1[i]);
    //     merged.push(word2[i]);
    // }

    // // Append the remainder directly from the string
    // if(arrWord1.length > minLen){
    //     merged.push(word1.slice(minLen))
    // }
    // if(arrWord2.length > minLen){
    //     merged.push(word2.slice(minLen))
    // }

    const [A, B] = [word1.length, word2.length];        // const A = word1.length, B = word2.length;
    let [a, b] = [0 , 0];                               // ->  let a = 0, b = 0;
    
    let merged = [];

    let word = 1;                                       //keep track of which word 
    while( a < A && b < B){
        if(word === 1){
            merged.push(word1[a]);
            a++;
            word = 2;
        }else{
            merged.push(word2[b]);
            b++;
            word = 1;
        }
    }

    while(a < A){
        merged.push(word1[a]);
        a++;
    }
    
    while(b < B){
        merged.push(word2[b]);
        b++;
    }
    

    return merged.join("")
};