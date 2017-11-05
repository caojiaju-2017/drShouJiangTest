#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render,render_to_response
from django.http import  HttpResponse
import json,uuid,time,base64,re
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
import qrcode
from HsShareData import *

from ShiFu.models import *

from django.template import Template, Context
#python manage.py inspectdb > yourSiteDirectory/yourApplication/models.py

class WebCenter(object):



    @staticmethod
    @csrf_exempt
    def goHome(request):
        if (not HsShareData.IsDebug)  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        # renterDict['title'] = config.title
        # renterDict['vote_intro'] = "      " + config.introduce.replace("<br>","\n").replace("&nbsp"," ")
        # renterDict['main_logo'] = "/static/%s" % config.logoimage
        # renterDict['start_date'] = config.startdate
        # renterDict['stop_date'] = config.stopdate
        # renterDict['ZhuBanOrg'] = config.zhubanorg
        # renterDict['ChengBanOrg'] = config.xiebanorg
        # renterDict['ZhiChiOrg'] = config.zhichiorg
        # renterDict['XieZhuOrg'] = config.xiezhuorg
        return render(request, 'Home.html',renterDict )

    @staticmethod
    @csrf_exempt
    def goUserHome(request):
        if not HsShareData.IsDebug  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        config = SjConfig.objects.filter(ckey="Help_Line").first()
        renterDict = {}
        if config:
            renterDict['Help_Line'] = config.cvalue

        # renterDict['title'] = config.title
        # renterDict['vote_intro'] = "      " + config.introduce.replace("<br>","\n").replace("&nbsp"," ")
        # renterDict['main_logo'] = "/static/%s" % config.logoimage
        # renterDict['start_date'] = config.startdate
        # renterDict['stop_date'] = config.stopdate

        return render(request, 'user_main.html',renterDict )


    @staticmethod
    @csrf_exempt
    def goUserQXOrder(request):
        if not HsShareData.IsDebug  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'user_qx_orders.html',renterDict )

    @staticmethod
    @csrf_exempt
    def goSetupOrder(request):
        if not HsShareData.IsDebug  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'user_setup_orders.html',renterDict )


    @staticmethod
    @csrf_exempt
    def goWXOrder(request):
        if not HsShareData.IsDebug  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'user_wx_orders.html',renterDict )


    @staticmethod
    @csrf_exempt
    def goRemarks(request):
        if not HsShareData.IsDebug  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'user_remarks.html',renterDict )

    @staticmethod
    @csrf_exempt
    def goUseTickes(request):
        if not HsShareData.IsDebug  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'user_tickets.html',renterDict )

    @staticmethod
    @csrf_exempt
    def goAddress(request):
        if not HsShareData.IsDebug  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'user_address.html',renterDict )


    @staticmethod
    @csrf_exempt
    def loginOrg(request):
        if not HsShareData.IsDebug  and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT,"Images"),"erweima_img.png"))
            return render(request, 'error_notice.html',{"erweima_img":"/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'login_org.html',renterDict )

    @staticmethod
    @csrf_exempt
    def loginEmplyee(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'login_emplyee.html', renterDict)
    @staticmethod
    @csrf_exempt
    def addUserAddress(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'user_add_address.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goSuggest(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'suggest.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goServiceFlow(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'service_flow.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goAddEmplyee(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'add_emplyee.html', renterDict)

    @staticmethod
    @csrf_exempt
    def startOrder(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        config = SjConfig.objects.filter(ckey="Help_Line").first()
        renterDict = {}
        if config:
            renterDict['Help_Line'] = config.cvalue

        citys = {}
        citys["chengdu"] = "成都市"
        citys["beijing"] = "北京市"
        citys["quanzhou"] = "泉州市"
        citys["guangzhou"] = "广州市"


        renterDict["City_Datas"] =citys
        return render(request, 'begin_order.html', renterDict)

    @staticmethod
    @csrf_exempt
    def openOrderDetail(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        renterDict = {}
        Code = request.GET.get('code')

        print "订单号码：", Code

        emplyeeData = None
        customOrder = SjCustomOrders.objects.filter(code = Code).first()
        if not customOrder:
            loginResut = json.dumps({"ErrorInfo": "订单数据异常", "ErrorId": 99999, "Result": None})
            return HttpResponse(loginResut)

        addressInfo = None
        if customOrder.addrcode:
            addressInfo = SjCustomAddress.objects.filter(code=customOrder.addrcode).first()

        srvData = None
        if customOrder.type == 0 and customOrder.srvcode :
            srvData = SjQxServices.objects.filter(code=customOrder.srvcode).first()

        if customOrder.type == 1 and customOrder.srvcode :
            srvData = SjWxServices.objects.filter(code=customOrder.srvcode).first()

        orgData = None
        if customOrder.ocode:
            orgData = SjSrvOrg.objects.filter(code=customOrder.ocode,state = 1)

        if customOrder.ecode:
            emplyeeData = SjEmplyees.objects.filter(code=customOrder.ecode,state=1).first()

        weixiuData = None

        if customOrder.type == 1:
            weixiuData = SjWeixiuOrders.objects.filter(ocode = customOrder.code).first()

        # showEmplyee = False
        # PaiDanButton = False
        # TerminalButton = False
        # FinishButton = False
        StateInfo = None
        # TerminalShow = False
        # 根据订单状态渲染
        if customOrder.state == 1:#派单中
            # showEmplyee = False
            # PaiDanButton = True
            # TerminalButton = True
            # FinishButton = False
            StateInfo = "派单中"
            # TerminalShow = False
            renterDict["showEmplyee"] = "disabled"
            renterDict["PaiDanButton"] = ""
            renterDict["TerminalButton"] = ""
            renterDict["FinishButton"] = "disabled"
            renterDict["TerminalShow"] = ""

            renterDict["WorkSpace1"] = "disabled"
            renterDict["WorkSpace2"] = ""
        elif customOrder.state == 2: #服务中
            # showEmplyee = True
            # PaiDanButton = False
            # TerminalButton = True
            # FinishButton = True
            StateInfo = "服务中"
            # TerminalShow = False
            renterDict["showEmplyee"] = ""
            renterDict["PaiDanButton"] = "disabled"
            renterDict["TerminalButton"] = ""
            renterDict["FinishButton"] = ""
            renterDict["TerminalShow"] = ""
            renterDict["WorkSpace"] = ""
            renterDict["WorkSpace1"] = "disabled"
            renterDict["WorkSpace2"] = ""

        elif customOrder.state == 3: #已完成
            # showEmplyee = True
            # PaiDanButton = False
            # TerminalButton = False
            # FinishButton = False
            StateInfo = "已完成"
            # TerminalShow = False
            renterDict["showEmplyee"] = ""
            renterDict["PaiDanButton"] = "disabled"
            renterDict["TerminalButton"] = "disabled"
            renterDict["FinishButton"] = "disabled"
            renterDict["TerminalShow"] = "disabled"
            renterDict["WorkSpace"] = "disabled"
            renterDict["WorkSpace1"] = "disabled"
            renterDict["WorkSpace2"] = "disabled"


        elif customOrder.state == 9: #已终止
            if emplyeeData:
                # showEmplyee = True
                renterDict["showEmplyee"] = ""
            else:
                # showEmplyee = False
                renterDict["showEmplyee"] = "disabled"
            # PaiDanButton = False
            # TerminalButton = False
            # FinishButton = False
            StateInfo = "已终止"
            # TerminalShow = True
            renterDict["PaiDanButton"] = "disabled"
            renterDict["TerminalButton"] = "disabled"
            renterDict["FinishButton"] = "disabled"
            renterDict["TerminalShow"] = "disabled"
            renterDict["WorkSpace"] = "disabled"
            renterDict["WorkSpace1"] = "disabled"
            renterDict["WorkSpace2"] = "disabled"
        if customOrder:
            renterDict["Order_Code"] = Code
            renterDict["Order_State"] = StateInfo

            if addressInfo:
                renterDict["Custom_Name"] = addressInfo.name
                renterDict["Custom_Phone"] = addressInfo.phone
                renterDict["Custom_Address"] = addressInfo.address

            if weixiuData:
                renterDict["Other_Info"] = weixiuData.devtype + weixiuData.setupdate + weixiuData.info
            else:
                renterDict["Other_Info"] = "无"

            if customOrder.state == 9 or customOrder.state == 3:
                renterDict["Terminal_Info"] = customOrder.info

            if emplyeeData:
                renterDict["Emp_Name"] = emplyeeData.name
                renterDict["Emp_Phone"] = emplyeeData.phone

            if customOrder.type == 0 and srvData:
                renterDict["Product_Name"] = srvData.name
                renterDict["Product_Price"] = srvData.price
            elif customOrder.type == 1 and srvData:
                renterDict["Product_Name"] = srvData.name
                renterDict["Product_Price"] = "现场确认"
            pass

        myEmpylees = SjEmplyees.objects.filter(ocode=customOrder.ocode,state=1)
        empDict = {}
        for one in myEmpylees:
            empDict[one.code] = one.name
        renterDict["Emplyee_Datas"]= empDict

        return render(request, 'order_detail_info.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goOrgHome(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        Code = request.GET.get('code')

        orgData = SjSrvOrg.objects.filter(code=Code,state=1).first()

        # config = DrConfig.objects.first()
        renterDict = {}
        if orgData:
            renterDict["Org_Name"] = orgData.name
            renterDict["Org_Phone"] = orgData.phone
        return render(request, 'org_main.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goEmplyeeHome(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        Code = request.GET.get('code')
        orgData = SjEmplyees.objects.filter(code=Code,state=1).first()
        renterDict = {}
        if orgData:
            renterDict["Emp_Name"] = orgData.name
            renterDict["Emp_Phone"] = orgData.phone
        return render(request, 'emplyee_main.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goOrderAj(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        Code = request.GET.get('code')
        orgData = SjEmplyees.objects.filter(code=Code,state=1).first()
        renterDict = {}
        if orgData:
            renterDict["Emp_Name"] = orgData.name
            renterDict["Emp_Phone"] = orgData.phone
        return render(request, 'start_order_aj.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goOrderGdQx(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        Code = request.GET.get('code')
        orgData = SjEmplyees.objects.filter(code=Code,state=1).first()
        renterDict = {}
        if orgData:
            renterDict["Emp_Name"] = orgData.name
            renterDict["Emp_Phone"] = orgData.phone
        return render(request, 'start_order_gd_qx.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goOrderQx(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        Code = request.GET.get('code')
        orgData = SjEmplyees.objects.filter(code=Code,state=1).first()
        renterDict = {}
        if orgData:
            renterDict["Emp_Name"] = orgData.name
            renterDict["Emp_Phone"] = orgData.phone

        config = SjConfig.objects.filter(ckey="Help_Line").first()
        renterDict = {}
        if config:
            renterDict['Help_Line'] = config.cvalue

        renterDict['Total_Price'] = 0
        renterDict['Total_Cut'] = 0
        return render(request, 'start_order_qx.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goOrderWx(request):
        if not HsShareData.IsDebug and not checkMobile(request):
            url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
            img = qrcode.make(url)
            img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
            return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        Code = request.GET.get('code')
        orgData = SjEmplyees.objects.filter(code=Code,state=1).first()
        renterDict = {}
        if orgData:
            renterDict["Emp_Name"] = orgData.name
            renterDict["Emp_Phone"] = orgData.phone
        return render(request, 'start_order_wx.html', renterDict)

    @staticmethod
    @csrf_exempt
    def goTest(request):
        # if not HsShareData.IsDebug and not checkMobile(request):
        #     url = "http://" + request.META['HTTP_HOST'] + request.META['PATH_INFO'] + request.META['QUERY_STRING']
        #     img = qrcode.make(url)
        #     img.save(os.path.join(os.path.join(STATIC_ROOT, "Images"), "erweima_img.png"))
        #     return render(request, 'error_notice.html', {"erweima_img": "/static/Images/erweima_img.png"})

        # config = DrConfig.objects.first()
        renterDict = {}
        return render(request, 'index.html', renterDict)

def getPostData(request):
    postDataList = {}
    if request.method == 'POST':
        for key in request.POST:
            try:
                postDataList[key] = request.POST.getlist(key)[0]
            except:
                pass

    import json
    if not postDataList or len(postDataList) == 0:
        try:
            bodyTxt = request.body
            postDataList = json.loads(bodyTxt)
        except Exception,ex:
            pass

    return  postDataList

def commitCustomDataByTranslate(objHandles):
    with transaction.atomic():
        for oneObject in objHandles:
            if not oneObject.dbHandle:
                continue

            try:
                if oneObject.operatorType == 0:
                    oneObject.dbHandle.save()
                elif oneObject.operatorType == 1:
                    oneObject.dbHandle.delete()
            except Exception,ex:
                return  False

    return True


#判断网站来自mobile还是pc
def checkMobile(request):
    """
    demo :
        @app.route('/m')
        def is_from_mobile():
            if checkMobile(request):
                return 'mobile'
            else:
                return 'pc'
    :param request:
    :return:
    """
    userAgent = request.META.get('HTTP_USER_AGENT', None)
    # userAgent = request.headers['User-Agent']
    # userAgent = env.get('HTTP_USER_AGENT')

    _long_matches = r'googlebot-mobile|android|avantgo|blackberry|blazer|elaine|hiptop|ip(hone|od)|kindle|midp|mmp|mobile|o2|opera mini|palm( os)?|pda|plucker|pocket|psp|smartphone|symbian|treo|up\.(browser|link)|vodafone|wap|windows ce; (iemobile|ppc)|xiino|maemo|fennec'
    _long_matches = re.compile(_long_matches, re.IGNORECASE)
    _short_matches = r'1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|e\-|e\/|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(di|rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|xda(\-|2|g)|yas\-|your|zeto|zte\-'
    _short_matches = re.compile(_short_matches, re.IGNORECASE)

    if _long_matches.search(userAgent) != None:
        return True
    user_agent = userAgent[0:4]
    if _short_matches.search(user_agent) != None:
        return True
    return False