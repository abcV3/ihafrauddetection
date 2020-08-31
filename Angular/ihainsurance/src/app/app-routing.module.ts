import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { FirstComponent } from './first/first.component';
import { SecondcomponentComponent } from './secondcomponent/secondcomponent.component';
import { ThirdComponent } from './third/third.component';
import { UnivariateComponent } from './univariate/univariate.component';
import { MultivariateComponent } from './multivariate/multivariate.component';

@NgModule({
  imports: [RouterModule.forRoot([
    { path: 'firstcomponent', component: FirstComponent },
    { path: 'secondcomponent', component: SecondcomponentComponent },
    { path: 'thirdcomponent', component: ThirdComponent },
    { path: 'univariatecomponent', component: UnivariateComponent },
    { path: 'multivariatecomponent', component: MultivariateComponent }
    
  ])],
  exports: [RouterModule]
})
export class AppRoutingModule { }
