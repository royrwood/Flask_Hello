-- psql -d helloflask -a -f create_db.sql
--
-- pg_ctl -o "-F -p 12345" start
-- sudo /etc/init.d/postgresql start|stop|restart
--

CREATE TABLE IF NOT EXISTS people(id serial primary key, firstname varchar(255), lastname varchar(255), tstamp timestamp default current_timestamp);
CREATE TABLE IF NOT EXISTS address(id serial primary key, people_id int, street varchar(255), city varchar(255));
CREATE TABLE IF NOT EXISTS bikes(id serial primary key, people_id integer, description varchar(255));

INSERT INTO people(firstname,lastname) VALUES('Roy','Wood');
INSERT INTO people(firstname,lastname) VALUES('Bart','Simpson');
INSERT INTO people(firstname,lastname) VALUES('Clarus','Dogcow');

INSERT INTO address(people_id,street,city) SELECT id,'1074 Dearness Drive','London' FROM people WHERE firstname='Roy' AND lastname='Wood';
INSERT INTO address(people_id,street,city) SELECT id,'742 Evergreen Terrace','Springfield' FROM people WHERE firstname='Bart' AND lastname='Simpson';
INSERT INTO address(people_id,street,city) SELECT id,'1 Infinite Loop','Cupertino' FROM people WHERE firstname='Clarus' AND lastname='Dogcow';

INSERT INTO bikes(people_id,description) SELECT id,'Gary Fisher Montare' FROM people WHERE firstname='Roy' AND lastname='Wood';
INSERT INTO bikes(people_id,description) SELECT id,'Trek Top Fuel 8' FROM people WHERE firstname='Roy' AND lastname='Wood';
INSERT INTO bikes(people_id,description) SELECT id,'KHS 3000' FROM people WHERE firstname='Roy' AND lastname='Wood';
INSERT INTO bikes(people_id,description) SELECT id,'Green BMX' FROM people WHERE firstname='Bart' AND lastname='Simpson';

SELECT p.id,p.firstname,p.lastname,a.street,a.city,b.description FROM people p LEFT OUTER JOIN address a ON a.people_id = p.id LEFT OUTER JOIN bikes b ON b.people_id = p.id;
