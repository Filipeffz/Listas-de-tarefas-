import sqlite3

# conecta ou cria o banco
conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()


def criar_tabela():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            concluida INTEGER NOT NULL
        )
    """)
    conexao.commit()


def adicionar_tarefa():
    nome = input("Digite o nome da tarefa: ")
    cursor.execute("INSERT INTO tarefas (nome, concluida) VALUES (?, ?)", (nome, 0))
    conexao.commit()
    print("Tarefa adicionada com sucesso!")


def listar_tarefas():
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\nLista de tarefas:")
    for tarefa in tarefas:
        status = "Concluída" if tarefa[2] == 1 else "Pendente"
        print(f"{tarefa[0]} - {tarefa[1]} ({status})")


def concluir_tarefa():
    listar_tarefas()
    try:
        numero = int(input("Digite o id da tarefa: "))
        cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (numero,))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Tarefa não encontrada.")
        else:
            print("Tarefa marcada como concluída!")
    except ValueError:
        print("Digite um número válido.")


def remover_tarefa():
    listar_tarefas()
    try:
        numero = int(input("Digite o id da tarefa para remover: "))
        cursor.execute("DELETE FROM tarefas WHERE id = ?", (numero,))
        conexao.commit()

        if cursor.rowcount == 0:
            print("Tarefa não encontrada.")
        else:
            print("Tarefa removida com sucesso!")
    except ValueError:
        print("Digite um número válido.")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            concluir_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida.")


criar_tabela()
menu()
conexao.close()