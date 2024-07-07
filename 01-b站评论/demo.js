
// 需要安装Node.js 和
// crypto-js库 npm install crypto-js --save
const CryptoJS = require('crypto-js')
i = {
    "oid": "959633549",
    "type": "1",
    "mode": "2",
    "pagination_str": "{\"offset\":\"{\\\"type\\\":3,\\\"direction\\\":1,\\\"Data\\\":{\\\"cursor\\\":232}}\"}",
    "plat": "1",
    "web_location": "1315875",

}
function get_data(data){

Z = Math.round(Date.now() / 1e3)
W = Object.assign({}, data, {
                wts: Z
            })
    //console.log(W)
//console.log(W)
R = "ea1db124af3c7062474693fa704f4ff8"
z = []
Y = /[!'()*]/g;
F = Object.keys(W).sort()
    //.console.log(F)
    // console.log(F)
    // console.log(typeof data)
    // console.log(data.length)
for (let D = 0; D < F.length; D++) {
                const X = F[D];
                let P = W[X];
                P && typeof P == "string" && (P = P.replace(Y, "")),
                P != null && z.push(`${encodeURIComponent(X)}=${encodeURIComponent(P)}`)
            }
            const Q = z.join("&");

console.log(Q)
    return {
                w_rid: CryptoJS.MD5(Q + R).toString(),
                wts: Z.toString()
            }
//return CryptoJS.MD5(Q+R).toString()
}

console.log(get_data(i));

//console.log(Q)
// function md5(text) {
// //     return CryptoJS.MD5(text).toString()
// // }
// //
// // console.log(md5(R + Q));