-- Creates the application user and gives it data access only (no schema changes)
-- Keep this password in sync with config/app_config.yaml
CREATE USER IF NOT EXISTS 'expenses_user'@'localhost' IDENTIFIED BY 'P@$$w0rd';
GRANT SELECT, INSERT, UPDATE, DELETE ON `Expenses`.* TO 'expenses_user'@'localhost';