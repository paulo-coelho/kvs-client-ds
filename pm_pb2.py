# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pm.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x08pm.proto\x12\x07project\"(\n\x05\x41luno\x12\x11\n\tmatricula\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\"(\n\tProfessor\x12\r\n\x05siape\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\"8\n\nDisciplina\x12\r\n\x05sigla\x18\x01 \x01(\t\x12\x0c\n\x04nome\x18\x02 \x01(\t\x12\r\n\x05vagas\x18\x03 \x01(\x05\"\x85\x01\n\x13RelatorioDisciplina\x12\'\n\ndisciplina\x18\x01 \x01(\x0b\x32\x13.project.Disciplina\x12%\n\tprofessor\x18\x02 \x01(\x0b\x32\x12.project.Professor\x12\x1e\n\x06\x61lunos\x18\x03 \x03(\x0b\x32\x0e.project.Aluno\"w\n\x10ResumoDisciplina\x12\'\n\ndisciplina\x18\x01 \x01(\x0b\x32\x13.project.Disciplina\x12%\n\tprofessor\x18\x02 \x01(\x0b\x32\x12.project.Professor\x12\x13\n\x0btotalAlunos\x18\x03 \x01(\x05\"%\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\x1b\n\rIdentificador\x12\n\n\x02id\x18\x01 \x01(\t\"8\n\x10\x44isciplinaPessoa\x12\x12\n\ndisciplina\x18\x01 \x01(\t\x12\x10\n\x08idPessoa\x18\x02 \x01(\t2\x85\x04\n\x0fPortalMatricula\x12\x41\n\x11\x41\x64icionaProfessor\x12\x19.project.DisciplinaPessoa\x1a\x0f.project.Status\"\x00\x12?\n\x0fRemoveProfessor\x12\x19.project.DisciplinaPessoa\x1a\x0f.project.Status\"\x00\x12=\n\rAdicionaAluno\x12\x19.project.DisciplinaPessoa\x1a\x0f.project.Status\"\x00\x12;\n\x0bRemoveAluno\x12\x19.project.DisciplinaPessoa\x1a\x0f.project.Status\"\x00\x12K\n\x11\x44\x65talhaDisciplina\x12\x16.project.Identificador\x1a\x1c.project.RelatorioDisciplina\"\x00\x12U\n\x19ObtemDisciplinasProfessor\x12\x16.project.Identificador\x1a\x1c.project.RelatorioDisciplina\"\x00\x30\x01\x12N\n\x15ObtemDisciplinasAluno\x12\x16.project.Identificador\x1a\x19.project.ResumoDisciplina\"\x00\x30\x01\x42)\n%br.ufu.facom.gbc074.projeto.matriculaP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pm_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n%br.ufu.facom.gbc074.projeto.matriculaP\001'
  _globals['_ALUNO']._serialized_start=21
  _globals['_ALUNO']._serialized_end=61
  _globals['_PROFESSOR']._serialized_start=63
  _globals['_PROFESSOR']._serialized_end=103
  _globals['_DISCIPLINA']._serialized_start=105
  _globals['_DISCIPLINA']._serialized_end=161
  _globals['_RELATORIODISCIPLINA']._serialized_start=164
  _globals['_RELATORIODISCIPLINA']._serialized_end=297
  _globals['_RESUMODISCIPLINA']._serialized_start=299
  _globals['_RESUMODISCIPLINA']._serialized_end=418
  _globals['_STATUS']._serialized_start=420
  _globals['_STATUS']._serialized_end=457
  _globals['_IDENTIFICADOR']._serialized_start=459
  _globals['_IDENTIFICADOR']._serialized_end=486
  _globals['_DISCIPLINAPESSOA']._serialized_start=488
  _globals['_DISCIPLINAPESSOA']._serialized_end=544
  _globals['_PORTALMATRICULA']._serialized_start=547
  _globals['_PORTALMATRICULA']._serialized_end=1064
# @@protoc_insertion_point(module_scope)
