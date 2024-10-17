---
title: "Publications &#038; Talks"
author: Joshua Fox
layout: page
---

**Google Scholar**   

---
 
Google Scholar [shows citations](https://scholar.google.com/citations?hl=en&user=d0FLp-q9vFEC&view_op=list_works&pagesize=100)
for academic and some other articles, but for technical articles, see below.

**On Software and the Cloud**

---
• ["DoiT-Easily: Simplifying your Google Marketplace Vendor Development"](https://engineering.doit.com/doit-easily-7bd8b75207a9)
> How to use the DoiT-Easily open-source project as a basis for developing your Google Marketplace offerings.

---
• ["Sell your SaaS on Google Marketplace"](https://engineering.doit.com/sell-your-saas-on-google-marketplace-43b5d10ec15e)
> How to integrate your solution into Google Marketplace.

---
• "Growing NLP to production: Cloud MLOps for speed and efficiency", Israel NLP Meetup at Microsoft
> How to scale up your ML processes as you go from university to “garage” to hypergrowth. 

---
•  "No WAFs: Don’t use a Web Application Firewall, and when you should, anyway" (Conference Talk). ([Video](https://www.youtube.com/watch?v=0Rk7koWsX4I&list=PLMM5_63TOT9BZZ5HCeTTg_GVJFny3jwBw&index=13)). Bsides Strasbourg; also at L ([Video](https://www.youtube.com/watch?v=XQywClfDEJw) )
>  WAFs look like a quick-fix for security problems, but generally lead to worse security. Yet sometimes they are needed. This article sorts that out.
  
---
• "[No WAFs: Don’t use a Web Application Firewall, and when you should, anyway](https://engineering.doit.com/no-wafs-26c7a977db7b/)" (Article) 
>  WAFs look like a quick-fix for security problems, but generally lead to worse security.  Yet sometimes they are needed. This article sorts that out.

---
• "Controlling cloud costs: Where to start, and where to go from there", [StackExchange Podcast](https://stackoverflow.blog/2024/03/27/controlling-cloud-costs-where-to-start-and-where-to-go-from-there/).
>  We explored the importance of controlling and understanding cloud costs, the role of good architecture in cost optimization, and strategies for dealing with surprise costs.

---
• "Level 7 Egress Control: Just now emerging in Kubernetes", a full talk given at _SRECon_ Dublin ([video](https://www.youtube.com/watch?v=WnELOww56nM&t=2s)); and various short versions  at  _DevOpsDays_ Vilna,  _DevOpsDays_ Ukraine, and _Kubernasties_ Tel Aviv. See videos of the short talks in [English](https://www.youtube.com/watch?v=hZmkZvT4BH4&list=PL_O8YSX8ckfcW4hfVQexlTsKFoM_Vb8S5&index=8); Yiddish ["װי מען רעגולירט אַרױסגאַנג לױטן ראַיאָן: כטולהון אַרט עס נישט"](https://www.youtube.com/watch?v=89eZIFkktRg); and Hebrew ["שליטה על יציאה מאשכול על פי מתחם"](https://www.youtube.com/watch?v=UEsx6hKC6sU).
> Controlling outgoing traffic from a VPN or a K8s cluster based on Level 7 Domain address. 

• "Outside advisors: A counter-intuitive approach to Customer Reliability Engineering", _DevOpsDays_, Vilna, Lithuania
> How does SRE work with outside advisers? If outsiders run DevOps, costs mount quickly. There is a better way. I will show how strictly defined limits on what outside CRE does,  lower cost, build  in-house skills, and leverage outside expertise for both architecture and urgent response. See video of a [similar talk](https://www.youtube.com/watch?v=ayh22hDd-eU) from Singapore. 

• ["Flexibility in Vizier’s Black Box Optimization"](https://engineering.doit.com/flexibility-in-viziers-black-box-optimization-b4caff09af0c) 
>  Further abilities of Vertex AI Vizier 
 
• ["The Advantages of Vizier’s Black Box Approach"](https://engineering.doit.com/the-advantages-of-the-viziers-black-box-approach-b73f32723c9f) 
>  Comparing Vizier to other hyperoptimizers
 
• ["Vertex AI Vizier for fewer repetitions of costly ML training "](https://engineering.doit.com/the-advantages-of-the-viziers-black-box-approach-b73f32723c9f) 
>  Introducing Vizier and Black Box Optimization
 
• "From Professional Services to Responsibility-Sharing", _Kubernetes Users Group_, Singapore.
[Video recording here](https://www.youtube.com/watch?v=ayh22hDd-eU)
> How does a Site Reliability Engineering team work with outside advisers? If outsiders run DevOps, costs mount quickly, while the in-house team lacks a connection to its own systems. 
In this talk, I will present a methodology that carefully defines boundaries and limits what outside CRE does, so lowering cost,  building in-house skills, and leveraging outside expertise for urgent response as well as longer-term architecture.

• "Untangling the Tangled Cloud", ([video](https://www.youtube.com/watch?v=zJCP_MTncVk))  _Usenix
SRECon_ Singapore.

> How do you arrange virtual machines, databases, and other services into logical groups?

> Whether with Google Cloud projects, AWS accounts, or Azure resource groups, my consulting customers find that either lumping all the resources together or parceling them out into tiny groups makes management, security, and cost analysis too difficult: It’s tough predicting the impact of a change.

> In this talk, related to my article at Usenix :login;, I explain how I advise architects to make their infrastructure follow the logical boundaries of microservices and the organization.

• ["FQDN Egress Control in Kubernetes"](https://www.tfir.io/fqdn-egress-control-in-kubernetes), _TFiR_.

> Allowing access only to specific domains from your Kubernetes application; limiting this access to pods in certain namespaces or with certain labels. 

• ["Allow outgoing traffic by domain: FQDN Egress Control"](https://engineering.doit.com/allow-outgoing-traffic-by-domain-813407d67717)

> When you block your applications in a VPC from outbound connections, but want to allow access to just one domain, a regular firewall won't do. This article describes various approaches, including old standbys, two Preview services in Google Cloud, and AWS services. It also discusses Kubernetes-aware solutions and mentions an upcoming Kubernetes standard.

• ["Untangling the Cloud: A Principled Method for Grouping Cloud Resources"](https://www.usenix.org/publications/loginonline/untangling-cloud), _;login:_, the Usenix technical journal.

> How to draw technical borders to divide your cloud resources into groupings, such as Google Cloud projects, AWS accounts, or Azure resource groups.

• "Black Box Optimization with Vizier AI Vizier", at multiple conferences including  _Google DevZone Day_ at Google Tel Aviv;  _Google Atlantis Summit_; _GeeCON Prague_; _DevFest Zagreb_; _Google Israel Cloud Summit_; Osijek GDG. See [the talk here](https://www.youtube.com/watch?v=2RbTIcv3ChU)

> The first-ever talk or article about the new Black Box Optimization  interaction pattern of  Vertex Vizier, a new way to optimize across slow and expensive iterations.

• ["Authentication between microservices. Is it really that hard?"](https://medium.com/google-cloud/authentication-between-microservices-is-it-really-that-hard-b73785510db4?source=friends_link&sk=d7826ed8e076ce9583899f2216b196c8), _Google Cloud Medium Publication_.

> I've always found it difficult to securely authenticate between microservices. And in fact, though there are plenty of ways to do it,  doing it securely is not easy.

• ["Multitenant inference architecture with SageMaker endpoints"](https://www.youtube.com/watch?v=BXp1uRHNA9o), _Multicloud Engineering Meetup_.

> With Michael Pelts, Senior Solutions Architect at AWS,  explore ways to allow tenants to expose their own models for inference when ensuring that it is accessed only by the tenant that created it.
 
• "[Throughput Metrics Across the Clouds](https://www.doit.com/throughput-metrics-across-the-clouds/)"

> This article describes the conclusions from my  open-source project, which is the first that I know of  measuring *throughput* (most others focus on latency)  and doing so *across clouds* and relating it to *distance*.

• "[AWS Machine Learning at the start of 2022](https://youtube.com/playlist?list=PLEBxNMZ7Mu38caHMHW5M4d1ZkiyH_Ng6X)

> My colleagues and I discuss the latest from AWS in Machine Learning and Artificial Intelligence.

• "[Let the Computer Enforce It For You](https://engineering.doit.com/let-the-computer-enforce-it-for-you-fe8155d643dc?source=friends_link&sk=a8ee21dc9646ae47dddeb02df9b99f37)"

> How to  document your code for best results: Keep the documentation close to the code, and machine-enforced.

• "[Implementing SaaS Tenant Isolation Using Amazon SageMaker Endpoints and IAM](https://aws.amazon.com/blogs/apn/implementing-saas-tenant-isolation-using-amazon-sagemaker-endpoints-and-iam/)"

> Machine Learning Software-as-a-Service providers that serve a lot of tenants need to keep these tenants prediction endpoints separate. Here are several ways to do that, balancing expense and  robustness. We show an advanced use of Identity and Access management for a flexible access control to the Sagemaker inferencing endpoints.

• "[Cloud Blaster: How to clean up your Google Cloud Project](https://engineering.doit.com/cloud-blaster-how-to-clean-up-your-google-cloud-project-easily-6ec1a5d33ea9?source=friends_link&sk=a5ae0e917f1bbf9a201a5b61e3699fc5)"

> As you experiment with the Google Cloud, your project tends to get cluttered. This open-source project cleans it up.

• "[AWS Firewalls: How and When to Use Each One](https://engineering.doit.com/aws-firewalls-101-how-and-when-to-use-each-one-d4ad8087a6b3?source=friends_link&sk=bf365adf9fba5a4119a72cd026faf1c4)"

> When I saw that AWS had a new firewall with the uninformative name “Network Firewall,” I thought “not another one.” This is my attempt to sort them all out. Then Jeff Barr, AWS Chief Evangelist, tweeted it! 

• "[Kotlin, Gradle, and the Cloud](https://engineering.doit.com/kotlin-gradle-and-the-cloud-4b454701e4b9?source=friends_link&sk=0de9f40992a744bc636b0bd1acc9dc71)"

> How to build Kotlin apps in the cloud with Gradle.

• "[Resource Labeling with Iris3](https://engineering.doit.com/iris-3-automatic-labeling-for-cost-control-7451b480ee13?source=friends_link&sk=b934039e5dc35c9d5e377b6a15fb6381)"

> My Iris 3 open-source project adds labels to resources like VM instances, Pub Sub Topics, and more, making for more detailed cost reports.

• “[The Quickest Quickstarts](https://engineering.doit.com/the-quickest-quickstart-9c4111bb0d7a?source=friends_link&sk=0168f8588c7be8d29fe89df13d6881a8])"

> When I want to use a new technology, I first want a script that gives me a working “Hello World”; I can tweak from there. This article presents nine such solutions for different compute infrastructures on AWS and GCP.

• “[From Notebook to AWS](https://engineering.doit.com/from-notebook-to-aws-9bcf29ca0156?source=friends_link&sk=a996e4d15caeff5455f2c1b3cafd3475)''

> Step by step from a research Jupyter Notebook to a AWS distributed Machine Language Deployment.

• "[Looking for an emulator for Google Cloud Tasks?](https://engineering.doit.com/looking-for-an-emulator-for-cloud-tasks-45f0ae2c67b5?source=friends_link&sk=05f7c4f7c0c63c2043cd53690ced3df4)"

> Though an emulator is often requested, Google does not offer one for developing with Cloud Tasks, comparable to what if offers for Datastore or PubSub. I created one.

• “[Safe Scrub: Clean up your Google Cloud projects.](https://engineering.doit.com/safe-scrub-clean-up-your-google-cloud-projects-f90f18aca311?source=friends_link&sk=bce56e27b568c8209f3da94eac17099f)''

> An open-source tool I wrote for safely deleting the resources cluttering your projects.

• “[The Hidden Costs of Datastore](https://engineering.doit.com/the-hidden-costs-of-datastore-c04ad354ec50?source=friends_link&sk=64b75ebbf0f17d37a00cbed33f713d74)''

> Datastore export costs don’t show up in Google Cloud Monitoring. Here’s how to set up real-time alerts to better keep track of export costs.

• “[You can handle pods, but what about clusters?](https://engineering.doit.com/you-can-handle-the-pods-but-what-about-the-clusters-486fbdb5345d?source=friends_link&sk=7fbf6c973dbfe4554829cac6813df03e)''

> Introducing a new open-source tool that I wrote for cloning clusters between the Google, Azure, and Amazon clouds.

• “[How Your Web App Can Serve the Chinese Market](https://engineering.doit.com/how-your-web-app-can-serve-the-chinese-market-eddca502b6a9?source=friends_link&sk=84887f539e7cbf8f8f3d86ba75abeb68)''

> For web app developers, serving users in China requires a completely different way of thinking. Here are the key steps you should take.

• “[How to Best Prepare for your Cloud Certification Exam](https://engineering.doit.com/facing-down-the-cloud-certification-exam-efe154b58190?source=friends_link&sk=63e60f33fb058502925b99f54f9e8484)''

> The best preparation materials for Google and AWS Cloud Architect Certification as you get ready for those critical two or three hours of the exam.


• “[Build on Your Experience to Earn Cloud Certifications](https://engineering.doit.com/bring-your-experience-to-the-cloud-certification-891278df5b5?source=friends_link&sk=3bd23669baed9017741760ae6007135f)''

> How to quickly absorb the knowledge that you don't yet have, building on your professional strengths.

• “[Google App Engine Flexible Environment: Beyond the Bounds of PaaS](https://www.youtube.com/watch?v=QmmzUbX7IEY&t=22s)”.  The first ever talk or article dedicated to this new Google PaaS. _Multicloud Engineering,_.

• “[Breaking boundaries: How Freightos achieved high speed graph search in the cloud](https://www.cloudcomputing-news.net/news/2016/oct/06/breaking-boundaries-how-freightos-achieved-high-speed-graph-search-cloud/) ,” _CloudTech_.

> Running heavy-duty graph algorithms against a very large dataset require some unusual design principles. Freightos may not be the only company doing it, but no cloud platform today is optimized for this; in fact, the usual design assumptions in cloud platforms are quite the opposite of what we needed. Here is how we did it.

• “Modeling Retail Products: A Big Data Approach,” _The Software Generalist_.

• “ [Search and You Shall Find](https://medium.com/@Twiggle/search-and-you-shall-find-c2d2c3c43cf2) ,” _Medium_.

> Today’s e-tail search  engines return inaccurate results; merchants stuff all product information into long titles. To optimize revenue, online retailers need a search engine that _understands_ the product selection.

• “ [Apache Spark and Java 8: The Big Data Team](https://www.datanami.com/2014/12/11/apache-spark-java-8-big-data-team-2015/) ,”, _Datanami_.

> Apache Spark with Java 8 is proving to be the perfect match for Big Data.  In this article, I show an example of collaborative filtering using Spark on Cassandra data, and explain how much  easier this is to do with the lambdas of Java 8. Code to accompany it is [here at GitHub](https://github.com/JoshuaFox/spark-cassandra-collabfiltering).

• “Documents in the cloud: Dynamic, Privacy-customized views,” _Cloudbook_.

> As documents move to the cloud, it becomes harder to protect the private information in them, but on the other hand becomes easier to control distribution of specific private information to exactly the people who are authorized to see it.

• “Flexible, Dynamic Redaction”, _MasterDataManagement.com_.

> Complying with privacy regulations used to mean “redaction,” blacking out words with a pen, slowly and expensively. But natural language processing techniques can protect exactly the information regulated by law while giving convenient access to authorized users.

• “Breaking Walls: How to Get Departments to Share Information,” with Michael Pelts, _Technology and Humans_

• “[People Who Live in Glass Houses Should Put Up Some Shades](https://www.infosecurity-magazine.com/opinions/comment-some-documents-require-fine-grained/) ,” _InfoSecurity_.

> Too much openness, as well as too little, both pose risks. Document viewing with automated privacy control is one part of the balance. Allowing authorized users to retrieve the redacted information is another.

• “Privacy for the Deeper Web,” with Michael Pelts, _Technology and Humans_.

• “Openness and Privacy for Regulatory Compliance,” with Michael Pelts, _Information on Demand Europe_.

• “[IBM Optim Data Redaction: Reconciling Openness with Privacy](/wp-content/uploads/2019/10/IMW14307USEN.PDF),” IBM White Paper.

> The White Paper for the product which I launched in IBM.

• “Openness and Privacy,” with Michael Pelts, _Security and Privacy Symposium_.

• “[Clojure: Challenge your Java Assumptions](https://web.archive.org/web/20231001000000*/https://www.javaworld.com/article/2078043/clojure--challenge-your-java-assumptions.amp.html) ,” _JavaWorld_.

> The article is aimed at senior Java developers, encouraging them to learn more about this exciting language. A dialect of Lisp, Clojure runs on the JVM with excellent integration with Java, and provides new, improved solutions for the biggest challenge to programming languages today: concurrency.

• “Mining Meaning from Java Code with Java Data Mining API”, _JavaOne,_ San Francisco. As with the earlier talk, the JavaOne committee gave this presentation the “Cool Stuff” award.

• “Mining for Services: Discovering Business Realities in Mainframe Metadata,” _IMPACT_, Las Vegas.

• “Finding Mashup Ingredients,” _Web 2.0 and Beyond Summit_.

• “[Mining for Meaning: Discovering Business Realities in Mainframe Metadata](/wp-content/uploads/2014/10/Fox_MainframeExec_SEP-OCT2008.pdf),” _Mainframe Executive_.

> To expose siloed mainframe functionality now locked up in siloed systems, it is essential to understand its business value. Automated classification technologies help make this happen.

• “Metadata Mining: Automated Semantic Classification for Service Repositories,” _XML Conference_, Boston.

• “Approaches for Modeling Metadata in XML”, industry experts panel, _XML Conference_, Boston

• “[The Portal as People-Centric SOA](/wp-content/uploads/2017/05/ThePortalAsPeopleCentricSOA.pdf),” MainSoft Corporation White Paper.

> As a consultant for a leading provider of Java-.NET interoperability software, I wrote a white paper evangelizing the company’s IBM WebSphere Portal product, showing how it functions as a user-facing on-ramp to SOA.

• “[The Hub and the Edge: Balancing the Responsibilities](/wp-content/uploads/2014/10/Hub-and-the-Edge.pdf),” _Architecture and Governance Magazine_.

> Architecture is as much about the organization as about technology. This article explains how to divide responsibilities in Service Oriented Integration to let each team do what they do best.

• “[JRuby on Rails](https://web.archive.org/web/20230610042818/https://www.javaworld.com/article/2077682/jruby-on-rails--the-power-of-java--the-simplicity-of-ruby-on-rails.amp.html) ,” _JavaWorld_.

> The article explain Ruby on Rails to Java developers, comparing it to Java web frameworks. It presents an example based on JavaSpaces, which leverages Java from within the Rails application. Even those Java developers who do not adopt Rails will benefit from the design principles built into the framework, as well as the rapidly emerging concept of non-Java languages integrated with Java and the JVM.

• “[Ruby for the Java World](https://web.archive.org/web/20230325135244/https://www.javaworld.com/article/2071794/ruby-for-the-java-world.amp.html) ,” _JavaWorld_.

> Dynamic languages are rapidly gaining in popularity. Ruby in particular has attracted attention, with a big boost from the Ruby on Rails Web framework. In this article, I introduce Java programmers to Ruby, focusing on the similarities, differences, and connectivity between the two languages, and describing the value of JRuby on the Java-platform. The article got some [buzz](https://www.google.com/search?q=%22joshua+fox%22+ruby+java) on the net, including from Frank Sommers at [Artima](https://www.artima.com/forums/flat.jsp?forum=276&thread=168997).

• “Enterprise Semantics: Aligning Service Oriented Architecture with the Business ,” with Joram Borenstein, *Web Services Journal*.

> A business-focused overview of the value that semantics bring to Service Oriented Architectures.

• “Business Processes: Connecting the Design-Time to the Run-time” (presentation here),  _Programming Languages and Development Environments Seminar_, Haifa.

• “XMI and the Many Metamodels of Enterprise Metadata,” with Joram Borenstein, _XML Conference_, Atlanta.

• “Semantic Enterprise Systems Management for Program Trading,” with Simon de M. Walker, _Securities Industry Middleware Council_, New York.

• “Java Metadata and the Semantic Web,” _JavaOne_, San Francisco. Awarded  “Intriguing and Unexpected: New and Cool” by the conference committee.

• “Aligning Business Process and Business Information Models: a Semantic Approach,” with Zvi Schreiber, _Global Business Process Forum_, London.

• “Metadata Management Converges with Business Modeling,” _DAMA Symposium and Wilshire Meta-Data Conference_, Los Angeles.

• “Semantic Information Management for Data Integration in the Enterprise,” _Tech Target_.

• “Semantic Information Management: Controlling Complexity with a Central Information Hub,” _Securities Industry Middleware Council_, New York.

• “Web Services: Trends Toward Adoption,” invited appearance at industry experts panel, _EIDX/CompTIA_, San Diego.

• “Know What Your Schemas Mean: Semantic Information Management for XML Assets,”  _XML Conference_.

> Schemas control the structure of information, But they don’t specify what a field means. Is that “salary” field monthly or annual? Semantic data management helps you keep track and avoid expensive mistakes.

• “[Active Information Models for Data Transformation](/wp-content/uploads/2014/10/Active_Information_Models_for_Data_Transformation_-_May_2003_-_Joshua_Fox.pdf),” _eAI Journal_ (later renamed to _Business Integration Journal_ and _Align Journal_).

> EAI gives _O(n)_ complexity for connecting _n_ applications on the network, but there remains an _O(n2)_ complexity for integrating the message formats that the applications use as input and output. With an ontology-based approach, however, this too can be reduced to _O(n)_.

• Semantic Discovery for Web Services,” with Joram Borenstein, _Web Services Journal_.

> Web Services lookup with UDDI requires client and server to agree on the exact syntax of the interaction. Using the principles of ontology, providers can publish and clients can discover Services based on the desired functionality rather than the syntactic details.

• “[Generating XSLT with a Semantic Hub](/wp-content/uploads/2014/10/Generating-XSLT-with-a-Semantic-Hub.pdf),”  _XML Conference_.

> XLST was a promising XML technology that never fulfilled its promise because it was so hard to write and maintain. But when generated automatically from semantic information about what data is used for, XSLT becomes an automated information interchange language.

• “Information Quality through Semantic Models ,” _Enterprise Data Forum_, Pittsburgh.

• “[Deploying Jini: HTTP Servers for the Dynamic Download of Code](https://web.archive.org/web/20230325130712/https://www.javaworld.com/article/2075942/deploy-code-servers-in-jini-systems.amp.html) ,” _JavaWorld_.

> I’ve found that once new Jini developers learn about the exciting distributed architecture, they often get bogged down by the challenge of simply configuring their system for development. They encounter a yet greater challenge in moving from the development configuration to deployment. Even experienced developers can get confused by the variety of components involved.
>
> In the article, I review a number of solutions and explain the advantages of various solutions such as ease of development,ease of migration from development to deployment, low memory and CPU burden, portability, compatibility with RMI Activation, security, and enterprise-class web-app features.

• “Ontology: Automated Integration of Enterprise XML,” _Web Services Edge_, Santa Clara.

• “Building a Successful Wireless Web Site,” _Wireless Business and Technology_.

> If you’re a software development manager with experience leading the development of a three-tier distributed application for the World Wide Web, perhaps you’re about to move on to spearhead the construction of a WAP-site. This article has reuse as its theme: I explain when you can reuse skillsets, infrastructure, and software components from the WWW site, and when you’re better off developing new skills, buying new infrastructure, or building new software.

• “[When is a Singleton not a Singleton](https://www.infoworld.com/article/2074897/when-is-a-singleton-not-a-singleton-.html) ,” _JavaWorld_ (republished in Infoworld, and Sun/Oracle;  appeared on the Java Developer Connection front page).

>  Sometimes you implement the Singleton Design Pattern, but mysteriously find that more than one object of the class is instantiated. This article explains how that can happen and how to avoid it.

• “Distributed Garbage Collection and Socket Option Keep-Alive,” _JavaOne_, San Francisco.

• “[Opaque Bodies, Transparent Envelopes](/wp-content/uploads/2014/10/XML_OpaqueTransparent.pdf) ,” _XML-Journal_.

> Separating layers of abstraction by packaging a body of one layer in an envelope of another layer is one of the fundamental design principles in data transfer. This principle holds for XML just as for any data transfer format, but implementing a system that observes layer separation can be difficult. This article describes how to do it.

• “Developing Java Servlets.” Software Productivity Center, Vancouver, Canada.

• “[So what is SO\_KEEPALIVE?](https://drdobbs.com/java/184404250#) ,” _Dr. Dobb’s Journal_.

> Garbage collecting distributed leases requires mechanisms such as keep-alives, heartbeats, leases, and Are-You-There/I-Hear-You protocols. Interestingly, the keep-alive mechanism built into TCP/IP sockets is not really practical; for this reason and the JDK didn't allow access to Socket Option Keep-Alive until the recent release of JDK 1.3. I explain the problems with SO\_KEEPALIVE and how to implement your own garbage collection mechanism for distributed resources.

• Seminars: Servlets, JSP, RMI and JDBC. Interbit Training and Consulting, a Sun Microsystems Training Center, Herzliya, Israel.

• “[Collaborative Applications with the Java Shared Data Toolkit](https://drdobbs.com/184403999#) ,” _Dr. Dobb’s Journal_.

> I describe and review a toolkit for allowing distributed applications to share objects, and more generally discuss the challenges of managing distributed objects. The JSDT was an official product from Sun, although it never made it to the status of a Java extension. It implemented some interesting ideas for distributing objects. I enjoyed collaborating with the  creator, and some of my suggestions (like one on failure detection), actually made it into the toolkit.



**Recruiting and Career**

---
* [Working as a cloud consultant at DoiT International](https://engineering.doit.com/why-i-work-at-doit-as-a-cloud-infrastructure-consultant/): About our unique work-style: I have never 
seen anything like this.
* [On informational interviews](https://web.archive.org/web/20140702154344/https://www.ere.net/2014/02/26/informational-interviews-for-people-who-dont-need-them/), from the employer’s perspective, at _ERE_, the leading  site for tech recruiters. 
* It [also appeared](http://www.gius.co.il/איך-זה-לעבוד-שם/) at Israel’s top news site for recruiters, gius.co.il.
* On the game-theoretical perspective on [kegerators](https://web.archive.org/web/20210416193222/https://pando.com/2013/12/21/in-praise-of-the-office-kegerator-the-future-of-better-jobs) at _Pando_.
* On building [ open-source communities](https://opensource.com/business/13/7/four-tips-project-to-business)  by recruiting top tech talent from among the members, at _OpenSource.com_.
* Career tips [for Generation Y professionals](https://web.archive.org/web/20141002070155/https://blog.brazencareerist.com/author/joshfox/) at _Brazen Careerist_.
* [The rise of the anti-recruiter](https://readwrite.com/2013/08/23/recruiters-jobs-matchmakers-developers) at _ReadWrite_.
* On a new approach to recruiting  at _Information Week,_  with Jack Perkins.
* On effective [employer branding](https://web.archive.org/web/20140624045748/https://www.ere.net/2014/06/18/not-too-expensive-employer-branding/) at _ERE_.
* [On informational Interviews](https://www.businessinsider.com/a-networking-trick-that-could-help-you-find-your-next-job-2014-2), from the professional’s perspective, at _Business Insider_.
