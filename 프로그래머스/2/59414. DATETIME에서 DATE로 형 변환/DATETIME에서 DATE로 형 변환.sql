-- 코드를 입력하세요
SELECT animal_id, name, DATE_FORMAT(datetime, "%Y-%m-%d") as 날짜 from ANIMAL_INS
order by animal_id