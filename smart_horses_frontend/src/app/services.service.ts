import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import {catchError, Observable, throwError} from 'rxjs';
import { tap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ServicesService {
  private baseUrl = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) { }

  startMatrix(): Observable<any> {
    console.log('Starting simulation...');
    return this.http.post<any>(`${this.baseUrl}/start`, {}).pipe(
      tap(response => console.log('Simulation started, initial matrix:', response))
    );
  }
}
