from bs4 import BeautifulSoup as bs
import openpyxl
import urllib.request
import re

def url(u):
    
    import ssl
    context = ssl._create_unverified_context()
    
    url ='https://yjszs.ecnu.edu.cn/system/sszszyml_list.asp'
    headers= {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'Cache-Control': 'max-age=0', 'Connection': 'keep-alive',
              'Cookie': 'ASPSESSIONIDAARSRDDC=KEIFPHMDJKBGPANCJCFMNBGG',
              'Host': 'yjszs.ecnu.edu.cn',
              'Sec-Fetch-Mode': 'navigate',
              'Sec-Fetch-Site': 'none',
              'Sec-Fetch-User': '?1',
              'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    req = urllib.request.Request(u,headers = headers)
    html = urllib.request.urlopen(req,context = context)
    html = html.read()

    return html


def tr():

    u = 'https://yjszs.ecnu.edu.cn/system/sszszyml_list.asp'

    ur =[]

    html = url(u)

    html = bs(html,'lxml')

    cont = html.findAll('tr',valign="middle")

    for i in cont:

        ii = i.findAll('td',valign="center")[1]

        u = 'https://yjszs.ecnu.edu.cn/system/'+ii.a.attrs['href']

        ur.append([u,i.a.text])

        print(i.a.text)

        print('\n')

    return ur


def excel(shu,name):

    wb = openpyxl.Workbook()

    word = wb.active

    word['A1'] = '序号'
        
    word['B1'] = '招生年份'
        
    word['C1'] = '招生专业'
        
    word['D1'] = '学位类型'
        
    word['E1'] = '招生人数'
        
    word['F1'] = '研究方向'
        
    word['G1'] = '考试科目'
        
    word['H1'] = '备注'

    for x in range(1,len(shu)+1):

        A = 'A{0}'.format(x+1)

        B = 'B{0}'.format(x+1)

        C = 'C{0}'.format(x+1)

        D = 'D{0}'.format(x+1)

        E = 'E{0}'.format(x+1)

        F = 'F{0}'.format(x+1)

        G = 'G{0}'.format(x+1)

        H = 'H{0}'.format(x+1)

        word[A] = shu[x-1][0]
        
        word[B] = shu[x-1][1]
        
        word[C] = shu[x-1][2]
        
        word[D] = shu[x-1][3]
        
        word[E] = shu[x-1][4]
        
        word[F] = shu[x-1][5]
        
        word[G] = shu[x-1][6]
        
        word[H] = shu[x-1][7]

    wb.save('{0}.xlsx'.format(name))

    print('保存完成'+name)
    print('\n')


def main():

    urllist = tr()#获取学系链接

    for i in urllist:

        name = i[1]#学系名字

        html = url(i[0])#表格内容

        html = bs(html,'lxml')

        cont = html.findAll('tr',valign="middle")

        ex = [] #列表保存内容

        for x in cont:

            content=[]#列表保存每一行内容

            list2 = x.findAll('td')

            for h in list2:
                hh = h.text
                hh = re.sub('\r','',hh)
                hh = re.sub('\t','',hh)
                hh = re.sub('\n','',hh)
                #print(hh)
                content.append(hh)

            ex.append(content)

        
        excel(ex,name)#生成表格



if __name__ == '__main__':
    main()

            

            
        



