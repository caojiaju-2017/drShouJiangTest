/**
 * Created by jiaju_cao on 2017/6/7.
 */

var userCookie=null;
var lastDate=null;
var isEnable = 1;

var isFinishLoad = false;
var currentPageIndex = 0;
var currentPageSize = 10;
var fliterString = "";

window.onload=function()
{

    // var openid = $.weixin_login();
    // $.queryUserInfo(openid);

};

$(document).ready(function()
{
    var openid = $.weixin_login();
    $.cookie("WX_OpenId",openid);
    $.queryUserInfo(openid);
});

// 自定义函数
$.extend({
     queryUserInfo:function (openid) {
        // 提取用户名
        $.get("/api/pub/?Command=Fetch_UserInfo&code=" + openid,
            function (data)
            {
                // 检查查询状态
                var  ErrorId = data.ErrorId;
                var  ErrorInfo = data.ErrorInfo;
                var Datas = data.Result;

                if (ErrorId == 200)
                {
                    $("#uName").html(Datas.Name);

                    if ($.CheckNull(Datas.Phone) == 0)
                    {
                        $("#phoneBind").html("绑定手机");
                    }
                    else
                    {
                        $("#phoneBind").html(Datas.Phone);
                    }
                }
                else
                {
                    //alert(data.ErrorInfo);
                    return null;
                }

            },
            "json");//这里返回的类型有：json,html,xml,text
    },
    CheckNull:function (datas) {
            return (datas == "" || datas == undefined || datas == null) ? 0 : 1;
    },
});