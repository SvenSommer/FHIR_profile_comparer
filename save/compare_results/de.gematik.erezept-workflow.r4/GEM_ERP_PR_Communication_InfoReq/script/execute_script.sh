#!/bin/bash
java -jar /home/dev/.fhir/validators/validator_cli_v5_6_89-SNAPSHOT-at2.jar -compare -tx n/a -proxy 192.168.110.10:3128 -dest "./compare_results/de.gematik.erezept-workflow.r4/GEM_ERP_PR_Communication_InfoReq" -version 4.0.1 -ig de.gematik.erezept-workflow.r4#1.1.1 -ig de.gematik.erezept-workflow.r4#1.2.0 -left "https://gematik.de/fhir/StructureDefinition/ErxCommunicationInfoReq|1.1.1" -right "https://gematik.de/fhir/erp/StructureDefinition/GEM_ERP_PR_Communication_InfoReq|1.2.0"
