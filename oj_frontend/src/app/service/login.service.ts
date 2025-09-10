import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private baseUrl: string = "http://127.0.0.1:8000/"
  constructor(private http: HttpClient) { }

  login(userData: {username: string; password: string;}): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/login/`, userData)
  }
}
