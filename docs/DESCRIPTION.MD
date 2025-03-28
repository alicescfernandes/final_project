## Description
The project is an website that can display graphs. The graphs are based on data submitted by the users, that are XLSX files extracted from another platform. The purpose of the the app is to allow users to see and manipulate that data. The platform should also provide advanced filtering capabilities that are not possible on the platform that the data is exported from.

### Users
- Users are split in groups of users
- Each group has a single account on the platform
- Each group can upload XLSX files.
- Each group can also delete XLSX files.
- The upload will be split by quarters, where the group has to create a quarter on the platform and then upload files to that quarter. The quarters are identified by string "Quarter" and a number, like "Quarter 2" (on the backend, it will be identified as "Q2").

### Charts
- Each XLSX file comes identified with the section and quarter that it belongs to (CostumerNeeds-Q2.xlsx)
- The graph can display data from that section, but for multiple graphs.
- Graphs can also have advanced filtering to allow for a more granular search
- Graphs are fixed, and cannot be changed


## XLSX
The XLXS files are strucutured in the following way.  
- The first line is a header, the name of the graph
- The first column will always be the "X axis" to identify the data. The column can can change, but it's always the first

## Pages
"Create Account / Login" - Allows the groups to create account
"Recover Password" - Allows the groups to recover the account password
"Homepage / Index" - Displays the data in charts. The sole purpose is to display those charts
"Settings" - Allows to change password, upload and remove files and create quarters to upload those files


## Stack
- Django for the "full-stack"
- Flowbite as the design system, integrated witihin django
- Pandas to analyse and transform the data into a more workable set
- Plotly as the charting library



## Roadmap
To allow for a phased development, we will split the work into milestoens

1. Create the app without any access control, where the app reads from XLSX files locally
2. We can then work on creating the upload functionality, and display the graphs based on the data uploaded
3. Using Django's Authentication System, we will then create access control for groups, and allow for uploads per group
 

