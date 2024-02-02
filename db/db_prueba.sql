CREATE TABLE clientes (
  id_cliente INT NOT NULL,
  nombre VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  PRIMARY KEY (id_cliente)
);

.mode csv

.import --skip 1 datos.csv clientes

SELECT * FROM clientes limit 10;
