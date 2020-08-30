import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UnivariateComponent } from './univariate.component';

describe('UnivariateComponent', () => {
  let component: UnivariateComponent;
  let fixture: ComponentFixture<UnivariateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UnivariateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UnivariateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
