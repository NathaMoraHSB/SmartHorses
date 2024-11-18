import { Component, OnInit, Input, Output, EventEmitter, SimpleChanges, OnChanges, ChangeDetectorRef } from '@angular/core';
import { MatCard, MatCardContent } from "@angular/material/card";
import { NgClass } from "@angular/common";
import { CommonModule } from '@angular/common';
import { HttpClientModule } from "@angular/common/http";
import { MatButtonModule } from "@angular/material/button";
import {CeldaClickEvent} from "../celda-click-event";

@Component({
  selector: 'app-grid',
  standalone: true,
  imports: [
    NgClass,
    CommonModule,
    HttpClientModule,
    MatButtonModule,
    MatCardContent,
    MatCard,
  ],
  templateUrl: './grid.component.html',
  styleUrls: ['./grid.component.css']
})

export class GridComponent implements OnInit, OnChanges {
  @Input() grid: number[][] = [];
  @Input() turno_humano: boolean = false;
  @Output() celdaClick = new EventEmitter<CeldaClickEvent>();


  possibleMoves: [number, number][] = [];
  highlightCells: Set<string> = new Set();

  constructor(private cdr: ChangeDetectorRef) {}
  ngOnInit(): void {}

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['turno_humano'] && this.turno_humano) {
      console.log("ngOnChanges detected cambio en turno_humano:", this.turno_humano);
      this.highlightPossibleMoves();
    } else {
      console.log("ngOnChanges detected cambio en turno_humano pero turno_humano es false:", this.turno_humano);
      this.highlightCells.clear();
    }
  }

  movimientosPosibles(x: number, y: number, n: number): [number, number][] {
    const movimientos = [
      [2, 1], [2, -1], [-2, 1], [-2, -1],
      [1, 2], [1, -2], [-1, 2], [-1, -2]
    ];
    const movimientosValidos: [number, number][] = [];

    movimientos.forEach(([dx, dy]) => {
      const nx = x + dx;
      const ny = y + dy;
      if (0 <= nx && nx < n && 0 <= ny && ny < n && this.grid[nx][ny] !== 11 && this.grid[nx][ny] !== 12) {
        movimientosValidos.push([nx, ny]);
      }
    });

    return movimientosValidos;
  }

  highlightPossibleMoves(): void {
    const { x, y } = this.getBlackHorsePosition();
    console.log("Position of black horse:", { x, y });
    this.possibleMoves = this.movimientosPosibles(x, y, this.grid.length);
    this.highlightCells.clear();
    this.possibleMoves.forEach(([row, col]) => {
      this.highlightCells.add(`${row},${col}`);
    });
    console.log("highlightCells after calling highlightPossibleMoves:", Array.from(this.highlightCells));
    this.cdr.detectChanges(); // Forzar actualización visual
  }

  onCellClick(rowIndex: number, colIndex: number): void {
    console.log(`Clicked on cell: (${rowIndex}, ${colIndex})`);
    if (this.highlightCells.has(`${rowIndex},${colIndex}`)) {
      console.log("Cell is in highlightCells - emitting event for click.");

      this.celdaClick.emit({
        row: rowIndex,
        col: colIndex,
        matrix: this.grid
      });

      this.highlightCells.clear();
      this.turno_humano = false;
      this.cdr.detectChanges();
    } else {
      console.log("Cell not in highlightCells - click ignored.");
    }
  }




  getBlackHorsePosition(): { x: number; y: number } {
    for (let i = 0; i < this.grid.length; i++) {
      for (let j = 0; j < this.grid[i].length; j++) {
        if (this.grid[i][j] === 12) {
          return { x: i, y: j };
        }
      }
    }
    return { x: -1, y: -1 };
  }
}

