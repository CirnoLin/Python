"""
查询json信息
"""
import demjson
import json
import time
path = r'E:\study\新建文件夹\try_json\华东师范大学2020年硕士研究生招生专业目录.json'
def Select():
    with open(path,'r',encoding='utf-8')as f:
        info = f.read()
    json_data = json.loads(info)
    while True:
        print("请输入查询编号：\n")
        print("1.查询序号；2.查询招生年份；3.查询招生专业；4.查询学位类型；5.查询招生人数；6.查询研究方向；7.查询考试科目,q.退出查询\n")
        print("-"*30)
        text = input("请输入:")
        try:
            if int(text) not in [1,2,3,4,5,6,7]:
                raise ValueError
            text = int(text)
        except Exception as e:
            print(e)
            if text == "q":
                print("退出查询")
                exit()
            print("输入查询代码错误,请重新输入")
            continue
        # 查询序号
        if text == 1:
            print("-"*30)
            index = input("请输入查询的序号：")
            print("*" * 30 + '\n')
            line = ""
            for info in json_data['']:
                if info['序号'].replace(" ","") == str(index):
                    line = "*" * 30 + '\n'
                    line += "序号:" + info['序号'].replace(" ","") + '\n'
                    line += "招生年份:" + info['招生年份'].replace(" ","") + '\n'
                    line += "招生专业:" + info['招生专业'].replace(" ","") + '\n'
                    line += "学位类型:" + info['学位类型'].replace(" ","") + '\n'
                    line += "招生人数:" + info['招生人数'].replace(" ","") + '\n'
                    line += "研究方向:" + info['研究方向'].replace(" ","")+ '\n'
                    line += "考试科目:" + info['考试科目'].replace(" ","") + '\n'
                    line += "备注:" + info['备注'] + '\n'
                    line += "*" * 30 + '\n'
                    print(line)
                    time.sleep(0.5)
            if line == "":
                print("暂无为{}序号的信息".format(index))
                print("*" * 20 + '\n')
                time.sleep(2)

        # 查询招生年份
        if text == 2:
            print("-"*30)
            index = input("请输入查询的招生年份：")
            print("*" * 30 + '\n')
            line = ""
            for info in json_data['']:
                if info['招生年份'].replace(" ","") == str(index):
                    line = "*" * 30 + '\n'
                    line += "序号:" + info['序号'].replace(" ","") + '\n'
                    line += "招生年份:" + info['招生年份'].replace(" ","") + '\n'
                    line += "招生专业:" + info['招生专业'].replace(" ","") + '\n'
                    line += "学位类型:" + info['学位类型'].replace(" ","") + '\n'
                    line += "招生人数:" + info['招生人数'].replace(" ","") + '\n'
                    line += "研究方向:" + info['研究方向'].replace(" ","")+ '\n'
                    line += "考试科目:" + info['考试科目'].replace(" ","") + '\n'
                    line += "备注:" + info['备注'] + '\n'
                    line += "*" * 30 + '\n'
                    print(line)
                    time.sleep(0.5)
            if line == "":
                print("暂无为{}招生年份的信息".format(index))
                print("*" * 30 + '\n')
                time.sleep(2)

        # 查询招生专业
        if text == 3:
            print("-"*30)
            index = input("请输入查询的招生专业：")
            print("*" * 30 + '\n')
            line = ""
            for info in json_data['']:
                if str(index) in info['招生专业'].replace(" ",""):
                    line = "*" * 30 + '\n'
                    line += "序号:" + info['序号'].replace(" ","") + '\n'
                    line += "招生年份:" + info['招生年份'].replace(" ","") + '\n'
                    line += "招生专业:" + info['招生专业'].replace(" ","") + '\n'
                    line += "学位类型:" + info['学位类型'].replace(" ","") + '\n'
                    line += "招生人数:" + info['招生人数'].replace(" ","") + '\n'
                    line += "研究方向:" + info['研究方向'].replace(" ","")+ '\n'
                    line += "考试科目:" + info['考试科目'].replace(" ","") + '\n'
                    line += "备注:" + info['备注'] + '\n'
                    line += "*" * 30 + '\n'
                    print(line)
                    time.sleep(0.5)
            if line == "":
                print("暂无为{}招生专业的信息".format(index))
                print("*" * 30 + '\n')
                time.sleep(2)

        # 查询学位类型
        if text == 4:
            print("-"*30)
            index = input("请输入查询的学位类型：")
            print("*" * 30 + '\n')
            line = ""
            for info in json_data['']:
                if info['学位类型'].replace(" ","") == str(index):
                    line = "*" * 30 + '\n'
                    line += "序号:" + info['序号'].replace(" ","") + '\n'
                    line += "招生年份:" + info['招生年份'].replace(" ","") + '\n'
                    line += "招生专业:" + info['招生专业'].replace(" ","") + '\n'
                    line += "学位类型:" + info['学位类型'].replace(" ","") + '\n'
                    line += "招生人数:" + info['招生人数'].replace(" ","") + '\n'
                    line += "研究方向:" + info['研究方向'].replace(" ","")+ '\n'
                    line += "考试科目:" + info['考试科目'].replace(" ","") + '\n'
                    line += "备注:" + info['备注'] + '\n'
                    line += "*" * 30 + '\n'
                    print(line)
                    time.sleep(0.5)
            if line == "":
                print("暂无为{}学位类型的信息".format(index))
                print("*" * 30 + '\n')
                time.sleep(2)

        # 查询招生人数
        if text == 5:
            print("-"*30)
            index = input("请输入查询的招生人数：")
            print("*" * 30 + '\n')
            line = ""
            for info in json_data['']:
                if str(index) in info['招生人数'].replace(" ",""):
                    line = "*" * 30 + '\n'
                    line += "序号:" + info['序号'].replace(" ","") + '\n'
                    line += "招生年份:" + info['招生年份'].replace(" ","") + '\n'
                    line += "招生专业:" + info['招生专业'].replace(" ","") + '\n'
                    line += "学位类型:" + info['学位类型'].replace(" ","") + '\n'
                    line += "招生人数:" + info['招生人数'].replace(" ","") + '\n'
                    line += "研究方向:" + info['研究方向'].replace(" ","")+ '\n'
                    line += "考试科目:" + info['考试科目'].replace(" ","") + '\n'
                    line += "备注:" + info['备注'] + '\n'
                    line += "*" * 30 + '\n'
                    print(line)
                    time.sleep(0.5)
            if line == "":
                print("暂无为{}招生人数的信息".format(index))
                print("*" * 30 + '\n')
                time.sleep(2)

        # 查询研究方向
        if text == 6:
            print("-"*30)
            print("*" * 30 + '\n')
            line = ""
            for info in json_data['']:
                line = "*" * 30 + '\n'
                line += "序号:" + info['序号'].replace(" ","") + '\n'
                line += "招生年份:" + info['招生年份'].replace(" ","") + '\n'
                line += "招生专业:" + info['招生专业'].replace(" ","") + '\n'
                line += "学位类型:" + info['学位类型'].replace(" ","") + '\n'
                line += "招生人数:" + info['招生人数'].replace(" ","") + '\n'
                line += "研究方向:" + info['研究方向'].replace(" ","")+ '\n'
                line += "考试科目:" + info['考试科目'].replace(" ","") + '\n'
                line += "备注:" + info['备注'] + '\n'
                line += "*" * 30 + '\n'
                print(line)
                time.sleep(0.5)
        
        # 查询考试科目
        if text == 7:
            print("-"*30)
            print("*" * 30 + '\n')
            line = ""
            for info in json_data['']:
                line = "*" * 30 + '\n'
                line += "序号:" + info['序号'].replace(" ","") + '\n'
                line += "招生年份:" + info['招生年份'].replace(" ","") + '\n'
                line += "招生专业:" + info['招生专业'].replace(" ","") + '\n'
                line += "学位类型:" + info['学位类型'].replace(" ","") + '\n'
                line += "招生人数:" + info['招生人数'].replace(" ","") + '\n'
                line += "研究方向:" + info['研究方向'].replace(" ","")+ '\n'
                line += "考试科目:" + info['考试科目'].replace(" ","") + '\n'
                line += "备注:" + info['备注'] + '\n'
                line += "*" * 30 + '\n'
                print(line)
                time.sleep(0.5)



Select()