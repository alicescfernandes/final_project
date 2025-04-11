# Dev Log

__Newer entries are inserted to the top of the file__

## 05/11/2025

- [ ] Read chart config from the chart classification type, and return that chart type
- [ ] Add support on the backend and frontend to allow for multiple filters (check the dimensions)
- [ ] Ensure that all charts are supported, without any bugs or errors
- [ ] Fork the branch for the FEIM presentation and freeze it
- [ ] Extract remaining tailwind classes into the CSS file
- [ ] Check if the flowbite JS file can be imported from node_modules

## 04/11/2025

- [x] Add sheet parsing to the endpoints
- [x] Make sure that the endpoints and the duplicated file logic still works
- [x] Disable edit excel on the admin, only removals and creations - This was fixed
- [x] Remove "Quarters" from the sheet names
- [x] Remove "Total" lines
- [x] Fix the slug on the admin. this needs to match the chart classification type
- [x] File deletion was disabled
- [x] Make the API return Plotly traces, and use those traces
- [x] File deletion was disabled

### Data filtering problems

The initial approach was to apply "templates" to the data, where each CSV would follow a very strict algorithm that would determine the available options to filter data by, and the X and Y's of the data. Upon further inspection, that logic seems flawed as it will produce graphs that won't be useful to the end user.

Example: on the Competitors Prices - NORAM.csv file, we have two main "filter" columns, Brand and Company, and 3 numeric columns, Price, Rebate, Priority.
If we apply the following filter Brand==Elevatech 3.0 AND Company== CTTG, then we only get a single line of information:
Elevatech 3.0 3,400 0 1

But if we only apply the following filter Company== CTTG, then we get multiple lines of information
Elevatech 3.0 3,400 0 1
Express 3.0   3,000 200 2
TurboLiteV2     1,850 100 3

The second data is more useful than the first, since it immediatly displays all products of the CTTG brand. The same thought process can be applied to all "double" charts, where we should really only filter by a single column information.

The second issue is that i need 2D data, meaning on X and one Y. If i have multiple axises then i cannot represent that data on a 2D scale
