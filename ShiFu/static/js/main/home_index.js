
var serviceItemTmp="                <div class=\"item_function\">\n" +
    "                    <div style=\"width: 220px;float: left\">\n" +
    "                        <img class=\"itemLogo\" src=\"{Image_Name}\">\n" +
    "                    </div>\n" +
    "                    <div style=\"width: 70%;float: left\">\n" +
    "                        <div style=\"margin-top: 10px;padding-left: 10px;font-size: 2.7em;color:#000\">{Product_Title}</div>\n" +
    "                        <div style=\"margin-top: 10px;padding-left: 10px;font-size: 2.0em;color: #666666\">{Product_Info}</div>\n" +
    "                    </div>\n" +
    "                    <div style=\"margin-top: 10px\">\n" +
    "                        <div style=\"font-size: 2.4em;float: left;margin-left: 10px\">¥{Product_Price}元</div>\n" +
    "                        <div style=\"font-size: 2.4em;float: right;margin-left: 10px;border-radius: 10px;\n" +
    "                        text-align:center;padding-top:10px;width: 140px;height: 80px;margin-right: 20px;\n" +
    "                        background-color: #EA5504;color: white\" onclick=\"$.openProduct('{Product_Code}')\">预约</div>\n" +
    "                    </div>\n" +
    "                </div>\n" +
    "                <div class=\"seperatoLine\"></div>;"

$(document).ready(function()
{
    setInterval("$.showLoopImage()",3000);

    var openid = $.weixin_login();
    // alert(openid);
    $.cookie("WX_OpenId",openid);
    $.queryUserInfo(openid);

    $(document).ready(function () {
        //添加图片
        $("div .subMenu>img").each(function () {
            var name = $(this).attr("data-imgname");
            var src = "/static/Images/main/" + name + ".png"
            //设置img的属性和值。
            $(this).attr("src", src);
        });

        //点击事件
        $("div .subMenu").click(function () {
            // 取消当前激活状态
            var $img = $(".active>img");
            //返回被选元素的属性值
            var name = $img.attr("data-imgname");
            var src = "/static/Images/main/" + name + ".png";
            $img.attr("src", src);
            $(".active").removeClass("active");

            // 添加新状态
            $(this).addClass("active");
            //找到所有 div(subMenu) 的子元素(img)
            $img = $(this).children("img");
            name = $img.attr("data-imgname");
            src = "/static/Images/main/" + name + "_active.png";
            //设置img的属性和值。
            $img.attr("src", src);

            $("#home_content").css('display','none');
            $("#my_content").css('display','none');
            $("#search_content").css('display','none');

            $("#" + name + "_content").css('display','block');
            //content根据点击按钮加载不同的html
            // var page = $(this).attr("data-src");
            // if(page){
                // $("#content").load("../html/" + page)

            // }
        });

        // 自动点击第一个菜单
        $("div .subMenu")[0].click();
    });


});

// 自定义函数
$.extend({
     queryUserInfo:function (openid) {
        // 提取用户名
        $.get("/api/pub/?Command=Get_QX_Product&type=9",
            function (data)
            {
                // 检查查询状态
                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                 // if (Result == null || Result.Datas.length < currentPageSize)
                 // {
                 //    // isFinishLoad = true;
                 // }

                if (Result == null)
                {
                    var oneT = $("#data_container").html();

                        if (oneT.length <= 0)
                        {
                            $("#data_container").html("<div style='font-size: 2.7em;text-align: center'>没有产品数据 </div>" );
                        }

                        return;
                }

                var Datas = Result;
                if (ErrorId == 200)
                {
                    if (Datas.length <= 0)
                    {
                        var oneT = $("#data_container").html();

                        if (oneT.length <= 0)
                        {
                            $("#data_container").html("<div style='font-size: 2.7em;text-align: center'>没有产品数据 </div>" );
                        }

                        return;
                    }
                    for (i=0;i<Datas.length ;i=i+1 )
                    {
                        var oneCode1 = Datas[i];
                        var abcTemp = {};

                        if (oneCode1.ImgName1 != null)
                        {
                            abcTemp["Image_Name"] = oneCode1.ImgName1;
                        }

                        if (oneCode1.Name != null)
                        {
                            abcTemp["Product_Title"] = oneCode1.Name;
                        }
                        else
                        {
                            abcTemp["Product_Title"] = "未命名产品";
                        }

                        if (oneCode1.Info != null)
                        {
                            abcTemp["Product_Info"] = oneCode1.Info.substr(0,36) + "...";
                        }
                        else
                        {
                            abcTemp["Product_Info"] = "";
                        }

                        if (oneCode1.Price != null)
                        {
                            abcTemp["Product_Price"] = oneCode1.Price;
                        }
                        else
                        {
                            abcTemp["Product_Price"] = "?";
                        }

                        abcTemp["Product_Code"] = oneCode1.Code;


                        var oneT = $("#data_container").html();

                        $("#data_container").html(oneT + $.format(serviceItemTmp,abcTemp) );

                    }
                }

            },
            "json");//这里返回的类型有：json,html,xml,text
    },
    CheckNull:function (datas) {
            return (datas == "" || datas == undefined || datas == null) ? 0 : 1;
    },
    /*content高度*/
    initSize:function () {
        var height = $(window).height() -$("#description").height() - $("#menu").height();
//        var height = $(window).height() - $("header").height() - $("#description").height() - $("#menu").height();
        $("#content").height(height + "px");
    },
    showLoopImage:function () {
        // alert("ok");
        var name = $("#loopImage").attr("data-imgname");

        if (name == "banner1")
        {
            var src = "/static/Images/" + "banner2.jpg"
            $("#loopImage").attr("data-imgname", "banner2");
            //设置img的属性和值。
            $("#loopImage").attr("src", src);
        }
        else if(name == "banner2")
        {
            var src = "/static/Images/" + "banner3.jpg"
            $("#loopImage").attr("data-imgname", "banner3");
            //设置img的属性和值。
            $("#loopImage").attr("src", src);
        }
        else
        {
            var src = "/static/Images/" + "banner1.jpg"
            $("#loopImage").attr("data-imgname", "banner1");
            //设置img的属性和值。
            $("#loopImage").attr("src", src);
        }
        // alert(name);
    },

    openProduct:function (param) {
        // alert(param);
        location.href = "./product_info.html?code=" + param;
    }
});