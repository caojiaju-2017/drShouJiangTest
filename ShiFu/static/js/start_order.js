/**
 * Created by jiaju_cao on 2017/6/7.
 */

window.onload=function()
{
    var openid = $.weixin_login();
    $.cookie("WX_OpenId",openid);
    $.loadUserInfo();
};

$(document).ready(function()
{

});

$(window).resize(function(){
});

// 自定义函数
$.extend({
    validCookie:function ()
        {
            userCookie = $.cookie('UserKey');
            lastDate = $.cookie('LastDate');

            // alert(ckValue);
            if (userCookie == "undefined" || userCookie == "" || userCookie == null)
            {
                userCookie = $.randomString(8);
                $.cookie("UserKey",userCookie);
            }

            if (lastDate == "undefined" || lastDate == "" || lastDate == null)
            {
                lastDate = $.getNowFormatDate();
                $.cookie("LastDate",lastDate);
            }
        },

    getNowFormatDate:function () {
        var date = new Date();
        var seperator1 = "-";
        var seperator2 = ":";
        var month = date.getMonth() + 1;
        var strDate = date.getDate();
        if (month >= 1 && month <= 9) {
            month = "0" + month;
        }
        if (strDate >= 0 && strDate <= 9) {
            strDate = "0" + strDate;
        }
        var currentdate = date.getFullYear() + seperator1 + month + seperator1 + strDate;
        return currentdate;
    },

    randomString:function(len) {
        len = len || 32;
        var $chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';    /****默认去掉了容易混淆的字符oOLl,9gq,Vv,Uu,I1****/
        var maxPos = $chars.length;
        var pwd = '';
        for (i = 0; i < len; i++) {
            pwd += $chars.charAt(Math.floor(Math.random() * maxPos));
        }
        return pwd;
    },
    isNull:function (datas) {
            return (data == "" || data == undefined || data == null) ? 0 : 1;
    },
    StringFormat:function() {
         if (arguments.length == 0)
             return null;
         var str = arguments[0];
         for (var i = 1; i < arguments.length; i++) {
             var re = new RegExp('\\{' + (i - 1) + '\\}', 'gm');
             str = str.replace(re, arguments[i]);
         }
         return str;
    } ,

    format : function(source,args){
					var result = source;
					if(typeof(args) == "object"){
						if(args.length==undefined){
							for (var key in args) {
								if(args[key]!=undefined){
									var reg = new RegExp("({" + key + "})", "g");
									result = result.replace(reg, args[key]);
								}
							}
						}else{
							for (var i = 0; i < args.length; i++) {
								if (args[i] != undefined) {
									var reg = new RegExp("({[" + i + "]})", "g");
									result = result.replace(reg, args[i]);
								}
							}
						}
					}
					return result;
				},

    changeMyDefaultCity:function (parmas) {
        // alert(parmas);
        var OpenId = $.cookie('WX_OpenId');
        var rtnCmd = "/api/user/?Command=Set_City";

        $.post(rtnCmd, {code: OpenId, city: parmas},
            function (data)
            {
                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    $("#light").hide();
                    $("#fade").hide();

                    $("#city_my").text(parmas);
                }
                else
                {
                    alert(data.ErrorInfo);
                }
            },
            "json");//这里返回的类型有：json,html,xml,text
    },

    loadUserInfo:function () {
        var OpenId = $.cookie('WX_OpenId');

        $.get("/api/pub/?Command=Fetch_UserInfo&code=" + OpenId,
            function (data)
            {
                // 检查查询状态
                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    $("#city_my").text(Result.City);
                }
                else
                {
                    alert(data.ErrorInfo);
                }
            },
            "json");//这里返回的类型有：json,html,xml,text
    },
});