/**
 * Created by jiaju_cao on 2017/6/7.
 */

window.onload=function()
{
    var screenHeight = document.documentElement.clientHeight;
    // alert(screenHeight);
    //

    var topDivHeight = screenHeight / 4;

    var marg_topValue = topDivHeight - 260;
    $("#top_div").height(topDivHeight);

    $('#top_image').css("margin-top", marg_topValue);

    $.checkCookie();

};

$(document).ready(function()
{

});

$(window).resize(function(){
});

// 自定义函数
$.extend({
      checkCookie:function ()
        {
            Org_Login_Phone = $.cookie('Org_Login_Phone');
            Org_Login_Date = $.cookie('Org_Login_Date');

            // alert(ckValue);
            if (Org_Login_Phone == "undefined" || Org_Login_Phone == "" || Org_Login_Phone == null)
            {
                return;
            }

            if (Org_Login_Date == "undefined" || Org_Login_Date == "" || Org_Login_Date == null)
            {
                return;
            }

            if (Org_Login_Date == $.getNowFormatDate())
            {
                // location.href="/org_main.html";
                location.replace("/org_main.html?code=" +  Org_Login_Phone);
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

    loginOrg:function () {
        var org_phone = $("#org_phone").val();
        var org_passwd = $("#org_passwd").val();
        var rtnCmd = "/api/manage/?Command=Org_Login";
        $.post(rtnCmd, {phone: org_phone, password: org_passwd,type:1},
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  accountCode = data.Result;

                if (ErrorId == 200)
                {
                    $.cookie("Org_Login_Phone",accountCode);
                    $.cookie("Org_Login_Date",$.getNowFormatDate());
                    location.replace("/org_main.html?code=" +  accountCode);
                }
                else
                {
                    alert(data.ErrorInfo);
                }
            },
            "json");//这里返回的类型有：json,html,xml,text
    },


});