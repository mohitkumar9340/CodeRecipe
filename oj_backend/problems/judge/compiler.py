import uuid
import time
import shutil
from pathlib import Path
from django.conf import settings
import subprocess


class Compiler:
    COMPILE_TIMEOUT = 30
    EXECUTION_TIMEOUT_BUFFER = 5

    def _cleanup(self, paths):
        for p in paths:
            if p is None:
                continue
            p = Path(p)
            if not p.exists():
                continue
            if p.is_dir():
                shutil.rmtree(p, ignore_errors=True)
            else:
                p.unlink(missing_ok=True)

    def run_code(self, language, code, input_data="", time_limit=1.0):
        if language not in ["c", "c++", "python", "java"]:
            return {'output': '', 'error': 'Invalid language', 'execution_time': 0, 'memory_used': 0}
        project_path = Path(settings.BASE_DIR)
        directories = {'codes', 'inputs', 'outputs', 'errors'}
        for directory in directories:
            dir_path = project_path / directory
            if not dir_path.exists():
                dir_path.mkdir(parents=True, exist_ok=True)

        codes_dir = project_path / 'codes'
        inputs_dir = project_path / 'inputs'
        outputs_dir = project_path / 'outputs'
        errors_dir = project_path / 'errors'

        unique = str(uuid.uuid4())

        code_file_name = f"{unique}.{language}"
        input_file_name = f"{unique}.txt"
        output_file_name = f"{unique}.txt"
        error_file_name = f"{unique}.txt"

        code_file_path = codes_dir / code_file_name
        input_file_path = inputs_dir / input_file_name
        output_file_path = outputs_dir / output_file_name
        error_file_path = errors_dir / error_file_name

        java_dir = codes_dir / unique if language == 'java' else None
        java_file = java_dir / 'Main.java' if language == 'java' else None
        executable_path = codes_dir / unique if language in ('c', 'c++') else None

        created_paths = [code_file_path, input_file_path, output_file_path, error_file_path]
        if language == 'java':
            created_paths.append(java_dir)
        if language in ('c', 'c++'):
            created_paths.append(executable_path)

        try:
            with open(code_file_path, 'w') as code_file:
                code_file.write(code)
            with open(input_file_path, 'w') as input_file:
                input_file.write(input_data)
            with open(output_file_path, 'w'):
                pass
            with open(error_file_path, 'w'):
                pass

            if language == 'java':
                java_dir.mkdir(parents=True, exist_ok=True)
                with open(java_file, 'w') as f:
                    f.write(code)

            start_time = time.time()
            memory_used = 0
            timed_out = False

            try:
                if language == 'c++':
                    compile_result = subprocess.run(
                        ['clang++', str(code_file_path), '-o', str(executable_path)],
                        stderr=subprocess.PIPE, text=True,
                        timeout=self.COMPILE_TIMEOUT
                    )
                    if compile_result.returncode == 0:
                        with open(input_file_path, 'r') as input_file:
                            with open(output_file_path, 'w') as output_file:
                                with open(error_file_path, 'w') as error_file:
                                    subprocess.run(
                                        [str(executable_path)],
                                        stdin=input_file, stdout=output_file, stderr=error_file,
                                        timeout=time_limit + self.EXECUTION_TIMEOUT_BUFFER
                                    )
                    else:
                        with open(error_file_path, 'w') as error_file:
                            error_file.write(compile_result.stderr)

                elif language == 'python':
                    with open(input_file_path, 'r') as input_file:
                        with open(output_file_path, 'w') as output_file:
                            with open(error_file_path, 'w') as error_file:
                                subprocess.run(
                                    ['python3', str(code_file_path)],
                                    stdin=input_file, stdout=output_file, stderr=error_file,
                                    timeout=time_limit + self.EXECUTION_TIMEOUT_BUFFER
                                )

                elif language == 'c':
                    compile_result = subprocess.run(
                        ['clang', str(code_file_path), '-o', str(executable_path)],
                        stderr=subprocess.PIPE, text=True,
                        timeout=self.COMPILE_TIMEOUT
                    )
                    if compile_result.returncode == 0:
                        with open(input_file_path, 'r') as input_file:
                            with open(output_file_path, 'w') as output_file:
                                with open(error_file_path, 'w') as error_file:
                                    subprocess.run(
                                        [str(executable_path)],
                                        stdin=input_file, stdout=output_file, stderr=error_file,
                                        timeout=time_limit + self.EXECUTION_TIMEOUT_BUFFER
                                    )
                    else:
                        with open(error_file_path, 'w') as error_file:
                            error_file.write(compile_result.stderr)

                elif language == 'java':
                    compile_result = subprocess.run(
                        ['javac', str(java_file)],
                        stderr=subprocess.PIPE, text=True,
                        timeout=self.COMPILE_TIMEOUT
                    )
                    if compile_result.returncode == 0:
                        with open(input_file_path, 'r') as input_file:
                            with open(output_file_path, 'w') as output_file:
                                with open(error_file_path, 'w') as error_file:
                                    subprocess.run(
                                        ['java', '-cp', str(java_dir), 'Main'],
                                        stdin=input_file, stdout=output_file, stderr=error_file,
                                        timeout=time_limit + self.EXECUTION_TIMEOUT_BUFFER
                                    )
                    else:
                        with open(error_file_path, 'w') as error_file:
                            error_file.write(compile_result.stderr)

            except subprocess.TimeoutExpired:
                timed_out = True
                with open(error_file_path, 'w') as error_file:
                    error_file.write("Time Limit Exceeded")

            except Exception as e:
                with open(error_file_path, 'w') as error_file:
                    error_file.write(str(e))

            elapsed = time.time() - start_time

            output_data = ""
            error_data = ""
            if output_file_path.exists():
                with open(output_file_path, 'r') as output_file:
                    output_data = output_file.read()
            if error_file_path.exists():
                with open(error_file_path, 'r') as error_file:
                    error_data = error_file.read()

            return {
                'output': output_data,
                'error': error_data,
                'execution_time': round(elapsed, 4),
                'memory_used': memory_used,
                'timed_out': timed_out,
            }

        finally:
            self._cleanup(created_paths)
