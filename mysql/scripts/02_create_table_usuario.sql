use ac5;

create table usuario(
    cpf varchar(11),
    nome varchar(20),
    idade tinyint,
    constraint pk_usuario primary key(cpf)
);