import { Component, signal, OnInit } from '@angular/core';
import { RouterOutlet, ActivatedRoute } from '@angular/router';
import { ClientesService } from './services/clientes';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})

export class App implements OnInit {
  clientes = signal<any[]>([]);
  private mostrarInativosAtual = false;

  constructor(
    private clientesService: ClientesService,
    private route: ActivatedRoute
  ) {}

  ngOnInit() {
    this.route.queryParamMap.subscribe(params => {
      this.mostrarInativosAtual = params.get('mostrar_inativos') === '1';
      this.carregarClientes(this.mostrarInativosAtual);
    });
  }

  carregarClientes(mostrarInativos: boolean) {
    this.clientesService
      .listar(mostrarInativos)
      .subscribe(data => {
        this.clientes.set(data);
      });
  }

  inativar(id: number) {
    this.clientesService.inativar(id).subscribe(() => {
      this.carregarClientes(this.mostrarInativosAtual);
    });
  }

  reativar(id: number) {
    this.clientesService.reativar(id).subscribe(() => {
      this.carregarClientes(this.mostrarInativosAtual);
    });
  }
}