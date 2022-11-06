BEGIN;
--
-- Create model User
--
CREATE TABLE "users_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "active" bool NOT NULL, "name" varchar(200) NOT NULL, "email" varchar(200) NOT NULL UNIQUE, "password" varchar(30) NOT NULL);
COMMIT;
[0m