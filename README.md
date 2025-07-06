# CodeRecipe 🍳

# 🖥️ Online Judge Platform

An online judge platform hosting coding problems and challenges. Users can solve DSA and coding problems with real-time code evaluation. Built with Angular and Django, this platform supports multiple programming languages and provides immediate feedback on submissions.

**Created by:** Mohit

## 🌟 Features

- **User Authentication and Role-Based Authorization**: Secure login and role-based access.
- **User Dashboard**: Personalized dashboard for participants.
- **Problem Creation and Management Service**: Admins can create and manage problems.
- **Submission Service**: Participants can submit their solutions.
- **Multiple Languages and Themes**: Support for various coding languages and IDE themes.
- **Interactive Coding Workspace**: Real-time coding environment.
- **Problem Filters**: Search problems based on tags.
- **Validations**: Ensuring the correctness of passwords and code.
- **Optimized Queries**: Faster response times and reduced bandwidth consumption.

## 🛠️ Tech Stack

- **Core**:
  - Angular
  - MySQL
  - Django

### User:
1. User logs in or registers.
2. User navigates through problem lists, participates in contests, solves problems.
3. User chooses a problem to solve.
4. User submits code.
5. Backend evaluates the code against test cases.
6. Submissions are stored and can be accessed later.

### Admin:
1. Admin logs in or registers.
2. Admin navigates through the dashboard.
3. Admin can create and edit problems.
4. Admin can change the status and test cases for the problems.
5. Admin can host a contest and see results [Coming Soon].


# Dokerizing Process:

1. docker image build --platform linux/amd64 -t online_judge:v1 .
2. docker container run -p 8000:8000 --name c1 c948c83e4877


3. docker login registry.e2enetworks.net -u username -p
   (Enter Password)

4. docker tag online_judge:v2 registry.e2enetworks.net/cr-149/online_judge:v2 

5. docker push registry.e2enetworks.net/cr-149/online_judge:v2     

 -----------------------------------------------------------------------------------------------
 On VM:
6. docker pull registry.e2enetworks.net/cr-149/online_judge@sha256:2fb90abc9e62c339b1a2a508c6e1baa3a2098a7b92b52d3c29861822dd2d50e8

7. docker run -p 8000:8000 5670a190e323
    It is image Id.