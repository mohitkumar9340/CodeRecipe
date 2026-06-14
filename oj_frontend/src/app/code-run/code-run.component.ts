import { Component, HostListener, ElementRef } from '@angular/core';
import { HeaderComponent } from "../header/header.component";
import { FormsModule } from '@angular/forms';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatIconModule } from '@angular/material/icon';
import { MatSelectModule } from '@angular/material/select';
import { MatCardModule } from '@angular/material/card';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatOptionModule } from '@angular/material/core';
import { CommonModule } from '@angular/common';
import { AngularSplitModule } from 'angular-split';
import { MatDividerModule } from '@angular/material/divider';
import { ProblemService } from '../service/problem.service';
import { MonacoEditorModule } from 'ngx-monaco-editor-v2';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';
import { MatSnackBar, MatSnackBarModule } from '@angular/material/snack-bar';
import { MatTooltipModule } from '@angular/material/tooltip';

const monacoLanguageMap: { [key: string]: string } = {
  'Python': 'python',
  'C++': 'cpp',
  'C': 'c',
  'Java': 'java'
};

@Component({
  selector: 'app-code-run',
  standalone: true,
  imports: [
    HeaderComponent,
    FormsModule,
    MatToolbarModule,
    MatIconModule,
    MatSelectModule,
    MatCardModule,
    MatGridListModule,
    MatFormFieldModule,
    MatInputModule,
    MatOptionModule,
    CommonModule,
    AngularSplitModule,
    MatDividerModule,
    MonacoEditorModule,
    MatProgressSpinnerModule,
    MatSnackBarModule,
    MatTooltipModule
  ],
  templateUrl: './code-run.component.html',
  styleUrl: './code-run.component.css'
})

export class CodeRunComponent {
  code: string = '';
  input: string = '';
  output: string = '';
  error: string = '';
  cleanError: string = '';
  selectedLanguage: string = 'Python';
  languages: string[] = ['Python', 'C++', 'C', 'Java'];
  languageMap: { [key: string]: string } = { 'Python': 'python', 'C++': 'c++', 'C': 'c', 'Java': 'java' };
  loadingRun = false;
  editorOptions = {
    theme: 'vs-dark',
    language: 'python',
    minimap: { enabled: false },
    fontSize: 14,
    automaticLayout: true,
    scrollBeyondLastLine: false,
    wordWrap: 'on' as const
  };

  languageSamples: { [key: string]: string } = {
    'Python': `print('Hello, world!')`,
    'C++': `#include <iostream>\nusing namespace std;\n\nint main() {\n\tcout << "Hello, world!" << endl;\n\treturn 0;\n}`,
    'C': `#include <stdio.h>\n\nint main() {\n\tprintf("Hello, world!");\n\treturn 0;\n}`,
    'Java': `public class Main {\n\tpublic static void main(String[] args) {\n\t\tSystem.out.println("Hello, world!");\n\t}\n}`
  };

  constructor(private elRef: ElementRef, private problemService: ProblemService, private snackBar: MatSnackBar) {
    this.setSampleCode(this.selectedLanguage); 
  }

  runCode() {
    this.loadingRun = true;
    this.output = '';
    this.error = '';
    this.cleanError = '';
    const codeData = {
      code: this.code,
      language: this.languageMap[this.selectedLanguage],
      input_data: this.input
    }
    this.problemService.runCode(codeData).subscribe(
      (data) => {
        this.loadingRun = false;
        this.error = data.error;
        if (this.error) {
          this.cleanError = (this.error.replace(/^.*?line \d+\n/, '').trim()).replace(/^.*?:\d+:\d+:\s/, '');
        }
        this.output = data.output || '';
      },
      (error) => {
        this.loadingRun = false;
        this.error = error.error?.error || 'Error executing code';
        this.cleanError = this.error;
      }
    );
  }

  isDragging = false;
  startY: number = 0;
  startHeight: number = 0;

  @HostListener('document:mousemove', ['$event'])
  onMouseMove(event: MouseEvent) {
    if (this.isDragging) {
      const deltaY = event.clientY - this.startY;
      const newHeight = this.startHeight + deltaY;
      this.elRef.nativeElement.querySelector('.input-output-content').style.height = `${newHeight}px`;
    }
  }

  @HostListener('document:mouseup')
  onMouseUp() {
    this.isDragging = false;
  }

  @HostListener('document:keydown.control.enter')
  handleCtrlEnter() {
    this.runCode();
  }

  onMouseDown(event: MouseEvent) {
    this.isDragging = true;
    this.startY = event.clientY;
    this.startHeight = this.elRef.nativeElement.querySelector('.input-output-content').clientHeight;
  }

  setSampleCode(language: string) {
    this.code = this.languageSamples[language] || '';
  }

  onLanguageChange(language: string) {
    this.selectedLanguage = language;
    this.editorOptions = { ...this.editorOptions, language: monacoLanguageMap[language] };
    this.setSampleCode(language);
  }

  copyText(text: string): void {
    navigator.clipboard.writeText(text).then(() => {
      this.snackBar.open('Copied to clipboard', '', { duration: 1500 });
    });
  }
}
