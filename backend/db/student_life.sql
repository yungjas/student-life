DROP TABLE IF EXISTS `school`;
CREATE TABLE `school` (
    `school_id` int(11) NOT NULL AUTO_INCREMENT,
    `school_name` varchar(64) NOT NULL,
    PRIMARY KEY(`school_id`)
);

DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
    `student_id` int(11) NOT NULL AUTO_INCREMENT,
    `student_name` varchar(64) NOT NULL,
    `school_id` int NOT NULL,
    PRIMARY KEY(`student_id`),
    FOREIGN KEY(`school_id`) REFERENCES `school` (`school_id`)
);

INSERT INTO `school` (`school_name`) VALUES
("School of Computing and Information Systems"),
("School of Social Sciences"),
("School of Business"),
("School of Economics"),
("School of Law");

INSERT INTO `student` (`student_name`, `school_id`) VALUES
("Jasmine", 1);


DROP TABLE IF EXISTS `book`;
CREATE TABLE `book` (
    `book_id` int(11) NOT NULL AUTO_INCREMENT,
    `book_name` varchar(64) NOT NULL,
    `book_qty` int(11) NOT NULL,
    PRIMARY KEY(`book_id`)
);

INSERT INTO `book` (`book_name`, `book_qty`) VALUES
("Le Book", 20);