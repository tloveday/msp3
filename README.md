# MC REVUE
[View live project here:] (https://m-c-re-vue.herokuapp.com/)
![Impostor Hunt](assets/images/ImpostorHuntMockUp.png)
MC REVUE is a Movie information and review website dedicated to the Marvel Cinematic Universe.
Its name itself is a play on the MCU acronym used by Marvel and its fans for the Marvel Cinematic Universe.

This is the third of four Mile Stone Projects.

The brief was to build an interactive front-end site that responds to users' actions, allowing them to actively engage with data, alter the way the site displays the information to achieve their preferred goals.


## Mock Up
Wireframes for
- Computer
![Wireframe](assets/Wireframe/Computer.png)
- Tablet
![Wireframe](assets/Wireframe/Tablet.png)
- Mobile
![Wireframe](assets/Wireframe/Mobile.png)

## User Experince

### New User
- View Movie and Television reviews
- Create movie and Television reviews for MCU Movies and Televison Shows

### Returning User
- Create reviews for MCU products  viewed
- View reviews for MCU products.
- Edit and delete personal reviews for MCU products 

## Design
### Colour schemes
The Colour Scheme of the website is inspired by Marvel Entertainment's colour scheme
Red - #ED1D24

### Typography 
"Poppins" - 

"Marvel" - is a complimentary font to "Poppins" and is more inkeepnig with the Marvel Studios product.

### Imagery
Majority of the imagry featured in the project comes from Marvel Entertainment and marvel Studios as Theatrical Poster Art or logos used to announce projects at ComicCon 2020 or at a Disney investor event of 2020.
Logos for the website "MC REVUE" and "Pan Industries" were created by myself
- MC RVUE is a spin on the Marvel Studios logo with the U in white to signal the MCU acronym for the Marvel Cinematic Universe
- Pan Industires is a play on the Paragrah syntax with a pseudo name for myself alongside one of the commonly used company names found within Marvel Lore 


### Languages Used
HTML
CSS
Javascript - JQuery
Python

## Frameworks used
- [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wire frames for design.
- [Font Awesome:](https://fontawesome.com/)
    - Font awesome was used for a range of font based images found throughout the project.
- [favconit:](http://faviconit.com/en)
    - Favconit was used to build and code the favcons that feature on the project.
- [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
- [Google Fonts:](https://fonts.google.com/)
    - Google Fonts provided the code for the fonts used throughout the project.
- [Heroku:] (https://heroku.com/)
    - Heroku was used as the platform as a service (PaaS) to build, run, and operate applications entirely in the cloud
- [IconScout:] (https://iconscout.com/unicons/)
    - Iconscout and its Unicons were used for a range of font based images like those found at fontawesome. 
- [Materialize CSS:](https://materializecss.com/)
    - Materialize CSS was used to assist with the responsiveness and styling of the website.
- [MongoDB:](https://www.mongodb.com/) 
    - MongoDB was used to create the database used throughout the project.
- [Procreate:] (https://procreate.art/) 
    - Procreate was used to create the visuals for the art used throughout the project.


## Testing
HTML was directly imput into (https://validator.w3.org/) and no warnings or errors were shown.
CSS was directly imput into (https://jigsaw.w3.org/css-validator/) with results showing no warnings or errors. 

### User goals

#### New User
- View Movie and Television reviews
    - OUTCOME
- Create movie and Television reviews for MCU Movies and Televison Shows
    - OUTCOME

#### Returning User
- Create reviews for MCU products viewed
    - OUTCOME
- View reviews for MCU products.
    - OUTCOME
- Edit and delete personal reviews for MCU products
    - OuTCOME


### Further Testing
Website was tested on a variety of browsers including Google Chrome, Safari, Firefox, And Edge.
The website was viewed on a variety of devices including desktop, laptop and mobile on both iOS and Android.

### Problems
- Trying to workout how to include images in Mongo DB
    - This was worked around by inserting a movie/television show  specific "codeword" in Mongo DB which aligned with the images filename added to the repository.

- Getting a Visual 5 star rating system controlled by JQuery to place information in the database upon submission of the review form.
    - Through discsssion with Antonio, my mentor, he suggested I look into using a hidden input that recorded the inormation printed to the console when clicking the stars from the Javascript/JQuery file. 


### Further Development




## Bugs
All images stored in the Static/Images folders Images not showing in both movie and television show information pages with the error code 404 emerging. -

## Deployment
### Heroku
"Heroku is a container-based cloud Platform as a Service (PaaS). Developers use Heroku to deploy, manage, and scale modern apps" Before you deploy to Heroku you will need to add a requirements.txt file and a Procfile to your application. Heroku needs both of these files to run, they must be pushed to the repository on GitHub.

To deploy your application to Heroku

1. Go to Heroku.com and login or create and account.
2. Your dashboard should open and there will be a 'New' button on the top-right of the screen, select this.
3. Select 'Create New App' from the buttons drop down menu
4. Add your app name (it must be unique, lowercase with a dash used instead of spaces)
5. Select the region closest to you and click create app
6. You will then need to connect your GitHub Repository, in the deploy tab, under method, select "Connect to GitHub".
7. Connect your GitHub account, ensure the correct profile name is displayed
8. Then add your repository name, search and select the correct repository
9. Open the settings tab and select 'Reveal Config Vars'
10. You will need to add here, any secret or hidden variables that are not visable to Heroku from your GitHub repository.
>    - IP : "0.0.0.0"
>   - PORT : "5000"
>    - MONGO_DBNAME : "(Insert the database name you wish to connect to)"
>   - MONGO_URI : "(Insert URI)" - The URI can be found on MongoDB under Clusters, "Connect" > "Connect your application" and replacing the generic values with your user name and password
>   - SECRET_KEY : "(Insert custom secret key you created in configuration to keep the sessions secure)
11. Hide Con Fig Vars and reopen the deploy tab
12. Under automatic deployment enable automatic deployment
13. In manual deploy section select the branch you wish to deploy from the drop down and click deploy branch
14. This will take a few moments, once complete and option to view the live app will appear

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Media
- [Marvel Studios](https://innersloth.com/gameAmongUs.php) 


### Acknowledgements

-  My Mentor Antonio for helpful feedback, and much needed guidance along a difficult path.
-  Tutor support at Code Institute for their support.
- My family for thier continual feedback and honest critique, thier support and love (Even Liwsi and your sleepless nights).

- 

### Final Thoughts
This project has been one of the hardest tests I've ever experienced. I have sat through hours of youtube tutorials, on top of multiple re-watches of the entire module leading into the project. I have spent days looking at singular problems with no way forward, at several points during the process I have considered quitting the course completely due to the negative impact it was having on my mental health and personal  well-being. Whilst this may not be perfect or as I originally wanted and intended but it is the best that I can currently provide with my limited experience in Javascript. The deployed and submitted project is a personal triumph for myself and watching the reactions from the community of streamer "Warwick Zero" with the negativity I was experiencing around the build has made me realise I am capable, I can deliver - it might take me a little longer on occasion- but I can get it done, and not to place too much pressure on myself.# Impostor Hunt
