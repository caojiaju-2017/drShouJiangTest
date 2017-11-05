/**
 * Created by jiaju_cao on 2017/6/7.
 */

$(document).ready(function()
{
    OpenId = $.cookie('WX_OpenId');
    // 查询参与投票的品牌
});
// 自定义函数
$.extend({
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

    paiOrder:function (cancelOrder) {
        var rtnCmd = "/api/pub/?Command=Order_Change";
        var Info = $("#extern_info").val();
        var options=$("#empy_select option:selected");
        // alert(options.val());
        // alert(options.text());
        $.post(rtnCmd, {code: cancelOrder, state: 2, info: Info,ecode:options.val()},
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                   location=document.referrer;
                }
                else
                {
                    alert(data.ErrorInfo);
                }
            },
            "json");//这里返回的类型有：json,html,xml,text
    },
    finishOrder:function (cancelOrder) {
        var rtnCmd = "/api/pub/?Command=Order_Change";
        var Info = $("#extern_info").val();
        // alert("aaa");
        $.post(rtnCmd, {code: cancelOrder, state: 3, info: Info},
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    location=document.referrer;
                }
                else
                {
                    alert(data.ErrorInfo);
                }
            },
            "json");//这里返回的类型有：json,html,xml,text
    },

    terminalOrder:function (cancelOrder) {
        var rtnCmd = "/api/pub/?Command=Order_Change";
        var Info = $("#extern_info").val();

        $.post(rtnCmd, {code: cancelOrder, state: 9, info: Info},
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    // location.replace("/org_main.html");
                    // location
                   location=document.referrer;
                }
                else
                {
                    alert(data.ErrorInfo);
                }


            },
            "json");//这里返回的类型有：json,html,xml,text
        // alert(cancelOrder);
    },
});