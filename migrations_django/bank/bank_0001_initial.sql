BEGIN;
--
-- Create model Account
--
CREATE TABLE "bank_account" ("number" integer NOT NULL UNIQUE, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "active" bool NOT NULL, "balance" decimal NOT NULL, "user_id" bigint NULL UNIQUE REFERENCES "users_user" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model KeyPix
--
CREATE TABLE "bank_keypix" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "active" bool NOT NULL, "key" varchar(255) NOT NULL, "type_key" varchar(16) NOT NULL, "account_id" bigint NOT NULL REFERENCES "bank_account" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Agency
--
CREATE TABLE "bank_agency" ("number" integer NOT NULL UNIQUE, "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "active" bool NOT NULL);
CREATE TABLE "bank_agency_accounts" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "agency_id" bigint NOT NULL REFERENCES "bank_agency" ("id") DEFERRABLE INITIALLY DEFERRED, "account_id" bigint NOT NULL REFERENCES "bank_account" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "bank_keypix_account_id_7ebba0ed" ON "bank_keypix" ("account_id");
CREATE UNIQUE INDEX "bank_agency_accounts_agency_id_account_id_5ead26b4_uniq" ON "bank_agency_accounts" ("agency_id", "account_id");
CREATE INDEX "bank_agency_accounts_agency_id_48f3eb15" ON "bank_agency_accounts" ("agency_id");
CREATE INDEX "bank_agency_accounts_account_id_9d9f6243" ON "bank_agency_accounts" ("account_id");
COMMIT;
[0m