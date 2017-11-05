# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class SjConfig(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ckey = models.CharField(db_column='CKey', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    cvalue = models.CharField(db_column='CValue', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_config'


class SjCustomAddress(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='CCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_custom_address'


class SjCustomOrders(models.Model):
    id = models.IntegerField(db_column='ID',  primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    odatetime = models.CharField(db_column='ODateTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='CCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(db_column='Price', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    addrcode = models.CharField(db_column='AddrCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    type = models.IntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    srvcode = models.CharField(db_column='SrvCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ocode = models.CharField(db_column='OCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.CharField(db_column='LastTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ecode = models.CharField(db_column='ECode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_custom_orders'

class SjWeixiuOrders(models.Model):
    id = models.IntegerField(db_column='ID',  primary_key=True)  # Field name made lowercase.
    ocode = models.CharField(db_column='OCode', unique=True, max_length=64, blank=True, null=True)  # Field name made lowercase.
    devtype = models.CharField(db_column='DevType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    setupdate = models.CharField(db_column='SetupDate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    info = models.TextField(db_column='Info', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sj_weixiu_orders'

class SjCustoms(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=32, blank=True, null=True)  # Field name made lowercase.
    lastlogintime = models.CharField(db_column='LastLoginTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_customs'

class SjCitys(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_citys'
class SjEmplyees(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    pswd = models.CharField(db_column='Pswd', max_length=8, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    ocode = models.CharField(db_column='OCode', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_emplyees'


class SjOrderRemark(models.Model):
    id = models.IntegerField(db_column='ID',  primary_key=True)  # Field name made lowercase.
    ocode = models.CharField(db_column='OCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    remarktime = models.CharField(db_column='RemarkTime', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='CCode', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_order_remark'


# class SjOrgEmplyees(models.Model):
#     id = models.IntegerField(db_column='ID',  primary_key=True)  # Field name made lowercase.
#     ocode = models.CharField(db_column='OCode', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
#     ecode = models.CharField(db_column='ECode', max_length=32, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'sj_org_emplyees'


class SjQuestion(models.Model):
    id = models.IntegerField(db_column='ID',  primary_key=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='CCode', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    cqq = models.CharField(db_column='CQQ', max_length=200, blank=True, null=True)  # Field name made lowercase.
    likepart = models.IntegerField(db_column='LikePart', blank=True, null=True)  # Field name made lowercase.
    # models.CharField(db_column='LikePart', max_length=20, blank=True, null=True)  # Field name made lowercase.
    stars = models.IntegerField(db_column='Stars', blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='Info', max_length=200, blank=True, null=True)  # Field name made lowercase.
    committime = models.CharField(db_column='CommitTime', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_question'


class SjQxPack(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(db_column='Price', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    origprice = models.TextField(db_column='OrigPrice', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    qxcodes = models.CharField(db_column='QXCodes', max_length=2000, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_qx_pack'


class SjQxServices(models.Model):
    id = models.IntegerField(db_column='ID',  primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    imgname = models.CharField(db_column='ImgName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=64, blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(db_column='Price', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    origprice = models.TextField(db_column='OrigPrice', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'sj_qx_services'


class SjSrvOrg(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    pswd = models.CharField(db_column='Pswd', max_length=8, blank=True, null=True)  # Field name made lowercase.
    longite = models.TextField(db_column='Longite', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    langite = models.TextField(db_column='Langite', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    city = models.CharField(db_column='City', max_length=8, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'sj_srv_org'


class SjTickets(models.Model):
    id = models.IntegerField(db_column='ID',  primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    ocode = models.CharField(db_column='OCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ccode = models.CharField(db_column='CCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    price = models.TextField(db_column='Price', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    state = models.IntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    extern1 = models.CharField(db_column='Extern1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    extern2 = models.CharField(db_column='Extern2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    extern3 = models.CharField(db_column='Extern3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='EndDate', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_tickets'


class SjWxServices(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', unique=True, max_length=32, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=64, blank=True, null=True)  # Field name made lowercase.
    imgname = models.CharField(db_column='ImgName', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sj_wx_services'
