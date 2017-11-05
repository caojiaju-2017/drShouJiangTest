/**
 * Created by jiaju_cao on 2017/6/7.
 */

var levelValue = -1;
var likeValue = -1;

window.onload=function()
{
};

$(document).ready(function()
{

});

$(window).resize(function(){
    $.validCookie();
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

    uncheckAll:function () {
        $("#level1").attr('src',"/static/Images/uncheck.png");
        $("#level1").attr('name',"0");

        $("#level2").attr('src',"/static/Images/uncheck.png");
        $("#level2").attr('name',"0");

        $("#level3").attr('src',"/static/Images/uncheck.png");
        $("#level3").attr('name',"0");

        $("#level4").attr('src',"/static/Images/uncheck.png");
        $("#level4").attr('name',"0");

        $("#level5").attr('src',"/static/Images/uncheck.png");
        $("#level5").attr('name',"0");

    },

    changeSelect:function (idName) {
        var src = $(idName)[0].name;

        if (src == 0)
        {
            $.uncheckAll();

            $(idName).attr('src',"/static/Images/check.png");
            $(idName).attr('name',"1");

            levelValue = idName.substr(idName.length-1,1);
        }
        else
        {
            $(idName).attr('src',"/static/Images/uncheck.png");
            $(idName).attr('name',"0");

            levelValue = -1;
        }
    },


    changeLikeSelect:function (idName) {
        var src = $(idName)[0].name;

        if (src == 0)
        {
                $("#like1").attr('src',"/static/Images/uncheck.png");
                $("#like1").attr('name',"0");

                $("#like2").attr('src',"/static/Images/uncheck.png");
                $("#like2").attr('name',"0");

                $("#like3").attr('src',"/static/Images/uncheck.png");
                $("#like3").attr('name',"0");

            $(idName).attr('src',"/static/Images/check.png");
            $(idName).attr('name',"1");

            likeValue = idName.substr(idName.length-1,1);
        }
        else
        {
            $(idName).attr('src',"/static/Images/uncheck.png");
            $(idName).attr('name',"0");
            likeValue = -1;
        }
    },
    
    commitQuestion:function () {
        var openid = $.weixin_login();

        if (levelValue <= 0)
        {
            alert("亲~，你还没给我们的服务打分呢！");
            return;
        }

        if (likeValue <= 0)
        {
            alert("亲~，你还没选您最喜欢的部分呢！");
            return;
        }

        var suggestInfo = $("#suggest_info").val();
        var useContact = $("#contace_input").val();

        var rtnCmd = "/api/user/?Command=Release_Suggest";

        $.post(rtnCmd, {ccode: openid, cqq: useContact, likepart: likeValue, stars: levelValue, info: suggestInfo},
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    $.uncheckAll();
                     $("#suggest_info").val("");
                     $("#contace_input").val("");
                     $("#like1").attr('src',"/static/Images/uncheck.png");
                    $("#like1").attr('name',"0");

                    $("#like2").attr('src',"/static/Images/uncheck.png");
                    $("#like2").attr('name',"0");

                    $("#like3").attr('src',"/static/Images/uncheck.png");
                    $("#like3").attr('name',"0");

                    alert("感谢您的宝贵意见！");
                }
                else
                {
                    alert(data.ErrorInfo);
                }

            },
            "json");//这里返回的类型有：json,html,xml,text
    },
});