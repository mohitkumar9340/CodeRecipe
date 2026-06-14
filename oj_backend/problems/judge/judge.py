from ..models import Problem, TestCases
from .compiler import Compiler

compiler = Compiler()

class Judge():
    def run_testcases(self, problem_id, language, code):
        testcases = TestCases.objects.filter(problem_id=problem_id)
        results = []
        all_passed = True
        total_time = 0.0
        total_memory = 0

        for i, testcase in enumerate(testcases, start=1):
            input_data = testcase.input_data or ""
            expected = testcase.output_data or ""
            result = compiler.run_code(language=language, code=code, input_data=input_data)
            actual = result.get('output', '')
            error = result.get('error', '')
            tc_time = result.get('execution_time', 0)
            tc_memory = result.get('memory_used', 0)
            total_time += tc_time
            total_memory = max(total_memory, tc_memory)

            if error:
                results.append({
                    'testcase': i,
                    'input': input_data,
                    'expected': expected,
                    'actual': '',
                    'error': error,
                    'passed': False,
                    'execution_time': tc_time,
                    'memory_used': tc_memory
                })
                all_passed = False
                break

            passed = actual.strip() == expected.strip()
            if not passed:
                all_passed = False

            results.append({
                'testcase': i,
                'input': input_data,
                'expected': expected,
                'actual': actual,
                'error': '',
                'passed': passed,
                'execution_time': tc_time,
                'memory_used': tc_memory
            })

            if not passed:
                break

        verdict = "All testcases passed" if all_passed else "Wrong Answer"
        return {
            'verdict': verdict,
            'results': results,
            'execution_time': round(total_time, 4),
            'memory_used': total_memory
        }
