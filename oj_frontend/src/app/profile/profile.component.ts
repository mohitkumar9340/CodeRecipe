import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatCardModule } from '@angular/material/card';
import { ReactiveFormsModule } from '@angular/forms';
import { HeaderComponent } from '../header/header.component';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbar } from '@angular/material/toolbar';
import { MatIcon } from '@angular/material/icon';
import { MatDialog } from '@angular/material/dialog';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { MatDialogModule } from '@angular/material/dialog';
import { UserService } from '../service/user.service';



interface User {
  name: string;
  email: string;
  username: string;
}



@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatCardModule,
    ReactiveFormsModule,
    HeaderComponent,
    MatButtonModule,
    MatToolbar,
    MatIcon,
    MatDialogModule,


  ],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent implements OnInit {
  user:User = {
    name: 'John Doe',
    email: 'john@example.com',
    username: 'johndoe',
  };

  editMode = false;
  profileForm!: FormGroup;

  constructor(
    private fb: FormBuilder,
    public dialog: MatDialog,
    private userService: UserService
  ) {}

  ngOnInit(): void {
    this.userService.userDetails().subscribe((user: User) => {
      this.user = user;    
    });
    this.profileForm = this.fb.group({
      name: [this.user.name, Validators.required],
      email: [this.user.email, [Validators.required, Validators.email]],
      username: [this.user.username, Validators.required],
    });
  }

  onSubmit() {
    if (this.profileForm.valid) {
      // Update the user profile data here
      this.user.email = this.profileForm.get('email')?.value;
      this.user.username = this.profileForm.get('username')?.value;
      this.editMode = false;
    }
  }

  cancelEdit() {
    this.editMode = false;
    this.profileForm.patchValue({
      email: this.user.email,
      username: this.user.username,
    });
  }

  openChangePasswordDialog() {
    const dialogRef = this.dialog.open(ChangePasswordDialogComponent, {
      width: '400px'
    });

    dialogRef.afterClosed().subscribe(result => {
      if (result) {
        // Handle the result from the dialog
        console.log('Password changed successfully');
      }
    });
  }
}

@Component({
  selector: 'app-change-password-dialog',
  templateUrl: './change-password.component.html',
  styles: [`
    .mat-form-field {
      width: 100%;
    }
  `],
  standalone: true,
  imports: [
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    ReactiveFormsModule,
    MatDialogModule,
    ReactiveFormsModule,
    MatDialogModule,
    MatCardModule,
    MatToolbar,
    MatIcon,
  ]
})
export class ChangePasswordDialogComponent {
  changePasswordForm = this.fb.group({
    oldPassword: ['', Validators.required],
    newPassword: ['', Validators.required],
    confirmNewPassword: ['', Validators.required]
  });

  constructor(
    private fb: FormBuilder,
    public dialogRef: MatDialogRef<ChangePasswordDialogComponent>
  ) {}

  onSubmit() {
    if (this.changePasswordForm.valid && this.passwordsMatch()) {
      // Handle password change logic here
      this.dialogRef.close(true); // Pass result data if needed
    }
  }

  onCancel() {
    this.dialogRef.close();
  }

  passwordsDoNotMatch(): boolean {
    return this.changePasswordForm.get('newPassword')?.value !== this.changePasswordForm.get('confirmNewPassword')?.value;
  }

  private passwordsMatch(): boolean {
    return this.changePasswordForm.get('newPassword')?.value === this.changePasswordForm.get('confirmNewPassword')?.value;
  }
}
