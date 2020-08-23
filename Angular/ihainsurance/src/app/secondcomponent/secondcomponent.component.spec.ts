import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SecondcomponentComponent } from './secondcomponent.component';

describe('SecondcomponentComponent', () => {
  let component: SecondcomponentComponent;
  let fixture: ComponentFixture<SecondcomponentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SecondcomponentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SecondcomponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
