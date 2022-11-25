CREATE SCHEMA  bankmanagement ;
USE bankmanagement ;

-- -----------------------------------------------------
-- Table bankmanagement.customer_info
-- -----------------------------------------------------
CREATE TABLE  bankmanagement.customer_info (
  accountNo INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  balance DECIMAL(15,3) NOT NULL,
  account_type CHAR(1) NOT NULL,
  password VARCHAR(16) NOT NULL,
  contact_no VARCHAR(10) NOT NULL,
  PRIMARY KEY (accountNo));

-- -----------------------------------------------------
-- Table bankmanagement.emp_details
-- -----------------------------------------------------
CREATE TABLE  bankmanagement.emp_details (
  emp_id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(45) NOT NULL,
  dob DATETIME NOT NULL,
  age INT NOT NULL,
  salary INT NOT NULL,
  password VARCHAR(45) NOT NULL,
  PRIMARY KEY (emp_id));


-- -----------------------------------------------------
-- Table bankmanagement.transactions
-- -----------------------------------------------------
CREATE TABLE  bankmanagement.transactions (
  transaction_id INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(8) NOT NULL,
  accontNo INT NULL,
  datetime DATETIME NOT NULL,
  empNo INT NULL,
  transaction_amount INT NULL,
  PRIMARY KEY (transaction_id),
  INDEX fk_transactions_1_idx (accontNo ASC) VISIBLE,
  INDEX fk_transactions_2_idx (empNo ASC) VISIBLE,
  CONSTRAINT fk_transactions_1
    FOREIGN KEY (accontNo)
    REFERENCES bankmanagement.customer_info (accountNo)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_transactions_2
    FOREIGN KEY (empNo)
    REFERENCES bankmanagement.emp_details (emp_id)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

 INSERT INTO emp_details(emp_id,name,dob,age,salary,password)
 VALUES (1,'Admin',NOW(),18,5000,'root');
