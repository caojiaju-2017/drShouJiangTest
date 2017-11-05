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

class DRApi(object):
    @staticmethod
    @csrf_exempt
    def CommandDispatch(req):
        # print "api invoke1"
        command = req.GET.get('Command').upper()
        # print "api invoke2"
        # return HttpResponse("ok")
        if  command  == "Bind_Phone".upper():
            return DRApi.Bind_Phone(req)
        elif command  == "Get_Addresses".upper():
            return DRApi.Get_Addresses(req)
        elif command  == "Add_Address".upper():
            return DRApi.Add_Address(req)
        elif command  == "Modi_Address".upper():
            return DRApi.Modi_Address(req)
        elif command  == "Dele_Address".upper():
            return DRApi.Dele_Address(req)
        elif command == "Add_Remark".upper():
            return DRApi.Add_Remark(req)
        elif command  == "Release_Suggest".upper():
            return DRApi.Release_Suggest(req)
        elif command  == "Add_Order".upper():
            return DRApi.Add_Order(req)
        elif command  == "Add_Order".upper():
            return DRApi.Add_Order(req)
        elif command  == "Set_City".upper():
            return DRApi.Set_City(req)

    @staticmethod
    def Set_City(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        Code = postDataList["Code".lower()]
        City = postDataList["City".lower()]

        custom = SjCustoms.objects.get(code=Code)
        if not custom:
            loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": ""})
            return HttpResponse(loginResut)

        custom.city = City

        commitDataList = []
        commitDataList.append(CommitData(custom, 0))

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
    def Add_Order(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        CCode = postDataList["CCode".lower()]
        Price = float(postDataList["Price".lower()])
        AddrCode = postDataList["AddrCode".lower()]
        OCode = postDataList["OCode".lower()]
        Type = int(postDataList["Type".lower()])
        PCode = postDataList["PCode".lower()]

        newOrder = SjCustomOrders()
        newOrder.code = uuid.uuid1().__str__().replace("-","")
        newOrder.ccode = CCode
        newOrder.price = Price
        newOrder.addrcode = AddrCode
        newOrder.ocode = OCode
        newOrder.type = Type
        newOrder.srvcode = PCode
        newOrder.odatetime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        newOrder.lasttime =  time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))


        commitDataList = []
        commitDataList.append(CommitData(newOrder, 0))

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
    def Release_Suggest(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        CCode = postDataList["CCode".lower()]
        CQQ = postDataList["CQQ".lower()]
        LikePart = int(postDataList["LikePart".lower()])
        Stars = int(postDataList["Stars".lower()])
        Info = postDataList["Info".lower()]


        newQuestion = SjQuestion()
        newQuestion.ccode = CCode
        newQuestion.cqq = CQQ
        newQuestion.likepart = LikePart#time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        newQuestion.stars = Stars
        newQuestion.info= Info
        newQuestion.committime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        commitDataList = []
        commitDataList.append(CommitData(newQuestion, 0))

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
    def Add_Remark(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        CCode = postDataList["CCode".lower()]
        Info = postDataList["Info".lower()]
        OCode = postDataList["OCode".lower()]

        # 查询订单信息
        order = SjCustomOrders.objects.filter(code = OCode).first()
        if not order:
            loginResut = json.dumps({"ErrorInfo": "未找到订单信息", "ErrorId": 200, "Result": ""})
            return HttpResponse(loginResut)

        newRemark = SjOrderRemark()
        newRemark.ocode = OCode
        newRemark.info = Info
        newRemark.remarktime = time.strftime('%Y-%m-%d %H-%M-%S', time.localtime(time.time()))
        newRemark.ccode = CCode
        commitDataList = []
        commitDataList.append(CommitData(newRemark, 0))

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
    def Dele_Address(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        Code = postDataList["Code".lower()]

        updateAddress = SjCustomAddress.objects.filter(code=Code).first()
        if not updateAddress:
            loginResut = json.dumps({"ErrorInfo": "删除成功", "ErrorId": 200, "Result": ""})
            return HttpResponse(loginResut)

        commitDataList = []
        commitDataList.append(CommitData(updateAddress, 1))

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
    def Modi_Address(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        Code = postDataList["Code".lower()]
        CCode = postDataList["CCode".lower()]
        Phone = postDataList["Phone".lower()]
        Address = postDataList["Address".lower()]
        Name = postDataList["Name".lower()]
        Flag = int(postDataList["Flag".lower()])

        empUser = SjCustoms.objects.get(code=CCode)
        if not empUser:
            loginResut = json.dumps({"ErrorInfo": "您的账号数据异常", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        updateAddress = SjCustomAddress.objects.get(code = Code)
        if not updateAddress:
            loginResut = json.dumps({"ErrorInfo": "当前修改的地址不存在", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        updateAddress.phone = Phone
        updateAddress.address = Address
        updateAddress.name = Name
        updateAddress.flag = Flag

        commitDataList=[]
        commitDataList.append(CommitData(updateAddress, 0))

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
    def Add_Address(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        Code = postDataList["Code".lower()]
        Phone = postDataList["Phone".lower()]
        Address = postDataList["Address".lower()]
        Name = postDataList["Name".lower()]
        Flag = int(postDataList["Flag".lower()])

        empUser = SjCustoms.objects.get(code=Code)

        if not empUser:
            loginResut = json.dumps({"ErrorInfo": "您的账号数据异常", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        newAddress = SjCustomAddress()
        newAddress.ccode = Code
        newAddress.phone = Phone
        newAddress.address = Address
        newAddress.name = Name
        newAddress.flag = Flag
        newAddress.code = uuid.uuid1().__str__().replace("-", "")

        commitDataList=[]
        commitDataList.append(CommitData(newAddress, 0))

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
    def Get_Addresses(request):
        # 提取post数据
        Code = request.GET.get('Code'.lower())

        user = SjCustoms.objects.get(code=Code)

        if not user:
            loginResut = json.dumps({"ErrorInfo": "账号数据异常", "ErrorId": 10001, "Result": ""})
            return HttpResponse(loginResut)

        addresses = SjCustomAddress.objects.filter(ccode = user.code)
        rtnResult = []
        for index, one in enumerate(addresses):
            oneRecord = {}
            oneRecord["code"] = one.code
            oneRecord['ccode'] = one.ccode
            oneRecord['phone'] = one.phone
            oneRecord['address'] = one.address
            oneRecord['name'] = one.name
            oneRecord['flag'] = one.flag

            rtnResult.append(oneRecord)

        print oneRecord
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnResult})
        return HttpResponse(loginResut)

    @staticmethod
    def Bind_Phone(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        Code = postDataList["Code".lower()]
        Phone = postDataList["Phone".lower()]

        empUser = SjCustoms.objects.get(code=Code)

        if not empUser:
            loginResut = json.dumps({"ErrorInfo": "您的账号不存在", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        empUser.phone = Phone
        commitDataList=[]
        commitDataList.append(CommitData(empUser, 0))

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
    def Staff_Login(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        userCode = postDataList["Phone".lower()]
        Password = postDataList["Password".lower()]
        empUser = SjEmplyees.objects.get(code = userCode)

        if not empUser:
            loginResut = json.dumps({"ErrorInfo": "您的账号不存在", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        if Password != empUser.pswd:
            loginResut = json.dumps({"ErrorInfo": "账号或密码错误", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
        return HttpResponse(loginResut)

    @staticmethod
    def Org_Login(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        userCode = postDataList["Phone".lower()]
        Password = postDataList["Password".lower()]
        srvUser = SjSrvOrg.objects.get(code = userCode)

        if not srvUser:
            loginResut = json.dumps({"ErrorInfo": "您的账号不存在", "ErrorId": 10001, "Result": ""})
            return HttpResponse(loginResut)

        if Password != srvUser.pswd:
            loginResut = json.dumps({"ErrorInfo": "账号或密码错误", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": None})
        return HttpResponse(loginResut)

    @staticmethod
    def View_Image(request):
        imagename = request.GET.get('imagename')
        type = int(request.GET.get('type'))

        #
        imageFilePath = None
        if type == 0: # 主logo
            imageFilePath = os.path.join(STATIC_ROOT, "%s"%imagename)
        elif type == 1: # 厂商
            imageFilePath = os.path.join(os.path.join(STATIC_ROOT,"factory"), "%s.jpg" % imagename)
        elif type == 2: # 厂商
            imageFilePath = os.path.join(os.path.join(STATIC_ROOT,"expert"), "%s.jpg" % imagename)
        elif type == 3:
            imageFilePath = os.path.join(os.path.join(STATIC_ROOT, "Images"), imagename)
        if not imageFilePath:
            return HttpResponse()

        image_data = None
        try:
            image_data = open(imageFilePath, "rb").read()
        except:
            pass

        # return image_data

        return HttpResponse(image_data)


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