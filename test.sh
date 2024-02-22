#!/bin/bash

pipenv shell

# cria alguns alunos
python3 admin_client.py --port 9000 --base aluno --op create --key aaaa --val joao
python3 admin_client.py --port 9000 --base aluno --op create --key bbbb --val maria
python3 admin_client.py --port 9000 --base aluno --op create --key cccc --val jose

#cria alguns professores
python3 admin_client.py --port 9000 --base professor --op create --key 1111 --val paulo
python3 admin_client.py --port 9000 --base professor --op create --key 2222 --val pedro
python3 admin_client.py --port 9000 --base professor --op create --key 3333 --val rafael

#cria alguns disciplinas com nome e numero de vagas
python3 admin_client.py --port 9000 --base disciplina --op create --key gbc001 --val materia1 1
python3 admin_client.py --port 9000 --base disciplina --op create --key gbc002 --val materia2 2
python3 admin_client.py --port 9000 --base disciplina --op create --key gbc003 --val materia3 3

#lista professores em outro portal administrativo
python3 admin_client.py --port 9001 --base professor --op getall

#edita professor em outro portal administrativo
python3 admin_client.py --port 9001 --base professor --op update --key 3333 --val luis

#lista professores no primeiro portal administrativo
python3 admin_client.py --port 9000 --base professor --op getall

#adiciona professores a disciplinas no portal de matriculas
python3 mat_client.py --port 8000 --op add_prof --val gbc001 1111
python3 mat_client.py --port 8000 --op add_prof --val gbc002 2222
python3 mat_client.py --port 8000 --op add_prof --val gbc003 3333

#adiciona alunos a disciplinas no portal de matriculas
python3 mat_client.py --port 8000 --op add_aluno --val gbc001 aaaa
python3 mat_client.py --port 8000 --op add_aluno --val gbc001 bbbb # excede limite da disciplina
python3 mat_client.py --port 8000 --op add_aluno --val gbc002 aaaa
python3 mat_client.py --port 8000 --op add_aluno --val gbc002 bbbb
python3 mat_client.py --port 8000 --op add_aluno --val gbc003 aaaa
python3 mat_client.py --port 8000 --op add_aluno --val gbc003 bbbb
python3 mat_client.py --port 8000 --op add_aluno --val gbc003 cccc

#imprime relatorios no portal de matriculas
python3 mat_client.py --port 8000 --op rel_disc --val gbc001
python3 mat_client.py --port 8000 --op rel_disc --val gbc002
python3 mat_client.py --port 8000 --op rel_disc --val gbc003
python3 mat_client.py --port 8000 --op rel_prof --val 1111
python3 mat_client.py --port 8000 --op rel_prof --val 2222
python3 mat_client.py --port 8000 --op rel_prof --val 3333
python3 mat_client.py --port 8000 --op rel_aluno --val aaaa
python3 mat_client.py --port 8000 --op rel_aluno --val bbbb
python3 mat_client.py --port 8000 --op rel_aluno --val cccc

#remove 1 aluno e 1 professor no portal administrativo
python3 admin_client.py --port 9000 --base aluno --op delete --key bbbb
python3 admin_client.py --port 9000 --base professor --op delete  --key 2222

#imprime novamente relatorios em outro portal de matriculas
python3 mat_client.py --port 8001 --op rel_disc --val gbc001
python3 mat_client.py --port 8001 --op rel_disc --val gbc002
python3 mat_client.py --port 8001 --op rel_disc --val gbc003
python3 mat_client.py --port 8001 --op rel_prof --val 1111
python3 mat_client.py --port 8001 --op rel_prof --val 2222
python3 mat_client.py --port 8001 --op rel_prof --val 3333
python3 mat_client.py --port 8001 --op rel_aluno --val aaaa
python3 mat_client.py --port 8001 --op rel_aluno --val bbbb
python3 mat_client.py --port 8001 --op rel_aluno --val cccc
