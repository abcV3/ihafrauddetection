import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-univariate',
  templateUrl: './univariate.component.html',
  styleUrls: ['./univariate.component.css']
})
export class UnivariateComponent implements OnInit {
  file;
  tid;

  constructor(private router: ActivatedRoute,private router2: Router,private httpClient: HttpClient) { }

  ngOnInit(): void {
    console.log("ssss")
    this.router.queryParams.subscribe(params => {
      this.tid = params['tid'];
      
  });
    this.file=this.httpClient.get('http://127.0.0.1:8000/generateUnivarite?tid='+this.tid, {observe:'response'}).subscribe( res => { 
     
      this.file = res.body['responseObject'];
   
      this.file='data:image/jpeg;base64,' + this.file;
      
     });

  }

}
