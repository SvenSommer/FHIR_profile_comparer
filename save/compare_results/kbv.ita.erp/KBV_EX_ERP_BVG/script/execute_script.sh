#!/bin/bash
java -jar /home/dev/.fhir/validators/validator_cli_v5_6_89-SNAPSHOT-at2.jar -compare -tx n/a -proxy 192.168.110.10:3128 -dest "./compare_results/kbv.ita.erp/KBV_EX_ERP_BVG" -version 4.0.1 -ig kbv.ita.erp#1.0.2 -ig kbv.ita.erp#1.1.0 -left "https://fhir.kbv.de/StructureDefinition/KBV_EX_ERP_BVG|1.0.2" -right "https://fhir.kbv.de/StructureDefinition/KBV_EX_ERP_BVG|1.1.0"
