# 6. В подключенном MySQL репозитории создать базу данных “Друзья человека”

create database Human_friends; 
use Human_friends;
drop database human_friends;
drop table animals;
drop table group_animals;
drop table animals;
drop table class_animals;
drop table animals_command;

# 7. Создать таблицы с иерархией из диаграммы в БД
create table group_animals
(
id int primary key auto_increment,
name_group varchar(45)
);

create table commands
(
id int primary key auto_increment,
name_commands varchar(45) not null
);

create table Animals 
(
id int primary key auto_increment,
name varchar(45) not null,
birthday date not null,
id_class_animals int not null,
foreign key(id_class_animals) references class_animals(id)
on delete cascade on update cascade)
;


create table animals_command
(
id_animals int not null,
foreign key(id_animals) references animals(id)
on delete cascade on update cascade,
id_commands int,
foreign key(id_commands) references commands(id)
on delete cascade on update cascade
);

create table class_animals
(
id int primary key auto_increment,
name_class varchar(45) not null,
id_group int not null,
foreign key(id_group) references group_animals(id)
on delete cascade on update cascade
);

select * from class_animals;

# 9. Заполнить низкоуровневые таблицы именами (животных), командами которые они выполняют и датами рождения

select * from group_animals;
INSERT INTO `human_friends`.`group_animals` (`name_group`)
VALUES ('Домашние животные'), ('Вьючные животные');

select * from commands;
INSERT INTO `human_friends`.`commands` (`name_commands`) VALUES 
('Ко мне'), -- 1
('Лежать'), -- 2
('Апорт'),  -- 3
('Бежать'), -- 4
('Прыгать'), -- 5
('Кувырок'), -- 6
('Охранять'), -- 7
('Рядом'), -- 8
('Нести'), -- 9
('Бежать на двух ногах'), -- 10
('Играть'), -- 11
('Галоп'), -- 12
('Крутиться'), -- 13
('Голос'), -- 14
('Петь'); -- 15

select * from class_animals;
INSERT INTO `human_friends`.`class_animals` (`name_class`, `id_group`) 
VALUES 
('Собака', '1'), -- 1
('Кошка', '1'), -- 2
('Хомяк', '1'), -- 3
('Лошадь', '2'), -- 4
('Осел', '2'), -- 5
('Верблюд', '2'); -- 6


select * from animals;
select * from animals
order by id_class_animals;
INSERT INTO `human_friends`.`animals` (`name`, `birthday`, `id_class_animals`) 
VALUES 
('Барсик', '2008-08-08', '1'),
('Васик', '2010-09-09', '2'),
('Рыжик', '2009-09-09', '4'),
('Иа', '2021-02-04', '5'),
('Гендель', '2024-03-01', '6'),
('Хома', '2023-03-05', '3'),
('Олененок', '2020-09-20', '6'),
('Черныш', '2019-12-29', '4'),
('Мурка', '2023-03-03', '2'),
('Малыш', '2023-09-11', '5'),
('Дружок', '2023-10-01', '1');

select a.id,a.name,ca.name_class from animals a
join class_animals ca
on
a.id_class_animals = ca.id
order by a.id;

insert into animals_command
(id_animals,id_commands)
values
(1,1),(1,2),(1,3),(1,14),
(2,13),(2,2),(3,1),(3,12),
(4,9),(5,9),(5,15),(6,6),
(7,9),(8,9),(8,12),(9,8),
(9,10),(10,11),(10,12),(10,13),
(11,13),(11,7),(11,14),(11,15);

select T.name as 'Имя',C.name_commands as 'Команда' from (select a.name, ac.id_commands from animals a
join animals_command ac
on a.id = ac.id_animals) as T
join commands C
on T.id_commands = C.id;

delete from animals
where id_class_animals = 6;

create table Horses_Donkeys   AS
SELECT * from animals WHERE id_class_animals = 4
UNION
SELECT * from animals WHERE id_class_animals = 5;
select * from Horses_Donkeys;

create table young_animals as
select id,name,birthday,id_class_animals,
datediff(curdate(),birthday) div 31 as 'возраст' from animals 
where birthday < '2023-07-09' and birthday > '2021-07-09';

select id, name, birthday, id_class_animals from horses_donkeys
union
select id, name, birthday, id_class_animals from young_animals;