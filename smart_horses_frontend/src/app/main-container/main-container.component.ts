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

  // Métodos para actualizar los puntos de cada jugador
  updateWhiteHorsePoints(points: number): void {
    this.whiteHorsePoints += points;
  }

  updateBlackHorsePoints(points: number): void {
    this.blackHorsePoints += points;
  }


}
