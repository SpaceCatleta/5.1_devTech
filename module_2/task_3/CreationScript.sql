
CREATE TABLE IF NOT EXISTS 'source' (
    'id' INT PRIMARY KEY,
    'name' VARCHAR(255)
    );

=====

CREATE TABLE IF NOT EXISTS 'status' (
    'id' INT PRIMARY KEY,
    'name' VARCHAR(255)
    );

=====

CREATE TABLE IF NOT EXISTS 'category' (
    'id' INT PRIMARY KEY,
    'name' VARCHAR(255)
    );

=====

CREATE TABLE IF NOT EXISTS 'good' (
    'id' INT PRIMARY KEY,
    'name' VARCHAR(255),
    'price' REAL
    );

=====

CREATE TABLE IF NOT EXISTS 'client' (
    'id' int PRIMARY KEY,
    'code' VARCHAR(45),
    'first_name' VARCHAR(45),
    'last_name' VARCHAR(45),
    'source_id' INT REFERENCES source (id)
    );

=====


CREATE TABLE IF NOT EXISTS 'sale' (
    'id' INT PRIMARY KEY,
    'client_id' INT REFERENCES client (id),
    'number' VARCHAR(255),
    'dt_created' VARCHAR(19),
    'dt_modified' VARCHAR(19),
    'sale_sum' REAL,
    'status_id' INT REFERENCES status (id)
    );

=====

CREATE TABLE IF NOT EXISTS 'sale_history' (
    'id' INT PRIMARY KEY,
    'sale_id' INT REFERENCES sale (id),
    'status_id' INT REFERENCES status (id),
    'sale_sum' REAL,
    'active_from' VARCHAR(19),
    'active_to' VARCHAR(19)
    );

=====

CREATE TABLE IF NOT EXISTS 'sale_has_good' (
    'sale_id' INT REFERENCES sale (id),
    'good_id' INT REFERENCES good (id),
    
    PRIMARY KEY (sale_id, good_id)
    );

=====

CREATE TABLE IF NOT EXISTS 'category_has_good' (
    'category_id' INT REFERENCES category (id),
    'good_id' INT REFERENCES good (id),
    
    PRIMARY KEY (category_id, good_id)
    );

=====
INSERT INTO good (id, name, price)
VALUES (1, 'good1', 10);
=====
INSERT INTO good (id, name, price)
VALUES (2, 'good2', 30);
=====
INSERT INTO good (id, name, price)
VALUES (3, 'good3', 15);

=====
INSERT INTO category (id, name)
VALUES (1, 'category1');
=====
INSERT INTO category (id, name)
VALUES (2, 'category2');
=====
INSERT INTO category (id, name)
VALUES (3, 'category3');

=====
INSERT INTO category_has_good (category_id, good_id)
VALUES (1, 1);
=====
INSERT INTO category_has_good (category_id, good_id)
VALUES (1, 3);
=====
INSERT INTO category_has_good (category_id, good_id)
VALUES (2, 2);
=====
INSERT INTO category_has_good (category_id, good_id)
VALUES (2, 3);
=====
INSERT INTO category_has_good (category_id, good_id)
VALUES (3, 1);
=====
INSERT INTO category_has_good (category_id, good_id)
VALUES (3, 2);

