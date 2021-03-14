## Scope

Build SQL transaction query set with at least 3 SAVEPOINTs and accoridingly 3 actions. Below just a sample of idea, attached the same just with SQL code.

## Exercise

Preferaly use latest class work from https://github.com/arturskarklins/sda/blob/main/lessons/2021-03-14/sda_book_class.sql as base.

1. Fill the missing gaps of code below, represented as [..].

```
-- either use db prefix or use USE db
[..]
-- start transaction
[..]
-- make savepoint
[..]
-- delete all entries for rating from 3.2 to 4.2
-- disable the safe mode preference before and restart app
-- Edit -> Preferences -> SQL Editor (at the end that's the checkbox, uncheck it and restart Workbench)
[..]
-- make second savepoint
[..]
-- insert entry (doesn't matter) add rating as 3.5
[..]
-- make savepoint
[..]
-- update all entries starting with C (try using REGEXP not LIKE, I know you already are familiar with second one)
[..]
-- commit
[..]
```

2. Then try to analize before using SELECT queries, what would be result in cases:

   2.1. There is no ROLLBACK;

   2.2. ROLLBACK TO 1st save point before commit;

   2.3. ROLLBACK TO 2nd save point before commit;

   2.4. ROLLBACK TO 3rd save point before commit;

3. Preferably add more content and similarely, first try to analyze the possbile result on your own and only after - verify with SELECT.
