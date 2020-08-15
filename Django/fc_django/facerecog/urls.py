# pages/urls.py
from django.urls import path
#from .views import addCollege,updateFeeDetails,getCourseDetails,addFeeDetails,addCourse,getFeeDetails,deleteCourse,updateCourse,deleteCollege,updateCollege,getEmpDetails,getCollegeDetails,addEmployee,updateEmployee,deleteEmployee,savePhoto,markAttendance,getAttendance,getMonthlyReport,addLoginCredentials,mcresponse,login,getTextToSpeech
from facerecog import views
from .views import saveFile,getAll

urlpatterns = [

    path('saveFile', saveFile, name='saveFile'),
    path('getAll', getAll, name='getAll')

]

