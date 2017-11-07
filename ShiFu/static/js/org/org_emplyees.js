/**
 * Created by jiaju_cao on 2017/6/7.
 */

var isFinishLoad = false;
var currentPageIndex = 0;
var currentPageSize = 10;

var currentLoadType = 0;

var emplyeeTemplate ="<div class=\"item_function_e\">\n" +
    "            <div style=\"width: 68%;float: left\">\n" +
    "                <img class=\"itemLogo2\" src=\"/static/Images/default_head.png\">\n" +
    "                <div class=\"itemTitle2\">{Empyee_Name}-{Empyee_Phone}</div>\n" +
    "\n" +
    "            </div>\n" +
    "\n" +
    "            <div style=\"width: 30%;float: right\">\n" +

    "                <img src='/static/Images/delete.png' class=\"order_oper2\"  onclick=\"$.deleEmpyee('{Empyee_Code}')\"> </img>\n" +
    "            </div>\n" +
    "        </div>\n" +
    "        <div class=\"seperatoLine\"></div>";

//"                <div class=\"order_oper\"  onclick=\"$.editEmpyee('{Empyee_Code}')\">  编辑</div>\n" +
window.onload=function()
{
    var screenWidth = document.documentElement.clientWidth;

    $('#add_button').css("margin-left", (screenWidth - 160) / 2);
};

$(document).ready(function()
{
    Org_Login_Phone = $.cookie('Org_Login_Phone');
    // 查询参与投票的品牌
    $.get_emplyee_query();


    // $(window).scroll(function(){
    //     var srollPos = $(window).scrollTop();
    //     var documentHd = $(document).height();
    //     var winHd = $(window).height() ;
    //     totalheight = parseFloat($(window).height()) + parseFloat(srollPos);
    //
    //     if (srollPos + winHd > documentHd*0.9 && !isFinishLoad)
    //     {
    //          // 加载数据
    //         currentPageIndex = currentPageIndex + 1;
    //         if (currentLoadType == 0)
    //         {
    //             $.get_current_query();
    //         }
    //         else
    //         {
    //             //$.get_emplyee_query();
    //         }
    //     }
    //
    //     });
});
// 自定义函数
$.extend({
    get_emplyee_query:function () {
        $.get("/api/manage/?Command=Get_Emplyees&code=" + Org_Login_Phone,
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
                    var oneT = $("#qx_order_list").html();

                        if (oneT.length <= 0)
                        {
                            $("#qx_order_list").html("<div style='font-size: 2.7em;text-align: center'>没有员工数据 </div>" );
                        }

                        return;
                }

                if (ErrorId == 200)
                {
                    if (Datas.length <= 0)
                    {
                        var oneT = $("#qx_order_list").html();

                        if (oneT.length <= 0)
                        {
                            $("#qx_order_list").html("<div style='font-size: 2.7em;text-align: center'>没有员工数据 </div>" );
                        }

                        return;
                    }
                    for (i=0;i<Datas.length ;i=i+1 )
                    {
                        var oneCode1 = Datas[i];
                        var abcTemp = {};


                        abcTemp["Empyee_Name"] = oneCode1.name;
                        abcTemp["Empyee_Phone"] = oneCode1.phone;
                        abcTemp["Empyee_Code"] = oneCode1.code;

                        var oneT = $("#qx_order_list").html();

                        $("#qx_order_list").html(oneT + $.format(emplyeeTemplate,abcTemp) );
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

    deleEmpyee:function (cancelOrder) {
        var rtnCmd = "/api/manage/?Command=Dele_Emplyee";

        $.post(rtnCmd, {ocode: Org_Login_Phone, ecode: cancelOrder},
            function (data)
            {

                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    $.loadDatas(currentLoadType);
                }
                else
                {
                    alert(data.ErrorInfo);
                }


            },
            "json");//这里返回的类型有：json,html,xml,text
    },

    loadDatas:function (cancelOrder) {
        isFinishLoad = false;
        currentPageIndex = 1;

        currentLoadType = cancelOrder;

        Org_Login_Phone = $.cookie('Org_Login_Phone');

        $("#qx_order_list").html("");


            $("#add_button").show();
            $.get_emplyee_query();
    },


});