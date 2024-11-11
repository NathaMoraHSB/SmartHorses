import { Component } from '@angular/core';
import {GridComponent} from "../grid/grid.component";
import {MatCard, MatCardContent, MatCardHeader, MatCardModule} from "@angular/material/card";
import {ServicesService} from "../services.service";

@Component({
  selector: 'app-main-container',
  standalone: true,
  imports: [
    GridComponent,
    MatCard,
    MatCardHeader,
    MatCardContent,
    MatCardModule
  ],
  templateUrl: './main-container.component.html',
  styleUrl: './main-container.component.css'
})
export class MainContainerComponent {

  grid: number[][] = [];
  whiteHorsePoints: number = 0;
  blackHorsePoints: number = 0;
  simulationInterval: any;

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
    this.matrixService.startSimulation().subscribe(
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
              // Stop the interval when we've shown all matrices
              clearInterval(this.simulationInterval);
              console.log("Simulation complete");
            }
          }, 1000); // Change interval time as needed (1000 ms = 1 second)

        } else {
          console.error('Simulation data or report not received');
        }
      },
      error => {
        console.error('Error during simulation:', error);
      }
    );
  }
}
