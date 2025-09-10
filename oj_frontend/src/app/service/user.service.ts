import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environment'

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private baseUrl: string = environment.baseUrl
  constructor(private http: HttpClient) { }

  userDetails(): Observable<any> {
    return this.http.get(`${this.baseUrl}/auth/user-details/`)
  }
}
