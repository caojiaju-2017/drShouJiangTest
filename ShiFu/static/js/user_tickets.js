/**
 * Created by jiaju_cao on 2017/6/7.
 */

var isFinishLoad = false;
var currentPageIndex = 0;
var currentPageSize = 12;

var OpenId = null;
var divTemplate ="<div class=\"item_function\">\n" +
    "            <div style=\"width: 100%;background-color: #e0e0e0;\">\n" +
    "                <div style=\"margin-left: 5%;padding-top: 20px;font-size: 2.0em;height: 4pc\">{Ticket_Code}</div>\n" +
    "            </div>\n" +
    "\n" +
    "            <div class=\"seperatoLine\"></div>\n" +
    "\n" +
    "            <div style=\"width: 60%;float: left\">\n" +
    "                <img class=\"itemLogo\" src=\"/static/Images/tickets.png\">\n" +
    "                <div class=\"itemTitle\">面值：{Ticket_Price}元</div>\n" +
    "            </div>\n" +
    "            <div style=\"width: 36%;float: right;border: none\">\n" +
    "                <img src='/static/Images/{Ticket_State}' class=\"order_oper\">  </img> " +
    "<div class=\"order_endtime\" >  过期：{Order_EndTime}</div>\n\n" +
    "            </div>\n" +
    "        </div>\n" +
    "        <div class=\"seperatoLine\"></div>";

window.onload=function()
{
};

$(document).ready(function()
{
    OpenId = $.cookie('WX_OpenId');
    // 查询参与投票的品牌
    $.get_current_query();

    $(window).scroll(function(){
        var srollPos = $(window).scrollTop();
        var documentHd = $(document).height();
        var winHd = $(window).height() ;


        totalheight = parseFloat($(window).height()) + parseFloat(srollPos);
            // if(($(document).height()-range) <= totalheight  && num != maxnum) {
            //     main.append("<div style='border:1px solid tomato;margin-top:20px;color:#ac"+(num%20)+(num%20)+";height:"+elemt+"' >hello world"+srollPos+"---"+num+"</div>");
            // }
        if (srollPos + winHd > documentHd*0.9 && !isFinishLoad)
        {
             // 加载数据
            currentPageIndex = currentPageIndex + 1;
            $.get_current_query();
        }

        });
});
// 自定义函数
$.extend({
    get_current_query:function () {
        $.get("/api/pub/?Command=Get_Tickets&ccode=" + OpenId + "&pageindex=" + currentPageIndex + "&pagesize=" + currentPageSize + "&state=9",
            function (data)
            {
                // 检查查询状态
                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                 if (Result == null || Result.Datas.length < currentPageSize)
                 {
                    isFinishLoad = true;
                 }

                if (Result == null)
                {
                        var oneT = $("#ticket_list").html();
                        if (oneT.length <= 0)
                        {
                            $("#ticket_list").html("<div style='font-size: 2.7em;text-align: center'>没有优惠券 </div>" );
                        }

                        return;
                }

                var Datas = Result.Datas
                if (ErrorId == 200)
                {
                    if (Datas.length <= 0)
                    {
                        var oneT = $("#ticket_list").html();

                        if (oneT.length <= 0)
                        {
                            $("#ticket_list").html("<div style='font-size: 2.7em;text-align: center'>没有优惠券 </div>" );
                        }

                        return;
                    }
                    for (i=0;i<Datas.length ;i=i+1 )
                    {
                        var oneCode1 = Datas[i];
                        var abcTemp = {};

                        var orderState = null;
                        if (oneCode1.State == 0)
                        {
                            orderState = "ticket_was_use.png";
                        }
                        else if(oneCode1.State == 1)
                        {
                            orderState = "ticket_can_use.png";
                            if ($.getNowFormatDate() > oneCode1.EndDate)
                            {
                                orderState = "ticket_out_date.png";
                            }
                        }


                        abcTemp["Ticket_Code"] = oneCode1.Code;
                        abcTemp["Ticket_Price"] = oneCode1.Price;


                        abcTemp["Ticket_State"] = orderState;
                        abcTemp["Order_EndTime"] = oneCode1.EndDate;

                        var oneT = $("#ticket_list").html();
                        $("#ticket_list").html(oneT + $.format(divTemplate,abcTemp) );
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

    // viewOrder:function (cancelOrder) {
    //     alert(cancelOrder);
    //     // alert(cancelOrder);
    // },
    // cancelOrder:function (cancelOrder) {
    //     alert(cancelOrder);
    //     // alert(cancelOrder);
    // },
});