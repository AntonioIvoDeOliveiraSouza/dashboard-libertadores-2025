create database libertadores2025;

use libertadores2025;

create table time(
	id_time int auto_increment not null,
	nome varchar(50) not null,
	pais varchar(25),
	primary key(id_time)
);

create table jogador(
	id_jogador int auto_increment not null,
	id_time int not null,
	nome varchar(50) not null,
	gols int,
	primary key(id_jogador),
	constraint fk_time foreign key(id_time) references time(id_time)
);

create table partida(
	id_partida int auto_increment not null,
	id_casa int not null,
	id_fora int not null,
	fase varchar(50) not null,
	data date,
	gols_casa int not null,
	gols_fora int not null,
	estadio varchar(50) not null,
	primary key(id_partida),
	constraint fk_time_casa foreign key(id_casa) references time(id_time),
	constraint fk_time_fora foreign key(id_fora) references time(id_time)
);

-- ## INSERTION DATA ##

insert into time(nome,pais)
	values("Botafogo","Brasil"),
	("LDU","Equador"),
	("Atlético Nacional","Colômbia"),
	("São Paulo","Brasil"),
	("Libertad","Paraguai"),
	("River Plate","Argentina"),
	("Universitario","Peru"),
	("Palmeiras","Brasil"),
	("Flamengo","Brasil"),
	("Internacional","Brasil"),
	("Cerro Porteno","Paraguai"),
	("Estudiantes","Argentina"),
	("Fortaleza","Brasil"),
	("Vélez Sarsfield","Argentina"),
	("Penarol","Uruguai"),
	("Racing","Argentina");

insert into partida(id_casa,id_fora,fase,data,gols_casa,gols_fora,estadio)
-- ## OITAVAS DE FINAL ##
values(1,2,'Oitavas de Final','2025-08-14',1,0,'Nilton Santos'),
(2,1,'Oitavas de Final','2025-08-21',2,0,'Rodrigo Paz Delgado'),
(3,4,'Oitavas de Final','2025-08-12',0,0,'El Atanasio'),
(4,3,'Oitavas de Final','2025-08-19',1,1,'Morumbis'),
(5,6,'Oitavas de Final','2025-08-14',0,0,'La Huerta'),
(6,5,'Oitavas de Final','2025-08-21',1,1,'Monumental'),
(7,8,'Oitavas de Final','2025-08-14',0,4,'Monumental U'),
(8,7,'Oitavas de Final','2025-08-21',0,0,'Allianz Parque'),
(9,10,'Oitavas de Final','2025-08-13',1,0,'Maracanã'),
(10,9,'Oitavas de Final','2025-08-20',0,2,'Beira-Rio'),
(11,12,'Oitavas de Final','2025-08-13',0,1,'ueno La Nueva Olla'),
(12,11,'Oitavas de Final','2025-08-20',0,0,'Jorge Luis Hirschi'),
(13,14,'Oitavas de Final','2025-08-12',0,0,'Castelão'),
(14,13,'Oitavas de Final','2025-08-19',2,0,'José Amalfitani'),
(15,16,'Oitavas de Final','2025-08-12',1,0,'Campeon Del Siglo'),
(16,15,'Oitavas de Final','2025-08-19',3,1,'Presidente Perón'),
-- ## QUARTAS DE FINAL ##
(2,4,'Quartas de Final','2025-09-18',2,0,'Rodrigo Paz Delgado'),
(4,2,'Quartas de Final','2025-09-25',0,1,'Morumbis'),
(6,8,'Quartas de Final','2025-09-17',1,2,'Monumental'),
(8,6,'Quartas de Final','2025-09-24',3,1,'Allianz Parque'),
(9,12,'Quartas de Final','2025-09-18',2,1,'Maracanã'),
(12,9,'Quartas de Final','2025-09-25',1,0,'José Luis Hirschi'),
(14,16,'Quartas de Final','2025-09-16',0,1,'José Amalfitani'),
(16,14,'Quartas de Final','2025-09-23',1,0,'Presidente Perón'),
-- ## SEMIFINAL ##
(2,8,'Semifinal','2025-10-23',3,0,'Rodrigo Paz Delgado'),
(8,2,'Semifinal','2025-10-30',4,0,'Allianz Parque'),
(9,16,'Semifinal','2025-10-22',1,0,'Maracanã'),
(16,9,'Semifinal','2025-10-29',0,0,'Presidente Perón');
-- ## FINAL SÓ 29 DE NOVEMBRO!

-- ##JOGADORES##
insert into jogador(id_time,nome,gols)
values(1,'Artur',1),
(2,'Villamíl',3),
(2,'Alzugaray',2),
(2,'Bryan Ramírez',1),
(2,'Michael Estrada',1),
(2,'Medina',1),
(4,'André Silva',1),
(5,'Robert Rojas',1),
(6,'Martínez Quarta',1),
(6,'Driussi',1),
(6,'Maximiliano Salas',1),
(8,'Bruno Fuchs',1),
(8,'Sosa',1),
(8,'Gustavo Gómez',2),
(8,'Raphael Veiga',2),
(8,'Vitor Roque',3),
(8,'Flaco López',4),
(9,'Bruno Henrique',1),
(9,'Arrascaeta',1),
(9,'Varela',1),
(9,'Carrascal',1),
(9,'Pedro',2),
(12,'Gastón Benedetti',1),
(12,'Ascacíbar',1),
(14,'Maher Carrizo',1),
(14,'Tomás Galván',1),
(15,'David Terans',1),
(15,'Nahuel Herrera',1),
(16,'Franco Pardo',1),
(16,'Adrián Martínez',3),
(16,'Santiago Solari',1);

-- #Jogadores de cada time
select time.nome as clube,jogador.nome as jogador from time join jogador on time.id_time = jogador.id_time;

-- #Total de times por país
select pais,count(*) as quantidade, group_concat(nome) as clubes from time group by pais order by clubes desc;

-- #Total de gols por time.
select time.nome, sum(jogador.gols) as gols_marcados from time join jogador on time.id_time = jogador.id_time group by jogador.id_time order by gols_marcados desc;

-- #Artilheiros da competição.
select time.nome, jogador.nome,jogador.gols as gols_no_mata_mata from time join jogador on jogador.id_time = time.id_time where gols>2 order by gols desc;

-- #Média de gols por fase.
select distinct fase,avg(gols_casa + gols_fora) as media_de_gol from partida group by fase;

-- #Quem fez mais gols como mandante
select time_casa.nome as clube, sum(partida.gols_casa) as gols_como_mandante
from time as time_casa join partida on time_casa.id_time = partida.id_casa
where partida.gols_casa>1 
group by time_casa.nome
order by gols_como_mandante desc;

-- #Quem fez mais gols como visitante.
select time_fora.nome as clube, sum(partida.gols_fora) as gols_como_visitante
from time as time_fora join partida on time_fora.id_time = partida.id_fora
where partida.gols_fora>1 
group by time_fora.nome
order by gols_como_visitante desc;

-- #Quais confrontos terminaram empatados.
select partida.fase,
	   concat(time_casa.nome,' X ',time_fora.nome) as jogo,
	   concat(partida.gols_casa,' X ',partida.gols_fora) as placar,
	   partida.estadio 
from partida join time as time_casa on partida.id_casa = time_casa.id_time 
			 join time as time_fora on partida.id_fora = time_fora.id_time
where gols_casa = gols_fora;


