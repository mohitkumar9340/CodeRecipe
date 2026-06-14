import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environment'

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private baseUrl: string = environment.baseUrl
  constructor(private http: HttpClient) { }

  login(userData: {username: string; password: string;}): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/login/`, userData)
  }
}
