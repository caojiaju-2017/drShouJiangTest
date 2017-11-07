#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render,render_to_response
from django.http import  HttpResponse
import json,uuid,time,base64,re
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
import qrcode
from HsShareData import *
from django.db.models import Q
from ShiFu.models import *

from django.template import Template, Context
from django.db.models import Q
class DRPublicApi(object):
    @staticmethod
    @csrf_exempt
    def CommandDispatch(req):
        # print "api invoke1"
        command = req.GET.get('Command').upper()
        # print "api invoke2"
        # return HttpResponse("ok")
        if  command  == "Fetch_UserInfo".upper():
            return DRPublicApi.Fetch_UserInfo(req)
        elif command  == "Query_Orders".upper():
            return DRPublicApi.Query_Orders(req)
        elif command  == "Get_Order_Remark".upper():
            return DRPublicApi.Get_Order_Remark(req)
        elif command  == "Get_Tickets".upper():
            return DRPublicApi.Get_Tickets(req)
        elif command  == "Get_QX_Product".upper():
            return DRPublicApi.Get_QX_Product(req)
        elif command  == "Get_WX_Product".upper():
            return DRPublicApi.Get_WX_Product(req)
        elif command  == "Get_Suggest".upper():
            return DRPublicApi.Get_Suggest(req)
        elif command == "Order_Change".upper():
            return DRPublicApi.Order_Change(req)
        # Get_Order_Remark
    @staticmethod
    def Order_Change(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Code = postDataList["Code".lower()]
        except:
            pass

        State = None
        try:
            State = int(postDataList["State".lower()])
        except:
            pass

        Info = None
        try:
            Info = postDataList["Info".lower()]
        except:
            pass

        ECode = None
        try:
            ECode = postDataList["ECode".lower()]
        except:
            pass

        orderData = SjCustomOrders.objects.get(code=Code)

        if not orderData:
            loginResut = json.dumps({"ErrorInfo": "订单数据不存在", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        if State:
            orderData.state =State

        if Info:
            orderData.info = Info

        if ECode:
            orderData.ecode = ECode

        commitDataList=[]
        commitDataList.append(CommitData(orderData, 0))

        # 事务提交
        try:
            result = commitCustomDataByTranslate(commitDataList)

            if not result:
                loginResut = json.dumps({"ErrorInfo": "数据库操作失败", "ErrorId": 99999, "Result": None})
                return HttpResponse(loginResut)
        except Exception, ex:
            loginResut = json.dumps({"ErrorInfo": "数据库操作失败", "ErrorId": 99999, "Result": None})
            return HttpResponse(loginResut)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
        return HttpResponse(loginResut)
    @staticmethod
    def Get_Suggest(request):
        PageSize = int(request.GET.get('PageSize'.lower()))
        PageIndex = int(request.GET.get('PageIndex'.lower()))

        results = SjQuestion.objects.order_by("committime")

        if not results:
            loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
            return HttpResponse(loginResut)

        rtnDict={}
        rtnResult = []
        for index, one in enumerate(results):
            if index < PageIndex*PageSize:
                continue
            if index >= (PageIndex * PageSize + PageSize):
                break

            oneRecord = {}
            oneRecord["CCode"] = one.ccode
            oneRecord['CQQ'] = one.cqq
            oneRecord['LikePart'] = one.likepart
            oneRecord['Stars'] = one.stars
            rtnResult.append(oneRecord)

        rtnDict["MaxCount"] = len(results)
        rtnDict["Datas"] = rtnResult
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnDict})
        return HttpResponse(loginResut)
    @staticmethod
    def Get_WX_Product(request):
        results = SjWxServices.objects.order_by("name")

        if not results:
            loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
            return HttpResponse(loginResut)

        rtnResult = []
        for index, one in enumerate(results):
            oneRecord = {}
            oneRecord["Code"] = one.code
            oneRecord['Name'] = one.name
            oneRecord['ImgName'] = one.imgname
            rtnResult.append(oneRecord)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnResult})
        return HttpResponse(loginResut)

    @staticmethod
    def Get_QX_Product(request):
        Type = int(request.GET.get('Type'.lower()))

        results = SjServices.objects.filter(state= 1).order_by("name")

        if Type != 9:
            results = results.filter(servicetype = Type)


        if not results:
            loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
            return HttpResponse(loginResut)

        rtnResult = []
        for index, one in enumerate(results):
            oneRecord = {}
            oneRecord["Code"] = one.code
            oneRecord['Name'] = one.name
            oneRecord['Price'] = one.price

            oneRecord['OrigPrice'] = one.origprice

            if one.imgname1 and len(one.imgname1) > 0:
                oneRecord['ImgName1'] = "/static/ProductImage/" + one.imgname1
            else:
                oneRecord['ImgName1'] = None

            if one.imgname2 and len(one.imgname2) > 0:
                oneRecord['ImgName2'] = "/static/ProductImage/" + one.imgname2
            else:
                oneRecord['ImgName2'] = None

            if one.imgname3 and len(one.imgname3) > 0:
                oneRecord['ImgName3'] = "/static/ProductImage/" + one.imgname3
            else:
                oneRecord['ImgName3'] = None

            if one.detailimage and len(one.detailimage) > 0:
                oneRecord['DetailImage'] = "/static/ProductImage/" + one.detailimage
            else:
                oneRecord['DetailImage'] = None

            oneRecord['Info'] = one.info
            oneRecord['BookCount'] = one.bookcount
            oneRecord['ViewCount'] = one.viewcount
            oneRecord['ServiceTime'] = one.servicetime
            oneRecord['ServiceType'] = one.servicetype
            rtnResult.append(oneRecord)

        print rtnResult
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnResult})
        return HttpResponse(loginResut)

    @staticmethod
    def Get_Tickets(request):
        # 提取post数据
        print request.GET

        try:
            CCode = request.GET.get('CCode'.lower())
            OCode = request.GET.get('OCode'.lower())
        except:
            pass

        try:
            State = int(request.GET.get('State'.lower()))
            PageSize = int(request.GET.get('PageSize'.lower()))
            PageIndex = int(request.GET.get('PageIndex'.lower()))
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20006, "Result": None})
            return HttpResponse(loginResut)

        if CCode:
            results = SjTickets.objects.filter(ccode=CCode).order_by("state")
        elif OCode:
            results = SjTickets.objects.filter(ocode=OCode).order_by("state")
        else :
            results = SjTickets.objects.order_by("state")

        if State != 9:
            results = results.filter(~Q(state= State))

        if not results:
            loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
            return HttpResponse(loginResut)

        rtnDict = {}
        rtnResult = []
        for index, one in enumerate(results):
            if index < PageIndex*PageSize:
                continue
            if index >= (PageIndex * PageSize + PageSize):
                break

            oneRecord = {}
            oneRecord["Code"] = one.code
            oneRecord['OCode'] = one.ocode
            oneRecord['CCode'] = one.ccode
            oneRecord['Price'] = one.price
            oneRecord['State'] = one.state
            oneRecord['Extern1'] = one.extern1
            oneRecord['Extern2'] = one.extern2
            oneRecord['Extern3'] = one.extern3
            oneRecord['EndDate'] = one.enddate

            rtnResult.append(oneRecord)

        rtnDict["MaxCount"] = len(results)
        rtnDict["Datas"] = rtnResult
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnDict})
        return HttpResponse(loginResut)

    @staticmethod
    def Get_Order_Remark(request):
        # 提取post数据
        Code = request.GET.get('Code'.lower())

        results = SjOrderRemark.objects.filter(ocode=Code).order_by("remarktime")

        if not results:
            loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
            return HttpResponse(loginResut)

        rtnResult = []
        for index, one in enumerate(results):
            oneRecord = {}
            oneRecord["OCode"] = one.ocode
            oneRecord['Info'] = one.info
            oneRecord['RemarkTime'] = one.remarktime
            oneRecord['CCode'] = one.ccode

            rtnResult.append(oneRecord)


        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnResult})
        return HttpResponse(loginResut)
    @staticmethod
    def Query_Orders(request):
        # 提取post数据
        print request.GET
        pageIndex = int(request.GET.get('PageIndex'.lower()))
        pageSize = int(request.GET.get('PageSize'.lower()))
        State = int(request.GET.get('State'.lower()))
        Type = int(request.GET.get('Type'.lower()))

        CCode = request.GET.get('CCode'.lower())

        OCode = request.GET.get('OCode'.lower())
        ECode = request.GET.get('ECode'.lower())

        results = None
        if CCode:
            results = SjCustomOrders.objects.filter(ccode = CCode).order_by("state").order_by("state")
        elif OCode:
            results = SjCustomOrders.objects.filter(ocode=OCode).order_by("state")
        elif ECode:
            results = SjCustomOrders.objects.filter(ecode=ECode).order_by("state")
        else:
            results = SjCustomOrders.objects.order_by("state")

        if Type != 9:
            results = results.filter(type = Type)

        if State == 0:
            results = results.filter(Q(state=1) | Q(state=2))
        elif State == 1:
            results = results.filter(Q(state=3) | Q(state=9))
        elif State == 8:
            pass
        elif State == 9:
            results = results.filter(state=9)
        else:
            pass

        if not results:
            loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
            return HttpResponse(loginResut)

        rtnDict={}
        rtnResult = []
        for index, one in enumerate(results):
            if index < pageIndex*pageSize:
                continue
            if index >= (pageIndex * pageSize + pageSize):
                break

            oneRecord = {}
            oneRecord["Code"] = one.code
            oneRecord['ODateTime'] = one.odatetime
            oneRecord['CCode'] = one.ccode
            oneRecord['Price'] = one.price
            oneRecord['Type'] = one.type
            oneRecord['SrvCode'] = one.srvcode
            oneRecord['OCode'] = one.ocode
            oneRecord['State'] = one.state
            oneRecord['LastTime'] = one.lasttime
            oneRecord['Info'] = one.info
            oneRecord['ECode'] = one.ecode

            oneRecord['ContactName'] = one.contactname
            oneRecord['Address'] = one.address
            oneRecord['ContactPhone'] = one.contactphone
            oneRecord['Count'] = one.count
            oneRecord['Extern1'] = one.extern1
            oneRecord['Extern2'] = one.extern2
            oneRecord['Extern3'] = one.extern3
            oneRecord['ServiceTime'] = one.servicetime

            rtnResult.append(oneRecord)
        rtnDict["MaxCount"] = len(results)
        rtnDict["Datas"] = rtnResult

        print rtnDict
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnDict})
        return HttpResponse(loginResut)
    @staticmethod
    def Fetch_UserInfo(request):
        # 提取post数据
        Code = request.GET.get('Code'.lower())

        try:
            custom = SjCustoms.objects.get(code=Code)
        except:
            loginResut = json.dumps({"ErrorInfo": "用户数据异常", "ErrorId": 20001, "Result": ""})
            return HttpResponse(loginResut)
            pass

        if not custom:
            loginResut = json.dumps({"ErrorInfo": "用户数据异常", "ErrorId": 20001, "Result": ""})
            return HttpResponse(loginResut)

        rtnDict = {}
        rtnDict["Code"] = custom.code
        rtnDict["Phone"] = custom.phone
        rtnDict["Name"] = custom.name
        rtnDict["City"] = custom.city
        rtnDict["LastLoginTime"] =custom.lastlogintime

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnDict})
        return HttpResponse(loginResut)

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