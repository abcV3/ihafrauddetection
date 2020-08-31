import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-multivariate',
  templateUrl: './multivariate.component.html',
  styleUrls: ['./multivariate.component.css']
})
export class MultivariateComponent implements OnInit {

  file;
  normalDistribution;
  raceWise;
  insuranceClaim;
  tid;
  

  constructor(private router: ActivatedRoute,private router2: Router,private httpClient: HttpClient) { }

  ngOnInit(): void {
    console.log("ssss")
    this.router.queryParams.subscribe(params => {
      this.tid = params['tid'];
      
  });
    this.httpClient.get('http://127.0.0.1:8000/generateMultivarite?tid='+this.tid, {observe:'response'}).subscribe( res => { 
     
      this.file = res.body['responseObject'];
   
      this.normalDistribution='data:image/jpeg;base64,' + this.file.normalDistribution;
      this.raceWise='data:image/jpeg;base64,' + this.file.raceWise;
      this.insuranceClaim='data:image/jpeg;base64,' + this.file.insuranceClaim;
     });

  }

}
