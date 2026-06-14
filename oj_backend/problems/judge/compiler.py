import uuid
import time
from pathlib import Path
from django.conf import settings
import subprocess
import os


class Compiler:
    def run_code(self, language, code, input_data=""):
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

        with open(code_file_path, 'w') as code_file:
            code_file.write(code)
        with open(input_file_path, 'w') as input_file:
            input_file.write(input_data)
        with open(output_file_path, 'w') as output_file:
            pass
        with open(error_file_path, 'w') as error_file:
            pass

        start_time = time.time()
        memory_used = 0

        try:
            if language == 'c++':
                executable_path = codes_dir / unique
                compile_result = subprocess.run(
                    ['g++', str(code_file_path), '-o', str(executable_path)],
                    stderr=subprocess.PIPE, text=True
                )
                if compile_result.returncode == 0:
                    with open(input_file_path, 'r') as input_file:
                        with open(output_file_path, 'w') as output_file:
                            with open(error_file_path, 'w') as error_file:
                                subprocess.run(
                                    [str(executable_path)],
                                    stdin=input_file, stdout=output_file, stderr=error_file
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
                                stdin=input_file, stdout=output_file, stderr=error_file
                            )

            elif language == 'c':
                executable_path = codes_dir / unique
                compile_result = subprocess.run(
                    ['gcc', str(code_file_path), '-o', str(executable_path)],
                    stderr=subprocess.PIPE, text=True
                )
                if compile_result.returncode == 0:
                    with open(input_file_path, 'r') as input_file:
                        with open(output_file_path, 'w') as output_file:
                            with open(error_file_path, 'w') as error_file:
                                subprocess.run(
                                    [str(executable_path)],
                                    stdin=input_file, stdout=output_file, stderr=error_file
                                )
                else:
                    with open(error_file_path, 'w') as error_file:
                        error_file.write(compile_result.stderr)

            elif language == 'java':
                java_dir = codes_dir / unique
                java_dir.mkdir(parents=True, exist_ok=True)
                java_file = java_dir / 'Main.java'
                with open(java_file, 'w') as f:
                    f.write(code)
                compile_result = subprocess.run(
                    ['javac', str(java_file)],
                    stderr=subprocess.PIPE, text=True
                )
                if compile_result.returncode == 0:
                    with open(input_file_path, 'r') as input_file:
                        with open(output_file_path, 'w') as output_file:
                            with open(error_file_path, 'w') as error_file:
                                subprocess.run(
                                    ['java', '-cp', str(java_dir), 'Main'],
                                    stdin=input_file, stdout=output_file, stderr=error_file
                                )
                else:
                    with open(error_file_path, 'w') as error_file:
                        error_file.write(compile_result.stderr)
        except Exception as e:
            with open(error_file_path, 'w') as error_file:
                error_file.write(str(e))

        elapsed = time.time() - start_time

        with open(output_file_path, 'r') as output_file:
            output_data = output_file.read()
        with open(error_file_path, 'r') as error_file:
            error_data = error_file.read()

        return {
            'output': output_data,
            'error': error_data,
            'execution_time': round(elapsed, 4),
            'memory_used': memory_used
        }


