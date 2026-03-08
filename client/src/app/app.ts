import { Component, inject } from '@angular/core';
import { AsyncPipe, JsonPipe } from '@angular/common';
import { TypedApiService } from './contracts/typed-api.service';
import { Observable } from 'rxjs';
import { HealthResponse } from './contracts/entity';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [AsyncPipe, JsonPipe],
  template: `
    <main style="font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial; padding: 16px;">
      <h1>FinCrime GraphOps (Day Zero)</h1>
      <p>Typed client → OpenAPI-first Django API</p>

      <button (click)="refresh()">Refresh health</button>

      <h2>Health</h2>
      <pre>{{ health$ | async | json }}</pre>
    </main>
  `
})
export class App {
  private readonly api = inject(TypedApiService);
  health$!: Observable<HealthResponse>;

  constructor() {
    this.refresh();
  }

  refresh(): void {
    const cid = crypto.randomUUID();
    this.health$ = this.api.health(cid);
  }
}
