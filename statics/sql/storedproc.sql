CREATE FUNCTION get_faculty_by_num(input_fac INTEGER)
RETURNS TABLE(fac_num int, first_name text, last_name text) AS $$
    SELECT f.fac_num, f.first_name, f.last_name
    FROM faculty f
    WHERE f.fac_num = input_fac
$$
LANGUAGE SQL;
