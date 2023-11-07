
# User Stories

## Andrew Butler - Persona/Stories

**Persona 1**

* Name: John Casper
* Role: Backend Developer
* Motivations: 
    * I want to quickly transform local Media into a link I can send to someone.
    * I need a fast app that will work multiple times in a minute.
    * I want a detailed interface showing me all functions available to me.
* Skills:
    * I Don't like online tools with ads.
    * I Work fast so my applications have to keep me productive.
* **USER STORY 1 (Expanded):**
    * User Story: When I’m editing work projects I want a place to store my ideas and code chunks.
    * Definition of Done: Text can be translated into hyperlink form for html access.
    * Tasks: Get Database to serve a link as a key for the text given to the app..
    * Personas: John Casper
    * Steps:
        * DataBase testing/confirmation
        * API Assurance
        * Working Product Iteration
* **USER STORY 2**
    * As a backend developer I'm constantly losing my algorithm code. I need a place to store them with html links.
* **USER STORY 3**
    * As a backend developer I want a place to store notes online that I can share publicly or keep private.
* **USER STORY 4**
    * As a backend developer I use hyperlinks to reference text in code. I need an easy way to do this.
* **USER STORY 5**
    * As a backend developer I work fast and need a fast processing server to use as a tool.

---

## Cooper - Persona/Stories

**Persona 2**

* Name: Sharyl Johnson
* Role: Old Lady
* Motivations:
    - I like an easy to use, simple interface with pretty colors.
    - There should be no pop-up ads on any application I use. 
    - I want to be able to save and access letters for my grandchildren. 
* Skills:
    * Limited technical knowledge.
    * Only owns a landline phone.
    * Uses an old slow laptop from 2012. 
* **USER STORY 1:**
    * As a person who is not technically savvy I would like the application to be easy to use so I can use it and not get lost in any technical jargon.
* **USER STORY 2:**
    * As a grandmother of someone in the tech field I want to be able to use technology in a simple way so that I can  show my grandchild I can. 
* **USER STORY 3 (EXPANDED):**
    * **Story**: As a forgetful old lady I want to be able to close my tab without thinking about saving my file so that I don’t forget to do so. 
    * **Def. of Done**: My files will autosave before I close them. 
    * **Task**: Make an autosave function that can tell when something new is added to a file. 
    * **Steps**: Create a function on the backend that collects the data and sends it to the Database consistently. 
* **USER STORY 4:**
    * As a homebody I want to be able to send my friends links with cute messages so I can stay in touch. 
* **USER STORY 5:**
    * As a mother I want to make a group document so I can help my kids stay in touch with each other. 


---


## Holden - Persona/Stories

**Persona 3**

* Name: Jack Lewis
* Role: Influencer
* Motivations: 
    * I want to keep track of all the links to social media sites I use
    * I want to create a personal account with a customizable profile
    * I want to be able to be able to send links to multiple contacts at once 
    * I want a public listing feature for the pastes I create
* Skills: I prefer a clean interface
    * I have extensive experience with social media platforms and mobile platforms
    * Alternates between apps and devices very frequently
* **USER STORY 1 (EXPANDED):**
    * **User Story:** As an influencer, I want to have the option to make my pastes available on the public page so my followers and fans can access all of my social media profiles in one place.
    * **Definition of Done:**
        * Pastes can be posted to a personal profile
        * Pastes and posts can be listed as publicly available 
    * **Tasks:**
        * User login interface (UX Designer)
        * Store account username and password in a database (Backend Dev)
        * Add paste options when creating or editing paste (UX Designer)
    * **Personas:** Jack Lewis
    * **Steps:**
        * Start application
            * Prompt user login
        * Create new paste
            * Display privacy settings
        * Click set to public
            * Posts paste to public feed and personal profile
* **USER STORY 2:**
    * As an influencer, I want to have a customizable personal profile, so that my followers can quickly search for my pastes.
* **USER STORY 3:**
    * As an influencer, I want to allow people to comment on the posts I create, so that my community can communicate with each other.
* **USER STORY 4:**
    * As an influencer, I want to be able to directly send my pastes so that I can privately share them with other people.
* **USER STORY 5:**
    * As an influencer, I want to be able to follow people, so that posts they make automatically show up in my feed.


---


## Nathaniel Bernich - Persona/Stories

**Persona**

* Name: Eustace Studenton
* Role: High school student
* Motivations / goals: 
    * I want to be able to save and access notes/TODO lists for myself easily, which can be edited/added to in the future
    * I want to be able to share notes easily with my classmates for group assignments
    * I want to be able to keep some content confidential and only accessible to people I want it shared with
    * I want to be able to easily access pastes made by other people
    * I want to be able to collaborate with friends and classmates on shared notes
* Skills / preferences / frustrations:
    * I have some technical skills, but I still want a simple and easy to use application
    * I don’t have the patience for long loading times associated with heavy, feature-rich, fancy text editors
    * Ease of use and speed are my main reasons for favoring a text hosting program

**User Stories:**



1. Expanded User Story
    1. Story:
        - _As a student, I want to be able to write notes and TODO lists for myself and edit them in the future, so I can add and remove listed tasks and reminders as needed._
    2. Definition Of Done:
        - all users are able to save new text pastes to the database
        - the user who created the pastes can edit them through a unique link provided to them
        - all tasks have been completed (developed, tested, reviewed, and validated)
    3. Tasks:
        - new paste page outline (UX designer)
        - edit paste page outline (UX designer)
        - styling and organization for webpages (UI designer)
        - webpage prototypes (frontend dev)
        - API integration -- endpoints for saving and editing (backend dev)
        - database actions for saving and editing (backend/database dev)
        - Integration testing (mostly backend)
        - usability and responsiveness testing (UX designer/frontend dev)
    4. Personas
        - Eustace Studenton, Student
    5. Steps:
        - start application
            - show main menu
        - click “new paste
            - Direct user to paste creation page and display content form
            - Create new database paste record
            - Give user editing link and viewing link for the paste 
        - type in text input box
            - Start throttled auto-saving
        - click “submit” or press Enter
            - Save most recent text edits
        - Go to editing link to make changes
            - request editing page from backend and display
        - Type in changes and then press enter
            - Save the same way as before
        - go to viewing link to check the paste 
            - Request paste content from database
            - If valid, display paste content in read-only form
2. User Story:
    - _As a student, I want to have a public viewing link for the text pastes I create, so that I can share information with classmates during group assignments._
3. User Story:
    - _As a student, I want to have the option to make a paste that is not listed publicly -- only accessible by link -- so that personal notes are not freely shared with strangers._
4. User Story:
    - _As a student, I want to be able to view posts made by other people, so that I can receive notes from others as well._
5. User Story:
    - _As a student, I want to be able to have shared editing abilities for some text pastes, so that I can collaborate with friends and classmates on shared notes._