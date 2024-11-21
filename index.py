def add_contact():
  name = input("Digite o nome do contato: ")
  tel = input("Digite o telefone do contato: ")
  email = input("Digite o e-mail do contato: ")
  isFavorite = input("Marcar contato como favorito [s/n]: ")

  contacts.append({
    "name": name,
    "tel": tel,
    "email": email,
    "isFavorite": True if isFavorite == 's' or isFavorite == 'S' else False,
  })

def show_all_contacts():
  print("\n Lista de todos os contatos:")
  for index, contact in enumerate(contacts):
    print(f"{index}. [Nome: {contact["name"]}, Tel: {contact["tel"]}, E-mail: {contact["email"]}, Favorito: {"✔" if contact["isFavorite"] else "X"}]")

def update_contact():
  show_all_contacts()
  index = int(input("\n Digite o indíce do contato que deseja editar: "))
  if index >= 0 or index < len(contacts):
    name = input("Digite o nome do contato: ")
    tel = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    isFavorite = input("Marcar contato como favorito [s/n]: ")

    contacts[index] = {
      "name": name,
      "tel": tel,
      "email": email,
      "isFavorite": True if isFavorite == 's' or isFavorite == 'S' else False,
    }
  else: 
    print("Indíce inválido")
  
def toggle_is_favorite():
  show_all_contacts()
  index = int(input("\n Digite o indíce do contato que deseja marcar/desmarcar como favorito: "))
  if index >= 0 or index < len(contacts):
    print(f"{index}. [Nome: {contacts[index]["name"]}, Tel: {contacts[index]["tel"]}, E-mail: {contacts[index]["email"]}, Favorito: {"✔" if contacts[index]["isFavorite"] else "X"}]")
    isFavorite = input("Marcar contato como favorito [s/n]: ")

    contacts[index]['isFavorite'] = True if isFavorite == 's' or isFavorite == 'S' else False
  else:
    print("Indíce inválido")

def show_all_favorite_contacts():
  print('\n Lista de todos os contatos favoritos: ')

  for index, contact in enumerate(contacts):
    if contact['isFavorite'] == True:
      print(f"{index}. [Nome: {contact["name"]}, Tel: {contact["tel"]}, E-mail: {contact["email"]}, Favorito: {"✔" if contact["isFavorite"] else "X"}]")

def delete_contact():
  show_all_contacts()
  index = int(input("\n Digite o indíce do contato que deseja deletar: "))
  if index >= 0 or index < len(contacts):
    contacts.pop(index)
  else:
    print("Indíce inválido")
contacts = []

while True:
  print("\n Agenda")
  print("1. Adicionar um contato")
  print("2. Visualizar lista de contatos cadastrados")
  print("3. Editar um contato")
  print("4. Marcar/desmarcar um contato como favorito")
  print("5. Ver lista de contatos favoritos")
  print("6. Apagar um contato")
  print("7. Encerrar o programa")

  option = input("Digite sua escolha: ")

  if option == "1":
    add_contact()
  elif option == "2":
    show_all_contacts()
  elif option == "3":
    update_contact()
  elif option == "4":
    toggle_is_favorite()
  elif option == "5":
    show_all_favorite_contacts()
  elif option == "6":
    delete_contact()
  elif option == "7":
    break
  else:
    print("Opção inválida")

print("Programa finalizado")
