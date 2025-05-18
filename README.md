# HealthcareApp
A prototype application for healthcare analysis. <br>
A CAPSTONE project in the Master of Engineering program at the University of California, Berkeley <br>

### Table of Contents

1.  [Landscape](#Landscape) <br>
2.  [Database Schema](#database) <br>
3.  [Preprocessing](#Preprocessing) <br>
4.  [Architectures and Results](#Architectures) <br>
    4.1.  [Lung Disease Prediction](#lung) <br>
    4.2.  [Brain Cancer Prediction](#brain) <br>
    4.3.  [Alzheimer Prediction](#alzheimer) <br>
    4.4.  [CNN Model Scores](#cnn_scores) <br>
    4.5.  [Gene Test](#gene) <br>
    4.6.  [Phenotype Model](#pheno) <br>
5.  [User Manual](#UserManual) <br>
6.  [Team](#team) <br>


### <a name="Landscape"></a>Landscape
The healthcare industry is shifting rapidly with AI and machine learning driving demand for precision medicine and personalized care. Providers face pressure to reduce errors, optimize workflows, and improve outcomes, while startups challenge traditional methods. Complex medical data remains underutilized without efficient analysis tools. 
This application bridges the gap, offering actionable insights to enhance clinicians' decision-making. It augments, NOT replaces, doctors by providing predictions based on patient’s data to improve accuracy and reduce false positives. Unlike generalized databases, it delivers specialized insights tailored to clinical needs.


### <a name='Database'></a>Database
To construct the database effectively afterwards, a database schema has been drawn so that code implementation can be done by referencing the schema diagram. 

<p align="center">
    <img src="App/Pictures For Report/databaseDiagram.drawio.png" alt="Figure 1" width="400">
</p>
<p align="center">
<b>Figure 1:</b> Database schema of the user records
</p>

Arrows, together with a star at one end in the **figure 1**, indicate that there is a one-to-many relationship between each test and user. For example, while each user can have multiple brain tests, one brain test can only belong to one user. 

<p align="center">
    <img src="App/Pictures For Report/Features.png" alt="Figure 2" width="700">
</p>
<p align="center">
    <b>Figure 2:</b> Feature sets of phenotype model
</p>

In **figure 2**, we can see the hierarchical view of the database. Based on each disease, the fields were 
separated. The leaf nodes indicate the prefixes of the fields' identification codes. The same 
fields might be related to many diseases.  <br>
Key datasets used in our analysis include: <br>
● DEMO (Demographic Data) <br>
● BMX (Body Measures) <br>
● BPX (Blood Pressure) <br>
● LBX (Laboratory Values: Glucose, Insulin, HbA1c) <br>
● DIQ (Diabetes Questionnaire) <br>
These datasets provided variables such as age, gender, race/ethnicity, BMI, fasting glucose, 
insulin levels, blood pressure, and HbA1c—all of which are established markers relevant to 
diabetes risk.

### <a name='Preprocessing'></a>Preprocessing

For each dataset, since the class distributions were varying, their weights should be generated 
so that the model can predict each class equally. If one class has more data than the other, then 
the model will predict that class more than the other ones. That means there will be a bias 
towards the classes with more training data. <br>

<p align="center">
    <img src="App/Pictures For Report/whole_class_dist.jpg" alt="Figure 6" width="700">
</p>
<p align="center">
    <b>Figure 3:</b> Class frequencies of every CNN model. It shows a high variation, which can cause 
biased predictions
</p>

In order to solve this problem, the following formula has been used to find the normalized 
weights. Also, because each image is processed independently, instead of processing them in one 
thread (the normal program flow), we can use multiple threads to process them in a parallel way. 
By doing that, we reduced the time spent on preprocessing by **83%**. <br>

<p align="center">
    <img src="Machine Learning/figures/thread_usage_images.png" alt="Figure 7" width="400">
</p>
<p align="center">
    <b>Figure 4:</b> The amount of time spent in preprocessing images with and without threads. 
</p>



### <a name='Architectures'></a>Architectures and Results

#### 1.<a name='brain'></a>Brain Cancer Prediction

<p align="center">
    <img src="App/Pictures For Report/brain_predictor.drawio.png" alt="Figure 3" width="300">
</p>
<p align="center">
    <b>Figure 5:</b> The model architecture for the brain cancer prediction
</p>

#### 2.<a name='alzheimer'></a>Alzheimer Prediction

<p align="center">
    <img src="App/Pictures For Report/alzh_predictor.drawio.png" alt="Figure 4" width="500">
</p>
<p align="center">
    <b>Figure 6:</b> The architecture of the model for the Alzheimer prediction
</p>

The model architecture used in the Alzheimer's prediction model has some differences. It is 
because of the nature of the data. Since the size of the data is big, the model should be less 
complex so that it can learn the trends instead of memorizing the data. <br>

#### 3.<a name='lung'></a>Lung Disease Prediction

<p align="center">
    <img src="App/Pictures For Report/lung_predictor.drawio.png" alt="Figure 5" width="300">
</p>
<p align="center">
    <b>Figure 7:</b> The model architecture for the lung disease prediction
</p>

The model architecture for lung disease prediction is almost the same architecture used in the 
brain tumor prediction model. The only difference is the last fully connected layer, which, in the 
case of the lung disease model, contains 3 nodes instead of 4 because of the possible number 
of outcomes. <br>

#### 4.<a name='cnn_scores'></a>CNN Model Scores

Each different model has been trained multiple times in order to get the highest accuracy. Test 
and training data were separated so that at the end of the training, the model was able to test 
with the data that it hadn’t seen before. By doing that, the model’s generalizability is tested. Test 
results of the three image-based models are as follows:

<p align="center">
    <img src="App/Pictures For Report/cnn_accuracies.jpg" alt="Figure 8" width="700">
</p>
<p align="center">
    <b>Figure 8:</b> The CNN model's test results
</p>

#### 5.<a name='gene'></a>Gene Test

Simulated Polygenic Risk Scores (PRS) added approximately 12% improvement in 
AUC (from 0.75 to 0.84), confirming the added predictive power of genetic information.  <br>
● The TCF7L2 variant (Transcription Factor 7-Like 2), a well-established diabetes risk 
gene, was identified as significantly associated with increased risk, showing a 1.4x 
higher risk in modeled populations. <br>
● Additional key genes identified via differential expression analysis included: <br>
   ○ INSR (insulin receptor): central to the insulin signaling pathway <br>
   ○ IRS1 (insulin receptor substrate 1): modulates insulin response <br>
   ○ PPARG (peroxisome proliferator-activated receptor gamma): involved in 
adipocyte differentiation and glucose metabolism <br>
   ○ SLC2A4 (GLUT4): glucose transporter gene regulating cellular uptake <br>
● KEGG enrichment analysis revealed overrepresentation of insulin signaling, AMPK 
pathway, and type 2 diabetes mellitus pathways, further supporting biological relevance. <br>

<p align="center">
    <img src="App/Pictures For Report/target_genes.jpg" alt="Figure 9" width="400">
</p>
<p align="center">
    <b>Figure 9:</b> The percentage of each target gene
</p>

Some individuals with low-risk clinical profiles were predicted as high-risk due to 
their genetic load, underscoring the importance of genomic screening. <br>
Ethnic disparities were observed in healthcare access and risk exposure, with 
certain minority populations showing underrepresentation in available genetic 
reference data, which may affect risk calibration. <br>

<p align="center">
    <img src="App/Pictures For Report/auc_target.jpg" alt="Figure 10" width="400">
</p>
<p align="center">
    <b>Figure 10:</b> The AUC curve of each target gene 
</p>

#### 6.<a name='pheno'></a>Phenotype Test

<p align="center">
    <img src="App/Pictures For Report/pheno_roc.jpg" alt="Figure 11" width="400">
</p>
<p align="center">
    <b>Figure 11:</b>  ROC curves comparing classification performance across different machine learning 
models 
</p>

This plot shows the Receiver Operating Characteristic (ROC) curves, which visualize the 
trade-off between the True Positive Rate (TPR: also known as sensitivity or recall, measures the 
proportion of actual positives correctly identified by the model.) and False Positive Rate (FPR: 
measures the proportion of actual negatives that are incorrectly classified as positive by the 
model.) for different classification thresholds. <br>
● Some individuals with non-obese BMI and normal glucose levels still exhibited 
high predicted risk due to the presence of multiple coexisting social and clinical 
risk indicators. <br>
● Ethnic disparities were observed, particularly among Mexican American and 
non-Hispanic Black subgroups, where risks were elevated even after adjusting 
for lifestyle factors. This highlights a potential intersection of genetic susceptibility 
and healthcare access. <br> 

### User Manual
...Coming..

### Team

**Cagin Tunc**: UC Berkeley, Master of Engineering / Bioengineering <br>
**Haoyu Zhao**: UC Berkeley, Master of Engineering / Bioengineering <br>
**Bikramjeet Singh**: UC Berkeley, Master of Engineering / Industrial Engineering and Operations Research <br>
**Shuo Li**: UC Berkeley, Master of Engineering / Bioengineering <br>
**Jiachen Xi**: UC Berkeley, Master of Engineering / Bioengineering <br>
