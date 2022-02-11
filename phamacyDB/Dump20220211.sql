-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: pharmacy
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pharma`
--

DROP TABLE IF EXISTS `pharma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `pharma` (
  `Ref` int NOT NULL,
  `MedName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Ref`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pharma`
--

LOCK TABLES `pharma` WRITE;
/*!40000 ALTER TABLE `pharma` DISABLE KEYS */;
INSERT INTO `pharma` VALUES (1020,'Aclender'),(1021,'Iron_X'),(4456,'eye'),(5467,'novel'),(5487,'DM');
/*!40000 ALTER TABLE `pharma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pharmacy`
--

DROP TABLE IF EXISTS `pharmacy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `pharmacy` (
  `Ref_no` int NOT NULL,
  `CmpName` varchar(45) DEFAULT NULL,
  `TypeMed` varchar(45) DEFAULT NULL,
  `Medname` varchar(45) DEFAULT NULL,
  `Lot` varchar(45) DEFAULT NULL,
  `Issuedate` varchar(45) DEFAULT NULL,
  `Expdate` varchar(45) DEFAULT NULL,
  `uses` varchar(45) DEFAULT NULL,
  `sideEffect` varchar(45) DEFAULT NULL,
  `warning` varchar(45) DEFAULT NULL,
  `dosage` varchar(45) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `product` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Ref_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pharmacy`
--

LOCK TABLES `pharmacy` WRITE;
/*!40000 ALTER TABLE `pharmacy` DISABLE KEYS */;
INSERT INTO `pharmacy` VALUES (1020,'pharmacytical','Liquid','Aclender','21548','12/12/2020','12/12/2021','flue.cold','allegies reaction','Dr.const','1','1200','3'),(4456,'pharmacytical','Tablet','eye','2154','12/12/2020','12/12/2022','fever','Yes','Dr.Const','3','450','12'),(5467,'pharmacytical','Capsules','novel','134','20/12/2020','20/12/2022','cold','no','Dr.const','5','200','10');
/*!40000 ALTER TABLE `pharmacy` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-02-11 15:43:35
