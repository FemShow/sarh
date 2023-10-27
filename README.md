# sarh
Data and statistics about the number of civilian search and rescue helicopter activity in the United Kingdom.

sarh (pivot)
This dataset could not be built, the error message was "Missing value found in data" which means that there is a blank value in an obsevation column which did not have a corresponding observation status value. NOTE: csvs should not have a blank line at the end of them.

The description of the dataset is talking about vehicle registrations! (describe)
No summary was provided. (describe)
No themes were provided. (describe)
There is no publication date. (describe)
There is no contact details. (describe)
The creator is Department for Transport, not Maritime and Coastguard Agency as described on Cover page, (tip: the contact information helps with this) (describe)
The publisher is also not the Maritime and Coastguard Agency. (*describe)
Why is "Search" capitalised in your keywords when everything else is lowercase? (describe)
The refPeriod column is correctly configured, with original columns correctly suppressed. (describe)
Obsevation columns needed to be pivoted to capture the data correctly (i.e. there should have been a dimension called "Tasking Location Type", with values from columns C. (transform, component separation)
The "ONScode" column contains codes which don't follow ONS geography codes patterns. Additionally, the data represented in the source docuemnt are not ONS Geographies but helicopter bases, and should be a dimension called "Base" with further details of the concepts created in a custom code list. (component id)
All the units are correct, with the correct extension, and correct label. (describe)
All the measures are incorrect
First, they are identified as scales, and should be "count". (describe)
The labels are all the same, despite representing "Mountain", "Other", "Beach/Cliff", etc. (component id)
People will not read the description to distinguish the difference between these measures (description)
The description includes the term "by base" for each of them, which is covered by the dimension "ONScode" despite its problems, this should have been omitted (describe)
sarh (standard)
This dataset could not be built, the error message was "Missing value found in data" which means that there is a blank value in an obsevation column which did not have a corresponding observation status value. NOTE: csvs should not have a blank line at the end of them.

This dataset is better built as a standard dataset, where the geography and tasking location are treated as dimensions.

The description of the dataset is talking about vehicle registrations! (describe)
No summary was provided. (describe)
No themes were provided. (describe)
There is no publication date. (describe)
There is no contact details. (describe)
The creator is Department for Transport, not Maritime and Coastguard Agency as described on Cover page, (tip: the contact information helps with this) (describe)
The publisher is also not the Maritime and Coastguard Agency. (*describe)
Why is "Search" capitalised in your keywords when everything else is lowercase? (describe)
The "Year" column is stored as a dimension when it should be omitted because you've got the Period column you created showing the correct refPeriod and using the correct quarters. (transform)
The existance of a "make" column in the qube-config.json is confusing, Where did this come from? (describe)
The "ONScode" column doesn't contain ONS Geography codes (describe, transform, component separation)
Additionally, the total values don't have any value, which will cause the build to fail as dimensions must be dense not sparse (component id, transform)
The "Location" column should have been treated as a simple dimension. (describe)
The "Value" column is correctly identified as an observation column type (describe)
The measure label looks good too (describe)
The measure is scale but should be count (describe)
The data_type is good (describe)
The unit is correct (describe)
