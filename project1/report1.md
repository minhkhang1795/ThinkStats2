# Associations between screen time and kids' mental health

## MinhKhang Vu, March 2019.

### 1. Introduction
Previous research on children and adolescents has suggested strong associations between screen time and their mental health, contributing to growing concerns among parents, teachers, counselors and doctors about digital technology's negative effects on children. According to the article [There’s Worrying New Research About Kids’ Screen Time and Their Mental Health](http://time.com/5437607/smartphones-teens-mental-health/), a new study published in the journal _Preventive Medicine Reports_ last year suggested "a clear and strong association" between more screen time and lower wellbeing among children. However, there might not be a direct correlation between kids' screen time and mental health as other researchers argued that anxious and depressed kids tend to spend more time using screens. Whether screen time affects children's wellbeing is questionable, but this study still provides an important insight into children's health and wellbeing.

![Cat Image](https://github.com/minhkhang1795/ThinkStats2/blob/master/project1/cat-image.jpg)

_Caption: Time spent on screens among children contributes to growing concerns about the negative effect of digital technology on children._

Reading the article, I couldn't find many useful statistics to support the relationship between screen time and children's mental health. Therefore, I'd like to explore whether this relationship exists and present the results with clear visualizations. In this project, I used the Census Bureau’s 2017 [National Survey of Children’s Health (NSCH)](https://www.census.gov/data/datasets/2017/demo/nsch/nsch2017.html) to investigate how children's screen time relates to their mental health. Besides the main question, I also experimented with other variables and found out that how often a family has meals together is also associated with their kids' screen time and mental health.

### 2. Methods
#### 2.1. Participants
Using the Census Bureau’s 2017 National Survey of Children’s Health (NSCH), I investigated a large (n=21,599) national random sample of 0- to 17-year-old children in the U.S. in 2017. The NSCH collects data on the physical and emotional health of American children every year, which includes information about their screen time usage and other comprehensive well-being measures, all of which are answered by parents.

#### 2.2. Measures
The survey asked two questions related to screen time, which are TV time usage level and Computers time usage level. These times are spent doing things other than schoolwork. The data provides many measures related to children's mental health, and I particularly choose questions related to anxiety and depression because both can help directly answer my question. Besides, I will also use a variable that indicates how often their family has meals together during the past week.

Please refer to this notebook to learn more about how I processed the data: https://github.com/minhkhang1795/ThinkStats2/blob/master/project1/data/datacleaning.ipynb

#### 2.3. Analysis plan
In the first section, I examine the associations between screen time level and the percentage of kids having anxiety, and between screen time level and the percentage of kids having depression across all ages using line plots with 90% CI. I also calculate the proportion of children having mental problems in the high screen time usage to those in the low screen time usage. I define "Low screen time usage" as spending on computers less than 3 hours a day (level 0 - 2), and "High screen time usage" as spending on computers equal or more than 3 hours (level 3 - 5). Please note that I do not take into account TV time usage when defining these two categories.

Next, I investigate how severe it could be if a child is having anxiety or depression. According to the codebook, the anxiety and depression severity were coded to 1 = Mild, 2 = Moderate and 3 = Severe. For each screen time level, I compute the mean severity score and visualize the results using line plots with 90% CI.

Finally, I explore whether how often a family has meals together would affect their children's mental health. The data provides the frequencies of family meal during the past week, which were coded as 0 = 0 days, 1 = 1-3 days, 2 = 4-6 days, 3 = every day. For each level of frequency, I calculate the percentage of children having anxiety, the percentage of children with depression, and the mean computer usage level. Because the mean computer usage level has a slightly different range compared to the percentages, to visualize these variables on the same plot, I use a two-scale plot: family meal frequency level is on the horizontal axis; the left vertical axis corresponds to percentages having anxiety/depression while the right vertical axis is for the screen time level.

### 3. Results
#### 3.1. Screen time versus anxiety/depression
Looking at the graphs, we can see that for kids spending 4 hours or more with computers, about 16% of them have some anxiety problems (CI 14.98 17.07), and 11% of them experience depression recently (CI 9.73 11.61).

![Screen time vs Percentages](https://github.com/minhkhang1795/ThinkStats2/blob/master/project1/screen-time-vs-percentages.png)

Between high and low screen usage groups, children who spend 3 hours or more daily using computers (high screen usage) are twice more likely to have an anxiety problem (CI 2.06 2.38) and four times more likely to experience depression (CI 3.97 5.11) than those who spend less than 3 hours (low screen usage).

#### 3.2. Gauging the anxiety/depression severity
In this section, I could not find any strong associations between the severity of kids' mental illness and screen time. The plots below do not show any apparent relationship between screen time and anxiety/depression severity levels. Surprisingly, kids having zero screen time even have severer anxiety/depression! There is a seemingly linear relationship on the left plot from screen time level 1 to 5, but the lines on the right plot are hard to tell whether there is a relationship between screen time and depression level.

![Screen time vs Severity](https://github.com/minhkhang1795/ThinkStats2/blob/master/project1/screen-time-vs-severity.png)

One reason for this result is that we don't have enough data in each group to determine whether there is a relationship. The 90% CI gap is too big, which suggests that there is high uncertainty in these graphs. As a result, I will not conclude anything about the associations between screen time and the anxiety/depression severity.

#### 3.3. Family meals
Along with the associations between screen time and diagnoses of anxiety and depression, how frequently a family has meals together also has strong linear relationships with both their children's screen time and mental health. Children who do not have any meal with their family during the past week are twice more likely to have anxiety and three times more likely to experience depression than children who have meals with their family every day.

![Family meals](https://github.com/minhkhang1795/ThinkStats2/blob/master/project1/family-meals.png)

This graph suggests strong linear relationships between anxiety/depression level and family meals as well as between computer time usage and family meals. Kids in families having more meals together are less likely to have anxiety/depression, and they also tend to use computers less. It's also worth noting that more than 16% of kids having no meals with their families during the past week experience anxiety problems, while only 8% of kids having meals every day with their families have anxiety. However, we should also be cautious about this result, because the Confidence Intervals on the left tails of the 3 lines are much wider than the CIs on the other end.


### 4. Discussion
In this study, I have shown the associations between screen time and the likelihood of experiencing anxiety/depression among children and adolescents, which confirms one argument made in the article. I also found interesting relationships between how frequently a family has meals together and their children's screen time as well as mental health.

However, I could not find any strong associations between the severity of kids' mental illness and screen time, partly because of the small sample size of the NSCH data. While the growing concerns among parents, counselors and doctors stated in the article are reasonable, the effect of screen time on children's mental health is still an open question that needs further investigation.
