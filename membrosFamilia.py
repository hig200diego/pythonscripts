#Membros da Família
familia = ['Vita', 'Diva', 'Damião', 'Diego', 'Vinicius', 'Vitoria', 'Pejoquinha', 'Bebê']
index = 0;
while index < len(familia):
    print(f"{index}: {familia[index]}")
    index += 1;
    
if "Angela" not in familia:
    familia.append("Angela")
    print(familia)