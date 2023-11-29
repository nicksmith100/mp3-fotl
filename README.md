# Folk on the Lawn Website

![Folk on the Lawn logo](readme_images/logo.png)

This project creates a website for a music festival called Folk on the Lawn. It allows external users to find information about the festival, and allows site admins to update line-up and artist information. The site is designed to be responsive and accessible on a range of devices, making it easy to navigate for external users and site admins alike.

[View the live project here](https://folk-on-the-lawn-5be73867df7e.herokuapp.com/)

![Folk on the Lawn website displayed on various devices](readme_images/responsive_screens.png)


## Table of Contents

1. [Project Goals](#project-goals)
2. [Research](#research)
3. [User Stories](#user-stories)
4. [Design](#design)
5. [Features](#features)
6. [Testing](#testing)
7. [Tecnologies Used](#technologies-used)
8. [Deployment](#deployment)
9. [Credits](#credits)


## Project Goals

### Purpose

A promotional website for a musical festival, which allows festival organisers to provide and update information about the festival with ease, while providing access that information to prospective festival goers.

### Client Goals

The client is a team of volunteers who organise the Folk on the Lawn festival every year. Their goals are to:

- Have an engaging site which promotes the festival and drives up audience numbers
- Minimise avoidable contact by clearly providing the information sought by prospective festival goers 
- Allow admin users to update information on the website quickly and easily, regardless of technical ability

### User Goals

The primary goals of the user are to:

- Find out key information about the festival such as location, dates and how to buy tickets
- Find out information about who is playing at the festival and when
- Find out where to go for more information or to contact the festival organisers

Detailed user stories are provided in the [User Stories](#user-stories) section below.

## Research

### User research

Before embarking on any design or development work, I used the festival's existing website and social media channels to gather user views. This research covered users' preferred online platforms, what particular information they were looking for when visiting the website, their experience of using the existing site to find that information, and any suggessted improvements.

42% of users preferred using the website (rather than social media) to access information about Folk on the Lawn, suggesting the website remains an important way for the festival to engage with its audience.

<details><summary>Preferred online platform</summary>

  ![Preferred platform](readme_images/preferred_platform.png)

</details>

\
The top 3 things users are seeking when visiting the website are:
- Line-up and schedule
- Dates and times
- Ticketing information

In terms of people's success finding that information on current platforms, the top rating of 5 scored highest, but the majority provided a rating of 4 or less, suggesting room for improvement.

<details><summary>Success ratings</summary>

  ![Success ratings](readme_images/success_ratings.png)

</details>

\
When it came to suggested improvements, 50% of respondents mentioned providing more up-to-date information, while 33% mentioned improvements to navigation and presentation, especially on mobile devices.

All of these factors were taken into account in developing the User Stories](#user-stories) below.

### Existing music festival websites

To aid consideration of presentation and content, I also researched existing music festival websites, particularly those appealing to a similar clientele. These included smaller festivals, comparable in size to Folk on the Lawn itself, as well as larger, commercial festivals.

#### Smaller festivals
- [Off The Beaten Track](http://www.otbtfest.org/tickets.html)
- [Bromyard Folk Festival](https://bromyardfolkfestival.co.uk/)
- [Barn on the Farm](https://www.barnonthefarm.co.uk/)

#### Larger festivals
- [Green Man](https://www.greenman.net/)
- [End of the Road](https://endoftheroadfestival.com/)
- [Cambridge Folk Festival](https://www.cambridgelive.org.uk/folk-festival)

Inevitably the presentation and content of these sites varies, but it is noted that line-up, dates and ticketing information are all prominent and accessible on each and every site - in line with the top three topics of interest identified through my user research. In addition, most of the sites provide highly visible social media and contact links. Many of the sites include a gallery, while further information such as location and camping details are less visible, often behind a broad "info" link.

## User Stories

(User stories)

## Design

### Wireframes

Wireframes were created using the Figma platform: [Figma - Folk on the Lawn](https://www.figma.com/file/IjXmZ89Phzn0gKjmCOi23H/Folk-On-The-Lawn?type=design&node-id=0%3A1&mode=design&t=OZXv6ccJLV76wfPm-1).

<details><summary>Desktop wireframes</summary>

  ![Desktop wireframes](readme_images/desktop_wireframes.png)

</details>

<details><summary>Mobile wireframes</summary>

  ![Mobile wireframes](readme_images/mobile_wireframes.png)

</details>

Based on prior experience I decided that desktop and mobile wireframes would be sufficient to keep the overall layout of the site on track, the expectation being that [Bootstrap's grid system](https://getbootstrap.com/docs/5.3/layout/grid/) would provide the responsiveness required at different device breakpoints in between (see [Layout and Styling](#layout-and-styling) section below).

(Detail any differences)

### Layout and Styling

The site uses the [Bootstrap 5.3 Grid system](https://getbootstrap.com/docs/5.3/layout/grid/) to ensure it is fully responsive on all device and viewport sizes. Bootstrap 5.3 uses the following [breakpoints](https://getbootstrap.com/docs/5.3/layout/breakpoints/), the shorthand references for which are used throughout the rest of this document:

| Breakpoint        | Shorthand   | Dimensions |
|-------------------|-------------|------------|
| Extra small       | xs          | <576px     |
| Small             | sm          | ≥576px     |
| Medium            | md          | ≥768px     |
| Large             | lg          | ≥992px     |
| Extra large       | xl          | ≥1200px    |
| Extra extra large | xxl         | ≥1400px    |

In addition, the site uses the following specific components from the Bootstrap library:

(Specific components)

### Imagery

- **Logo**: (Logo deails))

  <details><summary>Logo</summary>
  
  ![Static logo](readme_images/logo.png)
  
  </details>

(Details of other images)

- **404 image**: (404 image details)
       
### Colour Scheme

(Colour scheme details)

<details><summary>Colour scheme palette</summary>

![Website colour scheme palette](readme_images/palette.png)

</details>

### Typography

- #### Logo

  (Logo font details)

- #### Main heading

  (Main heading font details)
  
- #### Other headings, buttons and text

   (Other font details)

  
- #### Icons

  [Bootstrap Icons](https://icons.getbootstrap.com/) have been used for the main menu buttons, utilised as classes in the `<i>` tag.

  <details><summary>Menu icons</summary>

  (Icon details)

  </details>
  
- #### Favicon

   The favicon is (...), generated using [Favicon Generator](https://www.favicon-generator.org/). This proved more effective than trying to use the main logo as a favicon, as the detail of it was lost at such a small size.

  <details><summary>Favicon</summary>

  ![Favicon](readme_images/favicon.png)

  </details>

## Features

### Scope

- #### Minimum Viable Product

(MVP details)
         
- #### Additional Features (in scope)

(Additional features)
   
- #### Future Ideas (not currently in scope)
  
(Future ideas)

### Page Elements and Interaction

(Details)

- #### Header

  (Header details)
         
  <details><summary>Header (lg)</summary>
      
  ![Header (lg)](readme_images/header_lg.png)

  </details>
    
  <details><summary>Header (md)</summary>
      
  ![Header (md)](readme_images/header_md.png)

  </details>
    
  <details><summary>Header (sm)</summary>
      
  ![Header (xs)](readme_images/header_xs.png)

  </details>

  
- #### Home page

- #### Line-up page

- #### Edit line-up (Admin)

- #### Edit artist (Admin)

- #### 404 page

  A 404 page is provided in the event that the user browses to a page which does not exist. It depicts (...details...)

  <details><summary>404 page (lg)</summary>
    
  ![404 page (lg)](readme_images/404_lg.png)

  </details>

  <details><summary>404 page (xs)</summary>
    
  ![404 page (xs)](readme_images/404_xs.png)

  </details>    

### JavaScript Functionality

- #### Presentation and navigation

### Python Functionality

## Testing

### Automated testing

- #### HTML validation with [W3C Markup Validator](https://validator.w3.org/)

- #### CSS validation with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

- #### JavaScript validation using [JSHint](https://jshint.com/)

- #### Python validation using (...)

- #### Accessibility using [Lighthouse accessibility](https://developer.chrome.com/docs/lighthouse/accessibility/)

  Lighthouse audit scores (accessed through Chrome DevTools) show that the site is fully accessible and complies with best practices.

  <details><summary>Lighthouse scores</summary>

  ![Lighthouse scores](readme_images/lighthouse.png)

  </details>

### Manual Testing

- #### User stories

  The site was tested against the user stories as follows. (See [User story screenshots](#user-story-screenshots) below table for associated screenshots.)

    (User stories table)

- #### User story screenshots

  Screenshots are shown for xs viewports (i.e. mobile devices) because this is how the majority of users are expected to access the site. Screenshots for lg viewports (tablets, laptops and desktops) can be found in the [Features](#features) section. 

  (User stories screenshots)

- #### Feature testing

  (Feature testing table)
    

- #### Browser and device compatibility

  The above features were tested on the following browsers and devices:

  (Browser and device compatibility table)

### Bugs and fixes

(Bugs and fixes details)


## Technologies Used

### Languages
- [HTML](https://html.spec.whatwg.org/multipage/)
  - Standard markup language for web pages
- [CSS](https://www.w3.org/Style/CSS/)
  - Adding style to HTML
- [JavaScript](https://www.w3schools.com/js/)
  - Adding interactive elements
- [Python](https://www.w3schools.com/python/)
  - Providing backend application to provide website information 

### Frameworks
- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
  - Overall layout and styling, and specific components as described above

### Libraries
- [jQuery](https://jquery.com/)
  - Show and hide functionality
- [jQuery UI](https://jqueryui.com/)
  - Autocomplete on search form
- [Google Fonts](https://fonts.google.com)
  - Exo and Oswald fonts
- [Bootstrap icons](https://icons.getbootstrap.com/)
  - Icons on main menu buttons

### APIs
(Provide any APIs here)

### Platforms
- [Github](https://github.com/)
  - Storing code
- [Gitpod](https://gitpod.io/)
  - IDE used for project development
- [MongoDB](https://mongodb.com/)
  - Used for hosting database
- [Heroku](https://heroku.com/)
  - Deployment

### Other Tools
- [Figma](https://www.figma.com/)
  - Wireframes
- [Coolors](https://coolors.co/)
  - Colour palette
- [Favicon Generator](https://www.favicon-generator.org/)
  - Website favicon
- [Am I Responsive](https://ui.dev/amiresponsive)
  - Montage of different devices displaying the site
- [Canva](https://www.canva.com/)
  - Creation of main logo
- [Unsplash](https://unsplash.com/)
  - 404 image
- [Fix the photo](https://fixthephoto.com/uk/online-gimp.html)
  - Image editing
  

## Deployment

### Heroku

(Deploment info, including local deployment instructions)

## Credits

### Code

- [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/layout/grid/): Bootstrap Library used throughout the project, including responsive layout and specific components as outlined above.
- All other code snippets are credited in comments in the relevant files.

### Content

(Content info)

### Media

(Media info)   

### Acknowledgements

- My Mentor [Rory Patrick Sheridan](https://github.com/Ri-Dearg) for many helpful pointers.
- Our Cohort Facilitator [Iris Smok](https://github.com/Iris-Smok/Iris-Smok) for providing helpful guidance on project requirements throughout.
- [Emma Hewson](https://github.com/emmahewson) (...Swimmon project details...)