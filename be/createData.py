import random
import pandas as pd
def createName():
    firstName=['Phạm','Nguyễn','Trần','Lê','Huỳnh','Võ','Đặng','Bùi','Đỗ','Hồ','Ngô','Dương','Lý','Đào','Đinh','Kim','Phan','Vũ','Tạ','Trịnh','Chu','La','Lâm','Lưu','Mai','Quách','Thái','Tô','Hoa','Tăng','Đoàn','Trương','Nghiêm','Đinh','Đặng']
    middleName=['Thị','Văn','Đình','Ngọc','Hữu','Thế','Quốc','Văn','Thành','Hồng','Đức','Minh']
    lastName=['An','Bình','Châu','Dũng','Hải','Hào','Hiền','Hùng','Hưng','Khánh','Linh','Long','Mạnh','Minh','Nghĩa','Phú','Quân','Quang','Sơn','Thắng','Thành','Thu','Tiến','Trung','Tuấn','Tùng','Vinh','Xuân','Yến']
    name=random.choice(firstName)+' '+random.choice(middleName)+' '+random.choice(lastName)
    return name
def createPhone():
    phone='0'
    nhamang=['32','33','34','35','36','37','38','39','70','79','77','76','78','89','88','86','96','97','98','86','91','94','83','84','85','92','56','58','99']
    phone+=random.choice(nhamang)
    for i in range(7):
        phone+=str(random.randint(0,9))
    return phone
def createLocal():
    df=pd.read_csv('new2.csv')
    localList=df['tinh'].tolist()
    localnew=random.choice(localList)
    return localnew
def createCourse():
    listLeagues=['English','Japanese','Korean']
    listLevelEn=['A1','A2','B1','B2','C1','C2']
    listLevelJa=['N5','N4','N3','N2','N1']
    listLevelKo=['Sơ cấp','Trung cấp','Cao cấp']
    course={}
    course['leangue']=random.choice(listLeagues)
    if course['leangue']=='English':
        course['level']=random.choice(listLevelEn)
        course['goal']=random
    elif course['leangue'] == 'Japanese':
        course['level'] = random.choice(listLevelJa)
        course['goal'] = random
    else:
        course['level'] = random.choice(listLevelKo)
        course['goal'] = random
    return course
def createData():
    data={}
    data['name']=createName()
    data['phone']=createPhone()
    data['local']=createLocal()
    data['course']=createCourse()
    return data
def createDataList(n):
    dataList=[]
    for i in range(n):
        dataList.append(createData())
    return dataList
# print(createDataList(10))


    

        
    