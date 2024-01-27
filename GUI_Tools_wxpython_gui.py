#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx  
import messagebox  
import wx.xrc

###########################################################################
## Class jar_management_gui
###########################################################################


class MsgWindow:
    pass



class jar_management_gui(wx.Frame):
    
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY,
                      title=u"GUI_TOOLS_Py7h0n_Win",
                      pos=wx.DefaultPosition,
                      size=wx.Size(1352, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetWindowStyle(wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        # self.SetTransparent(500)  # 设置透明
        self.SetBackgroundColour(wx.Colour('#FFFFFF'))
        self.SetForegroundColour('#228B22')

        self.icon1 = wx.Icon(name="py74on.ico", type=wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon1)  # 图标

        gui_all = wx.BoxSizer(wx.VERTICAL)


        # 创建一个水平方向的Sizer来包含标题和图标
        title_and_icon_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # 添加一个空白的占位符，以使标题和图标居中
        title_and_icon_sizer.AddStretchSpacer()

        # 创建一个静态文本控件来显示标题
        title_label = wx.StaticText(self, wx.ID_ANY, u"GUI_TOOLS_Win_by_Py74on")

        # 添加标题文本到水平Sizer中
        title_and_icon_sizer.Add(title_label, 0, wx.ALIGN_CENTER)

        # 添加一个空白的占位符，以使标题和图标居中
        title_and_icon_sizer.AddStretchSpacer()

        # 添加图标到水平Sizer中
        title_and_icon_sizer.Add(wx.StaticBitmap(self, wx.ID_ANY, self.icon1), 0, wx.ALIGN_CENTER)

        # 添加标题和图标的水平Sizer到垂直Sizer中
        gui_all.Add(title_and_icon_sizer, 0, wx.EXPAND | wx.ALL, 5)

        # 设置主窗口的Sizer
        self.SetSizer(gui_all)


         
          

        gui_webshell = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"--------------------------------------------------------------------------------------------------------------------WebShell管理工具------------------------------------------------------------------------------------------------------------------------------"), wx.VERTICAL)

        webshell = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.godzilla = wx.Button(gui_webshell.GetStaticBox(), wx.ID_ANY, u"哥斯拉_v4.0.1", wx.DefaultPosition,
                                  size=(210, 23))
        self.godzilla.SetForegroundColour((0, 0, 0, 0))   #按钮前景颜色
        self.godzilla.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        #self.godzilla.SetToolTip(wx.ToolTip("Click this button to do something")) 
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.godzilla.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        webshell.Add(self.godzilla, 0, wx.ALL, 4)

        self.behinder = wx.Button(gui_webshell.GetStaticBox(), wx.ID_ANY, u"冰蝎_v3.0_Beta_11", wx.DefaultPosition,
                                  size=(210, 23))
        self.behinder.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.behinder.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        

        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.behinder.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        webshell.Add(self.behinder, 0, wx.ALL, 4)

        self.bx4 = wx.Button(gui_webshell.GetStaticBox(), wx.ID_ANY, u"冰蝎_v4.1", wx.DefaultPosition,
                             size=(210, 23))
        self.bx4.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.bx4.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.bx4.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        webshell.Add(self.bx4, 0, wx.ALL, 4)

        self.BehinderMode = wx.Button(gui_webshell.GetStaticBox(), wx.ID_ANY, u"冰蝎魔改_v3.3.2", wx.DefaultPosition,
                                      size=(210, 23))
        self.BehinderMode.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.BehinderMode.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.BehinderMode.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        webshell.Add(self.BehinderMode, 0, wx.ALL, 4)

        # self.antSword = wx.Button(gui_webshell.GetStaticBox(), wx.ID_ANY, u"中国蚁剑_v2.1.15", wx.DefaultPosition,
        #                           size=(210, 23))
        # self.antSword.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        # self.antSword.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        # c = wx.Cursor(wx.Image('pointer.png'))
        # # SET c AS CURSOR
        # self.antSword.SetCursor(c)
        # self.Centre()
        # #按钮获取焦点后鼠标变换为图片的样子
        
        # webshell.Add(self.antSword, 0, wx.ALL, 4)

        self.tianxie = wx.Button(gui_webshell.GetStaticBox(), wx.ID_ANY, u"天蝎权限管理工具_v1.0", wx.DefaultPosition,
                                 size=(210, 23))
        self.tianxie.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.tianxie.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.tianxie.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        webshell.Add(self.tianxie, 0, wx.ALL, 4)
        
        self.alien = wx.Button(gui_webshell.GetStaticBox(), wx.ID_ANY, u"Alien权限管理工具_v4.0", wx.DefaultPosition,
                                 size=(210, 23))
        self.alien.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.alien.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.alien.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        webshell.Add(self.alien, 0, wx.ALL, 4)

        gui_webshell.Add(webshell, 1, wx.EXPAND, 4)

        gui_all.Add(gui_webshell, 0, wx.EXPAND | wx.ALL, 4)

        gui_other = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"-----------------------------------------------------------------------------------------------------------------------渗透利器工具---------------------------------------------------------------------------------------------------------------------------------"), wx.VERTICAL)

        other = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.burp_suite = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"BurpSuite_Pro_2023.5.1",
                                    wx.DefaultPosition, size=(210, 23))
        self.burp_suite.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.burp_suite.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.burp_suite.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.burp_suite, 0, wx.ALL, 4)
        
        self.zhetian = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"DudeSuite", wx.DefaultPosition,
                                 size=(210, 23))
        self.zhetian.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.zhetian.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.zhetian.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.zhetian, 0, wx.ALL, 4)

        self.cs = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"CobaltStrike_4.7美化破解版",
                            wx.DefaultPosition,
                            size=(210, 23))
        self.cs.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.cs.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.cs.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.cs, 0, wx.ALL, 4)

        self.dogcs = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"DogCS_v2.1", wx.DefaultPosition,
                               size=(210, 23))
        self.dogcs.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.dogcs.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.dogcs.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.dogcs, 0, wx.ALL, 4)
        
        self.counter = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Counter-Strike1.6", wx.DefaultPosition,
                               size=(210, 23))
        self.counter.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.counter.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.counter.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.counter, 0, wx.ALL, 4)

        self.yakit = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"YAKIT", wx.DefaultPosition,
                               size=(210, 23))
        self.yakit.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.yakit.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.yakit.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.yakit, 0, wx.ALL, 4)

        self.xray = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"XRAY图形化版工具", wx.DefaultPosition,
                              size=(210, 23))
        self.xray.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.xray.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.xray.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.xray, 0, wx.ALL, 4)

        self.goby = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Goby_v2.4.7_1400+Poc版本", wx.DefaultPosition,
                              size=(210, 23))
        self.goby.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.goby.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.goby.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.goby, 0, wx.ALL, 4)
        
        self.owaspzap = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"OWASP-ZAP_2.14", wx.DefaultPosition,
                              size=(210, 23))
        self.owaspzap.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.owaspzap.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.owaspzap.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.owaspzap, 0, wx.ALL, 4)

        self.fscan = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Fscan_v1.8.3", wx.DefaultPosition,
                               size=(210, 23))
        self.fscan.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.fscan.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.fscan.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.fscan, 0, wx.ALL, 4)
        
        self.dddd = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"DDDD扫描探测工具_1.3", wx.DefaultPosition,
                               size=(210, 23))
        self.dddd.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.dddd.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.dddd.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.dddd, 0, wx.ALL, 4)

        self.tiquan = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"winPEASany提权工具", wx.DefaultPosition,
                                size=(210, 23))
        self.tiquan.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.tiquan.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.tiquan.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.tiquan, 0, wx.ALL, 4)

        self.sqlmap = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"SQLMAP", wx.DefaultPosition,
                                size=(210, 23))
        self.sqlmap.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.sqlmap.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.sqlmap.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.sqlmap, 0, wx.ALL, 4)

        self.supersql = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"超级SQL注入工具", wx.DefaultPosition,
                                  size=(210, 23))
        self.supersql.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.supersql.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.supersql.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.supersql, 0, wx.ALL, 4)

        self.ladon = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Ladon_GUI 12", wx.DefaultPosition,
                               size=(210, 23))
        self.ladon.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.ladon.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.ladon.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.ladon, 0, wx.ALL, 4)

        self.gorailgun = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Railgun-1.5.5", wx.DefaultPosition,
                                   size=(210, 23))
        self.gorailgun.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.gorailgun.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.gorailgun.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.gorailgun, 0, wx.ALL, 4)

        self.serein = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Kscan-1.85稳定版", wx.DefaultPosition,
                                size=(210, 23))
        self.serein.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.serein.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.serein.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.serein, 0, wx.ALL, 4)

        self.heartsk = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"棱镜X单兵作战系统",
                                 wx.DefaultPosition,
                                 size=(210, 23))
        self.heartsk.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.heartsk.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.heartsk.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.heartsk, 0, wx.ALL, 4)

        self.quasar = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Quasar最新内部成员汉化版远控_v1.4",
                                wx.DefaultPosition,
                                size=(210, 23))
        self.quasar.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.quasar.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.quasar.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.quasar, 0, wx.ALL, 4)

        self.aniya = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"AniYa-GUI免杀框架_v1.2", wx.DefaultPosition,
                               size=(210, 23))
        self.aniya.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.aniya.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.aniya.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.aniya, 0, wx.ALL, 4)

        self.yanri = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"掩日红队免杀工具_v20231208", wx.DefaultPosition,
                               size=(210, 23))
        self.yanri.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.yanri.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.yanri.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.yanri, 0, wx.ALL, 4)

        self.wbsc = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Webshell生成器_v1.2.3", wx.DefaultPosition,
                              size=(210, 23))
        self.wbsc.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.wbsc.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.wbsc.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.wbsc, 0, wx.ALL, 4)

        self.ruoji = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"弱鸡webshell免杀工具_v5.1", wx.DefaultPosition,
                               size=(210, 23))
        self.ruoji.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.ruoji.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.ruoji.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.ruoji, 0, wx.ALL, 4)
        
        self.xgmiansha = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"XG拟态WEB免杀工具_2.0", wx.DefaultPosition,
                               size=(210, 23))
        self.xgmiansha.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.xgmiansha.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.xgmiansha.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.xgmiansha, 0, wx.ALL, 4)

        self.goon3 = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"goon扫描探测爆破工具集_v3.6", wx.DefaultPosition,
                               size=(210, 23))
        self.goon3.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.goon3.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.goon3.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.goon3, 0, wx.ALL, 4)

        self.afrog = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"afrog可定制化漏洞扫描工具_v2.9.6",
                               wx.DefaultPosition,
                               size=(210, 23))
        self.afrog.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.afrog.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.afrog.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.afrog, 0, wx.ALL, 4)

        self.fvuln = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"fvuln自动化探测工具", wx.DefaultPosition,
                               size=(210, 23))
        self.fvuln.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.fvuln.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.fvuln.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.fvuln, 0, wx.ALL, 4)

        self.blue = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"蓝队分析辅助工具箱_v0.89", wx.DefaultPosition,
                              size=(210, 23))
        self.blue.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.blue.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.blue.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.blue, 0, wx.ALL, 4)

        self.winlog = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Fiddler代理工具汉化版", wx.DefaultPosition,
                                size=(210, 23))
        self.winlog.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.winlog.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.winlog.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.winlog, 0, wx.ALL, 4)
        
        self.proxifire = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"proxifire代理工具汉化版", wx.DefaultPosition,
                                size=(210, 23))
        self.proxifire.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.proxifire.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.proxifire.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.proxifire, 0, wx.ALL, 4)

        self.auxtools = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"AuxTools_V4.2", wx.DefaultPosition,
                                  size=(210, 23))
        self.auxtools.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.auxtools.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.auxtools.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.auxtools, 0, wx.ALL, 4)
        
        self.xshelltools = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"XshellTools工具库", wx.DefaultPosition,
                                  size=(210, 23))
        self.xshelltools.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.xshelltools.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.xshelltools.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.xshelltools, 0, wx.ALL, 4)
        
        
        
        self.tiquan1 = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Linux一键维权探测工具", wx.DefaultPosition,
                                  size=(210, 23))
        self.tiquan1.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.tiquan1.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.tiquan1.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.tiquan1, 0, wx.ALL, 4)
        
        self.hengxiang = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"内网横向移动利用工具", wx.DefaultPosition,
                                  size=(210, 23))
        self.hengxiang.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.hengxiang.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.hengxiang.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.hengxiang, 0, wx.ALL, 4)
        
        self.adyu = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"AD域自动化评估工具", wx.DefaultPosition,
                                  size=(210, 23))
        self.adyu.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.adyu.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.adyu.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.adyu, 0, wx.ALL, 4)
        
        self.vcenterKit = wx.Button(gui_other.GetStaticBox(), wx.ID_ANY, u"Vcenter综合渗透利用工具包", wx.DefaultPosition,
                                  size=(210, 23))
        self.vcenterKit.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.vcenterKit.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.vcenterKit.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        other.Add(self.vcenterKit, 0, wx.ALL, 4)




        gui_other.Add(other, 1, wx.EXPAND, 4)

        gui_all.Add(gui_other, 0, wx.EXPAND | wx.ALL, 4)

        gui_shouji = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"-----------------------------------------------------------------------------------------------------------------------信息探测工具---------------------------------------------------------------------------------------------------------------------------------"), wx.VERTICAL)

        shouji = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.xueying = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"雪影信息收集工具_v1.0", wx.DefaultPosition,
                                 size=(210, 23))
        self.xueying.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.xueying.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.xueying.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.xueying, 0, wx.ALL, 4)

        self.webfinder = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"WebFinder_修改版", wx.DefaultPosition,
                                   size=(210, 23))
        self.webfinder.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.webfinder.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.webfinder.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.webfinder, 0, wx.ALL, 4)

        self.fofa = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"Fofa_Viewer_v1.1.13", wx.DefaultPosition,
                              size=(210, 23))
        self.fofa.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.fofa.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.fofa.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.fofa, 0, wx.ALL, 4)
        
        self.sitescan = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"SiteScan探测工具", wx.DefaultPosition,
                                 size=(210, 23))
        self.sitescan.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.sitescan.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.sitescan.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.sitescan, 0, wx.ALL, 4)

        self.enscan = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"ENScan_V0.0.15", wx.DefaultPosition,
                                size=(210, 23))
        self.enscan.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.enscan.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.enscan.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.enscan, 0, wx.ALL, 4)

        self.yjdirscan = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"御剑2珍藏版", wx.DefaultPosition,
                                   size=(210, 23))
        self.yjdirscan.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.yjdirscan.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.yjdirscan.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.yjdirscan, 0, wx.ALL, 4)

        self.webtc = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"WEB存活批量探测&批量跑POC工具",
                               wx.DefaultPosition,
                               size=(210, 23))
        self.webtc.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.webtc.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.webtc.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.webtc, 0, wx.ALL, 4)

        self.subdomain = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"OneForAll子域名探测工具", wx.DefaultPosition,
                                   size=(210, 23))
        self.subdomain.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.subdomain.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.subdomain.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.subdomain, 0, wx.ALL, 4)

        self.tide = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"Tide指纹探测工具", wx.DefaultPosition,
                              size=(210, 23))
        self.tide.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.tide.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.tide.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.tide, 0, wx.ALL, 4)

        self.webpack = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"webpack敏感信息探测工具", wx.DefaultPosition,
                                 size=(210, 23))
        self.webpack.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.webpack.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.webpack.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.webpack, 0, wx.ALL, 4)

        self.dirsearch = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"DirSearch目录探测工具", wx.DefaultPosition,
                                 size=(210, 23))
        self.dirsearch.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.dirsearch.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.dirsearch.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.dirsearch, 0, wx.ALL, 4)

        self.appinfo = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"APP信息收集探测工具", wx.DefaultPosition,
                                 size=(210, 23))
        self.appinfo.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.appinfo.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.appinfo.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.appinfo, 0, wx.ALL, 4)
        
        self.bjx11 = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"北极熊扫描器_4.5", wx.DefaultPosition,
                                 size=(210, 23))
        self.bjx11.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.bjx11.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.bjx11.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.bjx11, 0, wx.ALL, 4)

        self.inscana = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"GOlin_1.2.5", wx.DefaultPosition,
                                 size=(210, 23))
        self.inscana.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.inscana.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.inscana.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        shouji.Add(self.inscana, 0, wx.ALL, 4)
        
        #aaa
        self.aaa = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"此处待安置", wx.DefaultPosition,
                                 size=(210, 23))
        self.aaa.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.aaa.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.aaa.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        shouji.Add(self.aaa, 0, wx.ALL, 4)
        #aaa
        
        #aaa
        self.bbb = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"此处待安置", wx.DefaultPosition,
                                 size=(210, 23))
        self.bbb.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.bbb.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.bbb.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        shouji.Add(self.bbb, 0, wx.ALL, 4)
        #aaa
        
        #aaa
        self.ccc = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"此处待安置", wx.DefaultPosition,
                                 size=(210, 23))
        self.ccc.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.ccc.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.ccc.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        shouji.Add(self.ccc, 0, wx.ALL, 4)
        #aaa
        
        #aaa
        self.ddd = wx.Button(gui_shouji.GetStaticBox(), wx.ID_ANY, u"此处待安置", wx.DefaultPosition,
                                 size=(210, 23))
        self.ddd.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.ddd.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.ddd.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        shouji.Add(self.ddd, 0, wx.ALL, 4)
        #aaa


        gui_shouji.Add(shouji, 1, wx.EXPAND, 4)

        gui_all.Add(gui_shouji, 0, wx.EXPAND | wx.ALL, 4)

        gui_scan = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"------------------------------------------------------------------------------------------------------------------综合漏洞探测利用工具----------------------------------------------------------------------------------------------------------------------------"), wx.VERTICAL)

        scan = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.oaexp = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"OA漏洞检测工具V2.0", wx.DefaultPosition,
                               size=(210, 23))
        self.oaexp.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.oaexp.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.oaexp.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.oaexp, 0, wx.ALL, 4)

        self.xunyun = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"OA-Tools-1.2.3",
                                wx.DefaultPosition,
                                size=(210, 23))
        self.xunyun.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.xunyun.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.xunyun.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.xunyun, 0, wx.ALL, 4)

        self.Gr33k = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Gr33k漏洞利用工具集_Win", wx.DefaultPosition,
                               size=(210, 23))
        self.Gr33k.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.Gr33k.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.Gr33k.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.Gr33k, 0, wx.ALL, 4)

        self.rjscan = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"弱鸡漏探工具_内测版", wx.DefaultPosition,
                                size=(210, 23))
        self.rjscan.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.rjscan.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.rjscan.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.rjscan, 0, wx.ALL, 4)
        
        self.day2023 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"0Day检测工具2023版", wx.DefaultPosition,
                                  size=(210, 23))
        self.day2023.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.day2023.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.day2023.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.day2023, 0, wx.ALL, 4)

        self.ruoyi = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"若依漏洞检测利用工具", wx.DefaultPosition,
                               size=(210, 23))
        self.ruoyi.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.ruoyi.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.ruoyi.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.ruoyi, 0, wx.ALL, 4)

        self.Log4j = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"woodpecker", wx.DefaultPosition,
                               size=(210, 23))
        self.Log4j.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.Log4j.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.Log4j.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.Log4j, 0, wx.ALL, 4)

        self.oracleShell = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"OracleShell_v0.1", wx.DefaultPosition,
                                     size=(210, 23))
        self.oracleShell.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.oracleShell.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.oracleShell.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.oracleShell, 0, wx.ALL, 4)
        
        self.postgre = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Postgresql一键利用工具", wx.DefaultPosition,
                                     size=(210, 23))
        self.postgre.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.postgre.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.postgre.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.postgre, 0, wx.ALL, 4)

        self.FrameScan = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"FrameScan_GUI_Win_v1.4.3", wx.DefaultPosition,
                                   size=(210, 23))
        self.FrameScan.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.FrameScan.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.FrameScan.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.FrameScan, 0, wx.ALL, 4)

        self.fastjson = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"FastJson检测利用工具", wx.DefaultPosition,
                                  size=(210, 23))
        self.fastjson.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.fastjson.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.fastjson.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.fastjson, 0, wx.ALL, 4)

        self.CVE_2020_10199 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"nuclei漏洞扫描器GUI版",
                                        wx.DefaultPosition,
                                        size=(210, 23))
        self.CVE_2020_10199.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.CVE_2020_10199.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.CVE_2020_10199.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.CVE_2020_10199, 0, wx.ALL, 4)

        self.CVE_2019_7238 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Redis-tools", wx.DefaultPosition,
                                       size=(210, 23))
        self.CVE_2019_7238.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.CVE_2019_7238.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.CVE_2019_7238.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.CVE_2019_7238, 0, wx.ALL, 4)

        self.aliyun_accesskey = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"阿里Key命令执行Tools",
                                          wx.DefaultPosition, size=(210, 23))
        self.aliyun_accesskey.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.aliyun_accesskey.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.aliyun_accesskey.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.aliyun_accesskey, 0, wx.ALL, 4)

        self.mdut = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"MDUT_v2.1.1", wx.DefaultPosition, size=(210, 23))
        self.mdut.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.mdut.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.mdut.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.mdut, 0, wx.ALL, 4)

        self.Liqunkit = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Liqun工具箱1.6.2交流版", wx.DefaultPosition,
                                  size=(210, 23))
        self.Liqunkit.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.Liqunkit.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.Liqunkit.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.Liqunkit, 0, wx.ALL, 4)

        self.poc2 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"poc2jar_V0.66", wx.DefaultPosition,
                              size=(210, 23))
        self.poc2.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.poc2.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.poc2.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.poc2, 0, wx.ALL, 4)

        self.SpringBootExploit = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"SpringBoot-Scan-GUI",
                                           wx.DefaultPosition,
                                           size=(210, 23))
        self.SpringBootExploit.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.SpringBootExploit.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.SpringBootExploit.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.SpringBootExploit, 0, wx.ALL, 4)

        self.fcke = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Httpx辅助工具", wx.DefaultPosition,
                              size=(210, 23))
        self.fcke.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.fcke.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.fcke.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.fcke, 0, wx.ALL, 4)

        self.vulmap = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"vulmap_v0.9", wx.DefaultPosition,
                                size=(210, 23))
        self.vulmap.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.vulmap.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.vulmap.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.vulmap, 0, wx.ALL, 4)

        self.xsstrike = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Xscan_1.9.4", wx.DefaultPosition,
                                  size=(210, 23))
        self.xsstrike.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.xsstrike.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.xsstrike.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.xsstrike, 0, wx.ALL, 4)

        self.RequestTemplate = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"RequestTemplate【KCON专版】",
                                         wx.DefaultPosition,
                                         size=(210, 23))
        self.RequestTemplate.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.RequestTemplate.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.RequestTemplate.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.RequestTemplate, 0, wx.ALL, 4)

        self.MYExploit = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"MYExploit_v2.0.4",
                                   wx.DefaultPosition,
                                   size=(210, 23))
        self.MYExploit.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.MYExploit.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.MYExploit.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.MYExploit, 0, wx.ALL, 4)

        self.jmjm = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"加密解密小工具(非MD5版)", wx.DefaultPosition,
                              size=(210, 23))
        self.jmjm.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.jmjm.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.jmjm.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.jmjm, 0, wx.ALL, 4)

        self.md5 = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"杂项加密解密小工具(MD5版)", wx.DefaultPosition,
                             size=(210, 23))
        self.md5.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.md5.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.md5.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.md5, 0, wx.ALL, 4)

        self.oajiance = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"OA—EXPTOOLS", wx.DefaultPosition,
                                  size=(210, 23))
        self.oajiance.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.oajiance.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.oajiance.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.oajiance, 0, wx.ALL, 4)

        self.apttools = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"APT_Tools", wx.DefaultPosition,
                                  size=(210, 23))
        self.apttools.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.apttools.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.apttools.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.apttools, 0, wx.ALL, 4)
        
        self.webbao = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"AK_SK利用工具New",
                                wx.DefaultPosition,
                                size=(210, 23))
        self.webbao.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.webbao.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.webbao.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.webbao, 0, wx.ALL, 4)

        self.aksk = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"AK_SK利用工具", wx.DefaultPosition,
                              size=(210, 23))
        self.aksk.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.aksk.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.aksk.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.aksk, 0, wx.ALL, 4)

        self.cf = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"AK_SK后cf利用工具", wx.DefaultPosition,
                              size=(210, 23))
        self.cf.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.cf.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.cf.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.cf, 0, wx.ALL, 4)

        self.ehole = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Ehole指纹识别工具魔改版", wx.DefaultPosition,
                            size=(210, 23))
        self.ehole.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.ehole.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.ehole.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.ehole, 0, wx.ALL, 4)

        self.eaySvn = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"Seay-Svn源代码泄露漏洞", wx.DefaultPosition,
                                size=(210, 23))
        self.eaySvn.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.eaySvn.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.eaySvn.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.eaySvn, 0, wx.ALL, 4)
        
        
        self.tscanplus = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"TscanPlus", wx.DefaultPosition,
                                size=(210, 23))
        self.tscanplus.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.tscanplus.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.tscanplus.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.tscanplus, 0, wx.ALL, 4)
        
        
        self.ez = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"EZ扫描检测工具", wx.DefaultPosition,
                                size=(210, 23))
        self.ez.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.ez.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.ez.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.ez, 0, wx.ALL, 4)
        
        self.tool0x7e = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"0x7eTeamTools", wx.DefaultPosition,
                                size=(210, 23))
        self.tool0x7e.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.tool0x7e.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.tool0x7e.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.tool0x7e, 0, wx.ALL, 4)
        
        self.SwordHost = wx.Button(gui_scan.GetStaticBox(), wx.ID_ANY, u"SwordHost", wx.DefaultPosition,
                                size=(210, 23))
        self.SwordHost.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.SwordHost.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.SwordHost.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        scan.Add(self.SwordHost, 0, wx.ALL, 4)

        gui_scan.Add(scan, 1, wx.EXPAND, 4)

        gui_all.Add(gui_scan, 0, wx.EXPAND | wx.ALL, 4)

        # f4漏洞利用工具
        gui_f4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"---------------------------------------------------------------------------------------------------------------------框架漏洞利用工具------------------------------------------------------------------------------------------------------------------------------"), wx.VERTICAL)

        f4 = wx.WrapSizer(wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS)

        self.f4_attack = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"Spring漏洞综合利用工具", wx.DefaultPosition,
                                   size=(210, 23))
        self.f4_attack.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4_attack.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4_attack.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4_attack, 0, wx.ALL, 4)
        
        self.f4_headdump = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"headdump解密工具", wx.DefaultPosition,
                                    size=(210, 23))
        self.f4_headdump.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4_headdump.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4_headdump.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4_headdump, 0, wx.ALL, 4)

        self.f4_attack2 = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"shiro_attack-4.7.0", wx.DefaultPosition,
                                    size=(210, 23))
        self.f4_attack2.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4_attack2.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4_attack2.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4_attack2, 0, wx.ALL, 4)

        self.f4 = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"thinkphp综合利用_V2.4.2_by蓝鲸",
                            wx.DefaultPosition,
                            size=(210, 23))
        self.f4.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4, 0, wx.ALL, 4)

        self.f4a = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"Thinkphp漏洞利用工具",
                             wx.DefaultPosition,
                             size=(210, 23))
        self.f4a.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4a.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4a.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4a, 0, wx.ALL, 4)

        self.f4b = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"WeblogicTool_1.3",
                                      wx.DefaultPosition, size=(210, 23))
        self.f4b.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4b.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4b.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4b, 0, wx.ALL, 4)

        self.javafan = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"Java反序列化终极测试工具 by 6哥",
                                 wx.DefaultPosition,
                                 size=(210, 23))
        self.javafan.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.javafan.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.javafan.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.javafan, 0, wx.ALL, 4)

        self.f4_chek = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"JAVA框架漏洞探测工具",
                                 wx.DefaultPosition, size=(210, 23))
        self.f4_chek.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4_chek.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4_chek.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4_chek, 0, wx.ALL, 4)

        self.f4_chek1 = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"struts2_全版本漏洞检测工具_19.02",
                                  wx.DefaultPosition, size=(210, 23))
        self.f4_chek1.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4_chek1.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4_chek1.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4_chek1, 0, wx.ALL, 4)

        self.f4_jboss = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"JBoss漏洞检测利用工具",
                                  wx.DefaultPosition, size=(210, 23))
        self.f4_jboss.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4_jboss.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4_jboss.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4_jboss, 0, wx.ALL, 4)

        self.f4_jndi = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"JNDI利用工具",
                                  wx.DefaultPosition, size=(210, 23))
        self.f4_jndi.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4_jndi.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4_jndi.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4_jndi, 0, wx.ALL, 4)
        
        self.f4_Woodpecker = wx.Button(gui_f4.GetStaticBox(), wx.ID_ANY, u"Woodpecker",
                                  wx.DefaultPosition, size=(210, 23))
        self.f4_Woodpecker.SetForegroundColour((0, 0, 0, 0 ))   #按钮前景颜色
        self.f4_Woodpecker.SetBackgroundColour((255, 255, 255, 255))  #按钮背景颜色
        
        c = wx.Cursor(wx.Image('pointer.png'))
        # SET c AS CURSOR
        self.f4_Woodpecker.SetCursor(c)
        self.Centre()
        #按钮获取焦点后鼠标变换为图片的样子
        
        f4.Add(self.f4_Woodpecker, 0, wx.ALL, 4)
        

        gui_f4.Add(f4, 1, wx.EXPAND, 4)

        gui_all.Add(gui_f4, 0, wx.EXPAND | wx.ALL, 4)

        self.SetSizer(gui_all)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.godzilla.Bind(wx.EVT_BUTTON, self.godzilla_click)
        self.behinder.Bind(wx.EVT_BUTTON, self.behinder_click)
        self.BehinderMode.Bind(wx.EVT_BUTTON, self.BehinderMode_click)
        # self.antSword.Bind(wx.EVT_BUTTON, self.antSword_click)
        self.tianxie.Bind(wx.EVT_BUTTON, self.tianxie_click)
        self.burp_suite.Bind(wx.EVT_BUTTON, self.burp_suite_click)
        self.cs.Bind(wx.EVT_BUTTON, self.cs_click)
        self.xray.Bind(wx.EVT_BUTTON, self.xray_click)
        self.ladon.Bind(wx.EVT_BUTTON, self.ladon_click)
        self.gorailgun.Bind(wx.EVT_BUTTON, self.gorailgun_click)
        self.webfinder.Bind(wx.EVT_BUTTON, self.webfinder_click)
        self.fofa.Bind(wx.EVT_BUTTON, self.fofa_click)
        self.yjdirscan.Bind(wx.EVT_BUTTON, self.yj_click)
        self.oaexp.Bind(wx.EVT_BUTTON, self.oaexp_click)
        self.Gr33k.Bind(wx.EVT_BUTTON, self.gr33k_click)
        self.ruoyi.Bind(wx.EVT_BUTTON, self.ruoyi_click)
        self.f4.Bind(wx.EVT_BUTTON, self.f4_click1)
        self.f4a.Bind(wx.EVT_BUTTON, self.f4a_click)
        self.f4b.Bind(wx.EVT_BUTTON, self.f4b_click)
        self.javafan.Bind(wx.EVT_BUTTON, self.javafan_click)
        self.f4_attack.Bind(wx.EVT_BUTTON, self.f4_attack_click)
        self.f4_attack2.Bind(wx.EVT_BUTTON, self.f4_attack2_click)
        self.f4_chek.Bind(wx.EVT_BUTTON, self.f4_chek_click)
        self.f4_chek1.Bind(wx.EVT_BUTTON, self.f4_chek1_click)
        self.oracleShell.Bind(wx.EVT_BUTTON, self.oracleshell_click)
        self.FrameScan.Bind(wx.EVT_BUTTON, self.framescan_click)
        self.fastjson.Bind(wx.EVT_BUTTON, self.fastjson_cilck)
        self.CVE_2020_10199.Bind(wx.EVT_BUTTON, self.cve_2020_10199_click)
        self.CVE_2019_7238.Bind(wx.EVT_BUTTON, self.cve_2019_7238_click)
        self.aliyun_accesskey.Bind(wx.EVT_BUTTON, self.aliyun_accesskey_click)
        self.mdut.Bind(wx.EVT_BUTTON, self.mdut_click)
        self.Liqunkit.Bind(wx.EVT_BUTTON, self.Liqunkit_click)
        self.eaySvn.Bind(wx.EVT_BUTTON, self.eaySvn_click)
        self.Log4j.Bind(wx.EVT_BUTTON, self.Log4j_click)
        self.poc2.Bind(wx.EVT_BUTTON, self.poc2_click)
        self.SpringBootExploit.Bind(wx.EVT_BUTTON, self.SpringBootExploit_click)
        self.fcke.Bind(wx.EVT_BUTTON, self.fcke_click)
        self.heartsk.Bind(wx.EVT_BUTTON, self.heartsk_click)
        self.webbao.Bind(wx.EVT_BUTTON, self.webbao_click)
        self.xsstrike.Bind(wx.EVT_BUTTON, self.xsstrike_click)
        self.RequestTemplate.Bind(wx.EVT_BUTTON, self.RequestTemplate_click)
        self.md5.Bind(wx.EVT_BUTTON, self.md5_click)
        self.xunyun.Bind(wx.EVT_BUTTON, self.xunyun_click)
        self.yanri.Bind(wx.EVT_BUTTON, self.yanri_click)
        self.ruoji.Bind(wx.EVT_BUTTON, self.ruoji_click)
        self.goon3.Bind(wx.EVT_BUTTON, self.goon3_click)
        self.afrog.Bind(wx.EVT_BUTTON, self.afrog_click)
        self.aniya.Bind(wx.EVT_BUTTON, self.aniya_click)
        self.MYExploit.Bind(wx.EVT_BUTTON, self.MYExploit_click)
        self.quasar.Bind(wx.EVT_BUTTON, self.quasar_click)
        self.bx4.Bind(wx.EVT_BUTTON, self.bx4_click)
        self.goby.Bind(wx.EVT_BUTTON, self.goby_click)
        self.xueying.Bind(wx.EVT_BUTTON, self.xueying_click)
        self.serein.Bind(wx.EVT_BUTTON, self.serein_click)
        self.subdomain.Bind(wx.EVT_BUTTON, self.subdomain_click)
        self.tide.Bind(wx.EVT_BUTTON, self.tide_click)
        self.webtc.Bind(wx.EVT_BUTTON, self.webtc_click)
        self.oajiance.Bind(wx.EVT_BUTTON, self.oajiance_click)
        self.blue.Bind(wx.EVT_BUTTON, self.blue_click)
        self.winlog.Bind(wx.EVT_BUTTON, self.winlog_click)
        self.inscana.Bind(wx.EVT_BUTTON, self.inscana_click)
        self.dogcs.Bind(wx.EVT_BUTTON, self.dogcs_click)
        self.wbsc.Bind(wx.EVT_BUTTON, self.wbsc_click)
        self.fvuln.Bind(wx.EVT_BUTTON, self.fvuln_click)
        self.auxtools.Bind(wx.EVT_BUTTON, self.auxtools_click)
        self.enscan.Bind(wx.EVT_BUTTON, self.enscan_click)
        self.vulmap.Bind(wx.EVT_BUTTON, self.vulmap_click)
        self.fscan.Bind(wx.EVT_BUTTON, self.fscan_click)
        self.appinfo.Bind(wx.EVT_BUTTON, self.appinfo_click)
        self.webpack.Bind(wx.EVT_BUTTON, self.webpack_click)
        self.jmjm.Bind(wx.EVT_BUTTON, self.jmjm_click)
        self.rjscan.Bind(wx.EVT_BUTTON, self.rjscan_click)
        self.yakit.Bind(wx.EVT_BUTTON, self.yakit_click)
        self.zhetian.Bind(wx.EVT_BUTTON, self.zhetian_click)
        self.sqlmap.Bind(wx.EVT_BUTTON, self.sqlmap_click)
        self.supersql.Bind(wx.EVT_BUTTON, self.supersql_click)
        self.tiquan.Bind(wx.EVT_BUTTON, self.tiquan_click)
        self.apttools.Bind(wx.EVT_BUTTON, self.apttools_click)
        self.f4_jboss.Bind(wx.EVT_BUTTON, self.f4_jboss_click)
        self.aksk.Bind(wx.EVT_BUTTON, self.aksk_click)
        self.cf.Bind(wx.EVT_BUTTON, self.cf_click)
        self.ehole.Bind(wx.EVT_BUTTON, self.ehole_click)
        self.f4_jndi.Bind(wx.EVT_BUTTON, self.f4_jndi_click)
        self.dirsearch.Bind(wx.EVT_BUTTON, self.dirsearch_click)
        self.counter.Bind(wx.EVT_BUTTON, self.counter_click)
        self.xshelltools.Bind(wx.EVT_BUTTON, self.xshelltools_click)
        self.day2023.Bind(wx.EVT_BUTTON, self.day2023_click)
        self.tiquan1.Bind(wx.EVT_BUTTON, self.tiquan1_click)
        self.f4_headdump.Bind(wx.EVT_BUTTON, self.f4_headdump_click)
        self.postgre.Bind(wx.EVT_BUTTON, self.postgre_click)
        self.proxifire.Bind(wx.EVT_BUTTON, self.proxifire_click)
        self.hengxiang.Bind(wx.EVT_BUTTON, self.hengxiang_click)
        self.owaspzap.Bind(wx.EVT_BUTTON, self.owaspzap_click)
        self.dddd.Bind(wx.EVT_BUTTON, self.dddd_click)
        self.sitescan.Bind(wx.EVT_BUTTON, self.sitescan_click)
        self.xgmiansha.Bind(wx.EVT_BUTTON, self.xgmiansha_click)
        self.alien.Bind(wx.EVT_BUTTON, self.alien_click)
        self.adyu.Bind(wx.EVT_BUTTON, self.adyu_click)
        self.vcenterKit.Bind(wx.EVT_BUTTON, self.vcenterKit_click)
        self.bjx11.Bind(wx.EVT_BUTTON, self.bjx11_click)
        self.tool0x7e.Bind(wx.EVT_BUTTON, self.tool0x7e_click)
        self.tscanplus.Bind(wx.EVT_BUTTON, self.tscanplus_click)
        self.ez.Bind(wx.EVT_BUTTON, self.ez_click)
        self.f4_Woodpecker.Bind(wx.EVT_BUTTON, self.Woodpecker_click)
        self.SwordHost.Bind(wx.EVT_BUTTON, self.SwordHost_click)
        # self.aaa.Bind(wx.EVT_BUTTON, self.aaa_click)
        # self.bbb.Bind(wx.EVT_BUTTON, self.bbb_click)
        # self.ccc.Bind(wx.EVT_BUTTON, self.ccc_click)
        # self.ddd.Bind(wx.EVT_BUTTON, self.ddd_click)


    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def godzilla_click(self, event):
        event.Skip()

    def behinder_click(self, event):
        event.Skip()

    def BehinderMode_click(self, event):
        event.Skip()

    # def antSword_click(self, event):
    #     event.Skip()

    def tianxie_click(self, event):
        event.Skip()

    def burp_suite_click(self, event):
        event.Skip()

    def cs_click(self, event):
        event.Skip()

    def xray_click(self, event):
        event.Skip()

    def ladon_click(self, event):
        event.Skip()

    def gorailgun_click(self, event):
        event.Skip()

    def webfinder_click(self, event):
        event.Skip()

    def fofa_click(self, event):
        event.Skip()

    def yj_click(self, event):
        event.Skip()

    def oaexp_click(self, event):
        event.Skip()

    def gr33k_click(self, event):
        event.Skip()

    def ruoyi_click(self, event):
        event.Skip()

    def f4_click1(self, event):
        event.Skip()

    def f4a_click(self, event):
        event.Skip()

    def f4_click(self, event):
        event.Skip()

    def javafan_click(self, event):
        event.Skip()

    def f4_attack_click(self, event):
        event.Skip()

    def f42_click(self, event):
        event.Skip()

    def f4_attack2_click(self, event):
        event.Skip()

    def f4_chek_click(self, event):
        event.Skip()

    def f4_chek1_click(self, event):
        event.Skip()
        
    def f4_headdump_click(self, event):
        event.Skip()

    def oracleshell_click(self, event):
        event.Skip()

    def framescan_click(self, event):
        event.Skip()

    def fastjson_cilck(self, event):
        event.Skip()

    def cve_2020_10199_click(self, event):
        event.Skip()

    def cve_2019_7238_click(self, event):
        event.Skip()

    def aliyun_accesskey_click(self, event):
        event.Skip()

    def aliyunakyools_click(self, event):
        event.Skip()

    def mdut_click(self, event):
        event.Skip()

    def Liqunkit_click(self, event):
        event.Skip()

    def lrxa_click(self, event):
        event.Skip()

    def eaySvn_click(self, event):
        event.Skip()

    def Log4j_click(self, event):
        event.Skip()

    def poc2_click(self, event):
        event.Skip()

    def SpringBootExploit_click(self, event):
        event.Skip()

    def bx4_click(self, event):
        event.Skip()

    def goby_click(self, event):
        event.Skip()

    def serein_click(self, event):
        event.Skip()

    def quasar_click(self, event):
        event.Skip()

    def aniya_click(self, event):
        event.Skip()

    def yanri_click(self, event):
        event.Skip()

    def ruoji_click(self, event):
        event.Skip()

    def goon3_click(self, event):
        event.Skip()

    def afrog_click(self, event):
        event.Skip()

    def xueying_click(self, event):
        event.Skip()

    def subdomain_click(self, event):
        event.Skip()

    def tide_click(self, event):
        event.Skip()

    def xunyun_click(self, event):
        event.Skip()

    def fcke_click(self, event):
        event.Skip()

    def heartsk_click(self, event):
        event.Skip()

    def heartsk_click(self, event):
        event.Skip()

    def webbao_click(self, event):
        event.Skip()

    def xsstrike_click(self, event):
        event.Skip()

    def RequestTemplate_click(self, event):
        event.Skip()

    def MYExploit_click(self, event):
        event.Skip()

    def md5_click(self, event):
        event.Skip()

    def webtc_click(self, event):
        event.Skip()

    def oajiance_click(self, event):
        event.Skip()

    def blue_click(self, event):
        event.Skip()

    def winlog_click(self, event):
        event.Skip()

    def inscana_click(self, event):
        event.Skip()

    def dogcs_click(self, event):
        event.Skip()

    def auxtools_click(self, event):
        event.Skip()

    def enscan_click(self, event):
        event.Skip()

    def vulmap_click(self, event):
        event.Skip()

    def fscan_click(self, event):
        event.Skip()

    def appinfo_click(self, event):
        event.Skip()

    def webpack_click(self, event):
        event.Skip()

    def jmjm_click(self, event):
        event.Skip()

    def rjscan_click(self, event):
        event.Skip()

    def yakit_click(self, event):
        event.Skip()

    def zhetian_click(self, event):
        event.Skip()

    def sqlmap_click(self, event):
        event.Skip()

    def supersql_click(self, event):
        event.Skip()

    def tiquan_click(self, event):
        event.Skip()

    def apttools_click(self, event):
        event.Skip()

    def f4_jboss_click(self, event):
        event.Skip()

    def aksk_click(self, event):
        event.Skip()

    def f4b_click(self, event):
        event.Skip()

    def cf_click(self, event):
        event.Skip()

    def ehole_click(self, event):
        event.Skip()

    def f4_jndi_click(self, event):
        event.Skip()

    def dirsearch_click(self, event):
        event.Skip()
        
    def counter_click(self, event):
        event.Skip()
        
    def xshelltools_click(self, event):
        event.Skip()
        
    def day2023_click(self, event):
        event.Skip()
        
    def tiquan1_click(self, event):
        event.Skip()
        
    def postgre_click(self, event):
        event.Skip()
        
    def proxifire_click(self, event):
        event.Skip()
        
    def hengxiang_click(self, event):
        event.Skip()
        
    def owaspzap(self, event):
        event.Skip()
        
    def dddd(self, event):
        event.Skip()
        
    def sitescan(self, event):
        event.Skip()
        
    def xgmiansha(self, event):
        event.Skip()
    
    def alien(self, event):
        event.Skip()
        
    def adyu(self, event):
        event.Skip()
        
    def vcenterKit(self, event):
        event.Skip()
        
    def bjx11(self, event):
        event.Skip()
        
    def tool0x7e(self, event):
        event.Skip()
        
    def tscanplus(self, event):
        event.Skip()
        
    def ez(self, event):
        event.Skip()
        
    def Woodpecker(self, event):
        event.Skip()
        
    def SwordHost(self, event):
        event.Skip()
        
    def aaa(self, event):
        event.Skip()
        
    def bbb(self, event):
        event.Skip()
        
    def ccc(self, event):
        event.Skip()
        
    def ddd(self, event):
        event.Skip()
  
  
        
    
  
    