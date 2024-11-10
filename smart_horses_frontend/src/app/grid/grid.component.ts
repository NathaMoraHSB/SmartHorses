import {Component, OnInit} from '@angular/core';
import {MatCard, MatCardContent} from "@angular/material/card";
import {NgClass, NgOptimizedImage} from "@angular/common";
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-grid',
  standalone: true,
  imports: [
    MatCard,
    MatCardContent,
    NgClass, CommonModule, NgOptimizedImage
  ],
  templateUrl: './grid.component.html',
  styleUrl: './grid.component.css'
})

export class GridComponent implements OnInit {

  grid: number[][] = [
    [8, 0, 0, 0, 4, 0, 20, 0],
    [0, 20, 1, 0, 0, 0, 0, 0],
    [0, 9, 0, 0, 12, 0, 20, 0],
    [0, 0, 7, 0, 0, 3, 0, 0],
    [10, 0, 0, 0, 0, 0, 6, 0],
    [20, 0, 0, 0, 0, 0, 0, 0],
    [0, 11, 0, 5, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
  ];

  ngOnInit(): void {

  }


}
