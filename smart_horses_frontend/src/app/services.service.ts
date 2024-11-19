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

  startSimulation(): Observable<any> {
    console.log('Starting simulation...');
    return this.http.post<any>(`${this.baseUrl}/partidaIaVSIa`, {}).pipe(
      tap(response => console.log('Simulation started, response:', response)),
      catchError(this.handleError)  // Manejo de errores
    );
  }

  startHumanVsMachineGame(): Observable<any> {
    console.log('Solicitud de primera jugada a la maquina...');
    return this.http.post<any>(`${this.baseUrl}/partidaIaVSIa`, {}).pipe(
      tap(response => console.log('Simulation started, response:', response)),
      catchError(this.handleError)  // Manejo de errores
    );
  }

  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      // Error del lado del cliente o red
      console.error('An error occurred:', error.error.message);
    } else {
      // Error del lado del servidor
      console.error(`Backend returned code ${error.status}, body was: ${error.error}`);
    }
    return throwError('Something bad happened; please try again later.');
  }

  sendHumanMove(data: any): Observable<any> {
    console.log('Enviando movimiento del humano al backend...', data);
    return this.http.post<any>(`${this.baseUrl}/human-move`, data).pipe(
      tap(response => console.log('Movimiento enviado, respuesta del backend:', response)),
      catchError(this.handleError)
    );
  }

  sendMachineMove(data: any): Observable<any> {
    console.log('Enviando movimiento de la máquina al backend...', data);
    return this.http.post<any>(`${this.baseUrl}/machineMove`, data).pipe(
      tap(response => console.log('Movimiento de la máquina enviado, respuesta del backend:', response)),
      catchError(this.handleError)
    );
  }


}
