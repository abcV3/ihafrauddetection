import { Component } from '@angular/core';

import { Router, ActivatedRoute, NavigationEnd } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ihainsurance';
  constructor(/*private httpClient: HttpClient*/private router: Router) { }
django:string=''
  /*public getNews(){
    return this.httpClient.get(`http://127.0.0.1:8000/homePageView`);
  }*/
  loginPage(){
    
this.router.navigate(['/firstcomponent'])
  }

}
