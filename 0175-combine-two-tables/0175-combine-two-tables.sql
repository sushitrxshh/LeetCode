# Write your MySQL query statement below
SELECT p.firstname, p.lastname, s.city, s.state
FROM Person p
LEFT JOIN Address s
ON p.personID = s.personId;