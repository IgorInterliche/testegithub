aluno = input('Digite o nome do aluno: ')
nota1 = int(input('Digite a \033[31mprimeira nota\033[m de {}: '.format(aluno)))
nota2 = int(input('Digite a \033[34msegunda nota\033[m de {}: '.format(aluno)))
media = (nota1+nota2)/2
print('A media do aluno \033[36m{}\033[m é \033[36m{}'.format(aluno, media))
