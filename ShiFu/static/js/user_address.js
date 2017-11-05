/**
 * Created by jiaju_cao on 2017/6/7.
 */
var isFinishLoad = false;
var currentPageIndex = 0;
var currentPageSize = 12;

var OpenId = null;
var divTemplate ="<div class=\"item_function\">\n" +
    "            <div style=\"width: 100%;background-color: #e0e0e0;text-align: left\">\n" +
    "                <div style=\"margin-left: 5%;padding-top: 20px;font-size: 2.0em;height: 4pc;\">{User_Address}</div>\n" +
    "            </div>\n" +
    "\n" +
    "            <div class=\"seperatoLine\"></div>\n" +
    "\n" +
    "            <div style=\"width: 68%;float: left\">\n" +
    "                <img class=\"itemLogo\" src=\"/static/Images/address.png\">\n" +
    "                <div class=\"itemTitle\">{User_Name}-{User_Phone}</div>\n" +
    "\n" +
    "            </div>\n" +
    "\n" +
    "            <div style=\"width: 30%;float: right\">\n" +
    // "                <div class=\"order_oper\"  onclick=\"$.editAddress('{Address_Code}')\">  编辑</div>\n" +
    "                <img src='/static/Images/delete.png' class=\"order_oper\"  onclick=\"$.deleAddress('{Address_Code}')\"> </img>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "        <div class=\"seperatoLine\"></div>";

$(document).ready(function()
{
    OpenId = $.cookie('WX_OpenId');
    // 查询参与投票的品牌
    $.get_current_query();
});
// 自定义函数
$.extend({
get_current_query:function () {
    $("#address_list").html("");
        $.get("/api/user/?Command=Get_Addresses&code=" + OpenId,
            function (data)
            {
                // 检查查询状态
                var  ErrorId = data.ErrorId;
                var  Datas = data.Result;

                if (Datas == null || Datas.length < currentPageSize)
                {
                    isFinishLoad = true;
                }

                if (Datas == null)
                {
                    var oneT = $("#address_list").html();

                        if (oneT.length <= 0)
                        {
                            $("#address_list").html("<div style='font-size: 2.7em;text-align: center'>没有订单数据 </div>" );
                        }

                        return;
                }

                // var Datas = Result.Datas
                if (ErrorId == 200)
                {
                    if (Datas.length <= 0)
                    {
                        var oneT = $("#address_list").html();

                        if (oneT.length <= 0)
                        {
                            $("#address_list").html("<div style='font-size: 2.7em;text-align: center'>没有记录</div>" );
                        }

                        return;
                    }
                    for (i=0;i<Datas.length ;i=i+1 )
                    {
                        var oneCode1 = Datas[i];
                        var abcTemp = {};

                        abcTemp["User_Address"] = oneCode1.address;
                        abcTemp["User_Name"] = oneCode1.name;
                        abcTemp["User_Phone"] = oneCode1.phone;
                        abcTemp["Address_Code"] = oneCode1.code;


                        var oneT = $("#address_list").html();


                        $("#address_list").html(oneT + $.format(divTemplate,abcTemp) );

                    }
                }

            },
            "json");//这里返回的类型有：json,html,xml,text
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

    editAddress:function (cancelOrder) {
        alert(cancelOrder);
        // alert(cancelOrder);
    },
    deleAddress:function (cancelOrder) {
                var rtnCmd = "/api/user/?Command=Dele_Address";

        $.post(rtnCmd, {code: cancelOrder},
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    $.get_current_query();
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