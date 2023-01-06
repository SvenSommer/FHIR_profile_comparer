#!/bin/bash
java -jar /home/dev/.fhir/validators/validator_cli_v5_6_89-SNAPSHOT-at2.jar -compare -tx n/a -proxy 192.168.110.10:3128 -dest "./compare_results/de.gkvsv.erezeptabrechnungsdaten/GKVSV_PR_TA7_Rechnung_Composition" -version 4.0.1 -ig de.gkvsv.erezeptabrechnungsdaten#1.2.0 -ig de.gkvsv.erezeptabrechnungsdaten#1.3.0 -left "https://fhir.gkvsv.de/StructureDefinition/GKVSV_PR_TA7_Sammelrechnung_Composition|1.2.0" -right "https://fhir.gkvsv.de/StructureDefinition/GKVSV_PR_TA7_Rechnung_Composition|1.3.0"
