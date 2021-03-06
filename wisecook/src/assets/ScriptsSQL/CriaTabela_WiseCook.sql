CREATE TABLE USUARIO (
	idUsuario BIGSERIAL NOT NULL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	restricoes VARCHAR(50)[]
);

CREATE TABLE ALIMENTO (
	nome VARCHAR(50) NOT NULL PRIMARY KEY,
	descricao VARCHAR(250),
	medida VARCHAR(50) NOT NULL
);

CREATE TABLE RECEITA (
	nome VARCHAR(50) NOT NULL PRIMARY KEY,
	modoPreparo VARCHAR(1000)
);

CREATE TABLE UTILIZA (
	nomeReceita VARCHAR(50),
	nomeAlimento VARCHAR(50),
	quantidade FLOAT8 NOT NULL,
	CONSTRAINT fk_receita
    	FOREIGN KEY (nomeReceita) REFERENCES RECEITA(nome)
			ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_alimento
    	FOREIGN KEY (nomeAlimento) REFERENCES ALIMENTO(nome)
			ON DELETE SET NULL ON UPDATE CASCADE,
    PRIMARY KEY (nomereceita, nomealimento)
);

CREATE TABLE POSSUI (
	usuario INT,
	nomeAlimento VARCHAR(50),
	dataValidade DATE NOT NULL,
	quantidade FLOAT8 NOT NULL,
	CONSTRAINT fk_usuario
    	FOREIGN KEY (usuario) REFERENCES USUARIO(idUsuario)
			ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_alimento
    	FOREIGN KEY (nomeAlimento) REFERENCES ALIMENTO(nome)
			ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (usuario, nomealimento, datavalidade)
);

CREATE TABLE RECOMENDADA(
	nomeReceita VARCHAR(50),
	usuario INT,
	correspondencia FLOAT8,
	CONSTRAINT fk_usuario
    	FOREIGN KEY (usuario) REFERENCES USUARIO(idUsuario)
			ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT fk_receita
    	FOREIGN KEY (nomeReceita) REFERENCES RECEITA(nome)
			ON DELETE CASCADE ON UPDATE CASCADE,
    PRIMARY KEY (nomereceita, usuario)
);