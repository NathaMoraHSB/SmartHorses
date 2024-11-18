import {Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import { GridComponent } from "../grid/grid.component";
import { MatCard, MatCardContent, MatCardHeader, MatCardModule } from "@angular/material/card";
import { MatFormFieldModule } from "@angular/material/form-field";
import { MatSelectModule } from "@angular/material/select";
import { MatRadioModule } from "@angular/material/radio";
import { MatButtonModule } from "@angular/material/button";
import { ServicesService } from "../services.service";
import {FormsModule} from "@angular/forms";
import {NgIf} from "@angular/common";
import {CeldaClickEvent} from "../celda-click-event";

@Component({
  selector: 'app-main-container',
  standalone: true,
  imports: [
    GridComponent,
    MatCard,
    MatCardHeader,
    MatCardContent,
    MatCardModule,
    MatFormFieldModule,
    MatSelectModule,
    MatRadioModule,
    MatButtonModule,
    FormsModule,
    NgIf
  ],
  templateUrl: './main-container.component.html',
  styleUrls: ['./main-container.component.css']
})
export class MainContainerComponent implements OnInit, OnChanges{
//Variable a enviar al backend
  grid: number[][] = [];
  whiteHorsePoints: number = 0;
  blackHorsePoints: number = 0;
  dos_x_blanco: boolean = false;
  dos_x_negro: boolean= false;
  difficultyLevel: number = 1;
  quedan_puntos: boolean = true;

  //Variables solo para el frontend
  simulationInterval: any;///para simulacion Ia vs IA
  humanVSmachine: boolean = false;
  juego_en_curso: boolean= false;
  turno_humano: boolean = false;

  constructor(private matrixService: ServicesService) {}

  ngOnInit() {
    this.startMatrix();
  }

  startMatrix(): void {
    this.matrixService.startMatrix().subscribe(
      response => {
        if (response && response.matrix) {
          this.grid = response.matrix;
          console.log('Matrix loaded:', this.grid);
        } else {
          console.error('No matrix received');
        }
      },
      error => {
        console.error('Error loading matrix:', error);
      }
    );
  }

  startSimulation(): void {
    this.juego_en_curso = true;
    if (!this.humanVSmachine) {
      this.runIaVsIaSimulation();
    } else {
      this.runIaVsHumanSimulation();
    }
  }

  updateHumanTurn(): void {
    this.turno_humano = true; // Activa el turno humano
    console.log("updateHumanTurn called - turno_humano set to true.");

  }

  runIaVsIaSimulation(): void {
    console.log("Running IA vs IA simulation...");
    /*this.matrixService.startSimulation().subscribe(
      response => {
        if (response && response.simulation && response.report) {
          const matrices = response.simulation; // Secuencia de matrices
          const report = response.report; // Puntos finales
          let index = 0;

          if (this.simulationInterval) {
            clearInterval(this.simulationInterval);
          }

          this.simulationInterval = setInterval(() => {
            if (index < matrices.length) {
              this.grid = matrices[index];
              this.whiteHorsePoints = index === matrices.length - 1 ? report["Puntos IA 1, caballo blanco"] : this.whiteHorsePoints;
              this.blackHorsePoints = index === matrices.length - 1 ? report["Puntos IA 2, caballo negro"] : this.blackHorsePoints;
              index++;
            } else {
              // Detiene el intervalo cuando se muestran todas las matrices
              clearInterval(this.simulationInterval);
              console.log("Simulation complete");
            }
          }, 1000);

        } else {
          console.error('Simulation data or report not received');
        }
      },
      error => {
        console.error('Error during simulation:', error);
      }
    );*/
  }

  resetGame(){
    this.whiteHorsePoints=0;
    this.blackHorsePoints =0;
    this.quedan_puntos= true;
    this.dos_x_blanco = false;
    this.dos_x_negro= false;
    this.startMatrix();
    this.juego_en_curso= false;
  }

  machineTurn(){
    console.log("Turno de la maquina");
    this.updateHumanTurn();

  }
  runIaVsHumanSimulation(): void {
    console.log("Running IA vs Humano simulation...");
    this.machineTurn();

  }

  handleCeldaClick(event: CeldaClickEvent): void {
    console.log("Celda clickeada:", event);

    const { row, col, matrix } = event;
    this.grid = matrix;

    this.sendDataToBackend({
      matrix,

      selectedCell: { row, col },
      whiteHorsePoints: this.whiteHorsePoints,
      blackHorsePoints: this.blackHorsePoints,
      quedan_puntos: this.quedan_puntos,
      dos_x_blanco: this.dos_x_blanco,
      dos_x_negro: this.dos_x_negro,
      difficultyLevel: this.difficultyLevel
    });
  }

  sendDataToBackend(data: any): void {
    console.log("Enviando datos al backend:", data);
    this.matrixService.sendHumanMove(data).subscribe(
      response => {
        console.log("Respuesta del backend:", response);
        // Puedes actualizar el estado del componente aquí si es necesario
      },
      error => {
        console.error("Error al enviar datos al backend:", error);
      }
    );
  }

  ngOnChanges(changes: SimpleChanges): void {
  }
}
