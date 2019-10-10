#--encoding:utf-8--
import wx
from script import mainprogram
from script import regin
from threading import Thread
from script import chater
import sys
import pymysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user="muwenlong", passwd="12345678", db="login", charset="utf8")
cus1 = conn.cursor()
sql = 'select passwd from users where name=%s'
def framE():
    app = wx.App()
    frame = wx.Frame(parent=None,title='Login',size=(432,320))
    panel = wx.Panel(frame,-1)
    STATIC=wx.StaticText(panel,-1,label="高级程序设计应用系统",pos=(120,20))
    font=wx.Font(15,wx.ROMAN,wx.NORMAL,wx.BOLD)
    STATIC.SetFont(font)
    #添加静态标签
    label_user = wx.StaticText(panel,-1,"账号:", pos=(80,80))
    label_pass = wx.StaticText(panel,-1,"密码:", pos=(80,120))
    #添加文本输入框
    global entry_pass
    global entry_user
    entry_user = wx.TextCtrl(panel,-1,size=(200,30), pos=(130,80))
    #style 为设置输入
    entry_pass = wx.TextCtrl(panel,-1, size=(200,30), pos=(130,120), style=wx.TE_PASSWORD)
    #添加按钮
    but_login = wx.Button(panel,-1,"登录", size=(120,50), pos=(170,200))
    but_login_1 = wx.Button(panel, -1, "新用户注册", size=(80, 30), pos=(330, 250))

    #设置按钮的颜色
    but_login.SetBackgroundColour("#0a74f7")
    but_login_1.SetBackgroundColour("white")
    but_login_1.Bind(wx.EVT_BUTTON,re)
        #给按钮绑定事件
    but_login.Bind(wx.EVT_BUTTON,on_but_login)

    frame.Center()
    frame.Show(True)

    app.MainLoop()
        #定义一个消息弹出框的函数
def re(event):
    regin.frame()


def show_message(word="",caption=""):
    dlg = wx.MessageDialog(None, word, caption, wx.YES_NO | wx.ICON_INFORMATION)
    if dlg.ShowModal() == wx.ID_YES:
            #self.Close(True)
        pass
    dlg.Destroy()
def on_but_login(event):
        #
    user_name = str(entry_user.GetValue())
    res = [user_name]
    pass_word= str(entry_pass.GetValue())
    pwd=pass_word
    cus1 = conn.cursor()
    cus1.execute(sql, res)
    psw = cus1.fetchall()
    if psw == ():
        show_message(word='用户不存在', caption='错误')
    elif psw[0][0] == pwd:
        mainprogram.program()
    else:
        show_message(word='密码错误', caption='错误')

def main():
    tr=Thread(target=framE)
    fr=Thread(target=chater.recive)
    tr.start()
    fr.start()


if __name__=="__main__":
    main()





