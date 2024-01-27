#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import GUI_Tools_wxpython_gui
import subprocess
from setting import java8_path
from setting import java9_path
from setting import java11_path
from setting import python_path

class MianWindow(GUI_Tools_wxpython_gui.jar_management_gui):

    # WebShell管理工具
    def godzilla_click(self, event):
        subprocess.Popen("cd gui_webshell/Godzilla && " + java8_path + ' -jar ' + 'Godzilla.jar', shell=True)

    def behinder_click(self, event):
        subprocess.Popen("cd gui_webshell/Behinder && " + java8_path + ' -jar ' + 'Behinder.jar', shell=True)

    def BehinderMode_click(self, event):
        subprocess.Popen("cd gui_webshell/Behinder-Mode && " + java8_path + ' -jar ' + 'Behinder-Mode.jar', shell=True)

    # def antSword_click(self, event):
    # 	  subprocess.Popen('cd gui_webshell/AntSword/AntSword/AntSword-Loader-v4.0.3-win32-x64 && AntSword.exe', shell=True)

    def tianxie_click(self, event):
    	  subprocess.Popen("cd gui_webshell/TianXie && " + java8_path + ' -jar ' + '天蝎权限管理工具.jar', shell=True)
          
    def alien_click(self, event):
    	  subprocess.Popen("cd gui_webshell/alien && WebShell.exe", shell=True)


    # 渗透测试工具
    def burp_suite_click(self, event):
        subprocess.Popen("cd gui_other/burpsuite_pro && BurpSuiteLoader.bat", shell=True)

    def cs_click(self, event):
        subprocess.Popen("cd gui_other/Cobalt_Strike_4.7 && cobaltstrike.bat",shell=True)

    def xray_click(self, event):
        subprocess.Popen('cd gui_other/xray && super-xray-1.7-system-jre.exe', shell=True)

    def ladon_click(self, event):
        subprocess.Popen('cd gui_other/ladon && LadonGUI.exe', shell=True)

    def gorailgun_click(self, event):
        subprocess.Popen('cd gui_other/gorailgun && gorailgun-normal-1.5.5.exe', shell=True)

    def serein_click(self, event):
        subprocess.Popen('cd gui_other/kscan && start.bat', shell=True)

    def aniya_click(self, event):
        subprocess.Popen('cd gui_other/aniya && AniYa.bat', shell=True)

    def yanri_click(self, event):
        subprocess.Popen('cd gui_other/yanri && yanri.bat', shell=True)

    def ruoji_click(self, event):
        subprocess.Popen('cd gui_other/ruoji && webshell_bypass_5.bat', shell=True)

    def goon3_click(self, event):
        subprocess.Popen('cd gui_shouji/goon && goon.bat', shell=True)

    def afrog_click(self, event):
        subprocess.Popen('cd gui_other/afrog && afrog.bat', shell=True)

    def auxtools_click(self, event):
        subprocess.Popen('cd gui_other/auxtools && Auxtools.exe', shell=True)
        
    def counter_click(self, event):
        subprocess.Popen('cd gui_other/Counter-Strike && cs.vbs', shell=True)
        
    def xshelltools_click(self, event):
        subprocess.Popen('cd gui_other/XshellTools && XlshellTools网络安全库加载器.exe', shell=True)
        
    def tiquan1_click(self, event):
        subprocess.Popen('cd gui_other/tiquan && start.bat', shell=True)
        
    




    # 信息收集工具
    def xueying_click(self, event):
        subprocess.Popen('cd gui_shouji/leiying/SnowShadow_v1.0 && SnowShadow.bat', shell=True)

    def webfinder_click(self, event):
        subprocess.Popen("cd gui_shouji && " + java9_path + ' -jar ' + 'webfinder-next.jar', shell=True)

    def fofa_click(self, event):
        subprocess.Popen("cd gui_shouji/fofaviewer/ && " + java11_path  +' -jar ' + 'fofaviewer.jar', shell=True)

    def yj_click(self, event):
        subprocess.Popen('cd gui_shouji/yjdirscanv1.1 && 御剑2.exe', shell=True)

    def subdomain_click(self, event):
        subprocess.Popen('cd gui_shouji/oneforall && start.bat', shell=True)

    def tide_click(self, event):
        subprocess.Popen('cd gui_shouji/tide && start.bat', shell=True)

    def enscan_click(self, event):
        subprocess.Popen('cd gui_other/enscan && enscan.bat', shell=True)
        
    def bjx11_click(self, event):
        subprocess.Popen('cd gui_shouji/bjx11 && bjx.exe', shell=True)

    # 漏洞扫描工具
    def oaexp_click(self, event):
        subprocess.Popen('cd gui_scan/OAexp && weekoa.exe', shell=True)

    def gr33k_click(self, event):
        subprocess.Popen('cd gui_scan/Gr33k && Gr33k.exe', shell=True)

    def webtc_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'WebBatchRequest.jar', shell=True)

    def ruoyi_click(self, event):
        subprocess.Popen("cd gui_scan/Ruoyi-All-master && " + java8_path + ' -jar ' + 'ruoyiVuln.jar', shell=True)

    def f4_click1(self, event):
        subprocess.Popen("cd gui_scan/thinkphp && " + java8_path + ' -jar ' + 'ThinkPHP.jar', shell=True)

    def f4a_click(self, event):
        subprocess.Popen("cd gui_scan/thinkphp && " + java8_path + ' -jar ' + 'ThinkphpGUI.jar', shell=True)

    def f4b_click(self, event):
        subprocess.Popen(
            "cd gui_scan/weblogic && " + java8_path + ' -jar ' + 'WeblogicTool_1.3.jar', shell=True)

    def javafan_click(self, event):
        subprocess.Popen("cd gui_scan/weblogic && " + java8_path + ' -jar ' + 'Java反序列化终极测试工具.jar',
                         shell=True)

    def Log4j_click(self, event):
        subprocess.Popen("cd gui_scan/Log4j && " + java8_path + ' -jar ' + 'woodpecker-framework.1.3.5.jar',
                         shell=True)

    def f4_attack_click(self, event):
        subprocess.Popen("cd gui_scan/shiro/shiro_attack_2.2 && " + java8_path + ' -jar ' + 'Spring_All_Reachable-2.1.jar',
                         shell=True)

    def f4_attack2_click(self, event):
        subprocess.Popen("cd gui_scan/shiro/shiro_attack2 && " + java8_path + ' -jar ' + 'shiro_attack-4.7.0-SNAPSHOT-all.jar',
                         shell=True)

    def oracleshell_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'oracleShell.jar', shell=True)

    def framescan_click(self, event):
        subprocess.Popen("cd gui_scan/FrameScan-GUI && FrameScan-GUI.exe", shell=True)

    def fastjson_cilck(self, event):
        subprocess.Popen("cd gui_scan/json && start.bat", shell=True)

    def cve_2020_10199_click(self, event):
        subprocess.Popen("cd gui_scan/nuclei && " + java11_path + ' -jar ' + 'nuclei-7.1.3.jar', shell=True)

    def cve_2019_7238_click(self, event):
        subprocess.Popen('cd gui_scan/redis-rogue-server && redis.exe', shell=True)

    def aliyun_accesskey_click(self, event):
        subprocess.Popen('cd gui_scan && 阿里Key命令执行Tools.exe', shell=True)

    def jdgui_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'jd-gui-1.6.6.jar', shell=True)

    def mdut_click(self, event):
        subprocess.Popen(
            "cd gui_scan/Multiple.Database.Utilization.Tools && " + java8_path + ' -jar ' + 'Multiple.Database.Utilization.Tools-2.1.1-jar-with-dependencies.jar',
            shell=True)

    def Liqunkit_click(self, event):
        subprocess.Popen(
            "cd gui_scan/LiqunKit_1.5.1 && " + java8_path + ' -jar ' + 'LiqunKit_1.6.2_交流版.jar', shell=True)

    def eaySvn_click(self, event):
        subprocess.Popen('cd gui_scan && Seay-Svn源代码泄露漏洞利用工具.exe', shell=True)
        
    def tool0x7e_click(self, event):
        subprocess.Popen(
            "cd gui_scan/0x7eteamtools && " + java8_path + ' -jar ' + '0x7e.jar', shell=True)
            
    def tscanplus_click(self, event):
        subprocess.Popen('cd gui_scan/tscanplus && TscanPlus.exe', shell=True)
        
    def ez_click(self, event):
        subprocess.Popen('cd gui_scan/ez && start.bat', shell=True)

    def poc2_click(self, event):
        subprocess.Popen("cd gui_scan/poc2jar-WINDOWS && " + java8_path + ' -jar ' + 'poc2jar.jar', shell=True)

    def fcke_click(self, event):
        subprocess.Popen('cd gui_scan/fcke && start.bat', shell=True)

    def vulmap_click(self, event):
        subprocess.Popen('cd gui_scan/vulmap && start.bat', shell=True)

    def heartsk_click(self, event):
        subprocess.Popen('cd gui_scan/heartsk && HeartsK.bat', shell=True)

    def webbao_click(self, event):
        subprocess.Popen('cd gui_scan/WebCrack-master && newaksk.exe', shell=True)

    def xsstrike_click(self, event):
        subprocess.Popen('cd gui_scan/xscan && start.bat', shell=True)

    def RequestTemplate_click(self, event):
        subprocess.Popen('cd gui_scan/RequestTemplate && RequestTemplate.bat', shell=True)

    def quasar_click(self, event):
        subprocess.Popen('cd gui_other/quasar && Quasar_zh-CHS.exe', shell=True)

    def bx4_click(self, event):
        subprocess.Popen("cd gui_webshell/Behinder4 && " + java11_path + ' -jar ' + 'Behinder.jar', shell=True)

    def MYExploit_click(self, event):
        subprocess.Popen("cd gui_scan && " + java8_path + ' -jar ' + 'MYExploit.jar', shell=True)

    def md5_click(self, event):
        subprocess.Popen('cd gui_scan/md5 && MD5.bat', shell=True)

    def goby_click(self, event):
        subprocess.Popen('cd gui_scan/goby/goby-win-x64-2.0.5 && Goby.exe', shell=True)

    def oajiance_click(self, event):
        subprocess.Popen("cd gui_scan/oatools && start.bat", shell=True)
    #struts2漏洞工具

    def f4_chek_click(self, event):
        subprocess.Popen("cd gui_scan/struts2 && " + java8_path + ' -jar ' + 'hyacinth.jar', shell=True)

    def f4_chek1_click(self, event):
        subprocess.Popen("cd gui_scan/struts2 && " + java8_path + ' -jar ' + 'struts2_19.jar', shell=True)
        
    def postgre_click(self, event):
        subprocess.Popen("cd gui_scan/postgre && " + java8_path + ' -jar ' + 'postgreUtil-1.0-SNAPSHOT-jar-with-dependencies.jar', shell=True)

    def SpringBootExploit_click(self, event):
        subprocess.Popen('cd gui_scan/spring && start.bat', shell=True)

    def xunyun_click(self, event):
        subprocess.Popen(
            'cd gui_scan/hvvoaexploit &&  start.bat',
            shell=True)

    def blue_click(self, event):
        subprocess.Popen('cd gui_other/blue && start.bat', shell=True)

    def winlog_click(self, event):
        subprocess.Popen('cd gui_other/fiddler && Fiddler.exe', shell=True)
        
    def proxifire_click(self, event):
        subprocess.Popen('cd gui_other/proxifire && Proxifier.exe', shell=True)

    def inscana_click(self, event):
        subprocess.Popen('cd gui_shouji/golin && start.bat', shell=True)
        
    def sitescan_click(self, event):
        subprocess.Popen('cd gui_shouji/sitescan && start.bat', shell=True)

    def dogcs_click(self, event):
        subprocess.Popen("cd gui_other/dogcs_v2.1 && " + java11_path + ' -jar ' + 'dogcs.jar', shell=True)
        
    def xgmiansha_click(self, event):
        subprocess.Popen("cd gui_other/ && " + java11_path + ' -jar ' + 'XG_NTAI.jar', shell=True)
        
    def hengxiang_click(self, event):
        subprocess.Popen("cd gui_other/hengxiang && " + java8_path + ' -jar ' + 'gogogo-jar-with-dependencies.jar', shell=True)
        
    def owaspzap_click(self, event):
        subprocess.Popen("cd gui_other/owaspzap && " + java11_path + ' -jar ' + 'zap-2.14.0.jar', shell=True)
        
    def day2023_click(self, event):
        subprocess.Popen('cd gui_scan/day2023 && start.bat', shell=True)
        
    def adyu_click(self, event):
        subprocess.Popen('cd gui_other/adyu && start.bat', shell=True)
        
    def vcenterKit_click(self, event):
        subprocess.Popen('cd gui_other/vcenterKit && start.bat', shell=True)
        
    def dddd_click(self, event):
        subprocess.Popen('cd gui_scan/dddd && start.bat', shell=True)

    def wbsc_click(self, event):
        subprocess.Popen("cd gui_other/webshellsc && " + java8_path + ' -jar ' + 'Webshell_Generate-1.2.3.jar',
                         shell=True)

    def fvuln_click(self, event):
        subprocess.Popen('cd gui_scan/fvuln && start.bat', shell=True)

    def fscan_click(self, event):
        subprocess.Popen('cd gui_scan/fscan && start.bat', shell=True)

    def appinfo_click(self, event):
        subprocess.Popen("cd gui_scan/appinfo && start.bat", shell=True)

    def webpack_click(self, event):
        subprocess.Popen("cd gui_scan/webpackscan && start.bat", shell=True)

    def dirsearch_click(self, event):
        subprocess.Popen("cd gui_scan/dirsearch && start.bat", shell=True)

    def jmjm_click(self, event):
        subprocess.Popen("cd gui_scan/jiamijiemi && BE-BerylEnigma.exe", shell=True)

    def rjscan_click(self, event):
        subprocess.Popen("cd gui_other/ruojiscan && start.bat", shell=True)

    def yakit_click(self, event):
        subprocess.Popen("cd gui_other/yakit && Yakit.exe", shell=True)

    def zhetian_click(self, event):
        subprocess.Popen("cd gui_other/zhetian && Dude.exe", shell=True)

    def sqlmap_click(self, event):
        subprocess.Popen("cd gui_scan/sqlmap && start.bat", shell=True)

    def supersql_click(self, event):
        subprocess.Popen("cd gui_scan/supersql && SuperSQLInjection.exe", shell=True)

    def tiquan_click(self, event):
        subprocess.Popen("cd gui_scan/tq && start.bat", shell=True)

    def apttools_click(self, event):
        subprocess.Popen("cd gui_scan/apt && " + java8_path + ' -jar ' + 'apt_tools-jar-with-dependencies.jar', shell=True)

    def f4_jboss_click(self, event):
        subprocess.Popen("cd gui_scan/jboss && " + java8_path + ' -jar ' + 'JavaJboss.jar', shell=True)

    def f4_jndi_click(self, event):
        subprocess.Popen("cd gui_scan/jndi && start.bat", shell=True)

    def aksk_click(self, event):
        subprocess.Popen("cd gui_scan/aksk && start.bat", shell=True)

    def cf_click(self, event):
        subprocess.Popen("cd gui_scan/cf && start.bat", shell=True)

    def ehole_click(self, event):
        subprocess.Popen("cd gui_scan/ehole && start.bat", shell=True)
        
    def f4_headdump_click(self, event):
        subprocess.Popen("cd gui_scan/headdump && start.bat", shell=True)
        
    def Woodpecker_click(self, event):
        subprocess.Popen("cd gui_other/Woodpecker && " + java8_path + ' -jar ' + 'woodpecker-framework.1.3.5.jar', shell=True)
        
    def SwordHost_click(self, event):
        subprocess.Popen("cd gui_other/SwordHost && " + java8_path + ' -jar ' + 'SwordHost.jar', shell=True)

    # def aaa_click(self, event):
    #     subprocess.Popen("cd gui_other/SwordHost && " + java8_path + ' -jar ' + 'SwordHost.jar', shell=True)
        
    # def bbb_click(self, event):
    #     subprocess.Popen("cd gui_other/SwordHost && " + java8_path + ' -jar ' + 'SwordHost.jar', shell=True)
        
    # def ccc(self, event):
    #     subprocess.Popen("cd gui_other/SwordHost && " + java8_path + ' -jar ' + 'SwordHost.jar', shell=True)
    
    # def ddd(self, event):
    #     subprocess.Popen("cd gui_other/SwordHost && " + java8_path + ' -jar ' + 'SwordHost.jar', shell=True)
    
if __name__ == '__main__':
    app = wx.App()
    frame = MianWindow(None)
    frame.Show()
    app.MainLoop()
    

