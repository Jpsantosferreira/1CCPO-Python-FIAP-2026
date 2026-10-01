from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Ciência da Computação")

# criar / instanciar 2 disciplinas
sers = Disciplina("Soluções Renováveis", "Tritiack")
cs = Disciplina("Computer Science", "Lucas")

# matricular o aluno nas disciplinas
aluno1.matricular(sers)
aluno1.matricular(cs)

# print(aluno1.disciplinas[0].nome)
# print(aluno1.disciplinas[0].professor)
# print(aluno1.disciplinas[1].nome)
# print(aluno1.disciplinas[1].professor)

# adicionar notas do aluno referente às disciplinas
aluno1.adicionar_nota(sers, 10)
aluno1.adicionar_nota(sers, 8)
aluno1.adicionar_nota(cs, 5)
aluno1.adicionar_nota(cs, 3)
print(aluno1.notas_por_disciplina)

# print da media!
print(aluno1.calcular_media_d(cs))

print(aluno1.calcular_media_g())