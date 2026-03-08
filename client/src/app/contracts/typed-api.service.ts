import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HealthResponse } from './entity';

@Injectable({ providedIn: 'root' })
export class TypedApiService {
  private readonly http = inject(HttpClient);
  private readonly baseUrl = 'http://127.0.0.1:8000';

  health(correlationId?: string): Observable<HealthResponse> {
    const headers = correlationId
      ? new HttpHeaders({ 'X-Correlation-ID': correlationId })
      : new HttpHeaders();

    return this.http.get<HealthResponse>(`${this.baseUrl}/api/health/`, { headers });
  }
}
