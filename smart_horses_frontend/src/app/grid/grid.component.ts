import {Component, OnInit, Input} from '@angular/core';
import {MatCard, MatCardContent} from "@angular/material/card";
import {NgClass} from "@angular/common";
import { CommonModule } from '@angular/common';
import {HttpClientModule} from "@angular/common/http";
import {MatButtonModule} from "@angular/material/button";

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
  styleUrl: './grid.component.css'
})

export class GridComponent implements OnInit {

  @Input() grid: number[][] = [];


  ngOnInit(): void {

  }


}
