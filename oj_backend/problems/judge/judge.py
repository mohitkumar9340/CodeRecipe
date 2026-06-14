from ..models import Problem, TestCases
from .compiler import Compiler

compiler = Compiler()

class Judge():
    def run_testcases(self, problem_id, language, code):
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return {
                'verdict': 'Error',
                'results': [],
                'execution_time': 0,
                'memory_used': 0,
                'error': 'Problem not found'
            }

        time_limit = problem.time_limit
        testcases = TestCases.objects.filter(problem_id=problem_id)
        results = []
        all_passed = True
        total_time = 0.0
        total_memory = 0

        for i, testcase in enumerate(testcases, start=1):
            input_data = testcase.input_data or ""
            expected = testcase.output_data or ""
            result = compiler.run_code(
                language=language, code=code, input_data=input_data, time_limit=time_limit
            )
            actual = result.get('output', '')
            error = result.get('error', '')
            timed_out = result.get('timed_out', False)
            tc_time = result.get('execution_time', 0)
            tc_memory = result.get('memory_used', 0)
            total_time += tc_time
            total_memory = max(total_memory, tc_memory)

            if timed_out:
                results.append({
                    'testcase': i,
                    'input': input_data,
                    'expected': expected,
                    'actual': '',
                    'error': 'Time Limit Exceeded',
                    'passed': False,
                    'execution_time': tc_time,
                    'memory_used': tc_memory
                })
                all_passed = False
                break

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

        if not all_passed:
            if any(r.get('error') == 'Time Limit Exceeded' for r in results):
                verdict = "Time Limit Exceeded"
            else:
                verdict = "Wrong Answer"
        else:
            verdict = "All testcases passed"

        return {
            'verdict': verdict,
            'results': results,
            'execution_time': round(total_time, 4),
            'memory_used': total_memory
        }
