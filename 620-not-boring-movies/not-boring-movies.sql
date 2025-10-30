select * from Cinema
where id%2!=0 and lower(description)!='boring'
order by rating desc;