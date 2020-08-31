import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-third',
  templateUrl: './third.component.html',
  styleUrls: ['./third.component.css']
})
export class ThirdComponent implements OnInit {
tid;
  constructor(private router: ActivatedRoute,private router2: Router,private httpClient: HttpClient) { }
  file;
  ngOnInit(): void {
    this.router.queryParams.subscribe(params => {
      this.tid = params['tid'];
      
  });
  }
  univariate(){
    console.log("SSS")
    this.router2.navigate(['/univariatecomponent'],{queryParams: { tid: this.tid }})
    

  }
  multivariate(){
    console.log("SSS")
    this.router2.navigate(['/multivariatecomponent'],{queryParams: { tid: this.tid }})
    

  }
}
