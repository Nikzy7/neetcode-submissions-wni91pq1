class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_cycle_count = 0
        while len(sandwiches) > 0:
            if sandwiches[0] == students[0]:
                sandwiches.pop(0)
                students.pop(0)
                student_cycle_count = 0 
            else:
                students.append(students.pop(0))
                student_cycle_count += 1

            if student_cycle_count > len(students):
                break

        return len(students)