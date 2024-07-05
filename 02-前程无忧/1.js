
var posList = [15, 35, 29, 24, 33, 16, 1, 38, 10, 9, 19, 31, 40, 27, 22, 23, 25, 13, 6, 11, 39, 18, 20, 8, 14, 21, 32, 26, 2, 30, 7, 4, 17, 5, 3, 28, 34, 37, 12, 36];
                var mask = _0x1e8e("0x0");
                var outPutList = [];
                var arg2 = "";
                var arg3 = "";
                for (var i = 0; i < arg1[_0x1e8e("0x1")]; i++) {
                    var this_i = arg1[i];
                    for (var j = 0; j < posList[_0x1e8e("0x1")]; j++) {
                        if (posList[j] == i + 1) {
                            outPutList[j] = this_i
                        }
                    }
                }
                arg2 = outPutList[_0x1e8e("0x2")]("");
                for (var i = 0; i < arg2[_0x1e8e("0x1")] && i < mask[_0x1e8e("0x1")]; i += 2) {
                    var GxjQsM = _0x1e8e("0x3")[_0x1e8e("0x4")]("|")
                      , QoWazb = 0;
                    while (!![]) {
                        switch (GxjQsM[QoWazb++]) {
                        case "0":
                            if (xorChar[_0x1e8e("0x1")] == 1) {
                                xorChar = "0" + xorChar
                            }
                            continue;
                        case "1":
                            var strChar = parseInt(arg2[_0x1e8e("0x5")](i, i + 2), 16);
                            continue;
                        case "2":
                            arg3 += xorChar;
                            continue;
                        case "3":
                            var xorChar = (strChar ^ maskChar)[_0x1e8e("0x6")](16);
                            continue;
                        case "4":
                            var maskChar = parseInt(mask[_0x1e8e("0x5")](i, i + 2), 16);
                            continue
                        }
                        break
                    }
                }
