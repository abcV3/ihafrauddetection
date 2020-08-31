import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FirstComponent } from './first/first.component';
import { SecondcomponentComponent } from './secondcomponent/secondcomponent.component';
import { ThirdComponent } from './third/third.component';
import { UnivariateComponent } from './univariate/univariate.component';
import { MultivariateComponent } from './multivariate/multivariate.component';

@NgModule({
  declarations: [
    AppComponent,
    FirstComponent,
    SecondcomponentComponent,
    ThirdComponent,
    UnivariateComponent,
    MultivariateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
