from survey_processor import SurveyProcessor

def main():
    print("Введите возрастные группы через пробел в порядке возрастания, например: 18 25 35 45 60 80 100")

    while True:
        try:
            age_bounds = list(map(int, input().strip().split()))
            if any(age > 123 for age in age_bounds):
                print("Ошибка: Возрастные группы не могут включать возраст более 123 лет.")
                continue
            if not all(age_bounds[i] < age_bounds[i + 1] for i in range(len(age_bounds) - 1)):
                print(
                    "Ошибка: Группы должны быть введены в порядке возрастания. Пожалуйста, попробуйте снова.")
                continue
            break
        except ValueError:
            print("Ошибка: Используйте только числа и одинарные пробелы для определения возрастных групп.")
            print("По окончании ввода, напишите END")

    processor = SurveyProcessor(age_bounds)

    print("Введите данные респондентов, по одному на строку, например: Иванов Иван Иванович,35")
    print("После ввода всех респондентов, напишите END")

    input_lines = []
    while True:
        line = input().strip()
        try:
            full_name, age_str = line.split(',')
            age = int(age_str)
            if age > 123:
                print(
                    "Ошибка: Введен возраст более 123 лет, такой возраст недопустим. Пожалуйста, введите корректные данные.")
                continue
            input_lines.append(line)
        except ValueError:
            if line == "END":
                break
            print("Ошибка: Введите данные в формате '<ФИО>,<возраст>'. Например, Иванов Иван Иванович,35")
        except IndexError:
            print("Ошибка: Пожалуйста, разделяйте имя и возраст запятой. Введите данные снова.")

    processor.process_respondents(input_lines)

    results = processor.get_results()
    print(results)


if __name__ == "__main__":
    main()