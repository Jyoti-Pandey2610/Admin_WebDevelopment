import { Component } from '@angular/core';
import { Patient } from './model/patient.model';
import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  
  title = 'PatientApp';
  someHTML ='Some HTML <script> alert("hello"); </script>'
  myURL = 'javascript:alert("hello")';

}


