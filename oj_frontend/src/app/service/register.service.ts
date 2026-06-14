import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environment'


@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  private baseUrl: string = environment.baseUrl
  constructor(private http: HttpClient) { }

  register(userdata: {username: string; password: string; email: string;}): Observable<any> {
    return this.http.post(`${this.baseUrl}/auth/register/`, userdata)
  }
}
