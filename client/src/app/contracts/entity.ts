export type EntityKind = 'PERSON' | 'COMPANY' | 'ADDRESS' | 'ACCOUNT';

export interface Entity {
  public_id: string;
  name: string;
  kind: EntityKind;
  country: string;
  created_at: string;
}

export interface DependencyStatus {
  ok: boolean;
  latency_ms: number;
  detail: string;
}

export interface HealthResponse {
  service: string;
  ok: boolean;
  dependencies: {
    database: DependencyStatus;
    redis: DependencyStatus;
  };
  correlation_id: string | null;
}
