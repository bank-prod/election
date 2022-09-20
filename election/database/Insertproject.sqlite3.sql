BEGIN TRANSACTION;
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
