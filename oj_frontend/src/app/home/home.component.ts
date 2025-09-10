import { Component, OnInit } from '@angular/core';
import { ProblemService } from '../service/problem.service';
import { RouterLink } from '@angular/router';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatDividerModule } from '@angular/material/divider';
import { HeaderComponent } from '../header/header.component';
import { MatChipsModule } from '@angular/material/chips';
import { MatSelectModule } from '@angular/material/select';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { FormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatFormField } from '@angular/material/form-field';
import { PageEvent } from '@angular/material/paginator';
import { MatPaginatorModule } from '@angular/material/paginator';



interface Tag {
  name: string;
}
@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    RouterLink,
    CommonModule,
    MatFormFieldModule,
    MatListModule,
    MatIconModule,
    MatButtonModule,
    MatCardModule,
    MatToolbarModule,
    MatDividerModule,
    HeaderComponent,
    MatChipsModule,
    MatSelectModule,
    MatSlideToggleModule,
    FormsModule,
    MatInputModule,
    MatFormField,
    MatPaginatorModule

  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  problems: any[] = [];
  allTags: any[] = [];
  filteredProblems: any[] = [];
  selectedDifficulty: string = '';
  selectedTags: string[] = [];
  selectedSort: string = 'title';
  difficulties = ['Easy', 'Medium', 'Hard'];
  hideTags: boolean = false;
  searchQuery: string = '';          // Search input (Define this property)
  totalProblems = 0;
  currentPage = 1;
  problemsPerPage: number = 4;
  constructor(private problemService: ProblemService) { }
  ngOnInit(): void {
    this.getProblems(this.currentPage);

    // this.problemService.getProblems(this.currentPage).subscribe(
    //   (data) => {
    //     console.log(data)
    //     this.problems = data;
    //     this.filteredProblems = data;
    //   },
    //   (error) => {
    //     console.error('Error fetching problems', error);
    //   }
    // );
    this.problemService.getTags().subscribe(
      (data) => {
        console.log(data)
        this.allTags = data;
      },
      (error) => {
        console.error('Error fetching tags', error);
      }
    );
  }

  getProblems(page: number) {
    this.problemService.getProblems(page).subscribe(
      (data) => {
        console.log(data)
        this.problems = data.problems;
        this.filteredProblems = data.problems;
        this.totalProblems = data.total_problems;
      },
      (error) => {
        console.error('Error fetching problems', error);
      }
    );
  }


  applyFilters() {
    console.log('Applying filters', this.searchQuery);
    this.filteredProblems = this.problems.filter((problem) => {
      const matchesSearchQuery = problem.title.toLowerCase().includes(this.searchQuery.toLowerCase());
      const matchesDifficulty = this.selectedDifficulty ? problem.difficulty === this.selectedDifficulty : true;
      const matchesTags = this.selectedTags.length
        ? this.selectedTags.every(tag =>
          Array.isArray(problem.tag_names) && problem.tag_names.some((pTagName: string) => pTagName === tag)
        )
        : true;
      console.log(this.selectedTags);
      console.log('Matches search query:', matchesSearchQuery);

      return matchesSearchQuery && matchesDifficulty && matchesTags;
    });
    console.log('Filtered problems:', this.filteredProblems);
  }

  applySorting(): void {
    if (this.selectedSort === 'title') {
      this.filteredProblems.sort((a, b) => a.title.localeCompare(b.title));
    } else if (this.selectedSort === 'difficulty') {
      const order: { [key: string]: number } = { 'Easy': 1, 'Medium': 2, 'Hard': 3 };
      this.filteredProblems.sort((a, b) => order[a.difficulty] - order[b.difficulty]);
    }
  }

  onPageChange(event: PageEvent) {
    this.currentPage = event.pageIndex + 1;  // Paginator starts from 0
    this.problemsPerPage = event.pageSize; 
    this.getProblems(this.currentPage);
  }
}
