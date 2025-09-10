import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ProblemService {

  private baseUrl: string = "http://127.0.0.1:8000"
  constructor(private http: HttpClient) { }

  getProblems(page: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/main/problems/?page=${page}`)
  }

  getProblemById(id: string): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/main/problems/${id}`);
  }
  runCode(data: {code: string; language: string; input_data: string;}): Observable<any> {
    return this.http.post(`${this.baseUrl}/main/run/`, data)
  }
  submitCode(data: {code: string; language: string; problem: string;}): Observable<any> {
    return this.http.post(`${this.baseUrl}/main/submit/`, data)
  }
  getTags(): Observable<any> {
    return this.http.get(`${this.baseUrl}/main/tags/`)
  }

  getUserSubmissions(id: string): Observable<any> {
    const params = new HttpParams().set('id', id);
    return this.http.get(`${this.baseUrl}/main/submissionsUser/`, {params})
  }

  getProblemSubmissions(id: string): Observable<any> {
    const params = new HttpParams().set('id', id); 
    return this.http.get(`${this.baseUrl}/main/submissionsAll/`, {params})
  }
}
