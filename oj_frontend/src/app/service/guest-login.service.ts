import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environment'

@Injectable({
  providedIn: 'root'
})
export class GuestLoginService {
  private baseUrl: string = environment.baseUrl
  constructor(private http: HttpClient) { }
  
  guestLogin(userData: {}): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/guest-login/`, userData)
  }
}
