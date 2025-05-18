# HealthcareApp
A prototype application for healthcare analysis <br>

### Table of Contents

1.[Landscape](#Landscape) <br>
2.[Database Schema](#database) <br>
3.[Architecture](#Models) <br>
3.1.[Lung Disease Prediction](#lung) <br>
3.2.[Brain Cancer Prediction](#brain) <br>
3.3.[Alzheimer Prediction](#alzheimer) <br>
3.4.[Gene Test](#gene) <br>
3.5.[Phenotype Model](#pheno) <br>
4.[User Manual](#UserManual) <br>



### <a name="Landscape"></a>Landscape
The healthcare industry is shifting rapidly with AI and machine learning driving demand for precision medicine and personalized care. Providers face pressure to reduce errors, optimize workflows, and improve outcomes, while startups challenge traditional methods. Complex medical data remains underutilized without efficient analysis tools. 
This application bridges the gap, offering actionable insights to enhance clinicians' decision-making. It augments, NOT replaces, doctors by providing predictions based on patient’s data to improve accuracy and reduce false positives. Unlike generalized databases, it delivers specialized insights tailored to clinical needs.


### <a name='Database'></a>Database
To construct the database effectively afterwards, a database schema has been drawn so that code implementation can be done by referencing the schema diagram. 

<p align="center">
    <img src="App/Pictures For Report/databaseDiagram.drawio.png" alt="Figure 1" width="400">
</p>
 
**Figure 1**: Database schema of the user records

Arrows, together with a star at one end, indicate that there is a one-to-many relationship between each test and user. For example, while each user can have multiple brain tests, one brain test can only belong to one user. 

<p align="center">
    <img src="App/Pictures For Report/Features.png" alt="Figure 2" width="700">
</p>
 
**Figure 2**: Feature sets of phenotype model


### <a name='Architecture'></a>Architecture




### User Manual

