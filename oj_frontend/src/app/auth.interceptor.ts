import { HttpInterceptorFn } from '@angular/common/http';
import { Injectable } from '@angular/core';


export const authInterceptor: HttpInterceptorFn = (req, next) => {
  const AuthToken = localStorage.getItem('access_token');
  console.log(req.url)
  console.log("request intercepted :", req)
  if(req.url != "http://127.0.0.1:8000/auth/login/"){
    console.log("AuthToken :", AuthToken)
    const headers = req.headers.append('Authorization', `Bearer ${AuthToken}` ?? '');
    const authReq = req.clone({ headers });
    console.log("authReq :", authReq)
    return next(authReq);
  }
  return next(req);
};
