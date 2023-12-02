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

A promotional website for a musical festival, which allows festival organisers to provide and update information about the festival with ease, while providing access to that information for prospective festival goers.

### Client Goals

The client is a team of volunteers who organise the Folk on the Lawn festival every year. Their goals are to:

- Have an engaging site which promotes the festival and attracts attendees
- Minimise avoidable contact by clearly providing the information sought by prospective attendees 
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

</details><br>

The top 3 things users are seeking when visiting the website are:
- Line-up and schedule
- Dates and times
- Ticketing information

In terms of people's success finding that information on current platforms, the top rating of 5 scored highest, but the majority provided a rating of 4 or less, suggesting room for improvement.

<details><summary>Success ratings</summary>

![Success ratings](readme_images/success_ratings.png)

</details><br>

When it came to suggested improvements:
- 50% of respondents mentioned providing more up-to-date information
- 33% mentioned improvements to navigation and presentation, especially on mobile devices

All of these factors were taken into account in developing the [User Stories](#user-stories) below.

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

Inevitably the presentation and content of these sites varies, but it is noted that line-up, dates and ticketing information are prominent and accessible on each and every site - in line with the top three topics of interest identified through my user research. In addition, most of the sites provide highly visible social media and contact links. Many of the sites include a gallery, while further information such as location and camping details are less visible, often behind a broad "info" link.

Adding "/admin" to the roots of these sites confirmed that many of them also have an admin function behind the public-facing page, e.g. [Green Man Admin](https://www.greenman.net/admin/). While I was obviously unable to view the actual admin pages, this reinforced my view that an admin function behind a login page was typical for websites of this type. 

## User Stories

Based on the research and project goals outlined above, I have identified the following user stories. These are split into a number of categories, namely **visitors** (external users of the site, e.g. potential festival attendees), **admins** (festival team members who are trusted to update the website) and **superusers** (a small number of individuals who can perform more fundamental actions relating to the website, in addition to all admin functions).  

A. As a **first-time visitor** I want to:
1. Determine key details of the festival such as location, dates and ticket information
2. Discover more about the festival and whether it is likely to interest me
  
B. As a **returning visitor** I want to:  
1. Find out who is playing the festival on which days
2. Buy tickets if I decide to attend
3. Find further sources of information such as social media pages

C. As an **admin user** I want to:
1. Provide key information about the festival such as dates and ticket information
2. Add line-up information and details of the artists playing
3. Provide up-to-date messages to attendees (or potential attendees) in the lead-up to the festival

D. As a **superuser**, in addition to the admin functions outlined above, I want to: 
1. Add or remove admins and amend their privileges
2. Back up important data, and restore it if necessary

## Design

### Wireframes

Wireframes were created using the Figma platform: [Figma - Folk on the Lawn](https://www.figma.com/file/IjXmZ89Phzn0gKjmCOi23H/Folk-On-The-Lawn?type=design&node-id=0%3A1&mode=design&t=OZXv6ccJLV76wfPm-1).

<details><summary>Desktop wireframes - public</summary>

![Desktop wireframes - public](readme_images/desktop_wireframes_public.png)

</details>

<details><summary>Desktop wireframes - admin/superuser</summary>

![Desktop wireframes - admin/superuser](readme_images/desktop_wireframes_admin.png)

</details>

<details><summary>Mobile wireframes - public</summary>

![Mobile wireframes - public](readme_images/mobile_wireframes.png)

</details><br>

Based on prior experience I decided that desktop and mobile wireframes would be sufficient to keep the overall layout of the site on track, the expectation being that [Bootstrap's grid system](https://getbootstrap.com/docs/5.3/layout/grid/) would provide the responsiveness required at different device breakpoints in between (see [Layout and Styling](#layout-and-styling) section below).

Furthermore, the mobile wireframes do not include the admin/superuser pages, as I envisaged that these would generally be accessed using a desktop device, and seldom from a mobile device. While the site is of course accessible from any device and its content will adjust accordingly, I considered there to be little value in producing specific wireframes for this purpose.

#### Differences between wireframes and final design

While the overall structure of the site stays true to the wireframes, there are some notable differences in the final design which came about for design and user experience reasons:

- The schedule table on the **Line-up** page utilises the [Boostrap Accordion](https://getbootstrap.com/docs/5.3/components/accordion/) component. While this was envisaged from an early stage, it was not included in the wireframes.
- During development I discovered [Boostrap Cards](https://getbootstrap.com/docs/5.3/components/card/), along with [Masonry layout](https://masonry.desandro.com/), providing an engaging design on the **Line-up** page quite different to that provided in the wireframes.
- The **Register** page was renamed **Superuser dashboard** due to the additional backup and restore functionality.

In addition, while not affecting the overall design, a number of the pages include features or fields not included in the wireframes. See the [Features](#features) section for more details.

### Layout and Styling

#### Bootstrap

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

- [Navbar](https://getbootstrap.com/docs/5.3/components/navbar/) for the header and subheader.
- [Form components](https://getbootstrap.com/docs/5.3/forms/overview/) throughout the admin and superuser pages.
- [Spacing](https://getbootstrap.com/docs/5.3/utilities/spacing/) and [typography](https://getbootstrap.com/docs/5.3/content/typography/) utility classes throughout, ensuring the layout and font are appropriate to the device in use.
- [Color](https://getbootstrap.com/docs/5.3/utilities/colors/) utility classes to provide specific meaning to text throughout.
- [Display property](https://getbootstrap.com/docs/5.3/utilities/display/) to toggle the visibility of some components at certain breakpoints.
- [Modal plugin](https://getbootstrap.com/docs/5.3/components/modal/) to display alerts before items are deleted.
- [Accordion](https://getbootstrap.com/docs/5.3/components/accordion/) to provide a collapsible menu for the schedule on the Line-up page.
- [Cards](https://getbootstrap.com/docs/5.3/components/card/) to display artist information on the Line-up page (public) and the Artists page (admin).

#### Masonry layout

The Line-up page uses [Masonry](https://masonry.desandro.com/) grid layout, placing the artist cards in optimal position based on available vertical space. 

### Imagery

- **Main image**: The main image displayed on the **Home** page is editable by admin users, providing a customisation option. For demonstration purposes the image provided is a man carrying an acoustic guitar standing in a grass field, courtesy of [Ben White on Unsplash](https://unsplash.com/photos/man-carrying-brown-cutaway-acoustic-guitar-standing-on-green-grass-field-iPyQg9QfepM).

- **Footer image** The footer includes a stylised image of a lawn in various shades of green aligned with the overall [colour scheme](#colour-scheme), on a transparent background.

- **Artist images**: Artist images are uploaded by admin users, and displayed on the **Line-up** page (public) and **Artists** page (admin).

- **403 image**: The **403 (Forbidden)** error page includes an image of a person holding their hand to the camera to indicate that access is denied, courtesy of [Nadine Shaabana on Unsplash](https://unsplash.com/photos/close-up-photography-of-person-lifting-hands-DRzYMtae-vA).

- **404 image**: The **404 (Page Not Found)** error page includes an image of a microphone on an empty stage, courtesy of [Oscar Keys on Unsplash](https://unsplash.com/photos/photo-of-microphone-on-foggy-stage-ojVMh1QTVGY).

- **500 image**: The **500 (Internal Server Error)** error page includes an image of an acoustic guitar on fire, courtesy of [Dark Rider on Unsplash](https://unsplash.com/photos/flaming-guitar-digital-wallpaper-JmVaNyemtN8).

- **Logo**: The logo is simply a stylised representation of the festival name using the [Effloresce font](https://www.dafont.com/effloresce.font). The logo appears in its full form on sm devices and above, and adjusts to a compressed format of "FotL" on xs devices.

  <details><summary>Full Logo</summary>
  
  ![Full logo](readme_images/logo.png)
  
  </details>

  <details><summary>Compressed Logo</summary>
  
  ![Small logo](readme_images/logo_xs.png)
   
  </details><br>

### Colour Scheme
  
- The **primary colour** of the website is a dark shade of green (#022832), reflecting the "lawn" of the festival name. This is used for the **header**, **headings** and **primary buttons** throughout the site, as well as the background of artist cards on the **Line-up** page.

- The **logo** uses Bootstrap's .text-light utility class (#F8F9FA). The **dates** and **location** also use this class, but with an opacity of 75% so that they show more of the green background, making them less pronounced.

- The **navbar** uses Bootstrap's .navbar-dark class, providing the navigation items with white text with approximately 50% opacity (#FFFFFF8C).

- The **admin menu** uses the same shade of green as the main header, but with 20% opacity (#02283233) so that it appears lighter, while complementing the darker shade of the main header. It uses Bootstrap's .navbar-light class which provides darker navigation items (#000000A6).

- The **footer** uses the primary green used elsewhere (#022832), along with complementary lighter shades (#7CA3AE, #426973), providing a similar colour contrast as the header.

- The **background** is an off-white (#F9F9FA), providing a contrast to the dark header and body text.

- Primary **buttons** use the main green colour (#022832) mentioned above, while buttons used on forms throughout the site use Bootstrap's .bg-danger (#DC3545) and .bg-warning (#FFC107) utility classes depending on their function.

- Body **text** is black (#000000), while Boostrap's utility classes are used to convey meaning to text throughout, in particular .text-danger (#DC3545) for urgent warnings, and .text-info (#0DCAF0) for flash messages.

  <details><summary>Colour scheme palette</summary>

  ![Website colour scheme palette](readme_images/palette.png)

  </details>

### Typography

- The **logo**, **headings** and **navigation items** use Effloresce, downloaded from [Dafont](https://www.dafont.com/effloresce.font) as a TrueType font and converted to @font-face using [Transfonter](https://transfonter.org/). The fallback font is Serif. Effloresce is a stylish serif font with a slight rustic feel, in keeping with the ethos of the festival.

    <details><summary>Effloresce</summary>

    ![Effloresce](readme_images/effloresce.png)

    </details><br>

- The **strapline** on the Home page uses Dancing Script, imported from [Google Fonts](https://fonts.google.com/specimen/Dancing+Script), with Sans Serif as the fallback font. Dancing Script is a playful but sophisticated script font which suits the content of the strapline "Innovative Folk for Innovative Folk".

    <details><summary>Dancing Script</summary>

    ![Dancing Script](readme_images/dancing_script.png)

    </details><br>

- The **body** and all other elements use Noto Serif, imported from [Google Fonts](https://fonts.google.com/noto/specimen/Noto+Serif), with Serif as the fallback font. Noto Serif is a straightforward serif font which complements the Effloresce font used for the logo and headings.

    <details><summary>Noto Serif</summary>

    ![Noto Serif](readme_images/noto_serif.png)

    </details><br>

### Icons

  [Bootstrap Icons](https://icons.getbootstrap.com/) have been used for **navigation items**, **social media links**, **buttons** and **form elements**, utilised as classes in the `<i>` tag.

  <details><summary>Navigation icons</summary>

  ![Navigation icons](readme_images/nav_icons.png)

  </details>

  <details><summary>Button icons</summary>

  ![Navigation icons](readme_images/button_icons.png)

  </details>
  
### Favicon

   The favicon is a grass icon using the site's colour scheme, generated using [Favicon Generator](https://www.favicon-generator.org/).

  <details><summary>Favicon</summary>

  ![Favicon](readme_images/favicon.png)

  </details>

## Features

### Scope

- #### Minimum Viable Product

  To be viable as a music festival website and meet the stated [Project Goals](#project-goals), the website **must have**:
  1. A public front-end website including key information about the festival such as location, dates, how to buy tickets and line-up.
  2. An admin portal which allows admin users to update line-up and artist information on the website quickly and easily, regardless of technical ability.
         
- #### Additional Features (in scope)

  To provide a good user experience in line with the stated [Project Goals](#project-goals), the website **should have**:
  1. Contact information and social media links.
  2. A schedule visible to public users which is automatically generated based on showtimes provided by admin users. 
  3. The ability for admins to add and edit key information about the festival such as dates and stage names, allowing the website to be updated year on year without adjusting any code.
  4. The ability for admins to provide up-to-date messages to attendees (or potential attendees) in the lead-up to the festival.
  5. A superuser dashboard, allowing admins to be added and deleted, and data to be backed up and restored.
   
- #### Future Ideas (not currently in scope)
  
   To provide a better user experience and better meet the stated [Project Goals](#project-goals), the website also **could have**:
   1. A schedule builder, allowing public users to build their own schedule of artists they wish to see from the overall schedule.
   2. An application portal, allowing artists to apply to perform at the festival.
   3. An artist booking system, allowing information about artists to be submitted to a page only visible by admins, allowing admins to comment on and/or vote on artists, and allowing bookings to be confirmed or denied once a decision has been made, the artist information then becoming public.
   4. A gallery page, either using a portal to allow admins to upload photos directly, or embedding the festival's Instagram feed.

### Python Functionality using Flask

Python has been used to build the core backend application which underpins the site, utilising the [Flask web framework](https://flask.palletsprojects.com/en/3.0.x/). In particular, Python and Flask have been used to:

- Provide routing of pages, allowing meaningful URLs to be used to return pages and content to the user.
- Connect to the backend database to retrieve information and serve it to the site, and to allow creation, updating and deletion of records.
- Provide login functionality and security, ensuring only authorised users can access and edit particular information.
- Display flash messages to the user.

### Database

The backend application connects to a database hosted on [MongoDB](https://www.mongodb.com/), which contains three collections as outlined below.

#### Admins

Contains entries for all admins registered on the site.

- Example admin entry:
  ```
  {
    _id: (unique value)
    name: "Nick Smith"
    username: "nicksmith"
    password: (hashed password)
    is_superuser: "on"
    date_added: "03/11/2023"
  }
  ```

#### Key Info

Contains a single entry providing key details of the festival and other information for displaying on the site.

- Example key_info entry:
  ```
  {
    _id: (unique value)
    event_start: 2023-07-13T00:00:00.000+00:00
    event_end: 2023-07-16T00:00:00.000+00:00
    stages: Array (4)
      0: "River"
      1: "Mill"
      2: "Cottage"
      3: "Bar"
    display_schedule: "on"
    main_img: "w93ykgjdg5dwi4es2zni"
    banner_heading: "Schedule now live!"
    banner_text: "Please take a look on the line-up page."
    fundraising_url: "https://www.justgiving.com/crowdfunding/fotl2023new"
    last_edit_by: "nicksmith"
    last_edit_on: "21-11-2023"
  }
  ```

#### Artists

Contains entries for all artists

- Example artists entry:
  ```
  {
    _id: (unique value)  
    artist_name: "Anna My Charlotte"
    artist_bio: "Anna was at the top of our ‘hit list’ for each FotL for a number of ye…"
    artist_url: "https://annamycharlotte.bandcamp.com/"
    artist_img: "bgc00xfj70g79c8s24xc"
    show1_stage: "Cottage"
    show1_start: 2023-07-15T18:00:00.000+00:00
    show1_duration: "45"
    show2_stage: "River"
    show2_start: 2023-07-16T11:00:00.000+00:00
    show2_duration: "45"
    show3_stage: ""
    show3_start: 1900-01-01T00:00:00.000+00:00
    show3_duration: ""
    last_edit_by: "nicksmith"
    last_edit_on: "21-11-2023"
  }
  ```

### Page Elements and Interaction

The website is divided between public-facing pages which provide information to external users sourced from the database, and admin pages (for logged in users) which allow admins to update information in the database. There is also a superuser dashboard which is only visible to logged in users with superuser credentials. 

#### Public pages and elements

- **Header**: All pages include a header with branding on the left-hand side, a navigation menu on the right-hand side, and festival dates and location with flexible positioning (see below). The festival dates are retrieved from the database by the backend application and served to the template, which parses the information and displays it accordingly. The header is fully responsive:
  - The branding (festival name) is displayed in its full form on sm viewports and above, but compresses to a shortened form on xs viewports.
  - The festival dates and location are displayed beneath the branding on sm viewports and above, but horizontally centred on xs viewports.
  - The navigation menu is displayed as a single line on lg viewports and above, but collapses to a hamburger menu on md viewports and below.
         
    <details><summary>Header (lg)</summary>
          
    ![Header (lg)](readme_images/header_lg.png)

    </details>
        
    <details><summary>Header (sm)</summary>
          
    ![Header (sm)](readme_images/header_sm.png)

    </details>
        
    <details><summary>Header (xs)</summary>
          
    ![Header (xs)](readme_images/header_xs.png)

    </details><br>

- **Home page**: Provides general information about the festival, and includes:
  - A **Hero Image** which is editable by admin users, overlaid with a strapline of "Innovative Folk for Innovative Folk" against a light, semi-transparent background.
  - An optional **Banner Message** which is editable by admin users.
  - A call to action to **Support the Festival** with a donation button which opens a fundraising page in a separate tab.
  - An **About** section with general background information.
  - A **Location** section with an embedded map from [Google Maps](https://developers.google.com/maps/documentation/embed/get-started) and directions.

    <details><summary>Home (lg)</summary>

    - Hero image and banner<br>  
      ![Home - Hero image and Banner (lg)](readme_images/home_hero_banner_lg.png)
    
    - Support, About and Location<br>    
      ![Home - support, about and location (lg)](readme_images/home_support_about_location_lg.png)

    </details>

    <details><summary>Home (xs)</summary>
    
    - Hero image, Banner and Support<br>
      ![Home - hero image, banner and support (xs)](readme_images/home_hero_banner_support_xs.png)
    
    - About<br>
      ![Home - about (xs)](readme_images/home_about_xs.png)

    - Location<br>
      ![Home - location (xs)](readme_images/home_location_xs.png)

    </details><br>

- **Line-up page**: Provides schedule information and details of artists playing, including:
  - A day-by-day **Schedule** with collapsible menu utilising the [Boostrap Accordion](https://getbootstrap.com/docs/5.3/components/accordion/) component. Showtime information is compiled in the backend application using information from the database and served to the template, which parses the information and displays it accordingly. 
  - An **Artist Index** with hyperlinks to provide easy access to artist information. The list of artists is retrieved from the database by the backend application and served to the template to form the links, which point to separate ```<div>``` elements for each artist.
  - Individual **Artist Cards** utilising [Boostrap Cards](https://getbootstrap.com/docs/5.3/components/card/), and [Masonry layout](https://masonry.desandro.com/), providing a photo of the artist, a list of their appearances, and an external link to their website. Each card also includes a transition which flips the card to display the artist's biography. The information provided in each card is retrieved from the database by the backend application and served to the template, which parses the information and displays it accordingly. 

  All elements are responsive, for example the stage listings within the Schedule appear side-by-side on lg viewports but vertically stacked on xs viewports, with the Artist Cards behaving similarly.

    <details><summary>Line-up page (lg)</summary>

    - Schedule<br>
      ![Line-up - schedule (lg)](readme_images/schedule_lg.png)
    
    - Artist Index<br>
      ![Line-up - artist index (lg)](readme_images/artist_index_lg.png)

    - Artist Cards<br>
      ![Line-up - artist cards (lg)](readme_images/artist_cards_lg.png)

    </details>

    <details><summary>Line-up page (xs)</summary>

    - Schedule<br>
      ![Line-up - schedule (xs)](readme_images/schedule_xs.png)
    
    - Artist Index<br>
      ![Line-up - artist index (xs)](readme_images/artist_index_xs.png)
    
    - Artist Cards<br>
      ![Line-up - artist cards (xs)](readme_images/artist_cards_xs.png)

    </details><br>

- **Confirmation modal**: For any change which will result in irreversible changes to data, e.g. deletion, a warning is displayed asking the user if they are sure. In such cases the delete button is coded to trigger the modal, and data attributes are used to provide the wording of the warning and the target for the confirm button. Pressing the confirm button then directs the user to the relevant target, triggering the intended action.

  <details><summary>Confirmation modal</summary>

  ![Confirmation modal](readme_images/confirmation.png)

  </details><br>

- **Flash messages**: Flash messages are displayed to provide information to the user, e.g. when logging in and logging out, or when changes are made to database entries.

  <details><summary>Flash messages</summary>

  ![Flash message - logout](readme_images/logout.png)<br>
  ![Flash message - artist updated](readme_images/artist_updated.png)
    
  </details>

- **403 (Forbidden)**: A 403 (Forbidden) error is displayed in the event that a user tries to browse to a page that they are not authorised for. The 403 page includes an image of a person holding their hand to the camera to indicate that access is denied, together with the message "Sorry, this area is for crew only! Please select an item from the navigation menu above." 

- **404 (Page Not Found)**: A 404 (Page Not Found) error is displayed in the event that a user tries to browse to a page that does not exist. The 404 page includes an image of a microphone on an empty stage, together with the message "Sorry, this stage is empty! Please select an item from the navigation menu above." 

- **500 (Internal Server Error)**: A 500 (Internal Server Error) error is displayed in the event of an error in the application or the server. The 500 page includes an image of an acoustic guitar on fire, along with the message "Well, this wasn't meant to happen! Please select an item from the navigation menu above to start again." 

#### Admin pages and elements

While all admin pages are fully responsive, screenshots below are shown in desktop format only, as they would be expected to be accessed primarily by desktop.

-  **Subheader**: All admin pages include an additional subheader, beneath the main header, with a label ("Admin menu") on the left-hand side and a navigation menu on the right-hand side.

    <details><summary>Subheader</summary>
          
    ![Subheader)](readme_images/subheader.png)

    </details>
        
- **Login**: Includes a simple login form with username and password, and an email link if the user has forgotten their password. The backend application puts the user in session if the username and password are correct, or alerts the user with a flash message otherwise. If an event start date has been provided (see below) and it is in the past, the user is directed to the Key Info page (since an event in the past indicates that the key information requires updating). Otherwise the user is directed to the Artists page.

    <details><summary>Login form</summary>
          
    ![Login form](readme_images/login.png)

    </details>

- **Key Info**: Provides a form allowing key information about the festival to be submitted by admins and saved in the database, in particular:
  - Start date
  - End date
  - Stage names (as comma separated values)
  - Whether the Schedule should be displayed on the Line-up page (toggle switch)
  - Main image for the Home page (with a preview of the current image)
  - Banner heading and text for the Home page
  - Fundraising link accessible through the button on the Home page

    The **start date** and **end date** utilise the [flatpickr](#flatpickr) date picker plugin.
    
    The **main image** is uploaded to the [Cloudinary](https://cloudinary.com/) image hosting platform, which returns a unique ID for the image. The ID is stored in the database and used along with a base URL provided in the backend application to render the image wherever it is required.
  
    The page includes a **Save changes** button. It also includes a **Delete event** button, although this actually submits blank values to the database (01-01-1900 in the case of dates), rather than actually deleting the entry in the database.

  <details><summary>Key Info</summary>
          
  ![Key Info 1](readme_images/key_info1.png)
  ![Key Info 2](readme_images/key_info2.png)

  </details><br>
      
- **Artists**:

  - Displays an index of artists already added, along with buttons to add an artist or delete all. Details of existing artists are displayed using [Bootstrap Cards](https://getbootstrap.com/docs/5.3/components/card/), along with buttons to delete the artist or edit their details. The information provided in each card is retrieved from the database by the backend application and served to the template, which parses the information and displays it accordingly.
  
    <details><summary>Artists</summary>
            
    ![Artist Index - admin](readme_images/artist_index_admin.png)
    ![Artist Cards - admin](readme_images/artist_cards_admin.png)

    </details><br>
  
  - If no artists have yet been added but dates and stages have been added to the Key Info collection, the user is informed that no artists have yet been added, and is presented with the Add Artist button.
  
    <details><summary>No artists warning</summary>
          
    ![No artists warning](readme_images/no_artists.png)

    </details><br>

  - If there are no artists, and dates or stages are missing from the Key Info database, the user is informed that they must provide this information before artists can be added.

    <details><summary>No dates warning</summary>
          
    ![Key Info 1](readme_images/no_dates.png)

    </details><br>

- **Add Artist**: Provides a form allowing artist information to be submitted by admins, in particular:
  - Name
  - Biography
  - Website
  - Image
  - Show information for up to three shows - including stage, date and time, and duration

    The image is uploaded to the [Cloudinary](https://cloudinary.com/) image hosting platform, which returns a unique ID for the image. The ID is stored in the database and used along with a base URL in the backend application to render the image wherever it is required.

    The entry for date and time for each show utilises the [flatpickr](#flatpickr) date picker plugin, with dates limited to those provided by the Key Info database.

    <details><summary>Show date picker</summary>
            
    ![Show date picker](readme_images/show_date.png)
    
    </details><br>

    The page includes an **Add** button to add the artist to the database using the submitted details.

  <details><summary>Add artist</summary>
            
    ![Add artist 1](readme_images/add_artist1.png)
    ![Add artist 2](readme_images/add_artist2.png)

  </details><br>

- **Edit artist**: As above for "Add artist", but existing information is presented to the user, including a preview of any image already submitted. The page includes a **Save changes** button which updates the database with the edited values.

  <details><summary>Edit artist</summary>
          
  ![Edit artist 1](readme_images/edit_artist1.png)
  ![Edit artist 2](readme_images/edit_artist2.png)

  </details><br>

#### Superuser dashboard

The site includes a Superuser Dasboard, accessed through a link in the admin menu which is only visible to logged in users with superuser credentials.

  <details><summary>Superuser link</summary>
          
  ![Superuser link](readme_images/subheader_superuser.png)
  
  </details><br>

The dashboard allows an admin with superuser access to:
- Register new admins.
- Toggle the superuser status of an existing admin.
- View all registered admins.
- Backup and restore the festival key information and artists.

  <details><summary>Superuser dashboard</summary>

  - Registration<br>     
    ![Superuser dashboard - registration](readme_images/registration.png)
  
  - Existing admins<br>
    ![Superuser dashboard - existing admins](readme_images/existing_admins.png)

  - Backup and restore<br>
    ![Superuser dashboard - backup and restore](readme_images/backup_restore.png)
  
  </details><br>


### JavaScript Functionality

#### jQuery

- The jQuery libary has been used to faciliate the use of JavaScript, in particular for adding event listeners.

#### flatpickr

- The [flatpickr plugin](https://flatpickr.js.org/) has been used to provide date pickers for festival dates and showtimes.

  <details><summary>Date picker</summary>

  ![Date picker](readme_images/flatpickr.png)
  
  </details><br>

#### Flip cards

- The flip card function on the **Line-up** page uses CSS, but JavaScript has been used to add an event listener for toggling the "flipped" class. This functionality is ignored for anchor tags to allow the artist website to be linked from the card without flipping it.

#### Masonry and imagesLoaded

- The artist cards on the **Line-up** page use the [Masonry](https://masonry.desandro.com/) JavaScript library to provide the particular grid layout. The [imagesLoaded](https://imagesloaded.desandro.com/) libary is also used to [prevent unloaded images throwing off the layout](https://masonry.desandro.com/layout#imagesloaded).

#### Varying modal content

- A JavaScript snippet from the [Boostrap documentation](https://getbootstrap.com/docs/5.3/components/modal/#varying-modal-content) has been adapted, allowing the content and function of confirmation modals to be varied using the data attributes of the buttons which trigger them. 


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