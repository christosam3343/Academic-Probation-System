-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 28, 2023 at 04:37 AM
-- Server version: 5.7.36
-- PHP Version: 8.1.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aigrpdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `advisor`
--

CREATE TABLE `advisor` (
  `advisorId` varchar(10) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `advisor`
--

INSERT INTO `advisor` (`advisorId`, `name`, `email`) VALUES
('AA006', 'Ayodeji Ahdediphae', 'ayodeji12@gmail.com'),
('AE008', 'Asafa Evans', 'asafaev85@gmail.com'),
('AG321', 'Angelica Mendez', 'mendez.angel@hotmail.com'),
('BB004', 'Barbara Brooks', 'brooks452@gmail.com'),
('BL002', 'Barington Levitin', 'barilevitin12@gmail.com'),
('CB001', 'Colleena Brown-Burke', 'burkebrown741@gmail.com'),
('DA005', 'David Akinladejo', 'davidakin658@yahoo.com'),
('DB996', 'Demi Bennett', 'rhea.ripley@gmail.com'),
('DG009', 'Dontai Gary', 'gary87dontai@yahoo.com'),
('JB007', 'Johsua Bonton', 'bonton856@gmail.com'),
('RR550', 'Roman Reigns', 'reign.roman@gmail.com'),
('SS010', 'Sandy Squirrel', 'sandy9875@yahoo.com'),
('ST003', 'Shann-Kay Thomlinson', 'kaykay635@gmail.com'),
('USO01', 'Jimmy Uso', 'jimmy.uso1@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `directors`
--

CREATE TABLE `directors` (
  `ID` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `directors`
--

INSERT INTO `directors` (`ID`, `name`, `email`) VALUES
(10400, 'Hadaline Berry', 'berry879@gmail.com'),
(11200, 'Elon Musk', 'muskelon951@gmail.com'),
(11900, 'Ryan Graham', 'graham9630@yahoo.com'),
(21560, 'Tony Oscars', 'oscarstony963@yahoo.com'),
(23202, 'Joseph Anoi', 'joseph.anoi@gmail.com'),
(27112, 'Joshua Fatu', 'josh.fatu@gmail.com'),
(30245, 'Micheal Chin', 'michealchil85@gmail.com'),
(33544, 'Rhea Ripley', 'rhea.ripley8@gmail.com'),
(50033, 'Ronda Ali', 'ali.ronda@gmail.com'),
(50050, 'Keke Palmer', 'palmer74@gmail.com'),
(60801, 'Romario Mendez', 'romaine.mendez@gmail.com'),
(65202, 'Jonathan Depp', 'depp230@gmail.com'),
(69205, 'Nadine Sutherland', 'nadinesud968@gmail.com'),
(80809, 'Seth Rollins', 'seth.rollins@gmail.com'),
(90301, 'Lauren London', 'londonlauren9863@gmail.com'),
(552010, 'Bradley-John Pitt', 'pitt7854@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `module_details`
--

CREATE TABLE `module_details` (
  `studentId` int(11) NOT NULL,
  `moduleId` varchar(10) NOT NULL,
  `semester` int(11) NOT NULL,
  `grade_points` double NOT NULL,
  `year` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `module_details`
--

INSERT INTO `module_details` (`studentId`, `moduleId`, `semester`, `grade_points`, `year`) VALUES
(1876321, 'POM01', 1, 3.5, 2023),
(1876321, 'DM00', 2, 3.8, 2023),
(1876321, 'SBM30', 1, 3.7, 2023),
(1897215, 'DM00', 2, 3.9, 2023),
(1897215, 'CMP55', 2, 3, 2023),
(1897215, 'CLCOMP', 2, 3.3, 2023),
(2045123, 'PT986', 1, 3, 2022),
(2045123, 'ENT04', 1, 3.6, 2022),
(2045123, 'PCAL', 1, 2.9, 2022),
(2045123, 'CPH10', 2, 3, 2022),
(2045123, 'PT987', 2, 3, 2022),
(2045123, 'PLE04', 2, 2.8, 2022),
(2018330, 'PT986', 1, 3.9, 2022),
(2018330, 'CPH10', 1, 3.3, 2022),
(2018330, 'IPP03', 1, 3.1, 2022),
(2018330, 'PCAL', 1, 3.3, 2022),
(2064187, 'CPH10', 1, 3.3, 2023),
(2064187, 'IPP03', 1, 3, 2023),
(2064187, 'PT986', 1, 3, 2023),
(2064187, 'PT987', 2, 3, 2024),
(2064187, 'PCAL', 2, 3.7, 2024),
(2064187, 'PLE04', 2, 3.1, 2024),
(1849321, 'PT986', 1, 2.6, 2024),
(1849321, 'PCAL', 1, 1.98, 2024),
(1849321, 'IPP', 1, 2.23, 2024),
(1849321, 'PLE04', 1, 1.98, 2024),
(2078901, 'IPP03', 1, 4.97, 2022),
(2078901, 'PCAL', 1, 4.8, 2022),
(2078901, 'PLE04', 1, 5.5, 2022),
(1950178, 'CRLW1', 1, 4.97, 2024),
(1950178, 'FL999', 1, 4, 2024),
(1950178, 'TAX31', 1, 3.77, 2024),
(1956432, 'CRLW1', 1, 2, 2023),
(1956432, 'CSP33', 1, 2.94, 2023),
(1956432, 'FL999', 2, 3.4, 2024),
(1956432, 'BLAW4', 2, 3.35, 2024),
(1990076, 'CRLW1', 1, 6, 2022),
(1990076, 'TAX33', 1, 5.5, 2022),
(1990076, 'BLAW', 1, 5.88, 2022),
(1990076, 'CR654', 2, 4.52, 2023),
(1990076, 'HRL011', 2, 4.09, 2023),
(1990076, 'IBL77', 2, 4.67, 2023),
(1839427, 'DS891', 1, 4.52, 2022),
(1839427, 'CMP55', 1, 3.5, 2022),
(1839427, 'DM00', 1, 4.01, 2022),
(1839427, 'AI101', 2, 3.82, 2022),
(1839427, 'CLCOMP', 2, 4.82, 2022),
(1839427, 'DATA0', 2, 5.67, 2022),
(195643, 'TAX31', 2, 1.2, 2022),
(195643, 'PLE04', 2, 1, 2022),
(195643, 'FL999', 2, 2.5, 2022),
(195643, 'CRLW1', 1, 1.5, 2022),
(195643, 'CR654', 2, 2.2, 2022),
(195643, 'BLAW4', 2, 1.2, 2022),
(1856724, 'SBM30', 1, 2.1, 2022),
(1856724, 'POM01', 1, 3, 2022),
(1856724, 'SM009', 1, 2.9, 2022),
(1856724, 'IBL77', 2, 2.12, 2023),
(1856724, 'ENT04', 2, 4, 2023),
(1856724, 'CF900', 2, 1.59, 2023),
(1881127, 'SM009', 1, 2.05, 2023),
(1881127, 'MICRO', 1, 2.55, 2023),
(1881127, 'ECJ10', 1, 3.21, 2023),
(1881127, 'DATA0', 2, 2.05, 2024),
(1881127, 'CSCP65', 2, 2.15, 2024),
(1881127, 'CR654', 2, 2.79, 2024),
(1902678, 'DATA0', 1, 3.23, 2022),
(1902678, 'OOP12', 1, 3, 2022),
(1902678, 'MICRO', 1, 1.99, 2022),
(1902678, 'DS891', 2, 3.96, 2023),
(1902678, 'DM00', 2, 3.69, 2023),
(1902678, 'CSCP65', 2, 2, 2023),
(1918790, 'DS891', 2, 3.96, 2023),
(1918790, 'SOE22', 2, 2.54, 2023),
(1918790, 'OOP12', 2, 3.01, 2023),
(1918790, 'MICRO', 2, 1.35, 2023),
(1918790, 'HMRO1', 2, 4.03, 2023),
(1918790, 'ENT04', 2, 2.98, 2023),
(1918790, 'DS891', 2, 1.45, 2023),
(1945210, 'TAX31', 1, 1.92, 2023),
(1945210, 'SBM30', 1, 3.91, 2023),
(1945210, 'POM01', 1, 2.37, 2023),
(1945210, 'SM009', 2, 2.34, 2024),
(1945210, 'HRM01', 2, 3.25, 2024),
(1945210, 'FINA2', 2, 2.93, 2024),
(1945210, 'ENT04', 2, 3.83, 2024),
(2002345, 'SOE22', 1, 1.11, 2022),
(2002345, 'OOP12', 1, 1.32, 2022),
(2002345, 'CMP55', 1, 1.94, 2022),
(2002345, 'CSCP65', 1, 3.09, 2022),
(2002345, 'DATA0', 1, 1.99, 2022),
(2015093, 'SM009', 1, 3.09, 2023),
(2015093, 'PLE04', 1, 2.19, 2023),
(2015093, 'IBL77', 1, 3.19, 2023),
(2015093, 'HRL011', 1, 3.69, 2023),
(2015093, 'FL999', 2, 1.85, 2024),
(2015093, 'ENT04', 2, 1.23, 2024),
(2015093, 'ECJ10', 2, 3.41, 2024),
(2015093, 'CSP33', 2, 3.11, 2024),
(2023658, 'SMB30', 1, 4.04, 2022),
(2023658, 'SM009', 1, 3.91, 2022),
(2023658, 'POM01', 1, 3.07, 2022),
(2023658, 'FINA2', 1, 3.45, 2022),
(2023658, 'TAX31', 2, 1.45, 2023),
(2023658, 'HRM01', 2, 1.05, 2023),
(2023658, 'BLAW4', 2, 2.15, 2023),
(2023658, 'ENT04', 2, 1.45, 2023),
(2067290, 'DM00', 1, 2.91, 2023),
(2067290, 'DATA0', 1, 3.91, 2023),
(2067290, 'SOE22', 1, 3.01, 2023),
(2067290, 'OOP12', 1, 3.12, 2023),
(2067290, 'AI101', 2, 2.12, 2024),
(2067290, 'CLCOMP', 2, 2.52, 2024),
(2067290, 'CMP55', 2, 1.12, 2024);

-- --------------------------------------------------------

--
-- Table structure for table `module_master`
--

CREATE TABLE `module_master` (
  `moduleId` varchar(10) NOT NULL,
  `moduleName` varchar(50) NOT NULL,
  `no_of_credits` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `module_master`
--

INSERT INTO `module_master` (`moduleId`, `moduleName`, `no_of_credits`) VALUES
('AI101', 'Artificial Intelligence', 4),
('BLAW4', 'Business Law', 4),
('CF900', 'Coorporate Finance', 2),
('CLCOMP', 'Cloud Computing', 5),
('CMP55', 'Computer Networks ', 3),
('CPH10', 'Clinical Pharmacy', 3),
('CR654', 'Criminalogy', 4),
('CRLW1', 'Criminal Law', 3),
('CSCP65', 'Cybersecurity & Cryptography', 4),
('CSP33', 'Court Systems & Procedures', 3),
('DATA0', 'Data Analysis', 3),
('DM00', 'Digital Marketing', 3),
('DS891', 'Data Structures', 4),
('ECJ10', 'Ethics in Criminal Justice', 4),
('ENT04', 'Entreprnuership', 4),
('FINA2', 'Financial Accounting', 2),
('FL999', 'Family Law', 3),
('HRL011', 'Hunam Rights Law', 3),
('HRM01', 'Human Resource Management', 2),
('IBL77', 'International Business Law', 5),
('IPP03', 'Introduction to Pharmacy Practices', 3),
('MICRO', 'Microprocessor Systems', 5),
('OOP12', 'Object Oriented Programming', 4),
('PCAL', 'Pharmaceutical Calculations', 5),
('PHY22', 'Pharmaacolog', 3),
('PLE04', 'Pharmacy Law and Ethics', 3),
('POM01', 'Principles of Marketing', 4),
('PT986', 'Pharmacotherapy I', 2),
('PT987', 'Pharmacotherapy II', 4),
('SBM30', 'Small Business Management', 3),
('SM009', 'Strategic Marketing', 3),
('SOE22', 'Software Engineering', 3),
('TAX31', 'Taxation Law', 5);

-- --------------------------------------------------------

--
-- Table structure for table `programme`
--

CREATE TABLE `programme` (
  `pid` varchar(11) NOT NULL,
  `program_Description` varchar(50) NOT NULL,
  `director` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `programme`
--

INSERT INTO `programme` (`pid`, `program_Description`, `director`) VALUES
('BOE01', 'Bachelor of Engineering', 30245),
('BOL23', 'Bachelor of Law', 21560),
('BSBA', 'Bachelor of Science in Business Administration', 11200),
('BSCC20', 'Bachelor of Science in Criminology', 21560),
('BSCE', 'Bachelors of Science in Construction Engineering ', 45011),
('BSCS', 'Bachelor of Science in Computer Science', 90301),
('BSP', 'Bachelor of Science in Pharmacy', 69205),
('DOCP', 'Doctorate in Pharmaceuticals', 10400),
('MEP', 'Marketing & Entrepenuership Programs', 50050),
('MOL', 'Masters in Law', 65202);

-- --------------------------------------------------------

--
-- Table structure for table `school`
--

CREATE TABLE `school` (
  `schoolID` varchar(11) NOT NULL,
  `schoolName` varchar(50) NOT NULL,
  `adminName` varchar(50) NOT NULL,
  `adminEmail` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `school`
--

INSERT INTO `school` (`schoolID`, `schoolName`, `adminName`, `adminEmail`) VALUES
('COHS', 'College of Health & Science', 'Jessica Brooks', 'jbrooks1000@gmail.com'),
('FOL', 'Faculty of Law', 'Mark Kronk', 'markronk456@yahoo.com'),
('SCIT', 'School of Computing & Information Technology', 'Lewan King', 'kingtoo@gmail.com'),
('SOBLM', 'School of Building & Land Management', 'Haile Matthers', 'Haile.Matthers@gmail.com'),
('SOMS', 'School of Mathematics & Statistics', 'Marshal Edwards', 'marshall23@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `student_master`
--

CREATE TABLE `student_master` (
  `studentId` int(11) NOT NULL,
  `student_Name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `programme` varchar(11) NOT NULL,
  `school` varchar(11) NOT NULL,
  `advisor` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student_master`
--

INSERT INTO `student_master` (`studentId`, `student_Name`, `email`, `programme`, `school`, `advisor`) VALUES
(195643, 'Lucas Lee ', 'luke.lee@gmail.com', 'MOL', 'FOL', 'AA006'),
(1839427, 'Sofia Rodriguez', 's.rodriguez@hotmail.com', 'BSCS', 'SCIT', 'AE008'),
(1849321, 'Amelia Turner', 'ameliaturner379@gmail.com', 'DOCP', 'COHS', 'SS010'),
(1856724, 'Carter Perez ', 'carter.preezz@yahoo.com', 'BSBA', 'SOBA', 'CB001'),
(1876321, 'Emma Johnson', 'emma.johnson@gmail.com', 'MEP', 'SOBA', 'ST003'),
(1881127, 'Simone Miniminter ', 'miniminter@outlook.com', 'BSCC20', 'FOL', 'DA005'),
(1897215, 'Noah Martinez ', 'n.martinez@yahoo.com', 'BSBA', 'SOBA', 'ST003'),
(1902678, 'Tyson Fury', 'tysonisfury@gmail.com', 'BSCS', 'SCIT', 'JB007'),
(1905623, 'Ethan Payne ', 'bezinga.payne@yahoo.com', 'MSCS', 'SCIT', 'AE008'),
(1918790, 'Blake Anderson ', 'blake.anderson@yahoo.com', 'BSCS', 'SCIT', 'JB007'),
(1945210, 'Vikram Clarke ', 'Vikkstar123@hotmail.com', 'MEP', 'SOBA', 'BB004'),
(1950178, 'Oliver Parker', 'ollie.parker@yahoo.com', 'BOL23', 'FOL', 'CB001'),
(1990076, 'Hazel-Grace Lancaster ', 'hazel.lancaster@yahoo.com', 'BOL23', 'FOL', 'DG009'),
(2002345, 'McKenna Torres ', 'mckenna.torres@hotmail.com', 'BSCS', 'SCIT', 'JB007'),
(2015093, 'Liam Anderson ', 'liam.anderson@yahoo.com', 'MOL', 'FOL', 'AA006'),
(2018330, 'Mia Garcia ', 'miagarcia@yahoo.com', 'DOCP', 'COHS', 'BL002'),
(2023658, 'Joshua Zerka ', 'zerkaaJ@gmail.com', 'BSCS', 'SOMS', '[value-6]'),
(2045123, 'Isabella White ', 'littleizzywhite@gmail.com', 'DOCP', 'COHS', 'BL002'),
(2064187, 'Ava Thompson ', 'ava.thompson@hotmail.com', 'BSP', 'COHS', 'BB004'),
(2067290, 'Tobias Brown ', 'tobijbrown@outlook.com', 'BSCS', 'SCIT', 'AE008'),
(2078901, 'Oladeji Tango ', 'deji.tango@gmail.com', 'BSP', 'COHS', 'BL002');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advisor`
--
ALTER TABLE `advisor`
  ADD PRIMARY KEY (`advisorId`);

--
-- Indexes for table `directors`
--
ALTER TABLE `directors`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `module_details`
--
ALTER TABLE `module_details`
  ADD KEY `FOREIGN` (`studentId`,`moduleId`),
  ADD KEY `moduleId` (`moduleId`);

--
-- Indexes for table `module_master`
--
ALTER TABLE `module_master`
  ADD PRIMARY KEY (`moduleId`);

--
-- Indexes for table `programme`
--
ALTER TABLE `programme`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `FOREIGN` (`director`);

--
-- Indexes for table `school`
--
ALTER TABLE `school`
  ADD PRIMARY KEY (`schoolID`);

--
-- Indexes for table `student_master`
--
ALTER TABLE `student_master`
  ADD PRIMARY KEY (`studentId`),
  ADD KEY `FOREIGN` (`advisor`,`school`,`programme`),
  ADD KEY `school` (`school`),
  ADD KEY `programme` (`programme`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `directors`
--
ALTER TABLE `directors`
  ADD CONSTRAINT `directors_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `programme` (`director`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `module_details`
--
ALTER TABLE `module_details`
  ADD CONSTRAINT `module_details_ibfk_1` FOREIGN KEY (`moduleId`) REFERENCES `module_master` (`moduleId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `module_details_ibfk_2` FOREIGN KEY (`studentId`) REFERENCES `student_master` (`studentId`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `student_master`
--
ALTER TABLE `student_master`
  ADD CONSTRAINT `student_master_ibfk_1` FOREIGN KEY (`advisor`) REFERENCES `advisor` (`advisorId`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `student_master_ibfk_2` FOREIGN KEY (`school`) REFERENCES `school` (`schoolID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `student_master_ibfk_3` FOREIGN KEY (`programme`) REFERENCES `programme` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
