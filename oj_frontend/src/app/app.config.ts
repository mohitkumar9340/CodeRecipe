import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';

import { routes } from './app.routes';
import { provideClientHydration } from '@angular/platform-browser';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { provideHttpClient, withFetch, withInterceptors } from '@angular/common/http';
import { authInterceptor } from './auth.interceptor';
import { toastInterceptor } from './toast.interceptor';
import { provideMonacoEditor } from 'ngx-monaco-editor-v2';

export const appConfig: ApplicationConfig = {
  providers: [provideZoneChangeDetection({ eventCoalescing: true }),
  provideRouter(routes),
  provideClientHydration(), 
  provideAnimationsAsync(),
  provideHttpClient(
    withFetch(),
    withInterceptors([authInterceptor, toastInterceptor])
  ),
  provideMonacoEditor({
    baseUrl: 'https://cdn.jsdelivr.net/npm/monaco-editor@0.50.0/min/vs'
  })
]
};
