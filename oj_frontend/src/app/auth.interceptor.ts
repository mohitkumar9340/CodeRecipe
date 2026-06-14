import { HttpInterceptorFn } from '@angular/common/http';
import { catchError, throwError } from 'rxjs';

const PUBLIC_URLS = ['/auth/login/', '/auth/register/', '/auth/guest-login/'];

export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const isPublic = PUBLIC_URLS.some(url => req.url.includes(url));
  const AuthToken = localStorage.getItem('access_token');

  if (AuthToken && !isPublic) {
    const headers = req.headers.append('Authorization', `Bearer ${AuthToken}`);
    const authReq = req.clone({ headers });
    return next(authReq).pipe(
      catchError((error) => {
        if (error.status === 401) {
          localStorage.removeItem('access_token');
          localStorage.removeItem('refresh_token');
          localStorage.removeItem('username');
          window.location.href = '/login';
        }
        return throwError(() => error);
      })
    );
  }
  return next(req);
};
