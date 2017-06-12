#!/usr/bin/env python
# -*- coding: gb2312 -*-

import msvcrt
import sys
import TradeX

print "\t*******************************************************************"
print "\t*                        TradeX.dll v1.3.0                        *"
print "\t*                                                                 *"
print "\t*  TradeX.dll ��Ʊ���򻯽��׽ӿ�ȫ�·�����                        *"
print "\t*                                                                 *"
print "\t*  �汾������                                                     *"
print "\t*  1��֧����ͨ�˻���������ȯ�����˻�ҵ�񣬰����µ�����������ѯ��  *"
print "\t*  ������ȯ��ҵ��                                               *"
print "\t*  2�������������µ��Ͷ��˻�ͬʱ�µ���ÿ�������µ��ɴ����ٵ���    *"
print "\t*  3��֧�ֹ�Ʊ�嵵��Level 2ʮ��ʵʱ�����Լ��ڻ�����չ���飬��     *"
print "\t*  ��ͬʱ����������ȡ���飻                                       *"
print "\t*  4��ֱ�����׷����������������������ת����ȫ���ȶ���ʵ�������У�*"
print "\t*  5��ȫ��C++��C#��Python��Delphi��Java�������Ե����Խӿڣ�       *"
print "\t*  6����������trade.dll�����׽����̩���������������⡣           *"
print "\t*                                                                 *"
print "\t*  ����QQȺ��318139137  QQ��3048747297                            *"
print "\t*  ������ҳ��https://tradexdll.com/                               *"
print "\t*  http://pan.baidu.com/s/1jIjYq1K                                *"
print "\t*                                                                 *"
print "\t*******************************************************************"

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t1����ʼ��...\n"
TradeX.OpenTdx()

#
#
#
print "\t2����¼���׷�����...\n"

# ���׷���������
sHost = "mock.tdx.com.cn"
nPort = 7708
sVersion = "6.40"
sBranchID = 9000
sAccountNo = "net828@163.com"
sTradeAccountNo = "001001001005792"
sPassword = "123123"
sTxPassword = ""

try:
	client = TradeX.Logon(sHost, nPort, sVersion, sBranchID, sAccountNo, sTradeAccountNo, sPassword, sTxPassword)
except TradeX.error, e:
	print "error: " + e.message
	sys.exit(-1)

print "\n\t�ɹ���¼\n"

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t3����ѯ�ʽ�...\n"

nCategory = 0

status, content = client.QueryData(nCategory)
if status < 0:
    print "error: " + content
else:
	print content

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t4����ѯ�ɷ�...\n"

nCategory = 1

status, content = client.QueryData(nCategory)
if status < 0:
    print "error: " + content
else:
	print content

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t5����ѯ�ɽ��׹�Ʊ����...\n"

nCategory = 0
nPriceType = 0
sAccount = ""
sStockCode = "000002"
fPrice = 3.11

status, content = client.GetTradableQuantity(nCategory, nPriceType, sAccount, sStockCode, fPrice)
if status < 0:
    print "error: " + content
else:
	print content

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t6��һ���¹��깺...\n"

status = client.QuickIPO()
if status < 0:
    print "error: " + str(status)
else:
	print "ok: " + str(status)

#
#
#
print "\t7���¹��깺��ϸ...\n"

status, content = client.QuickIPODetail()
if status < 0:
    print "error: " + content
elif status == 0:
	print content
else:
	for elem in content:
		errinfo, result = elem
		if errinfo != "":
			print errinfo
		else:
			print result

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t8��ί��...\n"

status, content = client.SendOrder(0, 4, "p001001001005793", "601988", 0, 100)
if status < 0:
    print "error: " + content
else:
	print content

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t9������ί��...\n"

status, content = client.SendOrders(((0, 0, "p001001001005793", "601988", 3.11, 100), (0, 0, "p001001001005793", "601988", 3.11, 200)))
if status < 0:
	print content
else:
	for elem in content:
		errinfo, result = elem
		if errinfo != "":
			print errinfo
		else:
			print result

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t10����ѯ�嵵����...\n"

status, content = client.GetQuotes(('000001', '600600'))
if status < 0:
	print content
else:
	for elem in content:
		errinfo, result = elem
		if errinfo != "":
			print errinfo
		else:
			print result

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t11����ѯ�ʽ𡢳ֲ�...\n"

Category = (0, 1, 3)

status, content = client.QueryDatas(Category)
if status < 0:
	print content
else:
	for elem in content:
		errinfo, result = elem
		if errinfo != "":
			print errinfo
		else:
			print result

print "\n\t�����������...\n"
msvcrt.getch()

#
#
#
print "\t12���رշ���������...\n"

del client
TradeX.CloseTdx()

#
#
#
print "\t��������˳�...\n"

msvcrt.getch()

