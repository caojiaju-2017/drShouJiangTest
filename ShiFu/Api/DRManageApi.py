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

class DRManageApi(object):
    @staticmethod
    @csrf_exempt
    def CommandDispatch(req):
        # print "api invoke1"
        command = req.GET.get('Command').upper()
        # print "api invoke2"
        # return HttpResponse("ok")
        if command == 'Org_Login'.upper():
            return DRManageApi.Org_Login(req)
        elif command  == "Staff_Login".upper():
            return DRManageApi.Staff_Login(req)
        elif command  == "Add_Config".upper():
            return DRManageApi.Add_Config(req)
        elif command == "View_Image".upper():
            return DRManageApi.View_Image(req)
        elif command == "Dele_Config".upper():
            return DRManageApi.Dele_Config(req)
        elif command == "Add_Ticket".upper():
            return DRManageApi.Add_Ticket(req)
        elif command == "Get_Emplyees".upper():
            return DRManageApi.Get_Emplyees(req)
        elif command == "Add_Emplyee".upper():
            return DRManageApi.Add_Emplyee(req)
        elif command == "Dele_Emplyee".upper():
            return DRManageApi.Dele_Emplyee(req)
        elif command == "Modi_Emplyee".upper():
            return DRManageApi.Modi_Emplyee(req)
        elif command == "Add_Product".upper():
            return DRManageApi.Add_Product(req)
        elif command == "Modi_Product".upper():
            return DRManageApi.Modi_QXProduct(req)
        elif command == "Dele_Product".upper():
            return DRManageApi.Dele_QXProduct(req)
        # elif command == "Add_WXProduct".upper():
        #     return DRManageApi.Add_WXProduct(req)
        # elif command == "Modi_WXProduct".upper():
        #     return DRManageApi.Modi_WXProduct(req)
        # elif command == "Dele_WXProduct".upper():
        #     return DRManageApi.Dele_WXProduct(req)
        elif command == "Get_Orgs".upper():
            return DRManageApi.Get_Orgs(req)
        elif command == "Add_Org".upper():
            return DRManageApi.Add_Org(req)
        elif command == "Modi_Org".upper():
            return DRManageApi.Modi_Org(req)
        elif command == "Dele_Org".upper():
            return DRManageApi.Dele_Org(req)


    # Access-Control-Allow-Origi
    @staticmethod
    def Dele_Org(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)


        try:
            Code = postDataList["Code".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        org = SjSrvOrg.objects.filter(code=Code).first()

        if not org:
            loginResut = json.dumps({"ErrorInfo": "产品数据不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        org.state = 0
        commitDataList = []
        commitDataList.append(CommitData(org, 0))

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
    def Modi_Org(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Code = postDataList["Code".lower()]
            Address = postDataList["Address".lower()]
            Phone = postDataList["Phone".lower()]
            Pswd = postDataList["Pswd".lower()]
            City = postDataList["City"]
            Longite =int(postDataList["Longite".lower()])
            Langite = int(postDataList["Langite".lower()])
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        orgHandle = SjSrvOrg.objects.filter(code = Code).first()

        if not orgHandle:
            loginResut = json.dumps({"ErrorInfo": "服务商不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        orgHandle.address = Address
        orgHandle.phone = Phone
        orgHandle.pswd = Pswd
        orgHandle.city = City
        orgHandle.longite = Longite
        orgHandle.langite = Langite

        commitDataList = []
        commitDataList.append(CommitData(orgHandle, 0))

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
    def Add_Org(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Address = postDataList["Address".lower()]
            Phone = postDataList["Phone".lower()]
            Pswd = postDataList["Pswd".lower()]
            City = postDataList["City".lower()]
            Name = postDataList["Name".lower()]
        except Exception ,ex:
            print postDataList
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        # 不強制要求
        Longite = int(postDataList["Longite".lower()])
        Langite = int(postDataList["Langite".lower()])

        # 服务商注册检查
        existOrg  = SjSrvOrg.objects.filter(phone=Phone,state=1).first()

        if existOrg:
            loginResut = json.dumps({"ErrorInfo": "该服务商注册过账号，请更换手机号码", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        print  postDataList
        newOrg = SjSrvOrg()
        newOrg.code = uuid.uuid1().__str__().replace("-", "")
        newOrg.address = Address
        newOrg.phone = Phone
        newOrg.pswd = Pswd
        newOrg.city = City
        newOrg.longite = Longite
        newOrg.langite = Langite
        newOrg.state = 1
        newOrg.name = Name

        commitDataList = []
        commitDataList.append(CommitData(newOrg, 0))

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
    def Get_Orgs(request):
        # 提取post数据
        try:
            pageIndex = int(request.GET.get('PageIndex'.lower()))
            pageSize = int(request.GET.get('PageSize'.lower()))
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)
        orgUsers = SjSrvOrg.objects.filter(~Q(code= 'admin')).filter(state=1)

        rtnDict={}
        rtnResult = []
        for index, one in enumerate(orgUsers):
            if index < pageIndex*pageSize:
                continue
            if index >= (pageIndex * pageSize + pageSize):
                break

            oneRecord = {}
            oneRecord["code"] = one.code
            oneRecord['address'] = one.address
            oneRecord['phone'] = one.phone
            oneRecord['longite'] = one.longite
            oneRecord['langite'] = one.langite
            oneRecord['city'] = one.city
            oneRecord['name'] = one.name

            rtnResult.append(oneRecord)
        rtnDict["MaxCount"] = len(orgUsers)
        rtnDict["Datas"] = rtnResult

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnDict})
        return HttpResponse(loginResut)
    @staticmethod
    def Dele_WXProduct(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Code = postDataList["Code".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        product = SjServices.objects.filter(code=Code).first()

        if not product:
            loginResut = json.dumps({"ErrorInfo": "产品数据不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        commitDataList = []
        commitDataList.append(CommitData(product, 1))

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
    def Modi_WXProduct(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Code = postDataList["Code".lower()]
            Name = postDataList["Name".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        product = SjServices.objects.filter(code = Code).first()

        if not product:
            loginResut = json.dumps({"ErrorInfo": "产品数据不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        product.name = Name

        commitDataList = []
        commitDataList.append(CommitData(product, 0))

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
    def Add_WXProduct(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Name = postDataList["Name".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        newService = SjWxServices()
        newService.code = uuid.uuid1().__str__().replace("-", "")
        newService.name = Name

        commitDataList = []
        commitDataList.append(CommitData(newService, 0))

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
    def Dele_QXProduct(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Code = postDataList["Code".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        product = SjServices.objects.filter(code=Code)

        if not product:
            loginResut = json.dumps({"ErrorInfo": "产品数据不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        product.state = 0

        commitDataList = []
        commitDataList.append(CommitData(product, 0))

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
    def Modi_QXProduct(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Code = postDataList["Code".lower()]
            Name = postDataList["Name".lower()]
            ImgName = postDataList["ImgName".lower()]
            City = postDataList["City".lower()]
            Price = float(postDataList["Price".lower()])
            OrigPrice = float(postDataList["OrigPrice".lower()])
            State = int(postDataList["State".lower()])
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        product = SjServices.objects.filter(code = Code)

        if not product:
            loginResut = json.dumps({"ErrorInfo": "产品数据不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        product.code = uuid.uuid1().__str__().replace("-", "")
        product.name = Name
        product.imgname = ImgName
        product.city = City
        product.price = Price
        product.origprice = OrigPrice
        product.state = State

        commitDataList = []
        commitDataList.append(CommitData(product, 0))

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
    def Add_Product(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)
        print postDataList
        Image1 = None
        Image2 = None
        Image3 = None
        DetailImage = None

        try:
            Image1 = base64.b64decode(postDataList['Image1'.lower()])
        except:
            pass

        try:
            Image2 = base64.b64decode(postDataList['Image2'.lower()])
        except:
            pass

        try:
            Image3 = base64.b64decode(postDataList['Image3'.lower()])
        except:
            pass


        try:
            DetailImage = base64.b64decode(postDataList['DetailImage'.lower()])
        except:
            pass


        try:
            Name = postDataList["Name".lower()]
            Price = float(postDataList["Price".lower()])

            try:
                OrigPrice = float(postDataList["OrigPrice".lower()])
            except:
                OrigPrice = -1

            Info = postDataList["Info".lower()]
            ServiceTime = postDataList["ServiceTime".lower()]
            ServiceType = int(postDataList["ServiceType".lower()])
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        newService = SjServices()
        newService.code = uuid.uuid1().__str__().replace("-", "")
        newService.name = Name
        newService.price = Price
        newService.origprice = OrigPrice
        newService.state = 1
        newService.info = Info
        newService.servicetime = ServiceTime
        newService.servicetype = ServiceType
        newService.viewcount = 0
        newService.bookcount = 0

        # 处理图片
        if Image1:
            img1Code = uuid.uuid1().__str__().replace("-", "")
            try:
                file = open(os.path.join(os.path.join(STATIC_ROOT,"ProductImage"),'%s.jpg'% img1Code), 'wb')
                file.write(Image1)
                file.close()
                newService.imgname1 = img1Code + ".jpg";
            except:
                pass
        if Image2:
            img2Code = uuid.uuid1().__str__().replace("-", "")
            try:
                file = open(os.path.join(os.path.join(STATIC_ROOT,"ProductImage"),'%s.jpg'% img2Code), 'wb')
                file.write(Image2)
                file.close()
                newService.imgname2 = img2Code + ".jpg";
            except:
                pass
        if Image3:
            img3Code = uuid.uuid1().__str__().replace("-", "")
            try:
                file = open(os.path.join(os.path.join(STATIC_ROOT,"ProductImage"),'%s.jpg'% img3Code), 'wb')
                file.write(Image3)
                file.close()
                newService.imgname3 = img3Code + ".jpg";
            except:
                pass

        if DetailImage:
            DetailImageCode = uuid.uuid1().__str__().replace("-", "")
            try:
                file = open(os.path.join(os.path.join(STATIC_ROOT,"ProductImage"),'%s.jpg'% DetailImageCode), 'wb')
                file.write(Image3)
                file.close()
                newService.detailimage = DetailImageCode + ".jpg";
            except:
                pass



        commitDataList = []
        commitDataList.append(CommitData(newService, 0))

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
    def Modi_Emplyee(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Code = postDataList["Code".lower()]
            OCode = postDataList["OCode".lower()]
            Phone = postDataList["Phone".lower()]
            Name = postDataList["Name".lower()]
            Password = postDataList["Password".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        emplyee = SjEmplyees.objects.filter(ocode=OCode, code=Code).first()

        if not emplyee:
            loginResut = json.dumps({"ErrorInfo": "员工数据不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        emplyee.phone = Phone
        emplyee.name = Name
        emplyee.pswd = Password

        commitDataList = []
        commitDataList.append(CommitData(emplyee, 0))

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
    def Dele_Emplyee(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            OCode = postDataList["ocode".lower()]
            ECode = postDataList["ecode".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        emplyee = SjEmplyees.objects.filter(ocode = OCode,code = ECode).first()

        if not emplyee:
            loginResut = json.dumps({"ErrorInfo": "员工数据不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        emplyee.state = 0
        commitDataList = []
        commitDataList.append(CommitData(emplyee, 0))

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
    def Add_Emplyee(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            Code = postDataList["code".lower()]
            Phone = postDataList["phone".lower()]
            Name = postDataList["name".lower()]
            Password = postDataList["password".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        newEmplyee = SjEmplyees()
        newEmplyee.ocode = Code
        newEmplyee.phone = Phone
        newEmplyee.name = Name
        newEmplyee.pswd = Password
        newEmplyee.state = 1
        newEmplyee.code = uuid.uuid1().__str__().replace("-", "")

        commitDataList = []
        commitDataList.append(CommitData(newEmplyee, 0))

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
    def Get_Emplyees(request):
        # 提取post数据

        try:
            Code = request.GET.get('code'.lower())
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        emplyees = SjEmplyees.objects.filter(ocode=Code,state = 1)

        rtnResult = []
        for index, one in enumerate(emplyees):
            oneRecord = {}
            oneRecord["code"] = one.code
            oneRecord['name'] = one.name
            oneRecord['phone'] = one.phone
            oneRecord['state'] = one.state
            oneRecord['ocode'] = one.ocode

            rtnResult.append(oneRecord)

        print rtnResult
        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": rtnResult})
        return HttpResponse(loginResut)

    @staticmethod
    def Add_Ticket(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            OCode = postDataList["ocode".lower()]
            Price = float(postDataList["price".lower()])
            CCode = postDataList["ccode".lower()]
            EndDate = postDataList["enddate".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        newTicket = SjTickets()
        newTicket.ocode = OCode
        newTicket.price = Price
        newTicket.ccode = CCode
        newTicket.enddate = EndDate

        commitDataList = []
        commitDataList.append(CommitData(newTicket, 0))

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
    def Dele_Config(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            CKey = postDataList["ckey".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        updateCfg = SjConfig.objects.filter(ckey=CKey).first()

        if not updateCfg:
            loginResut = json.dumps({"ErrorInfo": "配置型不存在", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)


        commitDataList = []
        commitDataList.append(CommitData(updateCfg, 1))

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
    def Add_Config(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            CKey = postDataList["ckey".lower()]
            CValue = float(postDataList["cvalue".lower()])
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        updateCfg = SjConfig.objects.filter(ckey=CKey).first()

        if not updateCfg:
            updateCfg = SjConfig()

        updateCfg.ckey = CKey
        updateCfg.cvalue = CValue


        commitDataList = []
        commitDataList.append(CommitData(updateCfg, 0))

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

        print postDataList
        try:
            userCode = postDataList["Phone".lower()]
            Password = postDataList["Password".lower()]
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)

        empUser = SjEmplyees.objects.filter(phone = userCode,state= 1).first()


        if not empUser:
            loginResut = json.dumps({"ErrorInfo": "您的账号不存在", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        # 检查员工归属服务商是否被删除
        orgData = SjSrvOrg.objects.filter(code = empUser.ocode,state = 1).first()

        if not orgData:
            loginResut = json.dumps({"ErrorInfo": "你的服务商已下线，你不可以操作", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        if Password != empUser.pswd:
            loginResut = json.dumps({"ErrorInfo": "账号或密码错误", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": empUser.code})
        return HttpResponse(loginResut)

    @staticmethod
    def Org_Login(request):
        # 提取post数据
        postDataList = {}
        postDataList = getPostData(request)

        try:
            userCode = postDataList["phone".lower()].encode('utf-8')
            Password = postDataList["password".lower()].encode('utf-8')
        except:
            loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
            return HttpResponse(loginResut)


        try:
            Type = int(postDataList["type".lower()])
        except:
            Type = -1

        srvUser = SjSrvOrg.objects.filter(phone = userCode,state = 1).first()

        if (Type == -1 and userCode != "admin") or not srvUser:
            loginResut = json.dumps({"ErrorInfo": "您的账号不存在", "ErrorId": 10001, "Result": ""})
            return HttpResponse(loginResut)

        if Password != srvUser.pswd or srvUser.state == 0:
            loginResut = json.dumps({"ErrorInfo": "账号异常或密码错误", "ErrorId": 10002, "Result": ""})
            return HttpResponse(loginResut)

        loginResut = json.dumps({"ErrorInfo": "操作成功", "ErrorId": 200, "Result": srvUser.code})
        return HttpResponse(loginResut)

    # @staticmethod
    # def View_Image(request):
    #     try:
    #         imagename = request.GET.get('imagename')
    #         type = int(request.GET.get('type'))
    #     except:
    #         loginResut = json.dumps({"ErrorInfo": "参数错误", "ErrorId": 20001, "Result": None})
    #         return HttpResponse(loginResut)
    #     #
    #     imageFilePath = None
    #
    #     imageFilePath = os.path.join(os.path.join(STATIC_ROOT,"ProductImage"), "%s" % imagename)
    #
    #     image_data = None
    #     try:
    #         image_data = open(imageFilePath, "rb").read()
    #     except:
    #         pass
    #
    #     # return image_data
    #
    #     return HttpResponse(image_data)


def getPostData(request):
    postDataList = {}
    if request.method == 'POST':
        for key in request.POST:
            try:
                postDataList[key.lower()] = request.POST.getlist(key)[0]
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