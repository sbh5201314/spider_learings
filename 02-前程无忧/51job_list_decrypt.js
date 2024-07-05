function get_acw_sc__v2(arg1_){
    var arg1 = arg1_;
    var posList = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32, 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36];
    var mask = "3000176000856006061501533003690027800375";
    var outPutList = [];
    var arg2 = "";
    var arg3 = "";
    for (var i = 0; i < arg1["length"]; i++) {
        var this_i = arg1[i];
        for (var j = 0; j < posList["length"]; j++) {
            if (posList[j] == i + 1) {
                outPutList[j] = this_i
            }
        }
    }
    arg2 = outPutList["join"]("");
    for (var i = 0; i < arg2["length"] && i < mask["length"]; i += 2) {
        var GxjQsM = "1|4|3|0|2"["split"]("|")
          , QoWazb = 0;
        while (!![]) {
            switch (GxjQsM[QoWazb++]) {
            case "0":
                if (xorChar["length"] == 1) {
                    xorChar = "0" + xorChar
                }
                continue;
            case "1":
                var strChar = parseInt(arg2["slice"](i, i + 2), 16);
                continue;
            case "2":
                arg3 += xorChar;
                continue;
            case "3":
                var xorChar = (strChar ^ maskChar)["toString"](16);
                continue;
            case "4":
                var maskChar = parseInt(mask["slice"](i, i + 2), 16);
                continue
            }
            break
        }
    }
    return arg3
}
arg2="3BBA1B8BE90AA557036DBA5F9850EFAF185AF1CF"
console.log(get_acw_sc__v2(arg2));