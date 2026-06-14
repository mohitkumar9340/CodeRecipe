import { Component, OnInit } from '@angular/core';
import { ProblemService } from '../service/problem.service';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatDividerModule } from '@angular/material/divider';
import { MatChipsModule } from '@angular/material/chips';
import { MatSelectModule } from '@angular/material/select';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { FormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatFormField } from '@angular/material/form-field';
import { PageEvent } from '@angular/material/paginator';
import { MatPaginatorModule } from '@angular/material/paginator';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    RouterLink, CommonModule, MatFormFieldModule, MatListModule, MatIconModule,
    MatButtonModule, MatCardModule, MatToolbarModule, MatDividerModule,
    MatChipsModule, MatSelectModule, MatSlideToggleModule,
    FormsModule, MatInputModule, MatFormField, MatPaginatorModule
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements OnInit {
  problems: any[] = [];
  allTags: any[] = [];
  selectedDifficulty: string = '';
  selectedStatus: string = '';
  selectedTags: string[] = [];
  difficulties = ['Easy', 'Medium', 'Hard'];
  statuses = ['Solved', 'Attempted', 'Unsolved'];
  hideTags: boolean = false;
  searchQuery: string = '';
  totalProblems = 0;
  currentPage = 1;
  problemsPerPage: number = 20;
  allProblems: any[] = [];
  progress: { [key: string]: { solved: number; total: number } } = { Easy: { solved: 0, total: 0 }, Medium: { solved: 0, total: 0 }, Hard: { solved: 0, total: 0 } };

  constructor(private problemService: ProblemService) { }

  ngOnInit(): void {
    this.getProblems(this.currentPage);
    this.problemService.getTags().subscribe(
      (data) => { this.allTags = data; },
      (error) => { console.error('Error fetching tags', error); }
    );
    this.loadAllForProgress();
  }

  loadAllForProgress() {
    this.problemService.getProblems(1).subscribe((data) => {
      const total = data.total_problems;
      const pages = data.total_pages;
      let collected: any[] = data.problems;
      if (pages > 1) {
        const requests = [];
        for (let p = 2; p <= pages; p++) {
          requests.push(this.problemService.getProblems(p).toPromise());
        }
        Promise.all(requests).then((results: any[]) => {
          for (const r of results) {
            collected = collected.concat(r.problems);
          }
          this.computeProgress(collected);
        });
      } else {
        this.computeProgress(collected);
      }
    });
  }

  computeProgress(allProblems: any[]) {
    this.allProblems = allProblems;
    for (const p of allProblems) {
      const diff = p.difficulty as keyof typeof this.progress;
      if (this.progress[diff]) {
        this.progress[diff].total++;
        if (p.user_status === 'Solved') this.progress[diff].solved++;
      }
    }
  }

  private get filterParams() {
    return {
      difficulty: this.selectedDifficulty || undefined,
      search: this.searchQuery || undefined,
      tags: this.selectedTags.length ? this.selectedTags.join(',') : undefined,
      status: this.selectedStatus.toLowerCase() || undefined
    };
  }

  getProblems(page: number) {
    this.problemService.getProblems(page, this.filterParams).subscribe(
      (data) => {
        this.problems = data.problems;
        this.totalProblems = data.total_problems;
      },
      (error) => { console.error('Error fetching problems', error); }
    );
  }

  applyFilters() {
    this.currentPage = 1;
    this.getProblems(1);
  }

  onPageChange(event: PageEvent) {
    this.currentPage = event.pageIndex + 1;
    this.problemsPerPage = event.pageSize;
    this.getProblems(this.currentPage);
  }
}
