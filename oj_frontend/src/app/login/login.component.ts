import { Component, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatSelectModule } from '@angular/material/select';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { LoginService } from '../service/login.service';
import { MatCard } from '@angular/material/card';
import { MatCardModule } from '@angular/material/card';
import { RouterLink } from '@angular/router';
import { GuestLoginService } from '../service/guest-login.service';


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatIconModule,
    MatButtonModule,
    FormsModule,
    MatCard,
    MatCardModule,
    RouterLink
    ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})

export class LoginComponent {

  constructor(private loginService: LoginService, private guestService: GuestLoginService,private router: Router) {}
  username: string = '';
  password: string = '';

  hide =  true;

  onSubmit() {
    this.loginService.login({username: this.username, password: this.password}).subscribe({
      next: (response) => {
        localStorage.setItem('access_token', response.token.access);
        localStorage.setItem('refresh_token', response.token.refresh);
        localStorage.setItem('username', response.username);
        this.router.navigate(['/home-component']);
      },
      error: (error) => {
        console.error('Registration failed', error);
      }
    });
  }

  guestLogin() {
    this.guestService.guestLogin({}).subscribe({
      next: (response) => {
        localStorage.setItem('access_token', response.token.access);
        localStorage.setItem('refresh_token', response.token.refresh);
        localStorage.setItem('username', response.username);
        this.router.navigate(['/home-component']);
      },
      error: (error) => {
        console.error('Guest login failed', error);
      }
    });
  }

}
