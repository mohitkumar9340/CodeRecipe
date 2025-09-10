import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  private baseUrl: string = "http://127.0.0.1:8000"
  constructor(private http: HttpClient) { }

  register(userdata: {username: string; password: string; email: string;}): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/register/`, userdata)
  }
}