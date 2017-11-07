/**
 * Created by jiaju_cao on 2017/6/7.
 */
var OpenId;
window.onload=function()
{
    OpenId = $.cookie('WX_OpenId');
};

$(document).ready(function()
{

});

$(window).resize(function(){
});

// 自定义函数
$.extend({
    changeCount: function (sepCount)
    {
        var currentCount = $("#order_prd_count").text();

        currentCount = parseInt(currentCount) + sepCount;

        if (currentCount == 0)
        {
            currentCount = 1;
        }

        var price = $("#product_price").text();
        price = parseFloat(price);

        $("#order_prd_count").text(currentCount);
        $("#product_price_total").text(currentCount * price);

    },

    // selectAddress:function () {
    //     // alert("aa");
    //     $("#address_selector").trigger("focus");
    // },
    
    address_change:function () {
        var options=$("#address_selector option:selected");

        var phone = options.val();
        // alert(value);
        var address = options.text();
        // alert(text);
        var name = options.attr('name');
        // alert(name);

        $("#address_input").val(address);
        $("#user_phone").val(phone);
        $("#select_address").val(name);

    },

    commitOrder:function (PCode) {
        var rtnCmd = "/api/user/?Command=Add_Order";
        var price = $("#product_price_total").text();
        var name = $("#select_address").val();
        var address = $("#address_input").val();
        var phone = $("#user_phone").val();

        if (phone == "联系电话")
        {
            alert("请输入联系电话");
            return;
        }

         if (address == "请填写详细地址")
        {
            alert("请填写详细地址");
            return;
        }

        if (name == "联系人")
        {
            alert("请输入联系人");
            return;
        }

        var serviceTime = $("#service_date").val();
        var timeSep = $("#service_time").val() ;
        var serviceTime = serviceTime + " " + timeSep;

        var ocodeTest = $("#org_selector").val() ;

        var count = $("#order_prd_count").text();
        var otherinfo = $("#other_info").val();
        if (otherinfo == "备注其他要求")
        {
            otherinfo = "";
        }
        $.post(rtnCmd, {ccode: OpenId, price: price,name:name,address:address,phone:phone,ocode:ocodeTest,pcode:PCode,count:count,otherinfo:otherinfo,servicetime:serviceTime},
            function (data)
            {
                var  ErrorId = data.ErrorId;
                var  Result = data.Result;

                if (ErrorId == 200)
                {
                    alert("感谢您的信任，我们工程师马上会同您联系");
                    location.replace("/home_index.html");
                }
                else
                {
                    alert(data.ErrorInfo);
                }


            },
            "json");//这里返回的类型有：json,html,xml,text
        }

});