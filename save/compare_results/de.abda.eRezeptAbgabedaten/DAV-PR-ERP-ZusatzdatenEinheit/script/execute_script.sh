#!/bin/bash
java -jar /home/dev/.fhir/validators/validator_cli_v5_6_89-SNAPSHOT-at2.jar -compare -tx n/a -proxy 192.168.110.10:3128 -dest "./compare_results/de.abda.eRezeptAbgabedaten/DAV-PR-ERP-ZusatzdatenEinheit" -version 4.0.1 -ig de.abda.eRezeptAbgabedaten#1.2.0 -ig de.abda.eRezeptAbgabedaten#1.3.0 -left "http://fhir.abda.de/eRezeptAbgabedaten/StructureDefinition/DAV-PR-ERP-ZusatzdatenEinheit|1.2.0" -right "http://fhir.abda.de/eRezeptAbgabedaten/StructureDefinition/DAV-PR-ERP-ZusatzdatenEinheit|1.3.0"
