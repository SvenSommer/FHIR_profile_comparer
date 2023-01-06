#!/bin/bash
java -jar /home/dev/.fhir/validators/validator_cli_v5_6_89-SNAPSHOT-at2.jar -compare -tx n/a -proxy 192.168.110.10:3128 -dest "./compare_results/de.gkvsv.erezeptabrechnungsdaten/GKVSV_EX_TA7_IK_Empfaenger" -version 4.0.1 -ig de.gkvsv.erezeptabrechnungsdaten#1.2.0 -ig de.gkvsv.erezeptabrechnungsdaten#1.3.0 -left "https://fhir.gkvsv.de/StructureDefinition/GKVSV_EX_TA7_IK_Empfaenger|1.2.0" -right "https://fhir.gkvsv.de/StructureDefinition/GKVSV_EX_TA7_IK_Empfaenger|1.3.0"