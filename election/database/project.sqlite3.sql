BEGIN TRANSACTION;
DROP TABLE IF EXISTS "votan";
CREATE TABLE IF NOT EXISTS "votan" (
	"id"	INTEGER NOT NULL,
	"matricule"	VARCHAR(50),
	"nom"	VARCHAR(25) NOT NULL,
	"prenom"	VARCHAR(100) NOT NULL,
	UNIQUE("matricule"),
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "post";
CREATE TABLE IF NOT EXISTS "post" (
	"id"	INTEGER NOT NULL,
	"nom"	VARCHAR(50),
	UNIQUE("nom"),
	PRIMARY KEY("id")
);
DROP TABLE IF EXISTS "candidature";
CREATE TABLE IF NOT EXISTS "candidature" (
	"id"	INTEGER NOT NULL,
	"votan_id"	INTEGER NOT NULL,
	"post_id"	INTEGER NOT NULL,
	UNIQUE("votan_id"),
	PRIMARY KEY("id"),
	FOREIGN KEY("votan_id") REFERENCES "votan"("id"),
	FOREIGN KEY("post_id") REFERENCES "post"("id")
);
DROP TABLE IF EXISTS "vote";
CREATE TABLE IF NOT EXISTS "vote" (
	"id"	INTEGER NOT NULL,
	"votan_id"	INTEGER NOT NULL,
	"candidature_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("votan_id") REFERENCES "votan"("id"),
	FOREIGN KEY("candidature_id") REFERENCES "candidature"("id")
);
INSERT INTO "votan" ("id","matricule","nom","prenom") VALUES (1,'RRDG65','ROUAMBA','ZACKARIE');
INSERT INTO "votan" ("id","matricule","nom","prenom") VALUES (2,'ZFZEF63','KABORE','BEN ABDOUL NASSIRE');
INSERT INTO "votan" ("id","matricule","nom","prenom") VALUES (3,'SDR445TTR','COULIBALY','MOUNIRA');
INSERT INTO "votan" ("id","matricule","nom","prenom") VALUES (4,'RHRHR','KABORE','ABDOUL');
INSERT INTO "votan" ("id","matricule","nom","prenom") VALUES (5,'SGREG','KAFANDO','KADER');
INSERT INTO "post" ("id","nom") VALUES (1,'Président');
INSERT INTO "post" ("id","nom") VALUES (2,'Trésorière');
INSERT INTO "post" ("id","nom") VALUES (3,'Vice Président');
INSERT INTO "candidature" ("id","votan_id","post_id") VALUES (1,1,1);
INSERT INTO "candidature" ("id","votan_id","post_id") VALUES (2,2,1);
INSERT INTO "candidature" ("id","votan_id","post_id") VALUES (3,3,2);
INSERT INTO "candidature" ("id","votan_id","post_id") VALUES (4,4,2);
COMMIT;
