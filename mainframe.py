from tkinter import *
from tkinter.filedialog   import askopenfilename
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tkinter.messagebox import *

rows = 0  #记录数
page_num = 0   #总页数
page_idx = 0   #当前页数
page_show = 25 #每页记录数
arr = np.ones(4)
yiqing_df = pd.DataFrame(arr)  #DataFrame数据对象
names={'国家和地区','确诊病例','死亡病例','治愈病例'}
# 设置中文字体，否则中文会出现方框状
plt.rcParams["font.sans-serif"] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def showList(): 
        list_items = []  
        rows = yiqing_df.shape[0] 
        start_idx = page_idx *  page_show  
        end_idx = (page_idx + 1) *  page_show  
        show ="        "+  "  ".join([f"{i:8s}"for i in names])
        
        list_items.append(show)

        for idx in range(start_idx, end_idx + 1):
                if idx < rows :
                    rowdata =  yiqing_df.iloc[idx, ::]
                    lst = list(rowdata)
                    lst_con=str(yiqing_df.index[idx])
                    lst = [f"{x:11.2f} " for x in lst]
                    lst.insert(0,f"{lst_con[:10]:12s}")
                    
                    show = " ".join(lst)      
                    list_items.append(show)
        list_box_var.set(list_items)
def dataprocess():#对DataFrame对象数据进行数据清洗
        pass
def btn_open():
        global yiqing_df, page_num, rows
        filename = askopenfilename()
        
        yiqing_df = pd.read_excel(filename,sheet_name='yiqing',names=names,index_col=0,skiprows=[0])

        rows = yiqing_df.shape[0]
        page_num = rows / page_show

        showList()

def btn_next():#下一页
        global page_idx
        if page_idx == page_num-1:
                showinfo(title='最后一页提示', message='当前是最后一页。')
                return
        page_idx+=1
        showList()
def btn_previous():#前一页
        pass
def btn_fistpage():#第一页
        pass
def btn_lastpage():#最后一页
        pass

def btn_page():#指定一页
        pass


def btn_sure():
        start_idx = page_idx *  page_show
        end_idx = (page_idx + 1) *  page_show

        x = yiqing_df['国家和地区'].values[start_idx:end_idx+1]
        y = yiqing_df['确诊病例'].values[start_idx:end_idx+1]

        # bar宽度
        bar_width = 5
        plt.bar(x, y, width=bar_width, alpha=0.7, label='人数', color='b')

        # 显示数值标签
        for a, b in zip(x, y):
                plt.text(a, b, '%.0f' % b, ha='left', va= 'center', fontsize=7)
        #设置标题
        plt.title('确诊病例柱状图')
        index_name = yiqing_df.index[start_idx:end_idx+1]
       # index_name = [x.strftime('%Y-%m-%d') for x in index_name]
        plt.xticks(x+bar_width/2,index_name)
        plt.gcf().autofmt_xdate() # 自动旋转日期标记
        plt.show()
        
def btn_death():
        start_idx = page_idx *  page_show
        end_idx = (page_idx + 1) *  page_show

        x = yiqing_df['国家和地区'].values[start_idx:end_idx+1]
        y = yiqing_df['死亡病例'].values[start_idx:end_idx+1]

        # bar宽度
        bar_width = 5
        plt.bar(x, y, width=bar_width, alpha=0.7, label='人数', color='b')

        # 显示数值标签
        for a, b in zip(x, y):
                plt.text(a, b, '%.0f' % b, ha='left', va= 'center', fontsize=7)
        #设置标题
        plt.title('死亡病例柱状图')
        index_name = yiqing_df.index[start_idx:end_idx+1]
       # index_name = [x.strftime('%Y-%m-%d') for x in index_name]
        plt.xticks(x+bar_width/2,index_name)
        plt.gcf().autofmt_xdate() # 自动旋转日期标记
        plt.show()



root = Tk()
root.title("疫情分析")   
width = 1000
height = 600
#设置窗口居屏幕中间显示
screenwidth = root.winfo_screenwidth()  
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
root.geometry(alignstr)


top = Frame(root)
body = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)

bottom.pack(side=TOP,expand=YES,fill=BOTH)
top.config(bg = 'green')
bottom.config(bg = 'yellow')
bottom.pack(side=TOP)


btn1 = Button(top,text='打开', command=btn_open)
btn2 = Button(top,text='确诊病例', command=btn_sure)
btn3 = Button(top,text='死亡病例', command=btn_death)
btn4 = Button(top,text='下一页', command=btn_next)
#定义一个文本变量
list_box_var = StringVar()
#设置文本变量的值
show ="        "+  "  ".join([f"{i:8s}"for i in names])
list_box_var.set([show])

list_box = Listbox(bottom,listvar=list_box_var)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
btn4.pack(side=LEFT)

list_box.pack(side=TOP,expand=YES,fill=BOTH)
root.mainloop()
