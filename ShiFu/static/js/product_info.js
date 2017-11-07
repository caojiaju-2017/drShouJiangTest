var index = 0;
var len = 0;
var OpenId;
window.onload=function()
{
    OpenId = $.cookie('WX_OpenId');
    len=$("#scroll ul li").length-1;
    var timer = window.setInterval("$.timego()",3000);
};

$.extend({
   timego:function () {
       if(index==0){
       index=len+1;
       }
       index--;
       $("#scroll ul li").eq(index).fadeIn().siblings().hide();
       },

    startOrder:function (code,name,price) {
       // alert("a");
       // alert(code);
       // alert(name);
       // alert(price);

        location.href='./begin_order.html?code='+ code + "&name=" + name + "&price=" + price + "&ucode=" +  OpenId;
    }
});
