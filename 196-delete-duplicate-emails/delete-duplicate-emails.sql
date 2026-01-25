# Write your MySQL query statement below
#Person table:
    DELETE p1 FROM Person p1
    JOIN Person p2
    ON p1.email = p2.email AND p1.id > p2.id; # if the 2 emails are the same
    # and if the first e-mail is larger, the other one (p2) will be deleted.



#import pandas as pd

#def delete_duplicate_emails(person: pd.DataFrame) -> None:
#    person.sort_values(by='id', inplace=True)
#   person.drop_duplicates(subset=['email'], inplace=True)