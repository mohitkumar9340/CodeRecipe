import { Component, OnInit } from '@angular/core';
import { ProblemService } from '../service/problem.service';
import { ActivatedRoute } from '@angular/router';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatOptionModule } from '@angular/material/core';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { FormsModule } from '@angular/forms';
import { HeaderComponent } from '../header/header.component';
import { MatToolbar } from '@angular/material/toolbar';
import { MatTabsModule } from '@angular/material/tabs';
import { MatTableModule } from '@angular/material/table';


@Component({
  selector: 'app-problem',
  standalone: true,
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatSelectModule,
    MatOptionModule,
    MatIconModule,
    MatButtonModule,
    FormsModule,
    HeaderComponent,
    MatToolbar,
    MatTabsModule,
    MatTableModule
  ],
  templateUrl: './problem.component.html',
  styleUrl: './problem.component.css'
})
export class ProblemComponent implements OnInit {
  problem: any;
  language: string = 'python';
  code: string = '';
  input_data: string = '';
  output: string = '';
  languageSamples: { [key: string]: string } = {
    'python': `print('Hello, world!')`,
    'c++': `#include <iostream>\nusing namespace std; \n\nint main() {\n\t cout << "Hello, world!" <<endl;\n\t return 0;\n }`,
    'c': `#include <stdio.h> \n\nint main() {\n\tprintf("Hello, world!"); \n\treturn 0;\n}`
  };
  // examples: any[]
  mySubmissions: any[] = [];
  allSubmissions: any[] = [];
  constructor(private route: ActivatedRoute, private problemService: ProblemService) {
    this.setSampleCode(this.language);
    console.log("Problem component initialized");
    console.log(this.code);
  }
  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.problemService.getProblemById(id!).subscribe(
      (data) => {
        console.log(data)
        this.problem = data;
      },
      (error) => {
        console.error('Error fetching problems', error);
      }
    );
    this.problemService.getProblemSubmissions(id!).subscribe(
      (data) => {
        console.log(data)
        this.allSubmissions = data;
        this.mySubmissions = data.filter((submission: any) => submission.problem === id);
      },
      (error: any) => {
        console.error('Error fetching problems', error);
      }
    );
  }

  runCode(): void {
    console.log('Running code:', this.code);
    // Implement the logic to run the code
    const codeData = {
      code: this.code,
      language: this.language,
      input_data: this.input_data
    }
    this.problemService.runCode(codeData).subscribe(
      (data) => {
        console.log(data)
        this.output = data.output;
      },
      (error) => {
        console.error('Error fetching problems', error);
      }
    );
  }

  submitCode(): void {
    console.log('Submitting code:', this.code);
    // Implement the logic to submit the code
    const codeData = {
      code: this.code,
      language: this.language,
      problem: this.problem.id
    }
    this.problemService.submitCode(codeData).subscribe(
      (data) => {
        console.log(data)
        this.output = data;
      },
      (error) => {
        console.error('Error fetching problems', error);
      }
    );
  }

  viewSubmission(submission: any): void {
    console.log('Viewing submission:', submission);
  }

  setSampleCode(language: string) {
    this.code = this.languageSamples[language] || '';
  }

  onLanguageChange(language: string) {
    console.log('Language changed:', language);
    this.language = language;
    this.setSampleCode(language);
  }
}
