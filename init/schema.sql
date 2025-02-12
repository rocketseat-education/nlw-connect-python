-- Criação da tabela Eventos
CREATE TABLE Eventos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
);

-- Criação da tabela Inscritos
CREATE TABLE Inscritos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    link TEXT,
    evento_id INTEGER NOT NULL,
    FOREIGN KEY (evento_id) REFERENCES Eventos (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Criação da tabela Eventos_link
CREATE TABLE Eventos_link (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evento_id INTEGER NOT NULL,
    inscrito_id INTEGER NOT NULL,
    link TEXT,
    FOREIGN KEY (evento_id) REFERENCES Eventos (id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (inscrito_id) REFERENCES Inscritos (id) ON DELETE CASCADE ON UPDATE CASCADE
);