CREATE TABLE usuarios (
	id INTEGER,
    nome VARCHAR(120) NOT NULL COMMENT 'Nome do usuário',
    email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuário',
    endereco VARCHAR(50) NOT NULL COMMENT 'Endereço do usuário',
    data_nascimento DATE NOT NULL COMMENT 'Data de nascimento do usuário'
    );

CREATE TABLE viagens.destino (
	id INTEGER,
    nome VARCHAR(120) NOT NULL UNIQUE COMMENT 'Nome do destino',
    descricao VARCHAR(255) NOT NULL COMMENT 'Descrição do destino'
);

CREATE TABLE viagens.reservas(
	id INTEGER COMMENT 'Identificador único da reserva',
    id_usuario INTEGER COMMENT 'Referência ao ID do usuário que fez a reserva',
    id_destino INTEGER COMMENT 'Referência ao ID do destino da reserva',
    data DATE COMMENT 'Data da reserva',
    status VARCHAR(255) DEFAULT 'Pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada)'
);

INSERT INTO destino
	(id, nome, descricao)
VALUES
	(1, 'Rio de Janeiro', 'A cidade maravilhosa');


INSERT INTO reservas
	(id, id_usuario, id_destino, data, status)
VALUES
	(1, 1, 1, '2024-07-12', 'aprovado');

-- Alterando o nome da tabela destino para destinos
ALTER TABLE destino RENAME destinos;

-- Abaixo, irei inserir os valores disponibilizados na aula

INSERT INTO viagens.usuarios (id, nome, email, data_nascimento, endereco) VALUES 
(2, 'João Silva', 'joao@example.com', '1990-05-15', 'Rua A, 123, Cidade X, Estado Y'),
(3, 'Maria Santos', 'maria@example.com', '1985-08-22', 'Rua B, 456, Cidade Y, Estado Z'),
(4, 'Pedro Souza', 'pedro@example.com', '1998-02-10', 'Avenida C, 789, Cidade X, Estado Y');

INSERT INTO viagens.destinos (id, nome, descricao) VALUES 
(2, 'Praia das Tartarugas', 'Uma bela praia com areias brancas e mar cristalino'),
(3, 'Cachoeira do Vale Verde', 'Uma cachoeira exuberante cercada por natureza'),
(4, 'Cidade Histórica de Pedra Alta', 'Uma cidade rica em história e arquitetura');

INSERT INTO viagens.reservas (id, id_usuario, id_destino, data, status) VALUES 
(2, 2, 2, '2023-07-10', 'confirmada'),
(3, 3, 1, '2023-08-05', 'pendente'),
(4, 4, 3, '2023-09-20', 'cancelada');

-- Alterando o tamanho da coluna endereco da tabela usuarios
ALTER TABLE usuarios MODIFY endereco VARCHAR(150);

-- Alterando a tabela usuarios para que id seja PK com autoincremento
ALTER TABLE usuarios
MODIFY COLUMN id INTEGER AUTO_INCREMENT, 
ADD PRIMARY KEY (id);

-- Alterando a tabela destinos para que id seja PK com autoincremento
ALTER TABLE destinos
MODIFY COLUMN id INTEGER AUTO_INCREMENT,
ADD PRIMARY KEY (id);

-- Alterando a tabela reservas para que id seja PK com autoincremento
ALTER TABLE reservas
MODIFY COLUMN id INTEGER AUTO_INCREMENT,
ADD PRIMARY KEY (id);

-- Adicionando as chaves estrangeiras na tabela reservas

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario)
REFERENCES usuarios(id);

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destino)
REFERENCES destinos(id);

-- Adicionando o evento de exclusão em cascata

ALTER TABLE reservas
ADD CONSTRAINT fk_usuarios
FOREIGN KEY (id_usuario) REFERENCES usuarios(id)
ON DELETE CASCADE

-- Normalizando o campo endereço da tabela usuarios

ALTER TABLE usuarios
ADD rua VARCHAR(100),
ADD numero VARCHAR(10),
ADD cidade VARCHAR(50),
ADD estado VARCHAR(20);

-- Preenchendo os novos campos

UPDATE usuarios
SET rua = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 1), ',', -1),
numero = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 2), ',', -1),
cidade = SUBSTRING_INDEX(SUBSTRING_INDEX(endereco, ',', 3), ',', -1),
estado = SUBSTRING_INDEX(endereco, ',', -1)

-- Apagando a coluna endereco

ALTER TABLE usuarios
DROP COLUMN endereco;

-- Realizando consulta com INNER JOIN

SELECT * FROM usuarios u
INNER JOIN reservas r ON u.id = r.id_usuario
INNER JOIN destinos d ON r.id_destino = d.id;

-- Contando quantos usuários possuem reserva

SELECT COUNT(*) AS total FROM usuarios u
INNER JOIN reservas r ON u.id = r.id_usuario

-- Trazendo o usuário com a maior idade

SELECT MAX(TIMESTAMPDIFF(YEAR, data_nascimento, CURRENT_DATE())) AS MAIOR_IDADE
FROM usuarios;

-- Consultando quantas reservas temos para o destino 3

SELECT COUNT(*), id_destino FROM reservas
GROUP BY id_destino;

-- Ordenando a consulta de maneira descendente

SELECT COUNT(*) AS Qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas DESC;

SELECT COUNT(*) AS Qtd_reservas, id_destino FROM reservas
GROUP BY id_destino
ORDER BY qtd_reservas DESC, id_destino DESC;

-- Inserindo 30 novos usuários

INSERT INTO usuarios (nome, email, data_nascimento, rua) VALUES
('João Silva', 'joao.silva@example.com', '1990-01-01', 'Rua A'),
('Maria Santos', 'maria.santos@example.com', '1992-03-15', 'Rua B'),
('Pedro Almeida', 'pedro.almeida@example.com', '1985-07-10', 'Rua C'),
('Ana Oliveira', 'ana.oliveira@example.com', '1998-12-25', 'Rua D'),
('Carlos Pereira', 'carlos.pereira@example.com', '1991-06-05', 'Rua E'),
('Laura Mendes', 'laura.mendes@example.com', '1994-09-12', 'Rua F'),
('Fernando Santos', 'fernando.santos@example.com', '1988-02-20', 'Rua G'),
('Mariana Costa', 'mariana.costa@example.com', '1997-11-30', 'Rua H'),
('Ricardo Rodrigues', 'ricardo.rodrigues@example.com', '1993-04-18', 'Rua I'),
('Camila Alves', 'camila.alves@example.com', '1989-08-08', 'Rua J'),
('Bruno Carvalho', 'bruno.carvalho@example.com', '1995-03-25', 'Rua K'),
('Amanda Silva', 'amanda.silva@example.com', '1996-12-02', 'Rua L'),
('Paulo Mendonça', 'paulo.mendonca@example.com', '1999-07-20', 'Rua M'),
('Larissa Oliveira', 'larissa.oliveira@example.com', '1987-10-15', 'Rua N'),
('Fernanda Sousa', 'fernanda.sousa@example.com', '1992-05-08', 'Rua O'),
('Gustavo Santos', 'gustavo.santos@example.com', '1993-09-18', 'Rua P'),
('Helena Costa', 'helena.costa@example.com', '1998-02-22', 'Rua Q'),
('Diego Almeida', 'diego.almeida@example.com', '1991-11-27', 'Rua R'),
('Juliana Lima', 'juliana.lima@example.com', '1997-04-05', 'Rua S'),
('Rafaela Silva', 'rafaela.silva@example.com', '1996-01-10', 'Rua T'),
('Lucas Pereira', 'lucas.pereira@example.com', '1986-08-30', 'Rua U'),
('Fábio Rodrigues', 'fabio.rodrigues@example.com', '1989-03-12', 'Rua V'),
('Isabela Santos', 'isabela.santos@example.com', '1994-12-07', 'Rua W'),
('André Alves', 'andre.alves@example.com', '1995-09-28', 'Rua X'),
('Clara Carvalho', 'clara.carvalho@example.com', '1990-02-15', 'Rua Y'),
('Roberto Mendes', 'roberto.mendes@example.com', '1992-07-21', 'Rua Z'),
('Mariana Oliveira', 'mariana.oliveira@example.com', '1997-05-03', 'Av. A'),
('Gustavo Costa', 'gustavo.costa@example.com', '1998-11-16', 'Av. B'),
('Lara Sousa', 'lara.sousa@example.com', '1993-06-09', 'Av. C'),
('Pedro Lima', 'pedro.lima@example.com', '1996-09-27', 'Av. D');

-- Utilizando o EXPLAIN

EXPLAIN
	SELECT * FROM usuarios
    WHERE email = "joao.silva@example.com";
-- Como a coluna email tem a sintaxe UNIQUE, ele identificou 1 linha.
    
EXPLAIN
	SELECT * FROM usuarios
    WHERE nome = "João Silva"
-- Como a coluna nome não tem a sintaxe UNIQUE nem índice, ele identificou 34 linhas

-- Vamos criar um INDEX para reavaliar essa busca

CREATE INDEX idx_nome ON usuarios(nome);

-- Agora vamos reavaliar a consulta:

EXPLAIN
	SELECT * FROM usuarios
    WHERE nome = "João";
-- Com o índice, ele identificou apenas 2 linha.