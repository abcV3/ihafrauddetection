import { Component, OnInit } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';


@Component({
  selector: 'app-first',
  templateUrl: './first.component.html',
  styleUrls: ['./first.component.css']
})
export class FirstComponent implements OnInit {

  constructor(private httpClient: HttpClient,private router: Router) { }
files:any={};
django=null
file :Blob;

base64textString=null
fileToUpload: File = null;
  ngOnInit(): void {
   
    this.files=this.httpClient.get('http://127.0.0.1:8000/getAll', {observe:'response'}).subscribe( res => { 
     
     this.files = res.body['responseObject'];
  

     
    });
    

  }
  public extractData(res: Response) {
    let body = res
    console.log("Body Data = "+body);
    return body || [];
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
second(ID){
  this.router.navigate(['/secondcomponent'],{queryParams: { id: ID }})
}
handleFile(event) {
  var binaryString = event.target.result;
         this.base64textString= binaryString
         
        
         let body={
          'filename':this.fileToUpload.name,
          'actualfile':this.base64textString
        }
     
     
     
     let body2=JSON.stringify(body)
     console.log(this.base64textString)
     this.django=this.httpClient.post('http://localhost:8000/saveFile',body2, {observe:'response'}).subscribe( res => { 
      console.log(res) ;

     let response = res.body;
    alert(response['status']+' '+response['responseObject'])
    location.reload()
    });

 }



  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
 }
}
