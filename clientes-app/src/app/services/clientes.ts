import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ClientesService {

  private api = 'http://127.0.0.1:8000/api/clientes/';

  constructor(private http: HttpClient) {}

  listar(mostrarInativos: boolean = false) {
    const url = mostrarInativos
      ? `${this.api}?mostrar_inativos=1`
      : this.api;

    return this.http.get<any[]>(url);
  }

  inativar(id: number) {
    return this.http.patch(`${this.api}${id}/inativar/`, {});
  }

  reativar(id: number) {
    return this.http.patch(`${this.api}${id}/reativar/`, {});
  }

}