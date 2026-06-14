import { HttpInterceptorFn, HttpResponse } from '@angular/common/http';
import { inject } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { tap, catchError, throwError } from 'rxjs';

const TOAST_POSITION = { horizontalPosition: 'end' as const, verticalPosition: 'top' as const };
const SKIP_MESSAGES = ['Code executed successfully', 'Solution submitted successfully'];

export const toastInterceptor: HttpInterceptorFn = (req, next) => {
  const snackBar = inject(MatSnackBar);

  return next(req).pipe(
    tap(event => {
      if (event instanceof HttpResponse) {
        const body = event.body as { message?: string };
        if (body?.message && typeof body.message === 'string' && !SKIP_MESSAGES.includes(body.message)) {
          snackBar.open(body.message, 'Close', { duration: 3000, ...TOAST_POSITION });
        }
      }
    }),
    catchError(error => {
      if (error.status !== 401) {
        const msg = error.error?.message || 'Something went wrong';
        snackBar.open(msg, 'Close', { duration: 5000, ...TOAST_POSITION });
      }
      return throwError(() => error);
    })
  );
};
