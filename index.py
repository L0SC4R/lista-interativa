students = []


def main_menu():
    while True:
        print("Menu Principal:")
        option = int(input(
            "Selecione uma opcao: \n (1) Estudante: \n (2) Disciplina: \n (3) Professor: \n (4) Turma: \n (5) Matrícula: \n (6) Sair: \n"))

        if option in [1, 2, 3, 4, 5]:
            handle_option()
        elif option == 6:
            print("Saindo do programa...")
            break
        else:
            print("Opcao invalida")


def handle_option():
    while True:
        print("\nSubmenu:")
        insert_or_list_option = int(
            input("Selecione uma opcao: \n (1) inserir: \n (2) Listar: \n (3) Voltar ao menu principal: \n (4) Sair: \n"))

        if insert_or_list_option == 1:
            student_name = input("Digite o nome do estudante: ")
            students.append(student_name)
        elif insert_or_list_option == 2:
            print(students)
        elif insert_or_list_option == 3:
            break
        elif insert_or_list_option == 4:
            print("Saindo do programa...")
            exit(0)  # exit the entire program
        else:
            print("Opcao invalida")


if __name__ == "_main_":
    main_menu()
