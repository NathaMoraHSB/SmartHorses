import {ChangeDetectorRef, Component, Input, OnChanges, OnInit, SimpleChanges} from '@angular/core';
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

  constructor(private matrixService: ServicesService, private cdr: ChangeDetectorRef) {}

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

  machineTurn() {
    console.log("Turno de la maquina");
    this.sendMachineMoveToBack();



  }

  runIaVsHumanSimulation(): void {
    console.log("Running IA vs Humano simulation...");
    this.machineTurn();

  }

  handleCeldaClick(event: CeldaClickEvent): void {
    console.log("Celda clickeada:", event);

    const { row, col, matrix } = event;
    this.grid = matrix;

    this.sendHumanMoveToBackend({
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

  sendHumanMoveToBackend(data: any): void {
    console.log("Enviando datos al backend:", data);
    this.matrixService.sendHumanMove(data).subscribe(
      response => {
        console.log("Respuesta del backend:", response);

        this.grid = response.matrix;
        this.blackHorsePoints = response.blackHorsePoints;
        this.dos_x_negro = response.dos_x_tomado;
        this.whiteHorsePoints = response.whiteHorsePoints;
        this.dos_x_blanco = response.dos_x_blanco;
        this.difficultyLevel = response.difficultyLevel;
        this.cdr.detectChanges();

        console.log("Estado actualizado despues Human move:", {
          grid: this.grid,
          blackHorsePoints: this.blackHorsePoints,
          dos_x_negro: this.dos_x_negro,
          whiteHorsePoints: this.whiteHorsePoints,
          dos_x_blanco: this.dos_x_blanco,
          difficultyLevel: this.difficultyLevel
        });
      },
      error => {
        console.error("Error al enviar datos al backend:", error);
      }
    );
    this.turno_humano=false

    if (this.quedan_puntos) {
      this.machineTurn();  // Llamar al turno de la máquina
    } else {
      this.endGame();
    }

  }

  sendMachineMoveToBack(): void {
    const data = {
      matrix: this.grid,
      whiteHorsePoints: this.whiteHorsePoints,
      blackHorsePoints: this.blackHorsePoints,
      quedan_puntos: this.quedan_puntos,
      dos_x_blanco: this.dos_x_blanco,
      dos_x_negro: this.dos_x_negro,
      difficultyLevel: this.difficultyLevel
    };

    // Enviar la información al backend usando el servicio
    this.matrixService.sendMachineMove(data).subscribe(
      response => {
        console.log("Respuesta del backend después del turno de la máquina:", response);

        // Actualizar el estado del componente con la respuesta del backend
        this.grid = response.matrix;
        this.whiteHorsePoints = response.whiteHorsePoints;
        this.blackHorsePoints = response.blackHorsePoints;
        this.dos_x_blanco = response.dos_x_blanco;
        this.dos_x_negro = response.dos_x_negro;
        this.quedan_puntos = response.quedan_puntos;

        // Refrescar la vista para reflejar los cambios
        this.cdr.detectChanges();

      },
      error => {
        console.error("Error al enviar datos de machineTurn al backend:", error);
      }
    );

    if (this.quedan_puntos) {
      this.turno_humano= true;
    } else {
      this.endGame();
    }
  }
  endGame(): void {
    console.log("El juego ha terminado");
    this.juego_en_curso = false;
    // Puedes realizar más acciones al final del juego, como mostrar una alerta o reiniciar la interfaz.
  }




  ngOnChanges(changes: SimpleChanges): void {
  }
}
