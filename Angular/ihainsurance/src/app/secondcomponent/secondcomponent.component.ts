import { Component, OnInit } from '@angular/core';
import { Router,ActivatedRoute, ParamMap } from '@angular/router';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-secondcomponent',
  templateUrl: './secondcomponent.component.html',
  styleUrls: ['./secondcomponent.component.css']
})
export class SecondcomponentComponent implements OnInit {
id:any;
file :Blob;
base64textString=null;
django=null;
files:any={}
fileToUpload: File = null;
  constructor(private router: ActivatedRoute,private router2: Router,private httpClient: HttpClient) { }

  ngOnInit(): void {
    this.router.queryParams.subscribe(params => {
      this.id = params['id'];
      
  });

  this.files=this.httpClient.get('http://127.0.0.1:8000/getAllTest?tid='+this.id, {observe:'response'}).subscribe( res => { 
     
      this.files = res.body['responseObject'];
   
      console.log(this.files)
      
     });
  }

  third(ID){
    this.router2.navigate(['/thirdcomponent'],{queryParams: { tid: this.id ,testID:ID}})
  }
  handleFileInput(files: FileList) {
    this.fileToUpload = files.item(0);
   // let me = this;
    this.file = this.fileToUpload;
   let reader = new FileReader();
let response=null;
   reader.readAsDataURL(this.file);
   reader.onload =this.handleFile.bind(this);
   


   reader.onerror = function (error) {
     console.log('Error: ', error);
   };



}


handleFile(event) {
  var binaryString = event.target.result;
         this.base64textString= binaryString
         
        
         let body={
          'filename':this.fileToUpload.name,
          'actualfile':this.base64textString,
          'tid':this.id
        }
     
     
     
     let body2=JSON.stringify(body)
     console.log(this.base64textString)
     this.django=this.httpClient.post('http://localhost:8000/saveTestFile',body2, {observe:'response'}).subscribe( res => { 
      console.log(res) ;

     let response = res.body;
    alert(response['status']+' '+response['responseObject'])
    location.reload()
    });

 }
}
