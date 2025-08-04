def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
      return "Error: Too many problems."
    else:
      first_line = ""
      second_line = ""
      third_line = ""
      fourth_line = ""

      last_problem = problems[-1]

      for problem in problems:
        first_operand = problem.split()[0]
        operator = problem.split()[1]
        second_operand = problem.split()[2]

        if not first_operand.isdigit() or not second_operand.isdigit():
          return "Error: Numbers must only contain digits."

        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator == "+":
          answer = int(first_operand) + int(second_operand)
        elif operator == "-":
          answer = int(first_operand) - int(second_operand)
        else:
          return "Error: Operator must be '+' or '-'."

        max_str = max(len(first_operand), len(second_operand))

        first_line += first_operand.rjust(max_str + 2)
        if problem != last_problem:
            first_line += " " * 4

        second_line += operator
        second_line += second_operand.rjust(max_str + 1)
        if problem != last_problem:
            second_line += " " * 4

        third_line += "-" * (max_str + 2)
        if problem != last_problem:
            third_line += " " * 4

        formatted_answer = str(answer).rjust(max_str + 2)
        fourth_line += formatted_answer
        if problem != last_problem:
            fourth_line += " " * 4

      arranged_problems = first_line + "\n" + second_line + "\n" + third_line
      if show_answers:
          arranged_problems += "\n" + fourth_line

      return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)}')
print(f'\n{arithmetic_arranger(["3801 - 2", "123 + 49"])}')
