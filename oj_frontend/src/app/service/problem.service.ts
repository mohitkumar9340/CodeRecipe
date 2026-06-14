import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environment'

@Injectable({
  providedIn: 'root'
})
export class ProblemService {

  private baseUrl: string = environment.baseUrl
  constructor(private http: HttpClient) { }

  getProblems(page: number, filters?: { difficulty?: string; search?: string; tags?: string; status?: string }): Observable<any> {
    let params = new HttpParams().set('page', page);
    if (filters?.difficulty) params = params.set('difficulty', filters.difficulty);
    if (filters?.search) params = params.set('search', filters.search);
    if (filters?.tags) params = params.set('tags', filters.tags);
    if (filters?.status) params = params.set('status', filters.status);
    return this.http.get(`${this.baseUrl}/main/problems/`, { params })
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

  getSubmissions(problemId: string): Observable<any> {
    const params = new HttpParams().set('id', problemId);
    return this.http.get(`${this.baseUrl}/main/submissions/`, {params})
  }
}
