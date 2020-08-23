# pages/views.py
import os, zipfile
from zipfile import ZipFile
from rest_framework import serializers
import base64
from io import StringIO
from django.http import HttpResponse
from .models import IhaDetails,IhaTestDetails
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from os import path
import json
import datetime,calendar
from datetime import date
from django.forms.models import model_to_dict



def getAll(request):
    ihaList=IhaDetails.objects.all()
    #encoded = ihaList[14].actualfile.decode("utf-8")
    """with open(ihaList[1].filename, "wb") as fh:
    
        fh.write(base64.decodebytes(ihaList[1].actualfile))"""
    resobj=[]
    for i in range(0,ihaList.count()):
        dic={'id':ihaList[i].id,'filename':ihaList[i].filename}
        resobj.append(dic)

    return JsonResponse({"status":'Success','responseObject':resobj},safe=False)

@csrf_exempt
def saveFile(request):
    response = {'status': 'Failure', 'responseObject': None}
    try:
        if request.method == "POST":

            body_unicode = request.body.decode('utf-8')

            body_data = json.loads(body_unicode)

            iha = IhaDetails()
            iha.filename = body_data['filename']

            """with open(iha.filename, "wb") as fh:
                decoded = base64.b64decode(body_data['actualfile'])
                fh.write(decoded)
                with zipfile.ZipFile(iha.filename) as zf:
                    zf.extractall()
            os.remove(iha.filename)
            iha.filename=iha.filename[:-(len('.zip'))]
            iha.filename=iha.filename+'.csv'
            data = open(iha.filename, 'rb').read()

            bs64 = base64.b64encode(data).decode('UTF-8')
            os.remove(iha.filename)"""




            if body_data['filename'].endswith('.zip'):

                if IhaDetails.objects.filter(filename=body_data['filename']).first() != None:
                    response = {'status': 'Failure', 'responseObject': 'File already exists'}
                else:
                    iha.actualfile =bytes(body_data['actualfile'], 'raw_unicode_escape')
                    print("success1")
                    iha.save()
                    print("success2")
                    response = {'status': 'Success', 'responseObject': None}
            else:
                response = {'status': 'Failure', 'responseObject': 'File is not in ZIP format.'}
        else:
            response = {'status': 'Failure', 'responseObject': None}
    except Exception as e:
        print(str(e))
        response = {'status': 'Failure', 'responseObject': str(e)}

    return JsonResponse(response,safe=False)


@csrf_exempt
def saveTestFile(request):
    response = {'status': 'Failure', 'responseObject': None}
    try:
        if request.method == "POST":

            body_unicode = request.body.decode('utf-8')

            body_data = json.loads(body_unicode)
            
            iha = IhaTestDetails()
            iha.filename = body_data['filename']

            """with open(iha.filename, "wb") as fh:
                decoded = base64.b64decode(body_data['actualfile'])
                fh.write(decoded)
                with zipfile.ZipFile(iha.filename) as zf:
                    zf.extractall()
            os.remove(iha.filename)
            iha.filename=iha.filename[:-(len('.zip'))]
            iha.filename=iha.filename+'.csv'
            data = open(iha.filename, 'rb').read()

            bs64 = base64.b64encode(data).decode('UTF-8')
            os.remove(iha.filename)"""

            if body_data['filename'].endswith('.zip'):

                print('tt')
                if IhaTestDetails.objects.filter(tid=body_data['tid']).first() != None:
                    response = {'status': 'Failure', 'responseObject': 'File already exists'}
                else:
                    print('ttt')
                    iha.actualfile =bytes(body_data['actualfile'], 'raw_unicode_escape')
                    iha.tid=body_data['tid']
                    print("success1")
                    iha.save()
                    print("success2")
                    response = {'status': 'Success', 'responseObject': None}
            else:
                response = {'status': 'Failure', 'responseObject': 'File is not in ZIP format.'}
        else:
            response = {'status': 'Failure', 'responseObject': None}
    except Exception as e:
        print(str(e))
        response = {'status': 'Failure', 'responseObject': str(e)}

    return JsonResponse(response,safe=False)



"""
def getEmpDetails(request):
    data=list(EmpDetails.objects.values())
    return JsonResponse(data, safe=False)
@csrf_exempt
def addEmployee(request):
    response=''
    newemp = EmpDetails()

    if request.method == "POST":
        response='Success'
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)


        newemp.firstname=body_data['firstname']
        newemp.lastname = body_data['lastname']
        if EmpDetails.objects.filter(firstname=body_data['firstname'],lastname=body_data['lastname']).first()!=None:
            print("Duplicate")
            newemp=None
            response = {'status': 'Failure', 'responseObject': newemp}
        elif body_data['firstname'].strip()!="" and body_data['lastname'].strip()!="":

            newemp.save()
            newemp=EmpDetails.objects.filter(firstname=body_data['firstname'],lastname=body_data['lastname']).first()
            print(newemp.id)
            newemp={'id':newemp.id,'firstname':newemp.firstname,'lastname':newemp.lastname}
            response={'status':'Success','responseObject':newemp}
        else:
            response = {'status': 'Failure', 'responseObject': None}
    else:
        response={'status':'Failure','responseObject':None}
    return JsonResponse(response, safe=False)


@csrf_exempt
def addCollege(request):
    response = {'status': 'Failure', 'responseObject': None}
    newclg = CollegeDetails()

    if request.method == "POST":

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)


        newclg.name=body_data['name'].lower()
        newclg.address = body_data['address'].lower()
        newclg.admitCriteria=body_data['admitCriteria']

        newclg.shortForm=body_data['shortForm'].lower()
        newclg.typeOfClg=body_data['typeOfClg'].lower()
        if CollegeDetails.objects.filter(name=body_data['name'],shortForm=body_data['shortForm']).first()!=None:
            print("Duplicate")
            newclg=None
            response = {'status': 'Failure', 'responseObject': newemp}
        elif body_data['name'].strip()!="" and body_data['shortForm'].strip()!="":

            newclg.save()
            newclg=CollegeDetails.objects.filter(name=body_data['name'],shortForm=body_data['shortForm']).first()
            print(newclg.id)

            response={'status':'Success','responseObject':{'id':newclg.id,'name':newclg.name,'shortForm':newclg.shortForm}}
        else:
            response = {'status': 'Failure', 'responseObject': None}
    else:
        response={'status':'Failure','responseObject':None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def addCourse(request):
    response = {'status': 'Failure', 'responseObject': None}
    newclg = Courses()
    print("OOO")
    if request.method == "POST":
        print("MMM")
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)


        newclg.name=body_data['name'].lower()
        newclg.cid=body_data['cid']
        print(newclg)
        if Courses.objects.filter(name=body_data['name'],cid=body_data['cid']).first()!=None:
            print("Duplicate")
            newclg=None
            response = {'status': 'Failure', 'responseObject': newclg}
        elif body_data['name'].strip()!="" and body_data['cid'].strip()!="":

            newclg.save()
            newclg=Courses.objects.filter(name=body_data['name'],cid=body_data['cid']).first()
            print(newclg.id)

            response={'status':'Success','responseObject':{'id':newclg.id,'name':newclg.name,'cid':newclg.cid}}
        else:
            response = {'status': 'Failure', 'responseObject': None}
    else:
        response={'status':'Failure','responseObject':None}
    return JsonResponse(response, safe=False)


@csrf_exempt
def updateCourse(request):
    response = ''
    newclg = Courses()
    try:
        if request.method == "PUT":
            response = 'Success'
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)

            print("KKK")
            if Courses.objects.get(id=body_data['id']) != None and body_data['name'].strip()!="":
                #newemp.firstname = body_data['firstname']
                #newemp.lastname = body_data['lastname']
                print("LLL")
                newclg=Courses.objects.filter(id=body_data['id']).update(name=body_data['name'].lower(),seats=body_data['seats'])
                #newemp.save(update_fields=["active"])
                #print(newemp.id)
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Success', 'responseObject': None}
                print("Success")
            else:
                print("Does not exist.")
                newclg = None
                response = {'status': 'Failure', 'responseObject': None}

        else:
            response = {'status': 'Failure', 'responseObject': None}
    except:
        print("There is some problem.")
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def updateCollege(request):
    response = ''
    newclg = CollegeDetails()
    try:
        if request.method == "PUT":
            response = 'Success'
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)


            if CollegeDetails.objects.get(id=body_data['id']) != None and body_data['name'].strip()!="":
                #newemp.firstname = body_data['firstname']
                #newemp.lastname = body_data['lastname']
                newclg=CollegeDetails.objects.filter(id=body_data['id']).update(name=body_data['name'].lower(),address=body_data['address'].lower(),
                                                                                admitCriteria=body_data['admitCriteria'].lower(),shortForm=body_data['shortForm'].lower(),typeOfClg=body_data['typeOfClg'].lower())
                #newemp.save(update_fields=["active"])
                #print(newemp.id)
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Success', 'responseObject': None}
                print("Success")
            else:
                print("Does not exist.")
                newclg = None
                response = {'status': 'Failure', 'responseObject': None}

        else:
            response = {'status': 'Failure', 'responseObject': None}
    except:
        print("There is some problem.")
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def deleteCourse(request):
    response = ''
    newclg = Courses()

    try:
        if request.method == "DELETE":
            response = 'Success'
            #body_unicode = request.body.decode('utf-8')
            #body_data = json.loads(body_unicode)
            id = request.GET['id']
            if Courses.objects.get(id=id) != None:
                newclg=Courses.objects.get(id=id)
                newclg.delete()

                response = {'status': 'Success', 'responseObject': None}
            else:
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Failure', 'responseObject': None}
        else:
            response = {'status': 'Failure', 'responseObject': None}

    except:
        print("There's something wrong")
        #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)


@csrf_exempt
def deleteCollege(request):
    response = ''
    newclg = CollegeDetails()

    try:
        if request.method == "DELETE":
            response = 'Success'
            #body_unicode = request.body.decode('utf-8')
            #body_data = json.loads(body_unicode)
            id = request.GET['id']
            if CollegeDetails.objects.get(id=id) != None:
                newclg=CollegeDetails.objects.get(id=id)
                newclg.delete()
                Courses.objects.filter(cid=id).delete()
                Fees.objects.filter(cid=id).delete()
                response = {'status': 'Success', 'responseObject': None}
            else:
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Failure', 'responseObject': None}
        else:
            response = {'status': 'Failure', 'responseObject': None}

    except:
        print("There's something wrong")
        #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)

def getCourseDetails(request):
    id=request.GET['id']
    data=list(Courses.objects.filter(cid=id))

    cnt=0
    for item in data:

        temp={'id':item.id,'name':item.name,'seats':item.seats}
        data[cnt]=temp
        cnt=cnt+1

    #return HttpResponse(data, content_type="application/json")
    return JsonResponse(data, safe=False)

def getFeeDetails(request):
    id=request.GET['cid']
    data=list(Fees.objects.filter(cid=id))

    cnt=0
    for item in data:

        temp={'id':item.id,'openCategory':item.openCategory,'obc':item.obc,'sbc':item.sbc,'sc':item.sc,'st':item.st}
        data[cnt]=temp
        cnt=cnt+1

    #return HttpResponse(data, content_type="application/json")
    return JsonResponse(data, safe=False)

@csrf_exempt
def addFeeDetails(request):
    response = {'status': 'Failure', 'responseObject': None}
    newfees = Fees()
    print("OOO")
    if request.method == "POST":
        print("MMM")
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        newfees.cid=body_data['cid']
        newfees.openCategory=body_data['openCategory']
        newfees.obc=body_data['obc']
        newfees.sbc=body_data['sbc']
        newfees.sc=body_data['sc']
        newfees.st=body_data['st']
        print(newfees)
        if Fees.objects.filter(cid=body_data['cid']).first()!=None:
            print("Duplicate")
            newclg=None
            response = {'status': 'Failure', 'responseObject': newfees}
        elif body_data['cid'].strip()!="":

            newfees.save()
            newfees=Fees.objects.filter(cid=body_data['cid']).first()
            print(newfees.id)

            response={'status':'Success','responseObject':{'id':newfees.id,'openCategory':newfees.openCategory
                                                           ,'obc':newfees.obc,'sbc':newfees.sbc,'sc':newfees.sc,'st':newfees.st}}
        else:
            response = {'status': 'Failure', 'responseObject': None}
    else:
        response={'status':'Failure','responseObject':None}
    return JsonResponse(response, safe=False)


@csrf_exempt
def updateFeeDetails(request):
    response = ''
    newfees = Fees()
    try:
        if request.method == "PUT":
            response = 'Success'
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)


            if Fees.objects.get(id=body_data['id']) != None:
                #newemp.firstname = body_data['firstname']
                #newemp.lastname = body_data['lastname']
                newfees=Fees.objects.filter(id=body_data['id']).update(openCategory=body_data['openCategory'],obc=body_data['obc'],
                                                                       sbc=body_data['sbc'],sc=body_data['sc'],st=body_data['st'])
                #newemp.save(update_fields=["active"])
                #print(newemp.id)
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Success', 'responseObject': None}
                print("Success")
            else:
                print("Does not exist.")
                newfees = None
                response = {'status': 'Failure', 'responseObject': None}

        else:
            response = {'status': 'Failure', 'responseObject': None}
    except:
        print("There is some problem.")
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def updateEmployee(request):
    response = ''
    newemp = EmpDetails()
    try:
        if request.method == "PUT":
            response = 'Success'
            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)


            if EmpDetails.objects.get(id=body_data['id']) != None and body_data['firstname'].strip()!="" and body_data['lastname'].strip()!="":
                #newemp.firstname = body_data['firstname']
                #newemp.lastname = body_data['lastname']
                newemp=EmpDetails.objects.filter(id=body_data['id']).update(firstname=body_data['firstname'],lastname=body_data['lastname'])
                #newemp.save(update_fields=["active"])
                #print(newemp.id)
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Success', 'responseObject': None}
                print("Success")
            else:
                print("Does not exist.")
                newemp = None
                response = {'status': 'Failure', 'responseObject': None}

        else:
            response = {'status': 'Failure', 'responseObject': None}
    except:
        print("There is some problem.")
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def deleteEmployee(request):
    response = ''
    newemp = EmpDetails()

    try:
        if request.method == "DELETE":
            response = 'Success'
            #body_unicode = request.body.decode('utf-8')
            #body_data = json.loads(body_unicode)
            id = request.GET['id']
            if EmpDetails.objects.get(id=id) != None:
                newemp=EmpDetails.objects.get(id=id)
                newemp.delete()
                response = {'status': 'Success', 'responseObject': None}
            else:
                #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
                response = {'status': 'Failure', 'responseObject': None}
        else:
            response = {'status': 'Failure', 'responseObject': None}

    except:
        print("There's something wrong")
        #newemp = {'id': newemp.id, 'firstname': newemp.firstname, 'lastname': newemp.lastname}
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response, safe=False)

@csrf_exempt
def savePhoto(request):
    response=''
    if request.method == "POST":
        try:

            body_unicode = request.body.decode('utf-8')
            body_data = json.loads(body_unicode)
            arr=body_data['photo'].split(",")

            if EmpDetails.objects.get(id=body_data['id']) != None:

                cwdname=os.path.abspath(os.getcwd())+os.path.sep+"TrainingData"+os.path.sep+str(body_data['id'])
                filepath = os.path.join(cwdname, body_data['filename'])
                if not os.path.exists(cwdname):
                    os.makedirs(cwdname)
                if path.exists(filepath)==False:
                    with open(filepath, "wb") as fh:
                        fh.write(base64.decodebytes(arr[1].encode('utf-8')))
                        response = {'status': 'Success', 'responseObject': None}
                        print("Success- -1")
                        faces=labels_for_training_data(cwdname)
                        print("Interim")
                        face_recognizer = train_classifier(faces, body_data['id'])
                        print("Success-0")
                        face_recognizer.write(cwdname+os.path.sep+'trainingData.yml')
                        print("Success-1")
                else:
                    response = {'status': 'Failure', 'responseObject': None}


            else:
                print("Else")
                response = {'status': 'Failure', 'responseObject': None}
        except Exception as e:
            print("PROBLEM.:-"+str(e))
            response = {'status': 'Failure', 'responseObject': None}
    else:
        response = {'status': 'Failure', 'responseObject': "Not Allowed"}
    return JsonResponse(response)

@csrf_exempt
def markAttendance(request):
    print(request)
    response = {'status': 'Failure', 'responseObject': None}
    conf = 0
    cid = 0
    try:

        result=0
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        arr = body_data['photo'].split(",")
        print(arr[1])
        os.makedirs("Temp")
        fp=os.path.abspath(os.getcwd())+os.path.sep+"Temp"
        fp=os.path.join(fp, "temp.jpg")
        with open(fp, "wb") as fh:
            fh.write(base64.decodebytes(arr[1].encode('utf-8')))

        test_img = cv2.imread(fp)  # test_img path
        faces_detected, gray_img = faceDetection(test_img)
        print("faces_detected:", faces_detected)
        face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        ids=EmpDetails.objects.values('id')

        for i in range(len(ids)):
            r = ids[i]
            r = json.dumps(r)
            loaded_r = json.loads(r)
            print("ID",loaded_r['id'])
            if os.path.exists(os.getcwd()+os.path.sep+ "TrainingData" + os.path.sep + str(loaded_r['id'])+os.path.sep+"trainingData.yml"):
                print("L1")
                filepath=os.getcwd()+os.path.sep+ "TrainingData" + os.path.sep + str(loaded_r['id'])+os.path.sep+"trainingData.yml"
                face_recognizer.read(filepath)
                print("ID", loaded_r['id'])
                for face in faces_detected:
                    (x, y, w, h) = face
                    roi_gray = gray_img[y:y + h, x:x + h]
                    label, confidence = face_recognizer.predict(roi_gray)  # predicting the label of given image
                    print("Confidence",confidence)

                    if (datetime.datetime.today().weekday()==0 or datetime.datetime.today().weekday()==6):
                        response = {'status': 'Failure', 'responseObject': None}
                    else:
                        if confidence<37:
                            conf=confidence
                            cid=loaded_r['id']
                            break



        if cid!=0:
            att = Attendance()
            print(EmpDetails.objects.get(id=cid).firstname+" is present")
            att.eid = cid
            att.attendance = 1
            now = datetime.datetime.now()
            date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
            print("date and time:", date_time)
            att.datetime = date_time

            att.save()
            response = {'status': 'Present', 'responseObject': None}
    except Exception as e:
        print("Exception is.:-"+str(e))
        response = {'status': 'Failure', 'responseObject': None}

    os.remove((os.path.abspath(os.getcwd())+os.path.sep+"Temp"+os.path.sep+"temp.jpg"))
    os.rmdir(os.path.abspath(os.getcwd())+os.path.sep+"Temp")
    return JsonResponse(response, safe=False)

def getAttendance(request):
    data = list(Attendance.objects.values())
    for i in range(len(data)):
        print("Created at %s:%s" % (data[i]['datetime'].hour, data[i]['datetime'].minute))
        data[i]['datetime']=data[i]['datetime'].strftime("%m/%d/%Y, %H:%M:%S")

    return JsonResponse(data, safe=False)

def getCollegeDetails(request):
    data = list(CollegeDetails.objects.values())
    print(data)

    return JsonResponse(data, safe=False)

@csrf_exempt
def getMonthlyReport(request):
    response = {'status': 'Failure', 'responseObject': None}
    try:
        print("A1")
        body_unicode = request.body.decode('utf-8')

        body_data = json.loads(body_unicode)
        attObj=[]
        attObj=Attendance.objects.filter(eid=body_data['eid'])
        fname=EmpDetails.objects.get(id=body_data['eid']).firstname
        lname=EmpDetails.objects.get(id=body_data['eid']).lastname
        print("A2")
        filename=os.getcwd()+os.path.sep+"Temp"+os.path.sep+fname+" "+lname+" "+"Monthly Attendace Report.xlsx"
        os.mkdir(os.getcwd()+os.path.sep+"Temp")
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        format = workbook.add_format()
        format.set_bg_color('gray')
        format.set_bold()
        worksheet.write(0,0,"Date",format)
        worksheet.write(0, 1, "Attendance", format)
        worksheet.write(0, 2, "In-Time", format)

        u=1

        n=len(attObj)
        print(attObj[0].datetime)
        for i in range(n):

            for j in range(3):
                if j==0:
                    date=attObj[u-1].datetime.strftime("%m/%d/%Y, %H:%M:%S")
                    arr=date.split(",")
                    worksheet.write(u, j,arr[0])
                elif j==1:
                    worksheet.write(u, j, 1)
                elif j==2:
                    date = attObj[u-1].datetime.strftime("%m/%d/%Y, %H:%M:%S")
                    arr = date.split(",")
                    worksheet.write(u, j, arr[1])
            u=u+1
        workbook.close()

        data = open(filename, 'rb').read()
        base64_encoded = base64.b64encode(data).decode('UTF-8')

        response = {'status': 'Success', 'filename': fname+" "+lname+" "+"Monthly Attendace Report.xlsx",'responseObject': base64_encoded}
        os.remove(filename)
        os.rmdir(os.getcwd()+os.path.sep+"Temp")
    except Exception as e:
        print("Exception.:-"+str(e))
        if os.path.exists(filename):
            os.remove(filename)
            os.rmdir(os.getcwd() + os.path.sep + "Temp")
        if os.path.exists(os.getcwd()+os.path.sep+"Temp"):
            os.rmdir(os.getcwd() + os.path.sep + "Temp")
    return JsonResponse(response,safe=False)


@csrf_exempt
def addLoginCredentials(request):
    response={'status': 'Failure', 'responseObject': None}
    try:
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        user=None
        try:
            user = LoginCredentials.objects.get(username=body_data['username'])
        except LoginCredentials.DoesNotExist:
            user = None
        if user==None:
            loginCred=LoginCredentials()
            loginCred.username=body_data['username']
            key = Fernet.generate_key()
            print(key)
            cipher_suite = Fernet(key)
            ciphered_text = cipher_suite.encrypt(body_data['password'])  # required to be bytes

            print(ciphered_text)

            loginCred.password=body_data['password']
            loginCred.firstname=body_data['firstname']
            loginCred.lastname=body_data['lastname']
            loginCred.save()
            response = {'status': 'Success', 'responseObject': None}
        else:
            response = {'status': 'Failure:UserName already exists', 'responseObject': None}
    except Exception as e:
        print(str(e))
        response = {'status': 'Failure:There is some problem', 'responseObject': None}
    return JsonResponse(response,safe=False)

@csrf_exempt
def login(request):
    response = {'status': 'Failure', 'responseObject': None}
    try:
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        user = None
        try:
            user =LoginCredentials.objects.get(username=body_data['username'],password=body_data['password'])
        except LoginCredentials.DoesNotExist:
            user = None
        if  user!= None:
            response = {'status': 'Success', 'responseObject': None}
        else:
            response = {'status': 'Failure:Invalid username/password', 'responseObject': None}
    except Exception as e:
        print(str(e))
        response = {'status': 'Failure', 'responseObject': None}
    return JsonResponse(response,safe=False)
def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)#convert color image to grayscale
    print("H1")
    cwdname = os.path.abspath(os.getcwd() + os.path.sep + "haarcascade_frontalface_default.xml")
    print("H2")
    face_haar_cascade=cv2.CascadeClassifier(cwdname)#Load haar classifier
    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)#detectMultiScale returns rectangles

    print("H3")
    return faces,gray_img

#Given a directory below function returns part of gray_img which is face alongwith its label/ID
def labels_for_training_data(directory):
    faces=[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            print(filename)
            if filename.startswith("."):
                print("Skipping system file")#Skipping files that startwith .
                continue
            #elif search("jpg",filename) and search("png",filename) and search("JPG",filename) and search("PNG",filename):
            print("Training...")
            id=os.path.basename(path)#fetching subdirectory names
            img_path=os.path.join(path,filename)#fetching image path
            print("img_path:",img_path)
            print("id:",id)
            test_img=cv2.imread(img_path)#loading each image one by one
            print("T1")
            if test_img is None:
                print("Image not loaded properly")
                continue
            print("T2")
            faces_rect,gray_img=faceDetection(test_img)#Calling faceDetection function to return faces detected in particular image
            if len(faces_rect)!=1:
                continue #Since we are assuming only single person images are being fed to classifier
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from grayscale image
            faces.append(roi_gray)
    print(len(faces))
    return faces


#Below function trains haar classifier and takes faces,faceID returned by previous function as its arguments
def train_classifier(faces,faceID):
    faceID=np.full(len(faces),faceID)
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces,faceID)
    return face_recognizer

#Below function draws bounding boxes around detected face in image
def draw_rect(test_img,face):
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=5)

#Below function writes name of person for detected label
def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,2,(255,0,0),4)

@csrf_exempt
def mcresponse(request):
    response={'status':"Failure",'respmsg':"",'respvoice':""}
    try:

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        msg=body_data['msg']
        msg=msg.replace('?','')
        if msg.lower()=="hi" or msg.lower()=="hello":
            voice=getTextToSpeech("Hello")
            response={'status':"Success",'respmsg':"Hello",'respvoice':voice}
        elif os.path.exists(os.getcwd()+os.path.sep+"intents.json")==False:
            print(os.getcwd()+" DOES NOT")
            voice = getTextToSpeech("Unable to understand you.Sorry.")
            response = {'status': "Success", 'respmsg': "Unable to understand you.Sorry.", 'respvoice': voice}
        elif os.path.exists(os.getcwd()+os.path.sep+"intents.json"):
            print("EXISTS")

            print("uuuuu")
            if os.path.exists(os.getcwd()+os.path.sep+"data.pickle")==False:
                dataPickle()
            print("ffff")
            with open("data.pickle", "rb") as f:
                words, labels, training, output = pickle.load(f)
            tensorflow.reset_default_graph()

            net = tflearn.input_data(shape=[None, len(training[0])])
            net = tflearn.fully_connected(net, 8)
            net = tflearn.fully_connected(net, 8)
            net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
            net = tflearn.regression(net)

            model = tflearn.DNN(net)

            model.load("model.tflearn")
            results = model.predict([bag_of_words(msg, words)])
            print(results)

            num = results[0][0] * 10
            num2=results[0][1]*10
            print(num2)
            if num > 1 and num2>1:
                voice = getTextToSpeech("Unable to understand you.Sorry.")
                response = {'status': "Success", 'respmsg': "Unable to understand you.Sorry.", 'respvoice': voice}
            else:


                results_index = numpy.argmax(results)
                print(results_index)
                tag = labels[results_index]

                with open(os.getcwd() + os.path.sep + "intents.json") as f:
                    data = json.load(f)

                    for tg in data['intents']:

                        if tg['tag'] == tag:
                            print(tg['tag'])
                            resp = tg['responses']
                            respf=''
                            print(respf)
                            if tg['context_set']!=None and tg['context_set'].strip()!='':

                                if tg['context_set']=='college_name':

                                    #EmpDetails.objects.get(id=body_data['id'])
                                    cname=uniqueWords(msg,words).lower()
                                    listOfColleges=list(CollegeDetails.objects.values())
                                    college=None
                                    try:
                                        college=CollegeDetails.objects.filter(name=cname).first()
                                        if college==None:
                                            college=CollegeDetails.objects.filter(shortForm=cname).first()
                                    except Exception as e:
                                        print(str(e))
                                    print(college)
                                    cnt1=0



                                    if college!=None:
                                        c_id=college.id
                                        print("Found----"+cname)
                                        respf = college.name + ' is located in ' + college.address
                                        courses=[]
                                        print(respf)
                                        courses=Courses.objects.filter(cid=c_id)
                                        if len(courses)>0:
                                            respf = respf + ' and offers courses like '
                                            cnt=0
                                            for k in courses:
                                                cnt = cnt + 1
                                                if cnt==((len(courses))):
                                                    respf=respf + ' & '+str(k.name)+'.'
                                                else:
                                                    respf = respf + str(k.name) +', '

                                        voice = getTextToSpeech(respf)
                                        response = {'status': "Success", 'respmsg': respf,
                                                    'respvoice': voice}
                                        break
                                    else:
                                        print("yyyy")
                                        voice = getTextToSpeech(
                                            "Requested college details not found in the database. Sorry.")
                                        respf = "Requested college details not found in the database. Sorry."
                                        response = {'status': "Success", 'respmsg': respf,
                                                    'respvoice': voice}
                                    break
                                elif tg['context_set']=='admissionCriteria':
                                    print('Admission Criteria')
                                    cname = uniqueWords(msg, words).lower()
                                    college = None
                                    try:
                                        college=CollegeDetails.objects.filter(name=cname).first()
                                        if college==None:
                                            college=CollegeDetails.objects.filter(shortForm=cname).first()
                                    except Exception as e:
                                        print(str(e))
                                    print(college)
                                    cnt1 = 0


                                    if college!=None:
                                        respf = 'The criteria to secure admission in '+college.name +' is '+' '+str(college.admitCriteria)+'% in 12th grade (HSC).'
                                        print(respf)
                                        voice = getTextToSpeech(respf)
                                        response = {'status': "Success", 'respmsg': respf,
                                                    'respvoice': voice}
                                        break
                                    else:
                                        voice = getTextToSpeech(
                                            "Requested college details not found in the database. Sorry.")
                                        respf = "Requested college details not found in the database. Sorry."
                                        response = {'status': "Success", 'respmsg': respf,
                                                    'respvoice': voice}

                                        break


                                elif tg['context_set']=='fees':
                                    print('FEES')
                                    cList=list(CollegeDetails.objects.values())

                                    feesRequired=None
                                    collegeId=0
                                    collegeName=''
                                    for it in cList:
                                        if is_part(msg.lower(),it['name'].lower())==True or is_part(msg.lower(),it['shortForm']):
                                            collegeName=it['name']
                                            collegeId=it['id']
                                            feesRequired=Fees.objects.filter(cid=collegeId).first()
                                            print(feesRequired)
                                            break
                                    if feesRequired!=None:
                                        if is_part(msg.lower(),'open')==True:
                                            respf = 'The fees for ' + collegeName + ' for ' + 'Open' + ' category is '+str(feesRequired.openCategory)+' Rupees.'
                                        elif is_part(msg.lower(),'obc')==True:
                                            respf = 'The fees for ' + collegeName + ' for ' + 'OBC' + ' category is ' + str(feesRequired.obc)+' Rupees.'
                                        elif is_part(msg.lower(),'sbc'):
                                            respf = 'The fees for ' + collegeName + ' for ' + 'SBC' + ' category is ' + str(feesRequired.sbc)+' Rupees.'
                                        elif is_part(msg.lower(),'sc'):
                                            respf = 'The fees for ' + collegeName + ' for ' +'SC' + ' category is ' + str(feesRequired.sc)+' Rupees.'
                                        elif is_part(msg.lower(),'st'):
                                            respf = 'The fees for ' + collegeName + ' for ' + 'ST' + ' category is ' + str(feesRequired.st)+' Rupees.'
                                        else:
                                            respf = 'The requested college or category is not available. Sorry'
                                    else:
                                        respf = 'The requested college, category or fee detail is not available. Sorry.'
                                    voice = getTextToSpeech(respf)
                                    response = {'status': "Success", 'respmsg': respf,
                                                'respvoice': voice}
                                    break



                                elif tg['context_set']=='type':
                                    print('TYPE')
                                    cname = uniqueWords2(msg, words).lower()
                                    list1 = None
                                    print(cname)
                                    try:

                                       list1=CollegeDetails.objects.filter(typeOfClg=cname)
                                    except Exception as e:
                                        print(str(e))
                                    print(list1)



                                    if list1!=None:
                                        respf='The '+cname+' based colleges in Savitribai Phule Pune University are as follows-'
                                        tmpcnt=0
                                        print(len(list1)!='0')
                                        if len(list1)!='0':
                                            for temp in list1:
                                                tmpcnt=tmpcnt+1

                                                respf=respf+' '+str(tmpcnt)+') '+temp.name+'. '
                                        else:
                                            respf='There are no colleges of requested type. Sorry.'
                                        print(respf)
                                        voice = getTextToSpeech(respf)
                                        response = {'status': "Success", 'respmsg': respf,
                                                    'respvoice': voice}
                                        break

                                    else:
                                        voice = getTextToSpeech(
                                            "Requested college details not found in the database. Sorry.")
                                        respf = "Requested college details not found in the database. Sorry."
                                        response = {'status': "Success", 'respmsg': respf,
                                                    'respvoice': voice}
                                        break
                                elif tg['context_set'] == 'seats':
                                    print("Seats")
                                    courseList=list(Courses.objects.values())
                                    courseName=''

                                    if courseList!=None:
                                        for temp1 in courseList:


                                            if is_part(msg,temp1['name'].lower())==True:
                                                print("Matched")
                                                courseName=temp1['name']
                                                print("Course Name is-"+courseName)
                                                break
                                        collegeName=uniqueWords3(msg,words,courseName)
                                        print("College Name is-"+collegeName)
                                        collegeId=None
                                        if CollegeDetails.objects.filter(name=collegeName).first()!=None or CollegeDetails.objects.filter(shortForm=collegeName).first()!=None:
                                            collegeId=CollegeDetails.objects.filter(shortForm=collegeName).first()
                                        if collegeId!=None:
                                            print("KKLLKK"+courseName)
                                            cobj=Courses.objects.filter(cid=collegeId.id,name=courseName).first()
                                            respf = 'The '+cobj.name+' course at '+collegeId.name+' has '+str(cobj.seats)+' seats available.'
                                        else:
                                            respf = 'There is no college or course of requested type. Sorry.'
                                    else:
                                        respf = 'There is no college or course of requested type. Sorry.'
                                    voice = getTextToSpeech(respf)

                                    response = {'status': "Success", 'respmsg': respf,
                                                'respvoice': voice}
                            else:
                                respf = random.choice(resp)
                            voice = getTextToSpeech(respf)
                            response = {'status': "Success", 'respmsg': respf,
                                        'respvoice': voice}

                            break
        else:
            voice = getTextToSpeech("Unable to understand you.Sorry.")
            response = {'status': "Success", 'respmsg': "Unable to understand you.Sorry.", 'respvoice': voice}
    except Exception as e:
        print(str(e))

    return JsonResponse(response,safe=False)



def is_part(some_string, target):
    return target in some_string

def dataPickle():
    words = []
    labels = []
    docs_x = []
    docs_y = []

    with open(os.getcwd() + os.path.sep + "intents.json") as f:
        data = json.load(f)
        for intent in data["intents"]:
            for pattern in intent["patterns"]:
                wrds = nltk.word_tokenize(pattern)
                words.extend(wrds)
                docs_x.append(wrds)
                docs_y.append(intent["tag"])

            if intent["tag"] not in labels:
                labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w != "?"]
    words = sorted(list(set(words)))

    labels = sorted(labels)
    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []

        wrds = [stemmer.stem(w.lower()) for w in doc]

        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)

    tensorflow.reset_default_graph()

    net = tflearn.input_data(shape=[None, len(training[0])])
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, 8)
    net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
    net = tflearn.regression(net)

    model = tflearn.DNN(net)

    model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)
    model.save("model.tflearn")

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def uniqueWords(msg,words):
    resword=''
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(msg)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    allwords=msg.lower().split(" ")
    for w in allwords:
        cnt=0
        for s in words:
            if w!='a' and w!='of' and w!='and' and w!='engineering' and w!='research' and w!='college' and w!=s and w!='institute'\
                    and w!='technology' and w!='admission' and w!='criteria' and w!='what' and w!='for' and w!='regarding' and w!='fee'\
                    and w!='fees' and w!='information' and w!='please' and w!='give'  and w!='admitted' and w!='percentage'\
                    and w!='required' and w!='in' and w!='college' and w!=' ' and w.strip()!='' and w!='college' and w!='colleges'\
                    and w!='aegis' and w!='me' and w!='you' and w!='share' and w!='all' and w!='list' and w!='of' and w!='the'\
                    and w!='fall' and w!='falls' and w!='does' and w!='offer' and w!='at' and w!='available' and w!='opt' and w!='for':
                cnt=cnt+1
        if cnt==len(words):

            resword= w
    print(resword)

    return resword

def uniqueWords3(msg,words,course):
    resword=''
    cautionword=''

    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(msg)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    allwords=msg.lower().split(" ")

    for w in allwords:
        cnt=0
        for s in words:
            if w!='a' and w!='of' and w!='bachelors' and w!="bachelor's" and w!='and' and w!='engineering' and w!='research' and w!='college' and w!=s and w!='institute'\
                    and w!='technology' and w!='admission' and w!='criteria' and w!='what' and w!='for' and w!='regarding' and w!='fee'\
                    and w!='fees' and w!='information' and w!='please' and w!='give'  and w!='admitted' and w!='percentage'\
                    and w!='required' and w!='in' and w!='college' and w!=' ' and w.strip()!='' and w!='college' and w!='colleges'\
                    and w!='aegis' and w!='me' and w!='you' and w!='share' and w!='all' and w!='list' and w!='of' and w!='the'\
                    and w!='fall' and w!='falls' and w!='does' and w!='offer' and w!='at' and w!='available' and w!='opt' and w!='for'\
                    and w!='seats' and w!='want' and w!='wanted' and w!='course' and w!='number' and w!='how' and w!='offer' and w!='offered'\
                    and w!='offers':
                if is_part(course.lower(),w)==False:

                    cnt = cnt + 1


        if cnt==len(words):

            resword= w


    return resword


def uniqueWords2(msg,words):
    resword=''
    bag = [0 for _ in range(len(words))]
    s_words = nltk.word_tokenize(msg)
    s_words = [stemmer.stem(word.lower()) for word in s_words]
    allwords=msg.lower().split(" ")
    for w in allwords:
        cnt=0
        for s in words:
            if w!='a' and w!='of' and w!='and' and w!='research' and w!='college' and w!=s and w!='institute'\
                    and w!='technology' and w!='admission' and w!='criteria' and w!='what' and w!='for' and w!='regarding' and w!='fee'\
                    and w!='fees' and w!='information' and w!='please' and w!='give'  and w!='admitted' and w!='percentage'\
                    and w!='required' and w!='in' and w!='college' and w!=' ' and w.strip()!='' and w!='college' and w!='colleges'\
                    and w!='aegis' and w!='me' and w!='you' and w!='share' and w!='all' and w!='list' and w!='of' and w!='the'\
                    and w!='fall' and w!='falls' and w!='based':
                cnt=cnt+1
        if cnt==len(words):
            print(w)
            resword= w
    print(resword)
    return resword



@csrf_exempt
def getTextToSpeech(msg):
    base64_encoded=''
    try:
        pythoncom.CoInitialize()

        if os.path.exists(os.getcwd() + os.path.sep + "Temp" ) == False:
            os.mkdir(os.getcwd() + os.path.sep + "Temp" )
        speak = wincl.Dispatch("SAPI.SpVoice")

        tts = gTTS(text=msg, lang='en')

        tts.save(os.getcwd() + os.path.sep + "Temp" + os.path.sep + "pcvoice.mp3")
        print("TTT")
        data =''
        with open(os.getcwd() + os.path.sep + "Temp" + os.path.sep + "pcvoice.mp3", 'rb') as f:
            data = f.read()
        print("XXX")
        base64_encoded = base64.b64encode(data).decode('UTF-8')
        print("CCC")

        os.remove(os.getcwd()+os.path.sep+"Temp"+os.path.sep+"pcvoice.mp3")
        os.rmdir(os.getcwd()+os.path.sep+"Temp")
    except Exception as e:
        if os.path.exists(os.getcwd() + os.path.sep + "Temp" + os.path.sep + "pcvoice.mp3"):
            os.remove(os.getcwd()+os.path.sep+"Temp"+os.path.sep+"pcvoice.mp3")
            os.rmdir(os.getcwd() + os.path.sep + "Temp")
        elif os.path.exists(os.getcwd() + os.path.sep + "Temp"):
            os.rmdir(os.getcwd() + os.path.sep + "Temp")
        print(str(e))

    return base64_encoded
"""