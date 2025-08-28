from ..models import Problem, TestCases;
from .compiler import Compiler;
compiler = Compiler()

class Judge():
    def run_testcases(self, problem_id, language, code):
        print("Entered run_testcases")
        problem = Problem.objects.filter(id=problem_id)
        testcases = TestCases.objects.filter(problem_id=problem_id)
        index = 1
        for i, testcase in enumerate(testcases, start = 1):
            print(testcase)
            input_data = testcase.input_data
            output_data = testcase.output_data
            output = compiler.run_code(language=language, code=code, input_data=input_data)
            print(f"Testcase {i}: Input = {input_data} Output = {output}, Expected = {output_data}")
            if output.strip() != output_data.strip():
                print("Wrong Answer")
                print(output)
                print(output_data)
                return f"Wrong Answer in Testcase {i}"
        return "All testcases passed"