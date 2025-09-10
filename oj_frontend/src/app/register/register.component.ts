import { Component } from '@angular/core';
import { Validators, FormsModule, ReactiveFormsModule, FormControl, FormGroupDirective, NgForm } from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';
import { merge } from 'rxjs';
import { MatButtonModule } from '@angular/material/button';
import { RegisterService } from '../service/register.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { MatCardModule } from '@angular/material/card';
import {ErrorStateMatcher} from '@angular/material/core';
import {GuestLoginService} from '../service/guest-login.service';

export class MyErrorStateMatcher implements ErrorStateMatcher {
  isErrorState(control: FormControl | null, form: FormGroupDirective | NgForm | null): boolean {
    const isSubmitted = form && form.submitted;
    return !!(control && control.invalid && (control.dirty || control.touched || isSubmitted));
  }
}



@Component({
  selector: 'app-register',
  standalone: true,
  imports: [
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatIconModule,
    FormsModule,
    ReactiveFormsModule,
    MatButtonModule,
    CommonModule,
    RouterModule,
    MatCardModule,
  ],
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})



export class RegisterComponent {
  hide = true;
  clickEvent(event: MouseEvent) {
    this.hide = !this.hide;
    event.stopPropagation();
  }
  emailFormControl = new FormControl('', [Validators.required, Validators.email]);
  matcher = new MyErrorStateMatcher();
  username: string = '';
  email: string = '';
  password: string = '';

  // errorMessage = '';

  constructor(private registerService: RegisterService, private guestService: GuestLoginService, private router: Router) {}



  isValidEmail(email: string): boolean {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  onSubmit() {
    console.log("Form submitted",this.username, this.email, this.password);
    this.registerService.register({username: this.username, email: this.email, password: this.password}).subscribe(
      response => {
        console.log('Registration successful', response);
        this.router.navigate(['login-component']).then(
          (nav) => {
            console.log('Navigation successful:', nav);
          },
          (err) => {
            console.error('Navigation failed:', err);
          }
        );
      },
      error => {
        console.error('Registration failed', error);
      }
    );
  }

  guestLogin() {
    // Handle guest login logic here
    console.log("Guest login clicked");
    // For example, you could navigate to a specific page or trigger guest login on the backend.
    this.guestService.guestLogin({}).subscribe(
      response => {
        console.log('Guest login successful', response);
        localStorage.setItem('access_token', response.token.access);
        localStorage.setItem('refresh_token', response.token.refresh);
        this.router.navigate(['/home-component']);
      },
      error => {
        console.error('Guest login failed', error);
      }
    );
  }
}
