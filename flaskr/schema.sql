DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS Sex;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS B_symptoms;
DROP TABLE IF EXISTS Histologic;
DROP TABLE IF EXISTS Stage;
DROP TABLE IF EXISTS Protocol;
DROP TABLE IF EXISTS Group_diag;
DROP TABLE IF EXISTS Anat_request;
DROP TABLE IF EXISTS Deauville_score;
DROP TABLE IF EXISTS Main_request;
DROP TABLE IF EXISTS Event;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

INSERT INTO user VALUES (1, 'admin', 'admin');

CREATE TABLE person (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  fio VARCHAR,
  early_toxicity VARCHAR,
  ray_therapy VARCHAR,
  ray_therapy_comp VARCHAR,
  sex INTEGER,
  event INTEGER,
  main_request INTEGER,
  deauville_score INTEGER,
  anat_request INTEGER,
  groups INTEGER,
  protocol INTEGER,
  stage INTEGER,
  histologic INTEGER,
  b_symptoms INTEGER,
  region VARCHAR,
  e_impact VARCHAR,
  bm_damage_myelogram VARCHAR,
  bm_damage_kt VARCHAR,
  request_pat VARCHAR,
  start_therapy_date DATE,
  end_therapy_date DATE,
  event_date DATE,
  last_date DATE,
  birth_date DATE,
  leykocytes INTEGER,
  hemoglobin INTEGER,
  trombocytes INTEGER,
  ldh INTEGER,
  ebv INTEGER,
  esr INTEGER,
  init_val INTEGER,
  tumor_val INTEGER
);

CREATE TABLE Sex (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Sex VALUES 
  ('male', 'M'),
  ('female', 'F'),
  ('unknown', 'U');

CREATE TABLE B_symptoms (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO B_symptoms VALUES
  ('sweating', 'Потливость'),
  ('fever', 'Лихорадка'),
  ('weight_loss', 'Снижение массы тела');


CREATE TABLE Histologic (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Histologic VALUES
  ('nod_sclerosis', 'Нодулярный склероз'),
  ('mixed_cell', 'Смешанно-клеточный вариант'),
  ('lymphocytic_predominance', 'Лимфоцитарное преобладание'),
  ('lymphocytic_depletion', 'Лимфоцитарное истощение'),
  ('nos', 'NOS'),
  ('nod_type', 'Нодулярный тип с лимфоцитарным преобладанием');

CREATE TABLE Stage (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Stage VALUES
  ('stage_1', 'I'),
  ('stage_2', 'II'),
  ('stage_3', 'III'),
  ('stage_4', 'IV');

CREATE TABLE Protocol (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Protocol VALUES
  ('euroNet', 'EuroNet-PHL-C1'),
  ('dal_2002', 'DAL-GPOH-2002'),
  ('dal_2003', 'DAL-GPOH-2003'),
  ('dal_1995', 'DAL-HD-1995'),
  ('no_protocol', 'Непрограмная терапия');

CREATE TABLE Group_diag (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Group_diag VALUES
  ('tg_1', 'TG-1'),
  ('tg_2', 'TG-2'),
  ('tg_3', 'TG-3');

CREATE TABLE Anat_request (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Anat_request VALUES
  ('full_remission', 'полная ремиссия'),
  ('full_not_resp', 'полная ремиссия неподтвержденная'),
  ('part_remission', 'частичная ремиссия'),
  ('not_change', 'без изменений'),
  ('progression', 'прогрессия');

CREATE TABLE Deauville_score (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Deauville_score VALUES
  ('ds_1', 'DS=1'),
  ('ds_2', 'DS=2'),
  ('ds_3', 'DS=3'),
  ('ds_4', 'DS=4'),
  ('ds_5', 'DS=5');

CREATE TABLE Main_request (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Main_request VALUES
  ('adequate', 'Адекватный ответ'),
  ('inadequate', 'Неадекватный ответ');

CREATE TABLE Event (
  id VARCHAR,
  code VARCHAR
);

INSERT INTO Event VALUES
  ('no', 'Отсутствует'),
  ('relapse', 'Рецидив'),
  ('progression', 'Прогрессия'),
  ('transform', 'Трансформация'),
  ('death', 'Смерть');
