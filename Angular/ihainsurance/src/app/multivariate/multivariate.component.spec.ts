import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MultivariateComponent } from './multivariate.component';

describe('MultivariateComponent', () => {
  let component: MultivariateComponent;
  let fixture: ComponentFixture<MultivariateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MultivariateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MultivariateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
