/**
 * Created by jiaju_cao on 2017/6/7.
 */

window.onload=function()
{
};

$(document).ready(function()
{

});

$(window).resize(function(){
});

// 自定义函数
$.extend({
    apply_permition: function (uCookie)
    {

        // 提取用户名
        $.get("/api/vote/?Command=Query_UserInfo&cookie=" + uCookie,
            function (data)
            {
                // 检查查询状态
                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    isEnable = parseInt(Result);
                    //alert(isEnable);
                }

            },
            "json");//这里返回的类型有：json,html,xml,text
    },

    get_current_query:function () {
        var rtnCmd = "/api/vote/?Command=Query_Factory&pageindex={0}&pagesize={1}&fliter={2}";

        rtnCmd = $.StringFormat(rtnCmd, currentPageIndex.toString(),currentPageSize.toString(),fliterString);

        return rtnCmd;
    },
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

    saveAddress:function (parmas) {
        var emp_name = $("#emp_name").val();
        var emp_phone = $("#emp_phone").val();
        var emp_passwd = $("#emp_passwd").val();
        var Org_Login_Phone = $.cookie('Org_Login_Phone');
        var rtnCmd = "/api/manage/?Command=Add_Emplyee";
        $.post(rtnCmd, {code: Org_Login_Phone, phone: emp_phone, name: emp_name, password: emp_passwd},
            function (data)
            {
                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    //
                    location.replace("/org_main.html");
                }
                else
                {
                    alert(data.ErrorInfo);
                }

            },
            "json");//这里返回的类型有：json,html,xml,text
    },

});