-- INNER JOIN, default (explicit join)
-- SELECT * FROM profiles
-- JOIN stories ON profiles.id = author

-- OUTER JOIN, LEFT
-- SELECT * FROM profiles
-- LEFT JOIN stories ON profiles.id = author

-- OUTER JOIN, RIGHT
-- SELECT * FROM profiles
-- RIGHT JOIN stories ON profiles.id = author

-- CROSS JOIN
-- SELECT * FROM profiles
-- CROSS JOIN stories

-- NATURAL JOIN (USING())
-- SELECT * FROM profiles
-- 3 following lines produce the same result
-- JOIN passwords ON profiles.id = passwords.id
-- JOIN passwords USING(id)
-- NATURAL JOIN passwords

-- FULL JOIN / UNION
-- SELECT * FROM profiles
-- FULL JOIN stories ON profiles.id = author

-- SELECT * FROM profiles
-- LEFT JOIN stories ON profiles.id = author
-- UNION
-- SELECT * FROM profiles
-- RIGHT JOIN stories ON profiles.id = author

-- (implicit join)
-- SELECT * FROM profiles, stories
-- WHERE profiles.id = author

-- multi-join
-- SELECT * FROM profiles
-- LEFT JOIN stories ON profiles.id = author
-- LEFT JOIN passwords ON profiles.id = passwords.id
