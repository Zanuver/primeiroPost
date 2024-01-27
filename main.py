import sqlite3;

conn = sqlite3.connect('D:\Projetos\DataGrip\Teste\identifier.sqlite')
cursor = conn.cursor()

def insert(id, name):
    cursor.execute('insert into teste (id, nome) values (?, ?)', (id, name))

cursor.execute('''
create table if not exists teste (
    id integer not null,
    name text not null,
    primary key (id)
    )
''')



# Faça uma chamada com a função insert





cursor.execute('select * from teste order by id')
recebido = cursor.fetchall()
for i in recebido:
    print(f"O id do usuario é: {i[0]} e o nome é: {i[1]}")



conn.commit()

conn.close()
