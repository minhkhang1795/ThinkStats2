# Association between screen time and kids' mental health

### MinhKhang Vu

#### Overview
In this project, I'd like to use the Census Bureau’s 2017 [National Survey of Children’s Health (NSCH)](https://www.census.gov/data/datasets/2017/demo/nsch/nsch2017.html) to explore the relationship between children's screen time and their mental health. Currently, I've successfully obtained and loaded the data into Jupyter Notebook. I also looked at the codebook and explored various variables that could be used in my project.

The main question I want to answer is **How does children's screen time relate to their mental health?** Recently, I came across the article "There’s Worrying New Research About Kids’ Screen Time and Their Mental Health", and become interested in this topic. In the article, the author of the study found "a clear and strong association" between more screen time and lower wellbeing. She expressed a concern that digital technology can have a negative effect on health and wellbeing of children. However, there might not be a direct correlation between kids' screen time and mental health as other researchers argued that anxious and depressed kids tend to spend more using screens. Whether screen time affects children's wellbeing is questionable, but this study still provides important insights into children's health and wellbeing.

**First step:** I'm currently trying to validate the association between screen time and children's wellbeing. I plotted the screen time usage versus whether the kids received mental treatment during the past year (answered by their parents), and got the result that supports the article. Children spending more screen time tend to need mental treatments than children spending less screen time.

![plot](https://github.com/minhkhang1795/ThinkStats2/blob/master/project1/screen-time-vs-mental-treatment.jpg)

**Next steps:** I'd like to
- Explore whether this association is consistent across different years. As far as I know, the NSCH 2016 is available. However, data prior to 2016 might not be.
- Use other variables that relate directly to anxiety and depression.
- Look into some specific age groups.
- Explore other relationships such as screen time versus performance in school, or mental health versus how often their families have meal together.



#### Guidelines for Data Use
According to the 2017 NSCN's [Guidelines for Data Use](https://www.census.gov/content/dam/Census/programs-surveys/nsch/tech-documentation/methodology/2017-NSCH-FAQs.pdf), users can use the data for statistical reporting and analysis. Also, users must not use the data to identify any respondents, inadvertently or otherwise. Finally, prior to releasing any statistics to the public, the Census Bureau conducts reviews to ensure that no information or characteristics can identify any individual.

#### Citation
The United States Census Bureau, Associate Director of Demographic Programs, National Survey of Children’s Health. 2017 National Survey of Children’s Health Frequently Asked Questions. September 2018. Available from: https://www.census.gov/content/dam/Census/programs-surveys/nsch/techdocumentation/methodology/NSCH%202016%20FAQs.pdf
