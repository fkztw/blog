Title: ITSE Ch8 - Conventional Techniques of Design  
Date: 2013-11-25 01:21  
Author: fkz  
Category: Course  
Tags: Software Engineering  
Slug: itse-ch8-conventional-techniques-of-design  
  
  
# NCTUCS 2013-Fall Introduction to Software Engineering by Professor Feng-Jian Wang  
# Ch8 - Conventional Techniques of Design  
  
+ ORB  
+ Microsoft COM  
+ Sun JavaBeans  
+ Classification  
    + Enumerated classification  
    + Faceted classification  
    + Attribute-value classification  
+ Indexing  
+ The Reuse Environment  
    + A component database capable of storing software components and the classification information necessary to retrieve them.  
    + A library management system that provides access to the database.  
    + A software component retrieval system (e.g., an object request broker) that enables a client application to retrieve components and services from the library server.  
    + CBSE tools that support the integration of reused components into a new design or implementation.  
  
---  
# User Interface Design  
  
## Typical Design Errors  
  
+ lack of consistency  
+ too much memorization  
+ no guidance / help  
+ no context sensitivity  
+ poor response  
+ Arcane/unfriendly  
  
> Arcane adj. 晦澀難解的  
  
## Golden Rules  
  
+ Place the user in control  
+ Reduce the user’s memory load  
+ Make the interface consistent  
  
## Place the User in Control  
  
+ not force a user into unnecessary or undesired actions  
+ Provide flexible interaction  
+ Allow user interaction to be interruptible and undoable. (undoable - impossible to achieve;)  
+ Streamline interaction. ()  
+ Allow the interaction to be customized.  
+ Hide technical internals from the casual user.  
+ Design for direct interaction with objects that appear on the screen.  
  
## Reduce the User’s Memory Load  
  
+ Reduce demand on short-term memory.  
+ Establish meaningful defaults.  
+ Define shortcuts that are intuitive.  
+ The visual layout of the interface should be based on a real world metaphor.  
+ Disclose information in a progressive fashion.  
  
## Make the Interface Consistent  
  
+ Allow the user to put the current task into a meaningful context.  
+ Maintain consistency across a family of applications.  
+ If past interactive models have created user expectations, do not make changes unless there is a compelling reason to do so.  
  
## User Interface Design Models  
  
+ User model — a profile of all **end users** of the system  
+ Design model — a design realization of the user model  
+ Mental model (system perception) — the user’s mental image of what the interface is  
+ Implementation model — the interface **“look and feel”** coupled with supporting information that describe interface syntax and semantics  
  
## User Interface Design Process  
![User Interface Design Process](/files/itse-ch8-conventional-techniques-of-design/user-interface-design-process.png)  
  
#### Interface Analysis  
#### User Analysis  
#### Task Analysis and Modeling  
  
* find some workflow tools  
  
#### Analysis of Display Content  
  
## Swimlane Diagram  
  
## Interface Design Steps  
  
￼￼￼￼￼￼1. define interface objects and actions (operations).  
2. Define events (user actions)  
3. Depict each interface state  
4. Indicate how the user interprets the state of the system  
  
## Design Issues  
  
+ Response time  
+ Help facilities  
+ Error handling  
+ Menu and command labeling  
+ Application accessibility  
+ Internationalization  
  
---  
  
# WebApp Interface Design  
  
+ Where am I?  
    + provide an indication of the WebApp that has been accessed  
    + inform the user of her location in the content hierarchy.  
+ What can I do now?  
    The interface should always help the user understand his current options  
    + what functions are available?  
    + what links are live?  
    + what content is relevant?  
+ Where have I been, where am I going?  
    Theinterfacemust facilitate navigation.  
    + Provide a “map” (implemented in a way that is easy to understand) of where the user has been and what paths may be taken to move elsewhere within the WebApp.  
  
  
## Effective WebApp Interfaces - by Bruce Tognozzi [TOG01]  
  
+ Effective interfaces are visually apparent and forgiving  
+ Effective interfaces do not concern the user with the inner workings of the system.  
+ Effective applications and services perform a maximum of work  
  
## Interface Design Principles  
  
+ Anticipation （預期;期望): A WebApp should be designed so that it anticipates the use’s next move.  
+ Communication  
+ Consistency  
+ Controlled autonomy  
+ Efficiency  
+ Focus  
+ Fitt’s Law  
+ Human interface objects  
+ Latency reduction  
+ Learnability  
+ Maintain work product integrity  
+ Readability  
+ Track state  
+ Visible navigation  
  
## Interface Design Workflow  
  
+ Review information contained in the analysis model and refine as required.  
+ Develop a rough sketch of the WebApp interface layout.  
+ Map user objectives into specific interface actions.  
+ Define a set of user tasks that are associated with each action.  
+ Storyboard screen images for each interface action.  
+ Refine interface layout and storyboards using input from aesthetic design.  
+ Identify user interface objects that are required to implement the interface.  
+ Develop a procedural representation of the user’s interaction with the interface.  
+ Develop a behavioral representation of the interface.  
+ Describe the interface layout for each state.  
+ Refine and review the interface design model.  
  
## Aesthetic Design  
  
+ Don’t be afraid of white space.  
+ Emphasize content.  
+ Organize layout elements from top-left to bottom right.  
+ Group navigation, content, and function geographically within the page.  
+ Don’t extend your real estate with the scrolling bar. (?  
+ Consider resolution and browser window size when designing layout. => Response Design  
  
# Design Evaluation Cycle  
![design evaluation cycle](/files/itse-ch8-conventional-techniques-of-design/design-evaluation-cycle.png)  
