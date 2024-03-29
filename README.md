# Key-value store client

Implementation of KVS according to specifications [here](https://paulo-coelho.github.io/ds_notes/projeto/).

## Compilation

Run `./compile.sh`

## Usage

### Servers (your own servers)

* Run at least one instance of each server with different port as argument:

`./admin_server.sh <port>`

`./mat_server.sh <port>`

### Clients

* Run clients to update the server state (use `-h` to see available arguments):

`./admin_client.sh <arg1> <arg2> ... <argn>`

`./mat_client.sh <arg1> <arg2> ... <argn>`


## Examples and expected output

Example with 3 classes, 3 students and 3 professors (available in `test.sh`)

```bash
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
```

Expected output:

```bash
args = Namespace(port=9000, op='create', base='aluno', key='aaaa', val=['joao'])
Response:


args = Namespace(port=9000, op='create', base='aluno', key='bbbb', val=['maria'])
Response:


args = Namespace(port=9000, op='create', base='aluno', key='cccc', val=['jose'])
Response:


args = Namespace(port=9000, op='create', base='professor', key='1111', val=['paulo'])
Response:


args = Namespace(port=9000, op='create', base='professor', key='2222', val=['pedro'])
Response:


args = Namespace(port=9000, op='create', base='professor', key='3333', val=['rafael'])
Response:


args = Namespace(port=9000, op='create', base='disciplina', key='gbc001', val=['materia1', '1'])
Response:


args = Namespace(port=9000, op='create', base='disciplina', key='gbc002', val=['materia2', '2'])
Response:


args = Namespace(port=9000, op='create', base='disciplina', key='gbc003', val=['materia3', '3'])
Response:


args = Namespace(port=9001, op='getall', base='professor', key=None, val=None)
Response:
[siape: "1111"
nome: "paulo"
, siape: "2222"
nome: "pedro"
, siape: "3333"
nome: "rafael"
]

args = Namespace(port=9001, op='update', base='professor', key='3333', val=['luis'])
Response:


args = Namespace(port=9000, op='getall', base='professor', key=None, val=None)
Response:
[siape: "1111"
nome: "paulo"
, siape: "2222"
nome: "pedro"
, siape: "3333"
nome: "luis"
]

args = Namespace(port=8000, op='add_prof', val=['gbc001', '1111'])
Response:


args = Namespace(port=8000, op='add_prof', val=['gbc002', '2222'])
Response:


args = Namespace(port=8000, op='add_prof', val=['gbc003', '3333'])
Response:


args = Namespace(port=8000, op='add_aluno', val=['gbc001', 'aaaa'])
Response:


args = Namespace(port=8000, op='add_aluno', val=['gbc001', 'bbbb'])
Response:
status: 1
msg: "Disciplina gbc001 já atingiu a capacidade máxima de 1"


args = Namespace(port=8000, op='add_aluno', val=['gbc002', 'aaaa'])
Response:


args = Namespace(port=8000, op='add_aluno', val=['gbc002', 'bbbb'])
Response:


args = Namespace(port=8000, op='add_aluno', val=['gbc003', 'aaaa'])
Response:


args = Namespace(port=8000, op='add_aluno', val=['gbc003', 'bbbb'])
Response:


args = Namespace(port=8000, op='add_aluno', val=['gbc003', 'cccc'])
Response:


args = Namespace(port=8000, op='rel_disc', val=['gbc001'])
Response:
disciplina {
  sigla: "gbc001"
  nome: "materia1"
  vagas: 1
}
professor {
  siape: "1111"
  nome: "paulo"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}


args = Namespace(port=8000, op='rel_disc', val=['gbc002'])
Response:
disciplina {
  sigla: "gbc002"
  nome: "materia2"
  vagas: 2
}
professor {
  siape: "2222"
  nome: "pedro"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}
alunos {
  matricula: "bbbb"
  nome: "maria"
}


args = Namespace(port=8000, op='rel_disc', val=['gbc003'])
Response:
disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}
alunos {
  matricula: "bbbb"
  nome: "maria"
}
alunos {
  matricula: "cccc"
  nome: "jose"
}


args = Namespace(port=8000, op='rel_prof', val=['1111'])
Response:
[disciplina {
  sigla: "gbc001"
  nome: "materia1"
  vagas: 1
}
professor {
  siape: "1111"
  nome: "paulo"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}
]

args = Namespace(port=8000, op='rel_prof', val=['2222'])
Response:
[disciplina {
  sigla: "gbc002"
  nome: "materia2"
  vagas: 2
}
professor {
  siape: "2222"
  nome: "pedro"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}
alunos {
  matricula: "bbbb"
  nome: "maria"
}
]

args = Namespace(port=8000, op='rel_prof', val=['3333'])
Response:
[disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}
alunos {
  matricula: "bbbb"
  nome: "maria"
}
alunos {
  matricula: "cccc"
  nome: "jose"
}
]

args = Namespace(port=8000, op='rel_aluno', val=['aaaa'])
Response:
[disciplina {
  sigla: "gbc001"
  nome: "materia1"
  vagas: 1
}
professor {
  siape: "1111"
  nome: "paulo"
}
totalAlunos: 1
, disciplina {
  sigla: "gbc002"
  nome: "materia2"
  vagas: 2
}
professor {
  siape: "2222"
  nome: "pedro"
}
totalAlunos: 2
, disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
totalAlunos: 3
]

args = Namespace(port=8000, op='rel_aluno', val=['bbbb'])
Response:
[disciplina {
  sigla: "gbc002"
  nome: "materia2"
  vagas: 2
}
professor {
  siape: "2222"
  nome: "pedro"
}
totalAlunos: 2
, disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
totalAlunos: 3
]

args = Namespace(port=8000, op='rel_aluno', val=['cccc'])
Response:
[disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
totalAlunos: 3
]

args = Namespace(port=9000, op='delete', base='aluno', key='bbbb', val=None)
Response:


args = Namespace(port=9000, op='delete', base='professor', key='2222', val=None)
Response:


args = Namespace(port=8001, op='rel_disc', val=['gbc001'])
Response:
disciplina {
  sigla: "gbc001"
  nome: "materia1"
  vagas: 1
}
professor {
  siape: "1111"
  nome: "paulo"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}


args = Namespace(port=8001, op='rel_disc', val=['gbc002'])
Response:
disciplina {
  sigla: "gbc002"
  nome: "materia2"
  vagas: 2
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}


args = Namespace(port=8001, op='rel_disc', val=['gbc003'])
Response:
disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}
alunos {
  matricula: "cccc"
  nome: "jose"
}


args = Namespace(port=8001, op='rel_prof', val=['1111'])
Response:
[disciplina {
  sigla: "gbc001"
  nome: "materia1"
  vagas: 1
}
professor {
  siape: "1111"
  nome: "paulo"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}
]

args = Namespace(port=8001, op='rel_prof', val=['2222'])
Response:
[]

args = Namespace(port=8001, op='rel_prof', val=['3333'])
Response:
[disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
alunos {
  matricula: "aaaa"
  nome: "joao"
}
alunos {
  matricula: "cccc"
  nome: "jose"
}
]

args = Namespace(port=8001, op='rel_aluno', val=['aaaa'])
Response:
[disciplina {
  sigla: "gbc001"
  nome: "materia1"
  vagas: 1
}
professor {
  siape: "1111"
  nome: "paulo"
}
totalAlunos: 1
, disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
totalAlunos: 2
]

args = Namespace(port=8001, op='rel_aluno', val=['bbbb'])
Response:
[]

args = Namespace(port=8001, op='rel_aluno', val=['cccc'])
Response:
[disciplina {
  sigla: "gbc003"
  nome: "materia3"
  vagas: 3
}
professor {
  siape: "3333"
  nome: "luis"
}
totalAlunos: 2
]
```
