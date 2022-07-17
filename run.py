from classes import *
from functions import *


def run():
    all_lists = []
    while True:
        print("\n==========[ Menu ]==========")
        if len(all_lists) == 0:
            print("Nenhuma lista criada...")
            print("\n↪ Opções:")
            print("\t[c] - Criar nova lista")
            print("\t[q] - Sair")
        else:
            for index, tk_list in enumerate(all_lists, start=1):
                print(f"{index}. {tk_list.name}")

            print("\n~> Opções:")
            if len(all_lists) > 0:
                string = f" - {len(all_lists)}" if len(all_lists) > 1 else ''
                print(f"\t[1{string}] - Acessar lista")
                print("\t[r] - Apagar lista")
            print("\t[c] - Criar nova lista")
            print("\t[q] - Sair")

        breakout = False
        while True:
            option = input("Opção escolhida: ")
            if len(all_lists) > 0 and option.isnumeric():
                option = int(option)
                for index, tk_list in enumerate(all_lists, start=1):
                    if option == index:
                        print("\n", tk_list.tasks)
                        
                        # TODO: Show, add and change tasks
                        print("\n~> Opções:")
                        print("[c] - Cria tarefa")
                        print("[m] - Completar tarefa") # Use a for loop to search for the task
                        print("[r] - Apagar tarefa")
                        print("[q] - Sair")
                    else:
                        pass

            elif option.lower() == 'c':
                while True:
                    tk_name = input("Nome da lista (50 caracteres): ")
                    if len(tk_name) == 0:
                        print("Nome inválido!")
                    else:
                        all_lists.append(new_task_list(tk_name))
                        break
                break
            elif option.lower() == 'q':
                breakout = True
                break
            else:
                print("Opção inválida!")
        if breakout:
            break

if __name__ == "__main__":
    run()
