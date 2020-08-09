import { Component, OnInit } from '@angular/core';
import { HttpClientModule, HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-first',
  templateUrl: './first.component.html',
  styleUrls: ['./first.component.css']
})
export class FirstComponent implements OnInit {

  constructor(private httpClient: HttpClient) { }
django=null
  ngOnInit(): void {
   
    this.django=this.httpClient.get('http://127.0.0.1:8000/homePageView', {observe:'response'}).subscribe( res => { 
      console.log(res) ;
     this.django = res.body;
    
    });
    

  }
  public extractData(res: Response) {
    let body = res
    console.log("Body Data = "+body);
    return body || [];
  }
  private handleError(error: any): Promise<any> {
    console.error('An error occurred', error); // for demo purposes only
    return Promise.reject(error.message || error);
 }
}
