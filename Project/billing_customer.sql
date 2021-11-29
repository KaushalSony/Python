-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: billing
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `S_No` int NOT NULL AUTO_INCREMENT,
  `C_ID` int DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Address` varchar(30) DEFAULT NULL,
  `Phone` int DEFAULT NULL,
  `Item_Purchased` varchar(30) DEFAULT NULL,
  `Brand` varchar(20) DEFAULT NULL,
  `Date_of_Purchase` date DEFAULT NULL,
  PRIMARY KEY (`S_No`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,101,'Ajay','Jaipur',986574312,'Monitor','Samsung','2020-06-25'),(2,101,'Ajay','Jaipur',986574312,'Mechanical Mouse','Logitech','2020-06-25'),(3,102,'Anil','Jaipur',547829431,'SMPS','INTEX','2020-06-28'),(4,103,'Ashok','Jaipur',789452136,'Mechanical Keyboard','Ant-E-Sports','2020-07-02'),(5,103,'Ashok','Jaipur',789452136,'Printer','Samsung','2020-07-02'),(6,103,'Ashok','Jaipur',789452136,'Home Theatre','Sony','2020-07-02'),(7,104,'Bhuvnesh','Jaipur',789451567,'Keyboard and Mouse Combo','Logitech','2020-07-02'),(8,101,'Ajay','Jaipur',986574312,'Nvidia Graphic Card(4GB)','Gigabyte','2020-07-10'),(9,104,'Bhuvnesh','Jaipur',789451567,'Laptop','Toshiba','2020-07-12'),(10,102,'Anil','Jaipur',547829431,'CPU','Intel(Core i5)','2020-11-28'),(11,104,'Bhuvnesh','Jaipur',789451567,'Scanner','Canon','2020-11-30'),(12,105,'Ankit','Sikar',657498123,'Scanner','Canon','2021-03-03');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-05 14:37:11
