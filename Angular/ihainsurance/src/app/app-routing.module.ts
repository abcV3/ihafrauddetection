import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FirstComponent } from './first/first.component';

@NgModule({
  imports: [RouterModule.forRoot([
    { path: 'firstcomponent', component: FirstComponent },
    
  ])],
  exports: [RouterModule]
})
export class AppRoutingModule { }
