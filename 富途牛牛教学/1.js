aa = {
    "transitional": {
        "silentJSONParsing": true,
        "forcedJSONParsing": true,
        "clarifyTimeoutError": false
    },
    "adapter": [
        "xhr",
        "http"
    ],
    "transformRequest": [
        null
    ],
    "transformResponse": [
        null
    ],
    "timeout": 5000,
    "xsrfCookieName": "XSRF-TOKEN",
    "xsrfHeaderName": "X-XSRF-TOKEN",
    "maxContentLength": -1,
    "maxBodyLength": -1,
    "env": {},
    "headers": {
        "Accept": "application/json, text/plain, */*",
        "futu-x-csrf-token": "cd1zage106rT3rMaO8V7P4Cx"
    },
    "baseURL": "/quote-api/quote-v2",
    "params": {
        "marketType": 2,
        "plateType": 1,
        "rankType": 1,
        "page": 2,
        "pageSize": 50
    },
    "method": "get",
    "url": "/get-stock-list"
}
const CryptoJS = require("crypto-js")
function HMACEncrypt(text,key) {

    return CryptoJS.HmacSHA512(text, key).toString();
}
function s(text,key){
    return CryptoJS.SHA256(text, key).toString();
}
N = function(e) {
                var t = {};
                for (var n in e)
                    if (Object.prototype.hasOwnProperty.call(e, n) && void 0 !== e[n]) {
                        var r = e[n];
                        t[n] = String(r)
                    }
                return JSON.stringify(t)
            }
function sss(e) {
     var t = function(e) {
                    e.length <= 0 && (e = "quote");
                    var t = HMACEncrypt(e, "quote_web");
                    return s(t.toString().slice(0, 10)).toString().slice(0, 10)
                }(JSON.stringify(e.data) || (0,
                N)(e.params) || "{}");
                return t

}
function get_token(s) {
    aa.params = s

    return sss(aa)
}

console.log(get_token(aa));
