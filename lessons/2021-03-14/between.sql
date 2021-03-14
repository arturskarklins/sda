-- 1. select ratings <3.8 >4.3
-- SELECT * FROM stories
-- 2 lines below produce the same result
-- WHERE rating >= 3.8 AND rating <= 4.3
-- WHERE rating BETWEEN 3.8 AND 4.3

-- 2. select stories with rating * 10
-- SELECT story, FLOOR(rating * 10) AS decimal_rating FROM stories
-- WHERE rating BETWEEN 3.8 AND 4.3