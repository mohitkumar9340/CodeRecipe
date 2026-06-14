import { Component, OnInit, Inject } from '@angular/core';
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
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';
import { MatDialog, MatDialogModule, MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatSnackBarModule, MatSnackBar } from '@angular/material/snack-bar';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MarkdownPipe } from '../markdown.pipe';
import { AngularSplitModule } from 'angular-split';

const monacoLanguageMap: { [key: string]: string } = {
  'python': 'python',
  'c++': 'cpp',
  'c': 'c',
  'java': 'java'
};

@Component({
  selector: 'app-problem',
  standalone: true,
  imports: [
    CommonModule, MatFormFieldModule, MatInputModule, MatSelectModule,
    MatOptionModule, MatIconModule, MatButtonModule, FormsModule,
    HeaderComponent, MatToolbar, MatTabsModule, MatTableModule,
    MonacoEditorModule, MatDialogModule, MatProgressSpinnerModule,
    MatSnackBarModule, MatTooltipModule, MarkdownPipe, AngularSplitModule
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
  testResults: any[] | null = null;
  loadingRun = false;
  loadingSubmit = false;
  judgingStatus: string = '';
  editorOptions = {
    theme: 'vs-dark', language: 'python', minimap: { enabled: false },
    fontSize: 14, automaticLayout: true, scrollBeyondLastLine: false, wordWrap: 'on' as const,
    padding: { top: 4 }
  };
  languageSamples: { [key: string]: string } = {
    'python': `print('Hello, world!')`,
    'c++': `#include <iostream>\nusing namespace std;\n\nint main() {\n\tcout << "Hello, world!" << endl;\n\treturn 0;\n}`,
    'c': `#include <stdio.h>\n\nint main() {\n\tprintf("Hello, world!");\n\treturn 0;\n}`,
    'java': `public class Main {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Hello, world!");\n\t}\n}`
  };
  submissions: any[] = [];
  submissionColumns: string[] = ['verdict', 'language', 'time', 'memory', 'view'];

  constructor(
    private route: ActivatedRoute,
    private problemService: ProblemService,
    private dialog: MatDialog,
    private snackBar: MatSnackBar
  ) {
    this.setSampleCode(this.language);
  }

  ngOnInit(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.problemService.getProblemById(id!).subscribe(
      (data) => { this.problem = data; },
      (error) => { console.error('Error fetching problem', error); }
    );
    this.loadSubmissions();
  }

  loadSubmissions(): void {
    const id = this.route.snapshot.paramMap.get('id');
    this.problemService.getSubmissions(id!).subscribe(
      (data) => { this.submissions = data; },
      (error) => { console.error('Error fetching submissions', error); }
    );
  }

  runCode(): void {
    this.loadingRun = true;
    this.output = '';
    const codeData = { code: this.code, language: this.language, input_data: this.input_data };
    this.problemService.runCode(codeData).subscribe(
      (data) => {
        this.loadingRun = false;
        this.output = data.output || data.error || 'No output';
      },
      (error) => {
        this.loadingRun = false;
        this.output = 'Error: ' + (error.error?.error || error.message);
      }
    );
  }

  submitCode(): void {
    this.loadingSubmit = true;
    this.judgingStatus = 'Judging...';
    this.output = '';
    this.testResults = null;
    const codeData = { code: this.code, language: this.language, problem: this.problem.id };
    this.problemService.submitCode(codeData).subscribe(
      (data) => {
        this.loadingSubmit = false;
        this.judgingStatus = '';
        this.output = data.verdict || data;
        this.testResults = data.results || null;
        this.loadSubmissions();
      },
      (error) => {
        this.loadingSubmit = false;
        this.judgingStatus = '';
        this.output = 'Error submitting code';
      }
    );
  }

  viewSubmission(submission: any): void {
    this.dialog.open(ViewSubmissionDialogComponent, {
      width: '800px',
      data: submission
    });
  }

  setSampleCode(language: string) {
    this.code = this.languageSamples[language] || '';
  }

  onLanguageChange(language: string) {
    this.language = language;
    this.editorOptions = { ...this.editorOptions, language: monacoLanguageMap[language] };
    this.setSampleCode(language);
  }

  copyText(text: string): void {
    navigator.clipboard.writeText(text).then(() => {
      this.snackBar.open('Copied to clipboard', '', { duration: 1500 });
    });
  }

  formatMemory(kb: number): string {
    if (!kb && kb !== 0) return '-';
    if (kb >= 1024) return (kb / 1024).toFixed(1) + ' MB';
    return kb + ' KB';
  }

  formatTime(seconds: number): string {
    if (!seconds && seconds !== 0) return '-';
    return seconds.toFixed(3) + 's';
  }

}

@Component({
  selector: 'app-view-submission-dialog',
  template: `
    <h1 mat-dialog-title>Submission Details</h1>
    <div mat-dialog-content>
      <p><strong>Verdict:</strong> <span [ngClass]="verdictClass">{{ data.verdict }}</span></p>
      <p><strong>Language:</strong> {{ data.language }}</p>
      <p><strong>Time:</strong> {{ data.execution_time ? data.execution_time + 's' : '-' }}</p>
      <p><strong>Memory:</strong> {{ data.memory_used ? data.memory_used + ' KB' : '-' }}</p>
      <p><strong>Submitted:</strong> {{ data.timestamp }}</p>
      <h3>Code:</h3>
      <ngx-monaco-editor [options]="viewEditorOptions" [(ngModel)]="data.code"></ngx-monaco-editor>
    </div>
    <div mat-dialog-actions>
      <button mat-button (click)="dialogRef.close()">Close</button>
    </div>
  `,
  styles: [`
    ngx-monaco-editor { height: 400px; display: block; }
    .accepted { color: #2e7d32; font-weight: bold; }
    .wrong { color: #c62828; font-weight: bold; }
    .error { color: #e65100; font-weight: bold; }
  `],
  standalone: true,
  imports: [CommonModule, MatDialogModule, MatButtonModule, FormsModule, MonacoEditorModule]
})
export class ViewSubmissionDialogComponent {
  viewEditorOptions = {
    theme: 'vs-dark', language: 'python', minimap: { enabled: false },
    fontSize: 13, automaticLayout: true, readOnly: true,
    scrollBeyondLastLine: false, wordWrap: 'on' as const
  };

  constructor(
    public dialogRef: MatDialogRef<ViewSubmissionDialogComponent>,
    @Inject(MAT_DIALOG_DATA) public data: any
  ) {
    const langMap: { [key: string]: string } = { 'python': 'python', 'c++': 'cpp', 'c': 'c', 'java': 'java' };
    this.viewEditorOptions = { ...this.viewEditorOptions, language: langMap[data.language] || 'python' };
  }

  get verdictClass() {
    const v = (this.data.verdict || '').toLowerCase();
    if (v.includes('pass')) return 'accepted';
    if (v.includes('wrong')) return 'wrong';
    return 'error';
  }
}
