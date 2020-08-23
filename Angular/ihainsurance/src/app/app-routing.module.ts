import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FirstComponent } from './first/first.component';
import { SecondcomponentComponent } from './secondcomponent/secondcomponent.component';

@NgModule({
  imports: [RouterModule.forRoot([
    { path: 'firstcomponent', component: FirstComponent },
    { path: 'secondcomponent', component: SecondcomponentComponent },
    
  ])],
  exports: [RouterModule]
})
export class AppRoutingModule { }
